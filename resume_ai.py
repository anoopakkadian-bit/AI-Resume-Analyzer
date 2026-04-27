import streamlit as st
import PyPDF2
from groq import Groq

# 1. Page Configuration (Website-inte thalakkettu)
st.set_page_config(page_title="AI Resume Analyzer", page_icon="🤖")

# 2. PDF Text Extract cheyyaan ulla function
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# 3. Groq AI Analysis function
def analyze_resume(resume_text, api_key):
    client = Groq(api_key=api_key)
    prompt = f"Analyze this resume for 80k salary AI/Python job. Candidate has 8 yrs Sales exp. Give score (0-10) and 3 tech changes in Malayalam: {resume_text}"
    
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant",
    )
    return response.choices[0].message.content

# --- STREAMLIT UI (Ividannu thudangunnu) ---
st.title("🤖 AI Resume Analyzer")
st.write("Ninte resume upload cheyyu, AI athu analyze cheythu tharum!")

# API Key - Ithu security-kku vendi UI-il ninnu vangiikkunnu
api_key = st.text_input("Enter Groq API Key:", type="password")

# File Uploader - Ippo computer-il ninnu file select cheyyaam
uploaded_file = st.file_uploader("Upload ninte Resume (PDF)", type="pdf")

if st.button("Analyze Resume"):
    if uploaded_file is not None and api_key:
        with st.spinner('AI ninte resume nokkukayaanu...'):
            # Text edukunnu
            text = extract_text_from_pdf(uploaded_file)
            # AI analysis edukunnu
            result = analyze_resume(text, api_key)
            
            st.success("Analysis Completed!")
            st.markdown("### 📢 AI Result:")
            st.write(result)
    else:
        st.error("Dayaayi API Key-yum Resume-yum nalkuka!")