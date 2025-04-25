import json

from twilio_api import send_whatsapp_message, fetch_latest_messages
from twilo_bot import TwilioBot
from user_prompts import UserPrompts
from llm import OpenAILLMClient
from beautify_json import beautify_json_response

USER_CALL_STACK = {}


# user_something[msg_sid] = {"prompt_count": 0 , "prompt_response": []}

def main_callback(bot: TwilioBot, msg_sid):
    """Main callback function to handle the message"""
    print(f"[MAIN] Processing message {msg_sid}")
    user_message = bot.processed_messages_dict[msg_sid]["body"]
    print(f"[MAIN] User message: {user_message}")

    author = bot.processed_messages_dict[msg_sid]["author"]
    if author == "BreakupGPT":
        return

    response = breakup_operations(bot, msg_sid, author, user_message)
    bot.send_message(bot.processed_messages_dict[msg_sid], response)


def breakup_operations(bot, msg_sid, author, user_message):
    """Function to handle the breakup operations"""
    response = ""
    user_session = USER_CALL_STACK.get(author, {})

    if user_session.get("prompt_count", 0) <= len(UserPrompts.user_prompts) - 1:
        if USER_CALL_STACK.get(author):
            user_session["prompt_response"].append(user_message)
            prompt = UserPrompts.user_prompts[user_session["prompt_count"]]
        else:
            user_session = {"prompt_count": 0, "prompt_response": []}
            prompt = UserPrompts.user_prompts[user_session["prompt_count"]]
            USER_CALL_STACK[author] = user_session
        response = prompt
        user_session["prompt_count"] += 1
    else:
        user_session["prompt_response"].append(user_message)
        ai_prompt = UserPrompts.USER_AI_PROMPT.format(KEY1=user_session["prompt_response"][0]
                                                      , KEY2=user_session["prompt_response"][1],
                                                      KEY3=user_session["prompt_response"][2])
        print(f"[MAIN] AI prompt: {ai_prompt}")
        open_ai = OpenAILLMClient()
        response = open_ai.call(prompt=ai_prompt)

        print(f"[OPENAI] Response: {response}")
        cleaned_response = open_ai.call(system_prompt=OpenAILLMClient.compliance_prompt, prompt=response)

        cleaned_json = json.loads(cleaned_response)
        risk = cleaned_json.get("risky", "")
        violation = cleaned_json.get("violation", "")
        cleaned = cleaned_json.get("cleaned", "")
        if risk:
            bot.send_message(bot.processed_messages_dict[msg_sid], "EU Law Risk - " + risk)
        if violation:
            bot.send_message(bot.processed_messages_dict[msg_sid], "EU Law Violations - " + violation)
        if cleaned:
            response = beautify_json_response(json.dumps(cleaned))
        else:
            response = beautify_json_response(response)

        print(f"[Compliance] Response: {response}")
        user_session["prompt_response"].append(response)

    return response


if __name__ == "__main__":
    """Main function to start the bot"""
    bot = TwilioBot(process_callback=main_callback)
    bot.start()
