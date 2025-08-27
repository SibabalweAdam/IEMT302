You've been given a reasonably extensive template for a Telegram Chatbox leveraging the Spacy NLP library. Your task is to adapt what you've been given to address a novel application. What would you see this Chatbot doing? We've spoken about some ideas in class, but you are not restricted to those.

Your repository should meet the following requirements:

Include a README.md which describes the problem your application is addressing
Your README should includes some instructions on how I can go about verifying that your solution works
Your README should also mention the limitations of your Chatbot. What does it do when it encounters something unexpected?
Make use of a virtual environment in your project folder, but exclude that from the repo.
Include a requirements file to assist me in recreating your virtual environment on my own machine.

Setup Instructions
Create a virtual environment:

bash
python -m venv travel-bot-env
source travel-bot-env/bin/activate  # On Windows: travel-bot-env\Scripts\activate
Install dependencies:

bash
pip install -r requirements.txt
Download SpaCy language model:

bash
python -m spacy download en_core_web_md
Set up your Telegram bot:

Message @BotFather on Telegram to create a new bot

Copy the API token provided

Create a .env file in the project root and add:

text
TELEGRAM_TOKEN=your_telegram_bot_token_here
Run the chatbot:

bash
python travel_chatbot.py
Testing the Bot
Start a conversation with your bot on Telegram

Try these example queries:

"I want to visit Paris"

"What are some fun activities in Tokyo?"

"Recommend a beach destination"

"What should I pack for a trip to London?"

"Find me hotels in New York"

Limitations
Knowledge Scope: The bot has limited knowledge about destinations and may not have information about less popular locations.

Context Understanding: While it can handle basic travel queries, it may struggle with complex, multi-part questions.

Unexpected Inputs: When encountering queries outside its travel domain:

It will try to redirect to travel topics

It may provide a default response asking for clarification

It might not understand highly specific or technical travel questions

No Real-time Data: The bot doesn't access live information about prices, availability, or current events.

Simple NLP: Uses basic pattern matching and may not understand nuanced language or slang.

File Structure
text
travel-chatbot/
├── travel_chatbot.py    # Main chatbot implementation
├── requirements.txt     # Python dependencies
├── .env.example        # Example environment variables
├── .gitignore          # Git ignore rules
└── README.md           # This file
Requirements
The requirements.txt file includes:

python-telegram-bot for Telegram integration

spaCy for natural language processing

python-dotenv for environment variable management

Other necessary dependencies
