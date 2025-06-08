"""Field to put JD 
2.Upload pdf
3.PDF to image-. processing """
from dotenv import load_dotenv
load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv('api_key'))

def get_gemini_response(input,pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert PDF to images
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]
        # Convert the first page to bytes
        img_byte_arr=io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr= img_byte_arr.getvalue()

        image_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    

#Streamlit APP
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Resume Expert")
input_text=st.text_area("Job Description: ", key="input")
uploaded_file=st.file_uploader("Upload a resume in PDF format", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF file uploaded successfully.")

submit1=st.button("Tell me about the resume")
submit2=st.button("How can I improve my resume?")
submit3=st.button("What keywords are missing in my resume?")
submit4=st.button("Percentage match")

input_prompt1="""" You are an experienced Hr with Tech experience in the field of Data Science, Full stack ,
Big Data, DevOps, Data Analyst. Your task is review the provided resume gainst the job description for these profiles.
Please share your professional evaluation on whether the candidate's profilr aligns with the job.
highlisht the strengths and weaknesses of the applicant in relation to the specific job"""

input_prompt2="""You are an Technical Human Resource Manager with expertise in data science,Full stack ,
Big Data, DevOps, Data Analyst your role is to scrutinize the resume in light of the job description provided.
Share your insights on the candidate's suitability for the role from an HR perspective.
Additionally, offer advice on enhancing the candidate's skills and identify areas"""

input_prompt3="""You are an Technical Human Resource Manager with expertise in data science,Full stack ,
Big Data, DevOps, Data Analyst ancd deep ats your role is to scrutinize the resume in light of the job description provided.
Yor task is to evaluate sthe core of the resume as a ATS expert. and provide score with percentage match"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The response is")
        st.write(response)

    else:
        st.write("Please upload a Resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("The response is")
        st.write(response)

    else:
        st.write("Please upload a Resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("The response is")
        st.write(response)

    else:
        st.write("Please upload a Resume")

elif submit4:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The response is")
        st.write(response)

    else:
        st.write("Please upload a Resume")
        
        
        
