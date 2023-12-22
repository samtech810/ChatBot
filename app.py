import openai
import json
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(layout="centered", page_icon="🤖", page_title="ChatBot")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
lottie_animation = load_lottiefile("ChatBot/Animation.json")

st_lottie(lottie_animation)
st.title("!!!وووووووي السلعة")

    


openai.api_key = st.secrets["OPENAI_API_KEY"]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

# for message in st.session_state.messages:
    
#     with st.chat_message(message["role"]):
#          st.markdown(message["content"])
         
    
                

if prompt := st.chat_input("صافا شوية ؟"):
    st.session_state.messages.append({"role": "user","content": prompt})
    with st.chat_message("user", avatar="🇩🇿"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        message_placeholder = st.empty()
        
            
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
hide_streamlit_style = """

            <style>

            #MainMenu {visibility: hidden;}

            footer {visibility: hidden;}

            </style>

            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)