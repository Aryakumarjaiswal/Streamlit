import streamlit as st
#Title
#st.title('### MaitriAI CHATBOT')#Font size can't be controlled
st.image('./MaitriLogo.png')
st.markdown('## CHATBOT👍')
st.header("Welcome")
st.subheader("How Can I help you")
st.info("Hi there I'm mini-bot \n..Feel Free to ask questions \n in Chatbox by uploading the image")

st.write(' MaitriAI is Startup that provides Technolgy based solution to their client')
st.warning('Please be socially responsible.')
st.file_uploader("Choose an image...", type="jpg")
st.chat_input('Your Message')

st.markdown('Please Share your Valuable feedback!!!')
st.select_slider('Rating',['Bad','Average','Good','Excellent','Outstanding'])
st.text_input("Suggessions Please!!")
st.balloons()
