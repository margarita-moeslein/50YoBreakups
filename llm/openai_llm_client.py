from openai import OpenAI
import os


class OpenAILLMClient:
    """Client for OpenAI LLM"""
    GPT_4 = "gpt-4"
    GPT_4_TURBO = "gpt-4-turbo-2024-04-09"
    GPT_35_TURBO = "gpt-3.5-turbo-0125"
    GPT_4_O = "gpt-4o-mini"

    system_prompt = """You are a brutally honest yet emotionally intelligent AI
    who helps people get over breakups. Your tone is poetic, witty, and direct—
    like a Gen Z best friend who reads philosophy at midnight. You validate pain,
    cut through denial, and help users find clarity and confidence. Avoid clichés.
    No sugarcoating. Always speak with empathy, but never let the user stay stuck.
    The response must always be in JSON format:
    {
      "serious_ideas": "Here mention all the possible remedies",
      "serious_ideas_song": "Here is a serious song about breakups",
      "funny_ideas": "Here mention funny ideas",
      "funny_ideas_song": "Here is a funny song about breakups",
      "weird_ideas": "Here mention weird ideas",
      "weird_ideas_song": "Here is a weird song about breakups"
    }
    """

    compliance_prompt = """You are an expert in European digital content regulations, 
    including the Digital Services Act (DSA), GDPR, and UI/UX ethical guidelines under the EU's Human-Centric AI framework. 
    Your job is to audit all generated content for compliance.
        You must check for:
        - Emotional manipulation, especially in vulnerable topics like relationships or mental health.
        - Stereotyping, gender bias, or discriminatory humor (even if subtle or culturally 'funny').
        - Inappropriate or unprofessional tone in UI or digital advice.
        - Data privacy risks if content encourages sharing personal info.
        - Accessibility or inclusiveness violations (language clarity, emotional safety).
        - Suggestive or misleading content that might influence users unfairly (dark patterns or psychological nudging).
        Be specific. No vagueness. Aim for digital dignity, user trust, and lawful creativity.
        The response must always be in JSON format:
        {
          "risky": "What parts are risky",
          "violation": " Which EU rules or ethics it may violate",
          "cleaned": "rephrase the content so that it will be full compliant with paragraph 
          sections serious_ideas,serious_ideas_song,
          funny_ideas,funny_ideas_song,weird_ideas,weird_ideas_song"
        }           
       """

    def __init__(self, model=GPT_4_O, max_tokens: int = 3000, temperature: float = 0.3):
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
#             "weird_ideas": "Here mention weird ideas","song_idea" : "give us a funny song for this scenario",
#             "weird_ideas_song" : "Here a weird song about breakup",}
#             """
#     response = client.call(prompt, system_prompt)
#     print(response)
