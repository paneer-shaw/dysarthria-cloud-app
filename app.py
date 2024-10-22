import streamlit as st
#import azure.cognitiveservices.speech as speechsdk
#FBFBFA
st.markdown(
    """
    <style>
    .main {
        background-color: #FBFBFA;
    }
    .banner {
        background-color: #014149; 
        color: white; 
        text-align: center; 
        font-size: 24px; 
        font-family: 'Helvetica',sans-serif;
        font-weight: bold; 
        border-radius: 8px; 
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="banner">ClearDysarthric</div>', unsafe_allow_html=True)
st.write("We aim to help people with dysarthria communicate.")
st.subheader('Project Objectives')
st.markdown("""- Helping people understand dysarthric speech
            - Using cloud services
            - Building a user-friendly, assistive tech that allows accessibility""")
