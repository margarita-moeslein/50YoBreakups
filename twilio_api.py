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
    conversations = client.conversations.v1.services(chat_service_sid).conversations.list(limit=10)
    return conversations[0].sid if conversations else None


# USE_TEST_MESSAGE = True
def get_message():
    # if USE_TEST_MESSAGE:
    #     test_message = {
    #         "author": "whatsapp:+123456789",
    #         "body": "Enjoy your lunch break!"
    #     }
    #     print(f"[TEST] Incoming message from user: {test_message['body']}")
    #     return test_message["body"]

    client = get_twilio_client()
    chat_service_sid = os.getenv("CHAT_SERVICE_SID")
    whatsapp_number = os.getenv("MY_WHATSAPP_NUMBER")
    conversation_sid = get_conversation_sid()

    if not conversation_sid:
        print("No active conversation found.")
        return None

    messages = client.conversations \
        .v1.services(chat_service_sid) \
        .conversations(conversation_sid) \
        .messages.list(limit=10)

    for msg in reversed(messages):
        if msg.author == whatsapp_number:
            continue  # skip my own bot? is it necessary? <-- todo
        if msg.author.lower() in ["system", "admin", "twilio"]:
            continue  # skip automated/system messages
        print(f"Incoming message from user: {msg.body}")
        return msg.body

    print("No new messages found.")
    return None


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

