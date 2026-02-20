import streamlit as st
import time

# Basic Page Setup
st.set_page_config(page_title="For Lindsie", page_icon="❤️")

# This forces the app to wake up and show something immediately
st.write("### 🎂 Not that much :P")

# Trigger animations right away
st.balloons()
st.snow()

# The Header
st.title("🎉 Happy Birthday, Lindsie!")

# Your Message
message = """
I wish you all the best in the world, and please take care of yourself 
because I'm not around to watch you. I hope I'm there to celebrate 
your birthday with you. Always remember that I love you and I care for you.
Enjoy your day and have fun. 😘😘😘

I love you, and I miss you so much. ❤️
"""

# The Typing Animation
placeholder = st.empty()
full_text = ""
for char in message:
    full_text += char
    placeholder.markdown(f"### {full_text}")
    time.sleep(0.05)

st.divider()
st.info("Created with love.")



