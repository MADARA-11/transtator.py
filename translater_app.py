import streamlit as st
from deep_translator import GoogleTranslator as gt


st.title("Language translator")
st.write('this help to translate')

text =st.text_area("Enter a text: ",height=150)
lang = gt().get_supported_languages()

s = st.selectbox("Enter a source lang",lang,)
t = st.selectbox("Enter a target lang", lang)


if st.button("Translate"):
    if text.strip()!= "":

        r = gt(source= s,target=t).translate(text)
        st.success(f"translate text :{r}")

    else:
        st.warning("Pls enter valid text")

