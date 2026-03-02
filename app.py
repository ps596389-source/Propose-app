import streamlit as st

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

# Aapki GF ka naam yahan likhein
st.title("Hi Suruchi! ❤️") 
st.header("Mujhe tumse kuch kehna hai...")

st.write("Hum jab se mile hain, meri life badal gayi hai. Kya tum mujhse shaadi krogi?")

col1, col2 = st.columns(2)

with col1:
    if st.button("YES! 😍"):
        st.balloons()
        st.success("I love you meri jaan!❤️ Main tumko bhaut pyaar krunga jaise krta hu abhi bhi!")
        
        # Aapka bheja hua photo link yahan add kar diya hai
        st.image("https://i.ibb.co/L6vXFmS/4w-Zb-NPt.jpg")
        

with col2:
    no_clicked = st.button("No 😢")
    if no_clicked:
        st.warning("ye dabane pr thappad khaogi babu tum😒")
