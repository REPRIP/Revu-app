import streamlit as st
import google.generativeai as genai

# Configure the Gemini model API key
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

# Streamlit app layout
st.title("Product Review Analyzer")

# Input field for the product link or name
user_input = st.text_input("Enter Product name:")

# Button to trigger review analysis
if st.button("Get Reviews"):
    if user_input:
        # Request to the model to generate content about the product reviews
        response = model.generate_content(f"How are the reviews of this product: {user_input}. You are requested to cite the sources at the last")
        
        # Display the response
        st.write("Product Reviews:")
        st.write(response.text)
    else:
        st.warning("Please enter a valid product link or name.")
