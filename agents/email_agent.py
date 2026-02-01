import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
def generate_email_response(email_content, subject, tone):
  prompt=f"""
  You are an expert email writer. Craft a {tone} response to the following email:
  Subject: {subject}
  Email Content: {email_content}
  Response:
"""
  response=client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {"role": "system", "content": "You are a helpful assistant that writes email responses."},
      {"role": "user", "content": prompt}
    ],
    max_tokens=500,
    temperature=0.7,
  )
  return response.choices[0].message.content.strip()