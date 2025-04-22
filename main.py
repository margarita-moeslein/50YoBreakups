from twilio.rest import Client
from dotenv import load_dotenv
import os
import pprint

load_dotenv()
account_sid = os.getenv("ACCOUNT_SID")
api_sid = os.getenv("API_KEY_SID")
api_secret = os.getenv("API_KEY_SECRET")
client = Client(api_sid, api_secret, account_sid)
chat_service_sid = os.getenv("CHAT_SERVICE_SID")


conversations = client.conversations.v1.services(
chat_service_sid
).conversations.list()

for record in conversations:
    print(record)

# pprint.pp(conversations)

message = (
    client.conversations.v1.services(chat_service_sid)
    .conversations("CHee9f39a7f22a4e3cb59d36def28b93b7")
    .messages.create()
)

print(message)


def main():
    pass


if __name__ == "__main__":
    main()