import streamlit as st

# പേജ് സെറ്റിംഗ്സ്
st.set_page_config(page_title="SaaSva", layout="wide")

# Custom CSS for Professional Look
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    .service-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        border: 1px solid #e0e0e0;
        margin-bottom: 10px;
    }
    .stButton>button {
        border-radius: 12px;
        border: 1px solid #007bff;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True) # ഇവിടെയാണ് തെറ്റ് തിരുത്തിയത്

# 1. Header Section
col1, col2 = st.columns([1, 4])
with col1:
    st.title("🌊 SaaSva")
with col2:
    st.text_input("", placeholder="സേവനങ്ങൾ തിരയുക (उदा: Aadhaar, MVD)...")

st.markdown("---")

# 2. Service Grid
st.subheader("Our Services")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown('<div class="service-box"><h3>🎫</h3><b>Book Token</b></div>', unsafe_allow_html=True)
    if st.button("Open", key="btn1"): st.write("Token Page Loading...")
with c2:
    st.markdown('<div class="service-box"><h3>🚗</h3><b>MVD</b></div>', unsafe_allow_html=True)
    if st.button("Open", key="btn2"): st.write("MVD Page Loading...")
with c3:
    st.markdown('<div class="service-box"><h3>⚡</h3><b>Bills</b></div>', unsafe_allow_html=True)
    if st.button("Open", key="btn3"): st.write("Bill Page Loading...")
with c4:
    st.markdown('<div class="service-box"><h3>📄</h3><b>Certificates</b></div>', unsafe_allow_html=True)
    if st.button("Open", key="btn4"): st.write("Certificate Page Loading...")
import streamlit as st

# പേജ് സെറ്റിംഗ്സ്
st.set_page_config(page_title="SaaSva - A Breath of Relief", layout="wide")

# 1. Header (Logo & Search)
col1, col2 = st.columns([1, 3])
with col1:
    st.markdown("### 🌊 SaaSva") # ഇവിടെ നിന്റെ ലോഗോ വരും
with col2:
    search_query = st.text_input("", placeholder="സേവനങ്ങൾ തിരയുക (उदा: Aadhaar, Bill, MVD)...")

st.markdown("---")

# 2. Services Grid (Boxes)
st.subheader("Our Services")
col_a, col_b, col_c, col_d = st.columns(4)

with col_a:
    st.info("🎫 *Book Token*")
with col_b:
    st.info("🚗 *MVD Services*")
with col_c:
    st.info("⚡ *Utility Bills*")
with col_d:
    st.info("📄 *Certificates*")

# 3. Smart Chat Interface (Bottom Section)
st.markdown("---")
st.subheader("💬 SaaSva AI Assistant")

user_msg = st.text_input("എങ്ങനെയാണ് ഞാൻ നിങ്ങളെ സഹായിക്കേണ്ടത്?", key="user_chat")

if user_msg:
    if "current bill" in user_msg.lower() or "current" in user_msg.lower():
        st.write("*SaaSva AI:* കറന്റ് ബില്ല് അടയ്ക്കുന്നതിനായി നിങ്ങളുടെ *E-Token നമ്പർ: #15* ആണ്. നിങ്ങളുടെ ഏകദേശ സമയം *2:00 PM - 2:30 PM* ആയിരിക്കും.")
        st.write("*SaaSva AI:* നിങ്ങൾക്ക് സെന്ററിൽ പോകാൻ ബുദ്ധിമുട്ടുണ്ടെങ്കിൽ ഈ ലിങ്ക് വഴി ഓൺലൈനായി അടയ്ക്കാം: [🔗 Pay Now]")
    else:
        st.write("*SaaSva AI:* ഞാൻ അത് പരിശോധിക്കുകയാണ്. ഉടൻ മറുപടി നൽകാം!")
        # UI കൂടുതൽ ലളിതമാക്കാൻ (UMANG Style)
st.markdown("### 🔍 Search for Services")
search_input = st.text_input("", placeholder='Search for "Token", "Bill", "MVD"...')

st.write("### Quick Services")
# UMANG മോഡലിൽ സർക്കിൾ ഐക്കണുകൾ പോലെ 4 കോളങ്ങൾ
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.button("🏥 Health")
with c2:
    st.button("🚗 MVD")
with c3:
    st.button("📑 PSC")
with c4:
    st.button("⚡ Utility")