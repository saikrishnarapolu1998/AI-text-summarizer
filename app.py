import streamlit as st
from transformers import pipeline

st.title("AI Text Summarizer")

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

text = st.text_area("Enter your text")

if st.button("Summarize"):
    if text:
        summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
        st.subheader("Summary")
        st.write(summary[0]["summary_text"])
