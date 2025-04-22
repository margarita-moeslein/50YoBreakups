# 💔 BreakupGPT

_“Because sometimes, the AI should end it for you.”_

BreakupGPT is a funny WhatsApp-based service that helps users end relationships with style, sarcasm, and memes. Powered by OpenAI, Twilio, and a touch of musical drama.

---

## 🎯 What It Does

BreakupGPT lets users send a message via WhatsApp and get back:
- 💬 A witty, AI-generated breakup message
- 🖼️ A breakup-themed meme or GIF
- 🎶 A song lyric or track that fits the mood

Because not every goodbye has to be awkward. Sometimes it just has to be hilarious.

---

## 📲 How to Use

1. **Send a WhatsApp message** to our bot
2. **Choose your content combo**: Text, Meme, Song (or all three)
3. **Optionally specify a breakup style**: funny, savage, sad, etc.
4. Get your personalized breakup kit sent right back to your phone

---

## 💡 Example

**You send:**  
> “I think we need to break up. He's obsessed with Star Wars.”

**BreakupGPT replies:**  
> “You're not my endgame. May the Force ghost be with you.”  
> 🎶 _"We are never ever getting back together..."_  
> 🖼️ ![Funny meme](https://example.com/meme.jpg)

---

## ⚙️ Tech Stack

- 🧠 OpenAI GPT (via `openai` Python SDK)
- 💬 Twilio Conversations API (WhatsApp support)
- 🎨 Imgflip API (for memes)
- 🐍 Python (polling-based backend, no Flask)
- 🔊 Optional: song snippets via YouTube or static links

---

## 🚀 Getting Started (Dev Setup)

1. Clone the repo  
2. Install dependencies:  
   ```bash
   pip install openai twilio python-dotenv
