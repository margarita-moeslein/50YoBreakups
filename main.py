from twilio_api import get_message, send_whatsapp_message, fetch_latest_messages

def main():
    user_message = get_message()
    if not user_message:
        return

    response = f"I'm testing: {user_message}"
    send_whatsapp_message(response)
    fetch_latest_messages()


if __name__ == "__main__":
    # get_message() ---> Message from user
    # here define logic layer

    # here define OpenAI Layer ---> json response
    # send_message() ----> Message to user
    main()
