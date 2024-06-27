import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
import os

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# gemini pro response
def get_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf(Uploaded_pdf):
    reader=pdf.PdfReader(Uploaded_pdf)
    text=""
    for page in reader.pages:
        page=reader.pages
        text+=str(page)
        return text

# prompt template
input_prompt="""You are an Applicant Tracking System (ATS). Your task is to evaluate a candidate's resume against a given job description. Specifically, you need to identify the missing keywords in the resume that are present in the job description and calculate the percentage score of the resume based on keyword matching. Follow these steps:

Input:

A candidate's resume:{text}.
A job description:{job_desription}
Process:

Extract keywords from the job description.
Extract keywords from the resume.
Identify the missing keywords in the resume that are present in the job description.
Calculate the percentage score of the resume based on the number of matching keywords.
Output:

List of missing keywords.
Percentage score of the resume.
"""

#streamlit app
st.title("ATS System")
st.text("Made to improve your resume ATS")
job_description=st.text_input("Inpur your job description")
Uploaded_pdf=st.file_uploader("Upload your Resume pdf file",type="pdf")
submit = st.button("Submit")

if submit:
    if Uploaded_pdf is not None:
        text=input_pdf(Uploaded_pdf)
        response=get_response(input_prompt)
        st.subheader(response)

