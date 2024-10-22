import streamlit as st
import azure.cognitiveservices.speech as speechsdk

def speech_to_text():
    speech_config = speechsdk.SpeechConfig(subscription="4749098b-74b0-4985-9ec8-5a7fde952795", region="India")
    audio_input = speechsdk.AudioConfig(use_default_microphone=True)
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
    
    st.write("Say something...")
    result = recognizer.recognize_once()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        st.write("Recognized: {}".format(result.text))
    else:
        st.write("No speech recognized")

st.title("ClearDysarthric")
if st.button("Record Speech"):
    speech_to_text()
