import streamlit as st
import transformers
from PIL import Image

# Load the sentiment classifier
sentiment_model = transformers.pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Load the image classification classifier
@st.cache
def load_model():
    model = transformers.pipeline("image-classification", model="Rajaram1996/FacialEmoRecog")
    return model
image_model = load_model()

# Define the Streamlit app
def main():
    st.set_page_config(page_title="DTCC ChatPGT Demo", page_icon=":smile:", layout="wide")
    st.title("A facial expression and sentiment analyzer")

    # Get the input text
    input_text = st.text_input("Enter a sentence to analyze sentiment:")

    # Predict the sentiment of the input text
    if input_text:
        sentiment = sentiment_model(input_text)[0]["label"].capitalize()
        st.write("Sentiment:", sentiment)

    # Get the input image
    uploaded_file = st.file_uploader("Upload an image to analyze facial expression:")

    # Predict the facial expression in the input image
    if uploaded_file:
        image = Image.open(uploaded_file)
        prediction = image_model(image)[0]
        st.write("Facial Expression:", prediction["label"])

if __name__ == "__main__":
    main()
