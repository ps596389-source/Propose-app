import streamlit as st
import random

# Page configuration
st.set_page_config(page_title="Ek Sawal...", page_icon="❤️")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #ffe6e6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Hi [suruchi]! ❤️")
st.header("Mujhe tumse kuch kehna hai...")

st.write("Hum jab se mile hain, meri life badal gayi hai. Kya tum meri life ka permanent hissa banogi?")

col1, col2 = st.columns(2)

with col1:
    if st.button("YES! 😍"):
        st.balloons()
        st.success("I love you too! ❤️ Main duniya ka sabse khush-kismat insaan hoon!")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHIyb3RrZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4ZzR4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCBmcm9tX2dpZl9zZWFyY2hfcmVzdWx0cyZjdD1n/KztT2c4u8mYYUiCi7W/giphy.gif")

with col2:
    no_clicked = st.button("No 😢")
    if no_clicked:
        st.warning("Oops! Try again... Ye button kaam nahi kar raha! 😉")
