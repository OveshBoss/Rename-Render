# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "23903140")

API_HASH = os.environ.get("API_HASH", "579f1bcf3eac1660d81ef34b09906012")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8541817576:AAGxlZEr--4ETbKqm2Lxbk0wZcL9eGrkP_c") 

FORCE_SUB = os.environ.get("FORCE_SUB", "VJ_Botz") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://Ovesh:ovesh.boss@ovesh.95jpp8g.mongodb.net/?retryWrites=true&w=majority&appName=Ovesh")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/12082ded31fcbd636e36b-fd8a81ec21d987a646.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1416433622').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
