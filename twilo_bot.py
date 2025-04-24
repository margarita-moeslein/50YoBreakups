import os
import time
from twilio.rest import Client
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone


class TwilioBot:
    def __init__(self, process_callback, poll_interval=5  ):
        load_dotenv()
        self.poll_interval = poll_interval
        self.process_callback = process_callback
        self.chat_service_sid = os.getenv("CHAT_SERVICE_SID")

        self.client = self.get_twilio_client()
        self.service = self.client.conversations.v1.services(self.chat_service_sid)

        self.processed_messages = set()
        self.processed_messages_dict = {}
        self.responded_conversations = set()

    def get_twilio_client(self):
        return Client(
            os.getenv("API_KEY_SID"),
            os.getenv("API_KEY_SECRET"),
            os.getenv("ACCOUNT_SID")
        )

    def poll_messages(self):
        print("Polling messages...")
        try:
            while True:
                self.check_new_messages()
                time.sleep(self.poll_interval)
        except Exception as e:
            print(f"[ERROR] {e}")

    def check_new_messages(self):
        conversations = self.service.conversations.list()
        for convo in conversations:            
            
            messages = convo.messages.list()
            for msg in messages:
                if msg.sid not in self.processed_messages:
                    self.processed_messages.add(msg.sid)
                    print(f"[NEW] {msg.author}: {msg.body}")
                    self.processed_messages_dict[msg.sid] = {
                        "author": msg.author,
                        "body": msg.body,
                        "conversation": convo,
                        "date_created": msg.date_created,
                        "date_updated": msg.date_updated                        
                    }
                    
                    # Use timezone-aware datetime for now()
                    thirty_minutes_ago = datetime.now(timezone.utc) - timedelta(minutes=1)
                    #check the message only form the last 30 minutes
                    if msg.date_created > thirty_minutes_ago:
                        #Trigger the application process     
                        self.process_callback(self, msg.sid)
   

    def get_new_messages(self, convo):
        new_messages = []
        messages = convo.messages.list()
        for msg in messages:
            if msg.sid not in self.processed_messages:
                self.processed_messages.add(msg.sid)
                new_messages.append(msg)
                #Trigger the application process                
                # how can i have a callback here to the main.py method??
                self.processed_messages_dict[msg.sid] = {
                    "author": msg.author,
                    "body": msg.body,
                    "conversation": convo
                }  
                self.process_callback(self ,msg.sid)
        return new_messages

    def send_message(self, processed_message: dict, message_to_send: str):
        convo = processed_message["conversation"]
        author = processed_message["author"]
        body = processed_message["body"]
        
        
        # if convo.sid in self.responded_conversations:
        #     return

        convo.messages.create(
            author="BreakupGPT",
            body= message_to_send
        )
        print(f"[AUTO-REPLY] Sent to conversation {convo.sid}")
        self.responded_conversations.add(convo.sid)

    def start(self):
        self.poll_messages()


