import streamlit as st

# 1. ആപ്പിന്റെ പേര് 'MentorAI' എന്ന് മാറ്റുന്നു
st.set_page_config(page_title="MentorAI", page_icon="🤖", layout="centered")

# 2. നമ്മുടെ ലോഗോ ആപ്പിൽ കാണിക്കുന്നു
st.image("image_0.png", width=120)

# 3. മെയിൻ ഹെഡർ മാറ്റാം
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>MentorAI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Empowering Aspirants with Intelligent Social Learning</p>", unsafe_allow_html=True)

# 4. ബാക്കി സ്റ്റേറ്റ് സെലക്ഷൻ അവിടെ തന്നെ നിൽക്കട്ടെ
state = st.selectbox(
    "Choose Your Region / പ്രദേശം തിരഞ്ഞെടുക്കുക",
    ["Kerala", "Tamil Nadu", "Karnataka", "Hyderabad (Telangana)", "Rest of India"]
)

st.write(f"Welcome to *MentorAI {state}* Community!")

# ലോഗിൻ ഫോം പഴയപോലെ തന്നെ തുടരാം
with st.form("login_form"):
    user_input = st.text_input("Username / Mobile")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Enter MentorAI")

    if submitted:
        if user_input and password:
            st.success(f"Connecting to MentorAI {state}...")
        else:
            st.error("Please enter details / വിവരങ്ങൾ നൽകുക.")