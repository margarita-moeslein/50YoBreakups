from twilio_api import send_whatsapp_message, fetch_latest_messages
import time


def set_interval(fn, sec):
    while True:
        time.sleep(sec)
        fn()


def breakup():
    print("break up all")

def main():
    message_to_send = input("Enter message to send via WhatsApp: ")
    send_whatsapp_message(message_to_send)
    fetch_latest_messages()


if __name__ == "__main__":
    # set_interval(breakup, 10)
    main()
