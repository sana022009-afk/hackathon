import streamlit as st

# 1. Your specific Githack link
VIDEO_URL = "https://rawcdn.githack.com/sana022009-afk/hackathon/refs/heads/main/Video%20Project%202.mp4"
AI_TUTOR_URL = "https://app.talkpal.ai/chat?modeType=main"

st.set_page_config(page_title="AI Tutor", layout="centered")
st.title("🎬 AI Tutor Video Lesson")

# 2. The Fixed Logic: Play the video if the URL is set
if VIDEO_URL:
    # This will now play the video properly
    st.video(VIDEO_URL, format="video/mp4")
else:
    st.warning("Video URL is missing. Please check your code!")

st.markdown("---")

st.write("Done watching? Click below to start your session.")
st.link_button("🚀 Open AI Tutor (TalkPal)", AI_TUTOR_URL, type="primary")
