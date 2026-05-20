import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Language Translation Tool")

text = st.text_area("Enter text to translate")

source_lang = st.selectbox("Source Language", ["en", "te", "hi", "ta", "fr", "es"])
target_lang = st.selectbox("Target Language", ["te", "en", "hi", "ta", "fr", "es"])

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        st.success(translated)