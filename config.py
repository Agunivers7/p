import re, os

id_pattern = re.compile(r'^.\d+$')


# Bot information
API_ID = 10651048

API_HASH = os.environ.get("API_HASH", "37775aca7d11f450ecde375baac17fe7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5694266322:AAFuhovA-kFby3QNJjTlGUttDxWtYUNdYuA") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Aguniversmovie") 

DB_NAME = os.environ.get("DB_NAME","qwerty")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Aadhi:42426840@cluster0.jqzpafx.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/a6fe48dd57f2a7f929c28.jpg")

ADMIN = os.environ.get("ADMIN", "1323557247") 
