import streamlit as st
import torch
from transformers import pipeline
from PIL import Image

st.set_page_config(page_title="DTCC ChatPGT Demo", page_icon=":guardsman:", layout="wide")
st.title("A facial expression and sentiment analyzer")

# Sentiment classifier
st.subheader("Sentiment Analyzer")
sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
text = st.text_input("Enter your text:")
if text:
    sentiment = sentiment_model(text)[0]["label"]
    st.write(f"The sentiment of the text is: {sentiment}")

# Facial expression classifier
st.subheader("Facial Expression Analyzer")
image_file = st.file_uploader("Upload an image of a face:")
if image_file:
    image = Image.open(image_file)
    facial_expression_model = pipeline("image-classification", model="Rajaram1996/FacialEmoRecog")
    facial_expression = facial_expression_model(image)[0]["label"]
    st.image(image, caption=f"The facial expression is: {facial_expression}")

