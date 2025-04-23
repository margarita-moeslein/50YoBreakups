from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()


def get_twilio_client():
    return Client(
        os.getenv("API_KEY_SID"),
        os.getenv("API_KEY_SECRET"),
        os.getenv("ACCOUNT_SID")
    )

def get_conversation_sid():
    client = get_twilio_client()
    chat_service_sid = os.getenv("CHAT_SERVICE_SID")

    conversations = client.conversations \
        .v1.services(chat_service_sid) \
        .conversations \
        .list(limit=10)

    if not conversations:
        print("No active conversations found.")
        return None

    latest = conversations[0]  # todo maybe - add logic to filter if needed
    print(f"Latest conversation SID: {latest.sid} | Name: {latest.friendly_name}")
    return latest.sid


def send_whatsapp_message(body_text):
    client = get_twilio_client()
    chat_service_sid = os.getenv("CHAT_SERVICE_SID")
    whatsapp_number = os.getenv("MY_WHATSAPP_NUMBER")
    conversation_sid = get_conversation_sid()

    if not conversation_sid:
        print("Could not find a valid conversation SID.")
        return

    message = (
        client.conversations.v1.services(chat_service_sid)
        .conversations(conversation_sid)
        .messages.create(author=whatsapp_number, body=body_text)
    )

    print(f"Sent message: {message.sid} | Text: {body_text}")


def fetch_latest_messages(limit=5):
    client = get_twilio_client()
    chat_service_sid = os.getenv("CHAT_SERVICE_SID")
    conversation_sid = get_conversation_sid()

    if not conversation_sid:
        print("Could not find a valid conversation SID.")
        return

    messages = client.conversations \
        .v1.services(chat_service_sid) \
        .conversations(conversation_sid) \
        .messages.list(limit=limit)

    print("\nLatest messages:")
    for msg in reversed(messages):
        print(f"{msg.author}: {msg.body}")

