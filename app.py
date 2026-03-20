import streamlit as st
from transformers import pipeline

st.title("AI Text Summarizer")

text = st.text_area("Enter your text")

max_len = st.slider("Max Summary Length", 50, 200, 100)
min_len = st.slider("Min Summary Length", 10, 100, 30)

if st.button("Summarize"):
    if text:
        with st.spinner("Summarizing..."):
            summarizer = pipeline("summarization")
            summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)

        st.subheader("Summary")
        st.write(summary[0]["summary_text"])
        st.write("Original Length:", len(text.split()))
        st.write("Summary Length:", len(summary[0]["summary_text"].split()))
