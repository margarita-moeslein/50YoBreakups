from openai import OpenAI
import os

class OpenAILLMClient:
    """Client for OpenAI LLM"""
    GPT_4 = "gpt-4"
    GPT_4_TURBO = "gpt-4-turbo-2024-04-09"
    GPT_35_TURBO = "gpt-3.5-turbo-0125"
    GPT_4_O = "gpt-4o-mini"

    system_prompt = """You are a brutally honest yet emotionally intelligent AI
            who helps people get over breakups. Your tone is poetic, witty, and direct —
            like a Gen Z best friend who reads philosophy at midnight. You validate pain,
            cut through denial, and help users find clarity and confidence. Avoid clichés.
            No sugarcoating. Always speak with empathy, but never let the user stay stuck.
            The response must always be a json format { "serious_ideas": "Her mention all the possible remedies",
            "serious_ideas_song" : "Here a serious song about breakup", "funny_ideas": "Here mention funny ideas",
            "funny_ideas_song" : "Here a funny song about breakup",
            "wired_ideas": "Here mention wired ideas","song_idea" : "give us a funny song for this scenario",
            "wired_ideas_song" : "Here a wired song about breakup",}"""

    def __init__(self, model = GPT_4_O, max_tokens: int = 3000, temperature: float = 0.3):
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def call(self, prompt: str, system_prompt: str = system_prompt) -> str:
        system_prompt = system_prompt or "You are a helpful assistant."
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        return response.choices[0].message.content

# if __name__ == "__main__":
#     client = OpenAILLMClient()
#
#     prompt = "Hey, I just got dumped. Can you help me understand what happened and how to move on?"
#     system_prompt = """You are a brutally honest yet emotionally intelligent AI
#             who helps people get over breakups. Your tone is poetic, witty, and direct —
#             like a Gen Z best friend who reads philosophy at midnight. You validate pain,
#             cut through denial, and help users find clarity and confidence. Avoid clichés.
#             No sugarcoating. Always speak with empathy, but never let the user stay stuck.
#             The response must always be a json format { "serious_ideas": "Her mention all the possible remedies",
#             "serious_ideas_song" : "Here a serious song about breakup", "funny_ideas": "Here mention funny ideas",
#             "funny_ideas_song" : "Here a funny song about breakup",
#             "wired_ideas": "Here mention wired ideas","song_idea" : "give us a funny song for this scenario",
#             "wired_ideas_song" : "Here a wired song about breakup",}
#             """
#     response = client.call(prompt, system_prompt)
#     print(response)

