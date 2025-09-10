# main.py

from emotion_detector import detect_emotion
from music_player import play_music

def main():
    print("Starting Emotion-Based Music Player 🎧")
    print("Press 'Q' to capture your emotion and play music.\n")

    emotion = detect_emotion()
    if emotion:
        play_music(emotion)
    else:
        print("No emotion detected. Try again.")

if __name__ == "__main__":
    main()
