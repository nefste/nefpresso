import streamlit as st
from streamlit_ace import st_ace

st.set_page_config(
    page_title="About Me",
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


st.title("Stephan Nef")

st.markdown('<p class="css">Da kommt noch was...</p>', unsafe_allow_html=True)




code = st_ace(
    value="""print("Hello at Nefpresso!")""",
    language='python', 
    theme='tomorrow_night',
    tab_size= 4,
    font_size=16, height=120
)

html = f"""
<html>
  <head>
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
  </head>
  <body>
    <py-script>{code}</py-script>
  </body>
</html>
"""
# st.markdown('<p class="css">Output:</p>', unsafe_allow_html=True)
st.components.v1.html(html, height=200, scrolling=False)