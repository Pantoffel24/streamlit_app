import streamlit as st

st.title('hello world')

intro_text = """
This is going to be a large block of text for testing purposes.

Do paragraphs work? Maybe. $\int x^2 dt$ here is an integral. Fascinating.
**bold text**

This is pretty cool. I can share my information online yippie!
"""
st.write(intro_text)