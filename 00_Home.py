import streamlit as st


st.set_page_config(
    page_title="Hello",
    page_icon="👨🏻‍💻",
)


streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Roboto';
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


st.title('Nefpresso')

st.markdown('<p class="css">Hello World und so...</p>', unsafe_allow_html=True)


## LOGIN just for fun:
# dial = st.dialog("Login", close_on_submit=False)
# with dial:
#     name = st.text_input("Enter Name")
#     password = st.text_input("Enter Password")
#     if st.form_submit_button("Submit"):
#         if name != "Stephan" :
#             st.error("Sorry, heute nicht...")
#         else:
#             dial.close()
# name = None

# if name is None :
#     dial.open()
    