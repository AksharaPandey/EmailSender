import streamlit as st
from agents.email_agent import generate_email_response
from utils.email_sender import send_email


st.set_page_config(page_title="Auto Email Response Generator", layout="wide")
st.title("Email Response Generator-Think less, Do more!")

email_text=st.text_area("Enter the email content you received:", height=300)
recipient_email=st.text_input("Enter the recipient's email address:")
subject=st.text_input("Enter the email subject:")
tone=st.selectbox("Select the tone of the email response:", ["Formal", "Informal", "Friendly", "Professional", "Casual"])

if st.button("Generate and Send Response"):
  if not recipient_email:
    st.error("Please enter the recipient's email address.")
  else:
    with st.spinner("Generating email response..."):
      response = generate_email_response(email_text,subject, tone)
      send_status=send_email(recipient_email, subject, response)
    st.subheader("Generated Email Response:")
    st.markdown(response, unsafe_allow_html=True)
    if send_status:
        st.success("Email sent successfully!")
    else:
        st.error("Failed to send email. Please check the email address and try again.")

    