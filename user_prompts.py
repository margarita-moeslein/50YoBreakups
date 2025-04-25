class UserPrompts:
    user_prompts = [
        "👋 Welcome to the funniest BreakUP-Methods by BreakupGPT. "
        "I am an AI Generator — don't forget that! Or I might break up with you. \n\n"
        "First, I'll ask you a few questions to customize your breakup. Please tell us your name and, if you like, "
        "your ex-partner's name.",
        "How long was your relationship, and what is the reason for the breakup?",
        "How would you like me to help you (e.g., 'Funny', 'Savage', 'Kind', 'Song lyric style')?"
    ]

    #print(user_prompts)

    
    USER_AI_PROMPT = """
    Hey, I need help creating a breakup message.
    - Name of user and breakup partner: {KEY1}
    - Relationship length and reason for breakup: {KEY2}
    - Tone: {KEY3}
    - If I want a song, please match it to my individual entries and do not duplicate it. Pay attention to my tone. 
      One song should fit the lyrics, and one song should fit the tone of my entries.
    """

   #print(USER_AI_PROMPT)
