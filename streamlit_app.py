import streamlit as st
from gtts import gTTS
import os

def text_to_speech(text, language='vi'):
    tts = gTTS(text, lang=language)
    tts.save("output.mp3")

    # Play the generated audio using your system's default audio player
    # os.system("mpg321 output.mp3")  # For Linux
    # os.system("afplay output.mp3")  # For macOS
    # os.system("start output.mp3")  # For Windows
    return "output.mp3"


# Define text translations for English and Vietnamese
translations = {
    'en': {
        'enter_text': "Enter text for speech conversion:",
        'speak_button': "Speak",
    },
    'vi': {
        'enter_text': "Nhập văn bản để chuyển đổi thành tiếng nói:",
        'speak_button': "Phát âm",
    }
}

st.title("Text to Speech Converter")
language = st.selectbox("Select language:", ('en', 'vi'))

user_input = st.text_area(translations[language]['enter_text'])

if st.button(translations[language]['speak_button']):
    if user_input:
        audio_file = text_to_speech(user_input, language)
        st.audio(audio_file, format="audio/mp3")

# Cleanup audio file
if os.path.exists("output.mp3"):
    os.remove("output.mp3")

