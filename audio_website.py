import streamlit as st

# Use the URL you got from Phase 4 of the previous steps
VIDEO_URL = "https://raw.githubusercontent.com/your-username/your-repo/main/Video%20Project%202.mp4"
AI_TUTOR_URL = "https://app.talkpal.ai/chat?modeType=main"

st.title("AI Tutor Video Lesson")

# 1. Display the video
st.video(VIDEO_URL)

# 2. Add the button to move to the next step
if st.button("I've finished the video! Go to AI Tutor"):
    # This line performs the redirect in the browser
    st.write(f'<meta http-equiv="refresh" content="0;url={AI_TUTOR_URL}">', unsafe_allow_html=True)
    st.success("Redirecting to TalkPal...")
