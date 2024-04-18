import streamlit as st
import streamlit_ext as ste
import openai
from streamlit_tags import st_tags

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

openai.api_key = OPENAI_API_KEY


def write_cover_letter(full_name, job_title, adv_tech_skills, int_tech_skills, personal_skills, job_description, contact_number, email):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"write a Qualitative Survey Discussion Guide with {full_name}, main questions, probing questions, closing questions and next steps {email} and {contact_number}, "
               f"applying for the following job vacancy to make him "
               f"an ideal candidate based on the selection criteria and his skills. Yonatan is a {job_title}, "
               f"with advanced {adv_tech_skills} skills, intermediate {int_tech_skills} skills, and personal "
               f"skills including {personal_skills}:"
               f"\n\n{job_description}",
        temperature=0.7,
        max_tokens=278,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']

st.header("Qualitative Survey Discussion Guide Generator")
st.write("Complete the form below and Noetic will generate your discussion guide")

with st.form("Cover Letter Generator", clear_on_submit=False):
    applicant_name = st.text_input("Enter the moderator's introduction and the study's purpose:")
    contact_number = st.text_input("Enter warm-up questions to ease participants into the discussion:")
    email = st.text_input("Email: ")
    job_title = st.text_input("Enter your job title:")
  
    ajob_description = st.text_area("Enter probing questions to further delve into topics based on participant responses:")
    bjob_description = st.text_area("Enter closing questions to wrap up the discussion:")
    
    cjob_description = st.text_area("Describe what will be conveyed to participants regarding next steps after the session:")

    submitted = st.form_submit_button("Write my damn cover letter!")
    if submitted:
        with st.spinner("Writing cover letter..."):
            cover_letter_text = write_cover_letter(full_name=applicant_name, job_title=job_title,
                                                   adv_tech_skills=advanced_technical_skills,
                                                   int_tech_skills=intermediate_technical_skills,
                                                   personal_skills=personal_skills, job_description=job_description,
                                                   contact_number=contact_number, email=email)
            st.subheader("Your cover letter:")
            st.write(cover_letter_text)
            ste.download_button("Download", cover_letter_text,
                                f"{applicant_name} - Cover letter.txt")
