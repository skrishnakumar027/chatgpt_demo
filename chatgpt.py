import openai
import streamlit as st

# Set up the OpenAI API key
openai.api_key = "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"

# Define the GPT-3 engine and prompt
ENGINE = "text-davinci-002"
PROMPT = "Generate a response to the following input:\n{input_text}\n\nResponse:"

def generate_response(input_text):
    # Generate a response using GPT-3
    prompt = PROMPT.format(input_text=input_text)
    response = openai.Completion.create(engine=ENGINE, prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.7)
    return response.choices[0].text.strip()

def main():
    st.title("OpenAI GPT-3.5 Turbo Chatbot")

    # Ask user for input
    input_text = st.text_input("Enter your message here")

    # Generate response when user clicks the "Send" button
    if st.button("Send"):
        response = generate_response(input_text)
        st.text_area("Response", value=response)

if __name__ == "__main__":
    main()
