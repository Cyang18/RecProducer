import os
from dotenv import load_dotenv 

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secert = os.getenv("CLIENT_SECERT")

print(client_id, client_secert)
