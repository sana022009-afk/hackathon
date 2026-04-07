import streamlit as st

# PASTE YOUR NEW RAWCDN LINK HERE
VIDEO_URL = "https://rawcdn.githack.com/YOUR_USER/YOUR_REPO/MAIN/Video%20Project%202.mp4"
AI_TUTOR_URL = "https://app.talkpal.ai/chat?modeType=main"

st.set_page_config(page_title="AI Tutor", layout="centered")
st.title("🎬 AI Tutor Video Lesson")

# The video player
if VIDEO_URL == "https://rawcdn.githack.com/sana022009-afk/hackathon/refs/heads/main/Video%20Project%202.mp4":
    st.warning("Please update the VIDEO_URL in your code with the link from Githack!")
else:
    # We use st.video and tell it the format is mp4
    st.video(VIDEO_URL, format="video/mp4")

st.markdown("---")

st.write("Done watching? Click below to start your session.")
st.link_button("🚀 Open AI Tutor (TalkPal)", AI_TUTOR_URL, type="primary")
