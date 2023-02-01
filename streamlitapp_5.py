import streamlit as st
from PIL import Image
from transformers import pipeline

st.set_page_config(page_title="DTCC ChatGPT Demo", page_icon=":robot:", layout="wide")

st.title("A facial expression and sentiment analyzer")

sentiment_classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
facial_expression_classifier = pipeline("image-classification", model="Rajaram1996/FacialEmoRecog")

text_input = st.text_input("Enter your text")

if text_input:
    sentiment_analysis = sentiment_classifier(text_input)[0]["label"]
    st.write("Sentiment:", sentiment_analysis)

uploaded_file = st.file_uploader("Upload an image")

if uploaded_file:
    image = Image.open(uploaded_file)
    facial_expression = facial_expression_classifier(image)
    st.image(image, caption=f"The facial expression is: {facial_expression[0]["label"]}")
