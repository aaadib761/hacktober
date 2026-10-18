import time
import ollama
import streamlit as st

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
    "Teen": "Talk in a casual, friendly, validating way.",
    "Adult": "Talk in a warm, professional tone.",
    "Senior": "Talk slowly and patiently, using simple words.",
}

st.set_page_config(page_title="Wellness Buddy", page_icon="🌿")
st.title("🌿 Wellness Buddy")
st.caption(DISCLAIMER)

mode = st.sidebar.selectbox("Age mode", list(AGES))
mood = st.sidebar.slider("Mood today (1 = low, 5 = great)", 1, 5, 3)

if st.sidebar.button("Calm me down (box breathing)"):
    box = st.empty()
    for n in range(1, 4):
        for step in ["Breathe in", "Hold", "Breathe out", "Hold"]:
            box.info(f"Round {n}/3: {step}... (4 seconds)")
            time.sleep(4)
    box.success("Well done. How do you feel now?")

if "history" not in st.session_state:
    st.session_state.history = []

for m in st.session_state.history:
    with st.chat_message(m["role"]):
        st.write(m["content"])

text = st.chat_input("How are you feeling?")
if text:
    st.session_state.history.append({"role": "user", "content": text})
    with st.chat_message("user"):
        st.write(text)

    if any(w in text.lower() for w in CRISIS_WORDS):
        reply = CRISIS_REPLY
    else:
        system = {"role": "system",
          "content": f"{BASE} {AGES[mode]} The user rated their mood {mood}/5."}
        reply = ollama.chat(
            model=MODEL, messages=[system] + st.session_state.history
        )["message"]["content"]

    st.session_state.history.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
        st.markdown(
    "<style>.stAppDeployButton, .stDeployButton {display: none;}</style>",
    unsafe_allow_html=True,
)