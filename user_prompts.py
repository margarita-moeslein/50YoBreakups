class UserPrompts:

    user_prompts = ["👋 Welcome to the funniest BreakUP-Methods by BreakupGPT. I am an AI Generator"
                    "don't forget that! Or I will break up our relationship."
                    "First, I'll ask you a few questions to customize your breakup."                    
                    "Please give us your name and your ex partner if you like.",
                    "How long was your relationship and the reason for break up?",
                    "How do you want me to help you (e.g.  'Funny', 'Savage', 'Kind', 'Song lyric style')?"]

    
    USER_AI_PROMPT = """
    Hey, I need help creating a breakup message.
    - name of user and break up partner: {KEY1}
    - Relationship length and the end: {KEY2}
    - Tone: {KEY3}
    - if I want a song please let match it to my 
    individual entrees and do not double it, pay attention of my tone. One song should fit with the songtext, 
    one song should fit the Tone to my entrees.
    """
