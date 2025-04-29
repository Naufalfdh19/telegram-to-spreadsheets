import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
import os
from setup import google_sheet as gs

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Main function to start the bot
def main():
    load_dotenv()

    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        raise ValueError("BOT_TOKEN not found in environment variables.")

    # Create the application instance
    application = Application.builder().token(bot_token).build()

    # Register handlers
    application.add_handler(CommandHandler("start", gs.start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, gs.handle_message))

    # Start polling for updates
    application.run_polling()

if __name__ == '__main__':
    main()
