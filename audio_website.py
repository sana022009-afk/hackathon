import subprocess
import webbrowser
import time
import psutil
import os
 
# 1. Your specific file path
video_path = r"https://github.com/sana022009-afk/hackathon/raw/refs/heads/main/Video%20Project%202.mp4"
web_url = "https://app.talkpal.ai/chat?modeType=main"
 
def run_sequence():
    if not os.path.exists(video_path):
        print("Error: Video file not found at the path provided.")
        return
 
    # 2. Launch the video and get a list of what's running BEFORE
    before_pids = {p.pid for p in psutil.process_iter()}
    os.startfile(video_path)
    print("Video launched. Identifying the player...")
    # Wait 3 seconds for the player to fully open
    time.sleep(3) 
    # 3. Find the NEW process (the video player)
    after_pids = {p.pid for p in psutil.process_iter()}
    new_pids = after_pids - before_pids
    # If we found the player's ID, we watch it
    if new_pids:
        player_pid = list(new_pids)[0]
        print(f"Tracking Video Player (ID: {player_pid}). Python is now WAITING...")
        # 4. Stay in this loop as long as the player is open
        while psutil.pid_exists(player_pid):
            time.sleep(1) # Check every 1 second
        print("Video player closed! Now opening your AI Tutor...")
        webbrowser.open(web_url)
    else:
        # Fallback: if we couldn't catch the PID, just wait for a manual key press
        print("Couldn't auto-detect player. Please close the video, then press ENTER here.")
        input()
        webbrowser.open(web_url)
 
run_sequence()
