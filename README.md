# Telegram to Spreadsheets
A simple Telegram bot that logs incoming messages to a Google Spreadsheet. The bot receives messages from users, processes the data, and adds it to a specified Google Sheet in real time.

## Features
- Receive messages: The bot listens for messages sent to it.

- Log to Google Sheets: All received messages are stored in a Google Spreadsheet for easy tracking and management.

- Simple and easy to use: Set up and get started quickly.

## Prerequisites
Before running the project, make sure you have:

- A Telegram account and a Telegram bot (created using BotFather).

- A Google Sheets API project set up with a service account and a JSON credentials file.

- Python 3.7 or higher installed. 
  _(Tested with Python 3.13.2)_
  
- Necessary Python packages.

## Setup and Installation
### 1. Clone the repository:

<pre> git clone https://github.com/yourusername/telegram-to-spreadsheets.git
 cd telegram-to-spreadsheets </pre>
 
### 2. Install dependencies:
   
<pre> pip install -r requirements.txt </pre>

### 3. Set up environment variables:
   
Create a `.env` file in the root directory of the project and add the following environment variables:

<pre> TELEGRAM_BOT_TOKEN=your-telegram-bot-token
 GOOGLE_SHEETS_CREDENTIALS_JSON=path-to-your-google-sheets-credentials.json </pre>
 
- Replace your-telegram-bot-token with your actual Telegram bot token.
    
- Replace path-to-your-google-sheets-credentials.json with the path to your Google Sheets API JSON credentials.
    
- Replace your-google-sheet-name with the name of your Google Sheet where messages will be logged.

### 4. Run the bot:
   
<pre> python main.py </pre>

This will start the bot and it will begin listening for messages on Telegram.

## How It Works
1. Bot listens for messages: The bot waits for messages from users.

2. Process the message: Each message received by the bot is processed and added to the Google Sheet.

3. Logging: Each message is appended as a new row in the sheet with the message content and other relevant data.
