import gspread
from oauth2client.service_account import ServiceAccountCredentials
from utils import constant
import os
from telegram import Update
from telegram.ext import ContextTypes
from setup import google_sheet
from ai import text_generation

def authenticate_google_sheets() -> gspread.Worksheet:
    scope = [
        "https://spreadsheets.google.com/feeds", 
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        os.getenv('GOOGLE_SHEETS_CREDENTIALS_JSON'), 
        scope
    )
    client = gspread.authorize(creds)
    sheet = client.open(constant.GOOGLE_SHEET_NAME).sheet1  # Change to your spreadsheet name
    return sheet

def add_to_sheet(message_text: str) -> None:
    sheet = authenticate_google_sheets()

    if not message_text.strip():
        raise ValueError("Message text is empty.")
    
    messages = message_text.split(',')
    sheet.append_row(messages)


# Command handler: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi! I am your bot, send me any message and I will log it to the spreadsheet.')

# Message handler: for handling any text message
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    user_message = text_generation.extract_information(user_message)
    google_sheet.add_to_sheet(user_message)  # Add the message to Google Sheets
    await update.message.reply_text(f"Message logged: {user_message}")