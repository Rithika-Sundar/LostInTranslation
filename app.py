import streamlit as st

corrections = {
    "I am having one doubt": "I have a question",
    "I will go and come": "I’ll be right back",
    "He is out of station": "He is out of town",
    "Do one thing": "Let me suggest something",
    "Pass out from college": "Graduate from college",
    "Today morning only I saw him": "I saw him this morning",
    "I didn’t took it": "I didn’t take it",
    "She is my cousin sister": "She is my cousin",
    "I am going to my native": "I am going to my hometown",
    "Give me missed call": "Give me a call",
    "Revert back to me": "Revert to me / Reply to me",
    "Prepone the meeting": "Move the meeting earlier",
    "Kindly do the needful": "Please take appropriate action",
    "Discuss about the topic": "Discuss the topic",
    "He is telling lie": "He is lying",
    "He is doing a course": "He is taking a course",
    "I am going for shopping": "I am going shopping"
}

def correct_indian_english(text):
    text_lower = text.lower()
    for phrase in corrections:
        if phrase.lower() in text_lower:
            return corrections[phrase]
    return "No correction needed. Looks good!"

st.set_page_config(page_title="Indian English Corrector", page_icon="📝")
st.title("📝 Indian-English Correction Tool")
st.markdown("Type a sentence in Indian English and get the standard English version.")

user_input = st.text_area("Enter your sentence:")

if st.button("Correct"):
    result = correct_indian_english(user_input)
    st.success(f"✅ Corrected Sentence:\n\n**{result}**")

st.markdown("---")
st.caption("Project by Rithika Sri S | AI/NLP | 2025")
