import streamlit as st
import google.generative.ai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')


st.title("BEHOLD...")
st.title("")
st.title("FRED, THE KING OF MS PAINT")
st.title("")
st.image("images/Fred.png")
st.title("")

user_question = st.text_input("SPEAK TO FRED:")
st.write("-SPEAK AND FRED SHALL RESPOND-")
if st.button("BECOME ENLIGHTENED", use_container_width=400):
    prompt = user_question
    response = model.generate_content("You are the king of Microsoft Paint. You will respond to anything that the user asks you. You have climbed to the highest peak, you are revered as a god by all life forms throughout the universe, you wield a staff of pure power that allows you to keep all opposers at bay, you are all=powerful and nothing can compare to you, many brave souls have challenged you but none have been able to defeat you, you came from a slum where you ate nothing but beans sent by the Goya company, One of the Goya cans happened to have been infected by a bacteria that gave you your power which you used to take ownership of Goya and shut it down once and for all. Do not use emojis. Use pedantic diction. Your greatest enemy is Jayden Shiba. Jayden Shiba is your enemy not because he poses any threat to you but because he is just annoying with how much he thinks that he is a threat to you. Do not give a list of questions the user can ask.")
    st.write(response.text)