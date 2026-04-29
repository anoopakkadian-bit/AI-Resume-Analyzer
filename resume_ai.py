import streamlit as st
import PyPDF2
from groq import Groq
import os

st.set_page_config(page_title="AI Resume Analyzer", page_icon="🤖")


def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def analyze_resume(resume_text):
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    prompt = f"Analyze this resume for 80k salary AI/Python job. Candidate has 8 yrs Sales exp. Give score (0-10) and 3 tech changes in Malayalam: {resume_text}"
    
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant",
    )
    return response.choices[0].message.content

# --
st.title("🤖 AI Resume Analyzer")
st.write("Ninte resume upload cheyyu, AI athu analyze cheythu tharum!")


import os 
api_key = st.secrets["GROQ_API_KEY"]


uploaded_file = st.file_uploader("Upload ninte Resume (PDF)", type="pdf")

if st.button("Analyze Resume"):
    if uploaded_file is not None:
        with st.spinner('AI ninte resume nokkukayaanu...'):
            
            text = extract_text_from_pdf(uploaded_file)
            
            result = analyze_resume(text)
            
            st.success("Analysis Completed!")
            st.markdown("### 📢 AI Result:")
            st.write(result)
    else:
    
        st.error("Dayaayi API Key-yum Resume-yum nalkuka!")
