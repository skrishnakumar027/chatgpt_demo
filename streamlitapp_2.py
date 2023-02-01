import streamlit as st
from transformers import pipeline
import PIL.Image
import requests

# Initialize the sentiment classifier
sentiment_classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Initialize the facial expression classifier
facial_expression_classifier = pipeline("image-classification", model="Rajaram1996/FacialEmoRecog")

def classify_sentiment(text):
    return sentiment_classifier(text)[0]['label']

def classify_facial_expression(image_url):
    image = PIL.Image.open(requests.get(image_url, stream=True).raw)
    return facial_expression_classifier(image)[0]['label']

st.set_page_config(page_title="DTCC ChatGPT Demo", page_icon=":smile:", layout="wide")

st.title("A facial expression and sentiment analyzer")

text = st.text_input("Enter text to analyze sentiment")

if text:
    sentiment = classify_sentiment(text)
    st.write("Sentiment: ", sentiment)

image_url = st.text_input("Enter image URL to analyze facial expression")

if image_url:
    facial_expression = classify_facial_expression(image_url)
    st.write("Facial Expression: ", facial_expression)