# Travel Planning Telegram Chatbot
A conversational AI chatbot built with Python and SpaCy that helps users plan trips and get travel recommendations through Telegram.

### Features:
- Destination recommendations based on user preferences
- Activity suggestions (sightseeing, adventures, cultural experiences)
- Accommodation information
- Travel tips and advice
- Basic conversation capabilities

## Setup Instructions
### 1. Create a virtual environment:
```bash
python -m venv travel-bot-env
source travel-bot-env/bin/activate # On Windows: travel-bot-env\Scripts\activate 
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Download SpaCy language model:
```bash
python -m spacy download en_core_web_md
```

### 4. Set up your Telegram bot:
- Message @BotFather on Telegram to create a new bot
- Copy the API token provided
- Create a `.env` file in the project root and add:
```env
TELEGRAM_TOKEN=your_telegram_bot_token_here
```

### 5. Run the chatbot:
```bash
python travel_chatbot.py
```

### Testing the chatbot:
1. Start a conversation with your bot on Telegram
2. Try these example queries:
  - "I want to visit Paris"
  - "What are some fun activities in Tokyo?"
  - "Recommend a beach destination"
  - "What should I pack for a trip to London?
  - "Find me hotels in New York"

### Limitations:
1. Knowledge Scope: The bot has limited knowledge about destinations and may not have information about less popular locations.
2. Context Understanding: While it can handle basic travel queries, it may struggle with complex, multi-part questions.
3. Unexpected Inputs: When encountering queries outside its travel domain:
   - It will try to redirect to travel topics
   - It may provide a default response asking for clarification
   - It might not understand highly specific or technical travel questions
4. No Real-time Data: The bot doesn't access live information about prices, availability, or current events.
5. Simple NLP: Uses basic pattern matching and may not understand nuanced language or slang.
   
## File Structure

```
travel-chatbot/
├── travel_chatbot.py    # Main chatbot implementation
├── requirements.txt     # Python dependencies
├── .env                 # Example environment variables
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

