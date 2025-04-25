import json

def beautify_json_response(json_str):
    data = json.loads(json_str)
    lines = []
    for key, value in data.items():
        lines.append(f"{key}: {value}")
    return "\n\n".join(lines)

# Test structure
json_str = '''{
  "serious_ideas": "Ernie, it’s time to face the music. ...",
  "serious_ideas_song": "The Night We Met by Lord Huron ...",
  "funny_ideas": "Hey Bert, remember that time ...",
  "funny_ideas_song": "I Will Survive by Gloria Gaynor ...",
  "wired_ideas": "How about we both take a spontaneous trip ...",
  "song_idea": "Breakup Song by Frances ...",
  "wired_ideas_song": "We Are Never Ever Getting Back Together by Taylor Swift ..."
}'''

#print(beautify_json_response(json_str))
