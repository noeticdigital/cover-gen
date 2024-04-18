import streamlit as st
import streamlit_ext as ste
import openai
from streamlit_tags import st_tags

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

openai.api_key = OPENAI_API_KEY


def write_cover_letter(applicant_name, ajob_description, bjob_description, cjob_description, warm_up):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"write a Qualitative Survey Discussion Guide with main questions{applicant_name}, probing questions {ajob_description}, closing questions {bjob_description} and next steps {cjob_description} and {warm_up}, "
            ,
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
    warm_up = st.text_input("Enter warm-up questions to ease participants into the discussion:")

  
    ajob_description = st.text_area("Enter probing questions to further delve into topics based on participant responses:")
    bjob_description = st.text_area("Enter closing questions to wrap up the discussion:")
    
    cjob_description = st.text_area("Describe what will be conveyed to participants regarding next steps after the session:")

       if st.form_submit_button("Generate Product Concept"):
            guide_text = write_product_concept(applicant_name, ajob_description, bjob_description, cjob_description, warm_up)
            st.subheader("Generated Product Concept (English):")
            st.write(guide_text)
