
import streamlit as st
from transformers import pipeline

st.title("📝 Text Summarization Using LLM")

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="Qwen/Qwen3-0.6B")

text = st.text_area("Enter your text")

if st.button("Generate Summary"):
    if text.strip():
        model = load_model()
        prompt = (
            "Summarize this text in 2 short sentences. "
            "Return only the summary.\n" + text
        )
        result = model(
            prompt,
            max_new_tokens=60,
            do_sample=False,
            return_full_text=False
        )
        st.subheader("Generated Summary")
        st.write(result[0]["generated_text"])
    else:
        st.warning("Please enter some text.")
