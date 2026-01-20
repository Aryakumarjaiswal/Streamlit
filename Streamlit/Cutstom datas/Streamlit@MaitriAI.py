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
chai = st.selectbox("Your fav chai: ", ["Masala chai", "Lemon Tea", "Adrak Chai", "Kesar Chai"])#Your.. will be output and dropdown will come for selecting 1
st.write(f"Your choose {chai}. Excellent choise")

st.success("Your chai has been brewed")
cups = st.number_input("How many cups", min_value=1, max_value=10, step=1)
st.write(f"Selected sugar level {cups}")
tea_type = st.radio("Pick your chai base: ", ["Milk", "Water", "Almond Milk"])
st.write(f"Selected base {tea_type}")
st.markdown('Please Share your Valuable feedback!!!')
st.select_slider('Rating',['Bad','Average','Good','Excellent','Outstanding'])
st.text_input("Suggessions Please!!")
dob = st.date_input("Select your date of birth")#Select.... will be displayed asking for selecting date
st.write(f"Your date of birth {dob}")#
st.balloons()




