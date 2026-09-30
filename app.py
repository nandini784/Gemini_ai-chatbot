import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# ---------------- LOAD ENVIRONMENT VARIABLES ----------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Check API key
if not api_key:
    st.error("Gemini API key not found. Please add GEMINI_API_KEY to your .env file.")
    st.stop()

# Create Gemini client
client = genai.Client(api_key=api_key)

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(
            135deg,
            #0f172a 0%,
            #1e293b 50%,
            #0f172a 100%
        );
        color: white;
    }

    /* Main title */
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
        color: #38bdf8;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #cbd5e1;
        margin-bottom: 30px;
    }

    /* Text area */
    textarea {
        background-color: #1e293b !important;
        color: white !important;
        border: 1px solid #475569 !important;
        border-radius: 12px !important;
        font-size: 16px !important;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        background: linear-gradient(
            90deg,
            #2563eb,
            #06b6d4
        );
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px;
        font-size: 17px;
        font-weight: 600;
        transition: 0.3s;
    }

    .stButton > button:hover {
        transform: scale(1.02);
        background: linear-gradient(
            90deg,
            #06b6d4,
            #2563eb
        );
    }

    /* Response box */
    .response-box {
        background-color: #1e293b;
        border-left: 5px solid #38bdf8;
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
        color: #f8fafc;
        line-height: 1.7;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 13px;
        margin-top: 40px;
    }

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    '<div class="main-title">🤖 Gemini AI Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask Gemini anything and get an AI-powered response</div>',
    unsafe_allow_html=True
)

# ---------------- PROMPT INPUT ----------------
prompt = st.text_area(
    "💬 Enter your prompt:",
    placeholder="Explain Artificial Intelligence in simple words...",
    height=150
)

# ---------------- GENERATE RESPONSE ----------------
if st.button("✨ Generate Response"):

    if prompt.strip():

        with st.spinner("🤖 Gemini is thinking..."):

            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                st.success("✅ Response generated!")

                st.markdown(
                    f"""
                    <div class="response-box">
                        {response.text}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except Exception as e:
                st.error(f"❌ Error: {e}")

    else:
        st.warning("⚠️ Please enter a prompt.")

# ---------------- FOOTER ----------------
st.markdown(
    '<div class="footer">Powered by Google Gemini & Streamlit 🚀</div>',
    unsafe_allow_html=True
)
