import streamlit as st
import google.generativeai as genai

# Configure the GenAI with the API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def generate_email_response(email_content, subject, tone):
    # 'gemini-2.5-flash-lite' has the most reliable free-tier quota right now (up to 1,000 per day)
    model = genai.GenerativeModel('gemini-2.5-flash-lite') 
    
    prompt = f"""
You are an expert email writer. Draft a {tone} response to the following email:

Original Email Content: {email_content}
Original Subject: {subject}

Instructions:
1. Write a {tone} response.
2. Be concise.
3. You MUST end the email with this specific signature format:

Sincerely,

Akshara Pandey \n
CSE Grad
"""
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        # If 2.5-lite still fails, the last resort for free is 1.5-flash
        return f"Error: {str(e)}. Try switching to gemini-1.5-flash."