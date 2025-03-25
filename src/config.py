from dotenv import load_dotenv
import os


load_dotenv()
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
SOURCE_CHAT_ID = int(os.environ.get("SOURCE_CHAT_ID"))
TARGET_CHAT_ID = int(os.environ.get("TARGET_CHAT_ID"))
'''
    Specifies from which topic of the source chat to which topic of the target chat to send a message in the format: `“0”: 0`, where the numbers are the id's of the topics in the chats
'''
SOURCE_TO_TARGET_TOPICS = {}
