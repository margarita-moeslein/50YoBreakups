from twilio_api import send_whatsapp_message, fetch_latest_messages
from twilo_bot import TwilioBot
from user_prompts import UserPrompts
from llm import OpenAILLMClient

def main():
    message_to_send = "something random"
    send_whatsapp_message(message_to_send)
    fetch_latest_messages()

user_something = {}
#user_something[msg_sid] = {"prompt_count": 0 , "prompt_response": []}

def main_callback(bot : TwilioBot, msg_sid):
    print(f"[MAIN] Processing message {msg_sid}")
    user_message = bot.processed_messages_dict[msg_sid]["body"]
    print(f"[MAIN] User message: {user_message}")

    author = bot.processed_messages_dict[msg_sid]["author"]
    if author == "BreakupGPT":
        return

    user_session = user_something.get(author, {})

    if user_session.get("prompt_count", 0) <= len(UserPrompts.user_prompts) -1:
        if user_something.get(author):
            user_session["prompt_response"].append(user_message)
            prompt = UserPrompts.user_prompts[user_session["prompt_count"]]
        else:
            user_session = {"prompt_count": 0 , "prompt_response": []}
            prompt = UserPrompts.user_prompts[user_session["prompt_count"]]
            user_something[author] = user_session
        message_to_send = prompt
        user_session["prompt_count"] += 1
    else:
        user_session["prompt_response"].append(user_message)
        ai_prompt = UserPrompts.USER_AI_PROMPT.format(KEY1=user_session["prompt_response"][0]
                                                        ,KEY2=user_session["prompt_response"][1],
                                                        KEY3=user_session["prompt_response"][2])
        open_ai = OpenAILLMClient()
        response = open_ai.call(prompt=ai_prompt)
        message_to_send = response

    bot.send_message(bot.processed_messages_dict[msg_sid], message_to_send)
    

if __name__ == "__main__":
    UserPrompts

    bot = TwilioBot(process_callback=main_callback)
    bot.start()
    #main()
