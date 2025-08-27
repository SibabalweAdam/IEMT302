import os
import re
import random
import spacy
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Load environment variables
load_dotenv()

# Load SpaCy NLP model
try:
    nlp = spacy.load("en_core_web_md")
except OSError:
    print("Please download the SpaCy model first: python -m spacy download en_core_web_md")
    exit(1)

# Travel knowledge base
TRAVEL_KNOWLEDGE = {
    "destinations": {
        "paris": {
            "description": "Paris, the City of Light, is famous for the Eiffel Tower, Louvre Museum, and delicious cuisine.",
            "activities": ["Eiffel Tower visit", "Louvre Museum", "Seine River cruise", "Notre-Dame Cathedral"],
            "accommodation": "Luxury hotels near Champs-Élysées or cozy boutiques in Le Marais",
            "best_time": "April to June and September to November"
        },
        "tokyo": {
            "description": "Tokyo offers a blend of ultramodern and traditional, from neon-lit skyscrapers to historic temples.",
            "activities": ["Senso-ji Temple", "Shibuya Crossing", "Tsukiji Fish Market", "Imperial Palace"],
            "accommodation": "Business hotels in Shinjuku or traditional ryokans",
            "best_time": "March to May and September to November"
        },
        "new york": {
            "description": "New York City is known for its iconic skyline, Broadway shows, and diverse neighborhoods.",
            "activities": ["Statue of Liberty", "Central Park", "Times Square", "Broadway show"],
            "accommodation": "Hotels in Manhattan or trendy boutiques in Brooklyn",
            "best_time": "April to June and September to early November"
        },
        "bali": {
            "description": "Bali is a tropical paradise known for its volcanic mountains, rice terraces, and beaches.",
            "activities": ["Ubud rice terraces", "Beach relaxation", "Temple visits", "Water sports"],
            "accommodation": "Beach resorts in Seminyak or villas in Ubud",
            "best_time": "April to October (dry season)"
        }
    },
    "activities": {
        "beach": ["Maldives", "Hawaii", "Thailand", "Greek Islands", "Cancun"],
        "adventure": ["New Zealand", "Costa Rica", "Switzerland", "Nepal", "Peru"],
        "cultural": ["Italy", "Japan", "India", "Egypt", "Turkey"],
        "city": ["London", "Tokyo", "New York", "Paris", "Singapore"]
    },
    "travel_tips": [
        "Always check travel advisories before booking",
        "Purchase travel insurance for international trips",
        "Keep digital copies of important documents",
        "Learn basic phrases in the local language",
        "Pack light and leave room for souvenirs"
    ]
}

# Keyboard layout for quick responses
TRAVEL_KEYBOARD = [
    ["Destinations", "Activities"],
    ["Accommodation", "Travel Tips"],
    ["Help", "About"]
]

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /start command"""
    welcome_message = """
    🌍 Welcome to Travel Planner Bot! 🌍
    
    I can help you plan your next adventure! Here's what I can do:
    
    • Recommend destinations based on your interests
    • Suggest activities and attractions
    • Provide travel tips and advice
    • Help with accommodation ideas
    
    Try asking me about:
    - "I want to visit Paris"
    - "Beach destinations"
    - "Adventure activities"
    - "Travel tips for Europe"
    """
    
    keyboard = ReplyKeyboardMarkup(TRAVEL_KEYBOARD, resize_keyboard=True)
    await update.message.reply_text(welcome_message, reply_markup=keyboard)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /help command"""
    help_text = """
    🤖 How to use Travel Planner Bot:
    
    You can ask me about:
    - Specific destinations (e.g., "Tell me about Tokyo")
    - Types of vacations (e.g., "beach destinations")
    - Activities (e.g., "adventure activities")
    - Travel tips and advice
    - Accommodation suggestions
    
    Examples:
    • "I want to go to a beach destination"
    • "What can I do in Paris?"
    • "Recommend some cultural destinations"
    • "Travel tips for Asia"
    """
    await update.message.reply_text(help_text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Process incoming messages"""
    message_type = update.message.chat.type
    text = update.message.text.lower()
    
    # Process the message with SpaCy
    doc = nlp(text)
    
    # Extract entities and keywords
    entities = [ent.text.lower() for ent in doc.ents]
    keywords = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    
    response = generate_travel_response(text, entities, keywords)
    
    await update.message.reply_text(response)

def generate_travel_response(text, entities, keywords):
    """Generate appropriate response based on user input"""
    
    # Check for destination queries
    for destination, info in TRAVEL_KNOWLEDGE["destinations"].items():
        if destination in text:
            response = f"🌆 {destination.title()} 🌆\n\n"
            response += f"{info['description']}\n\n"
            response += f"Popular activities: {', '.join(info['activities'][:3])}\n"
            response += f"Best time to visit: {info['best_time']}\n"
            response += f"Accommodation: {info['accommodation']}"
            return response
    
    # Check for activity types
    for activity_type, destinations in TRAVEL_KNOWLEDGE["activities"].items():
        if activity_type in text or any(activity_type in word for word in keywords):
            response = f"🏖️ Great {activity_type} destinations: 🏖️\n\n"
            response += f"{', '.join(destinations)}\n\n"
            response += f"Which destination would you like to know more about?"
            return response
    
    # Check for accommodation queries
    if "hotel" in text or "accommodation" in text or "stay" in text:
        return "🏨 For accommodation, I can recommend:\n- Luxury hotels in city centers\n- Boutique hotels\n- Vacation rentals\n- Hostels for budget travel\n\nWhich destination are you considering?"
    
    # Check for travel tips
    if "tip" in text or "advice" in text or "pack" in text:
        tips = random.sample(TRAVEL_KNOWLEDGE["travel_tips"], 3)
        response = "📋 Travel Tips: 📋\n\n"
        response += "\n".join([f"• {tip}" for tip in tips])
        response += "\n\nNeed more specific advice?"
        return response
    
    # Default response for unrecognized queries
    default_responses = [
        "I'm here to help with travel planning! Try asking about destinations, activities, or travel tips.",
        "I specialize in travel advice. Want to know about a specific destination or type of vacation?",
        "Let's talk travel! Where would you like to go or what kind of experience are you looking for?",
        "I can help you plan your next trip. What destination or activity interests you?"
    ]
    
    return random.choice(default_responses)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors"""
    print(f"Update {update} caused error {context.error}")
    await update.message.reply_text("Sorry, I encountered an error. Please try again.")

def main():
    """Start the bot"""
    # Get the token from environment variables
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    
    if not TOKEN:
        print("Please set TELEGRAM_TOKEN in your .env file")
        return
    
    # Create application
    application = Application.builder().token(TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_error_handler(error_handler)
    
    # Start the bot
    print("Travel Planner Bot is running...")
    application.run_polling(poll_interval=3)

if __name__ == "__main__":
    main()
