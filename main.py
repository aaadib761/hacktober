import time
import ollama

MODEL = "llama3.2:1b"
DISCLAIMER = "I'm an AI companion, not a substitute for professional care."

CRISIS_WORDS = ["suicide", "kill myself", "self harm", "self-harm",
                "end my life", "want to die"]
CRISIS_REPLY = ("I'm really sorry you're hurting. You deserve real support. "
                "Please talk to someone you trust or contact a local "
                "helpline right now.")

BASE = ("You are a supportive wellness companion, not a therapist or doctor. "
        "Never diagnose or give medication advice. Reply in 2-3 short "
        "sentences and suggest one small healthy action.")

AGES = {
    "1": ("Teen", "Talk in a casual, friendly, validating way."),
    "2": ("Adult", "Talk in a warm, professional tone."),
    "3": ("Senior", "Talk slowly and patiently, using simple words."),
}


def breathing():
    input("Box breathing: 3 rounds. Press Enter when ready.")
    for n in range(1, 4):
        print(f"Round {n}")
        for step in ["Breathe in", "Hold", "Breathe out", "Hold"]:
            print(f"  {step}... (4 seconds)")
            time.sleep(4)
    print("Well done. How do you feel now?")


def main():
    print(DISCLAIMER)
    print("Pick an age mode: 1) Teen  2) Adult  3) Senior")
    name, tone = AGES.get(input("> ").strip(), AGES["2"])
    print(f"{name} mode. Type 'calm' for a breathing exercise, 'q' to quit.")

    history = [{"role": "system", "content": f"{BASE} {tone}"}]
    while True:
        text = input("\nHow are you feeling? ").strip()
        if text.lower() == "q":
            break
        if text.lower() == "calm":
            breathing()
            continue
        if any(w in text.lower() for w in CRISIS_WORDS):
            print(CRISIS_REPLY)
            continue
        history.append({"role": "user", "content": text})
        reply = ollama.chat(model=MODEL, messages=history)["message"]["content"]
        history.append({"role": "assistant", "content": reply})
        print(reply)


main()