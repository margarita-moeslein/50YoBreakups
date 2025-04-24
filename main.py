from twilio_api import send_whatsapp_message, fetch_latest_messages

def main():
    #message_to_send = input("Enter message to send via WhatsApp: ")
    message_to_send = "something random"
    send_whatsapp_message(message_to_send)
    fetch_latest_messages()


if __name__ == "__main__":
    # get_message() ---> Message from user
    # here define logic layer
    # here define OpenAI Layer ---> json respone
    # send_message() ----> Message to user
    main()
