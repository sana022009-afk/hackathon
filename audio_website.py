import streamlit as st

# Use the link from raw.githack.com here!
VIDEO_URL = "https://rawcdn.githack.com/your-username/your-repo/main/Video%20Project%202.mp4" 
AI_TUTOR_URL = "https://app.talkpal.ai/chat?modeType=main"

st.set_page_config(page_title="AI Tutor", layout="centered")

st.title("🎬 AI Tutor Video Lesson")

# 1. Improved Video Player
# We add 'format' to tell the browser exactly what it is
st.video(VIDEO_URL, format="video/mp4")

st.markdown("---")

# 2. Improved Redirect (New Tab Method)
st.write("Done watching? Click below to start your session.")

# Using a link styled as a button is much more reliable than a script redirect
st.link_button("🚀 Open AI Tutor (TalkPal)", AI_TUTOR_URL, type="primary")

st.info("Note: The AI Tutor will open in a new tab so you don't lose this page.")
