#!/usr/bin/env python3
import sys, requests, json
nick = sys.argv[1]
LLM_API_URL = "http://LM-STUDIO-IP-ADDRESS:1234/v1/chat/completions" # replace with lm-studio's ip address
MODEL = "YOUR-MODEL"  # replace with the model you loaded in LM Studio
SYSTEM_PROMPT = ( f"Your name is {nick}. You are an IRC bot and your responses must not include emoji." ) # Set your eggdrop bots name
def query_lmstudio(text):
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ],
        # change response behavior.
    "temperature": 1,
    "presence_penalty": 1,
    "frequency_penalty": 1
    }
    r = requests.post(LLM_API_URL, json=payload)
    data = r.json()
    return data["choices"][0]["message"]["content"]

if __name__ == "__main__":
    user_nick = sys.argv[1]
    user_text = sys.argv[2]
    reply = query_lmstudio(user_nick, user_text)
    print(reply)
