import streamlit as st
from groq import Groq
import os

try:
    api_key = st.secrets["GROQ_API_KEY"]
except:
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

st.set_page_config(page_title="YK Draft", page_icon="📝", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Bebas+Neue&display=swap');
.stApp { background-color: #030303 !important; color: #ffffff !important; font-family: 'Space Mono', monospace !important; }
.stButton > button { background: transparent !important; color: #E91E8C !important; border: 1px solid #E91E8C !important; font-family: 'Space Mono', monospace !important; font-size: 0.75rem !important; letter-spacing: 0.15em !important; text-transform: uppercase !important; padding: 1rem 2rem !important; transition: all 0.3s ease !important; width: 100% !important; }
.stButton > button:hover { background: #E91E8C !important; color: #030303 !important; }
.stTextArea textarea { background: #0a0a0a !important; border: 1px solid #181818 !important; color: #ffffff !important; font-family: 'Space Mono', monospace !important; font-size: 0.85rem !important; border-radius: 0 !important; }
.stTextArea textarea:focus { border-color: #E91E8C !important; }
div[data-testid="metric-container"] { background: transparent !important; border: 1px solid #181818 !important; padding: 1.5rem !important; }
div[data-testid="metric-container"] label { font-family: 'Space Mono', monospace !important; font-size: 0.6rem !important; letter-spacing: 0.2em !important; text-transform: uppercase !important; color: #888 !important; }
div[data-testid="metric-container"] div[data-testid="stMetricValue"] { font-family: 'Bebas Neue', sans-serif !important; font-size: 2.5rem !important; color: #ffffff !important; }
.stDownloadButton > button { background: #E91E8C !important; color: #030303 !important; border: 1px solid #E91E8C !important; font-family: 'Space Mono', monospace !important; font-size: 0.75rem !important; font-weight: 700 !important; padding: 1rem 2rem !important; }
.stSelectbox > div { background: #030303 !important; border: 1px solid #181818 !important; }
hr { border-color: #181818 !important; }
.stMarkdown p { color: #888 !important; font-size: 0.8rem !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
@keyframes ringPulse { 0%{opacity:0.15;transform:translate(-50%,-50%) scale(0.3)} 100%{opacity:0;transform:translate(-50%,-50%) scale(1)} }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.5} }
@keyframes slideUp { to{transform:translateY(0)} }
@keyframes marquee { 0%{transform:translateX(0)} 100%{transform:translateX(-50%)} }
</style>
<div style='text-align:center;padding:6vh 2rem 3vh 2rem;position:relative;overflow:hidden;'>
<div style='position:absolute;width:500px;height:500px;border-radius:50%;border:1px solid #E91E8C;opacity:0;top:50%;left:50%;transform:translate(-50%,-50%);animation:ringPulse 6s ease infinite;pointer-events:none;'></div>
<div style='position:absolute;width:500px;height:500px;border-radius:50%;border:1px solid #E91E8C;opacity:0;top:50%;left:50%;transform:translate(-50%,-50%);animation:ringPulse 6s ease 2s infinite;pointer-events:none;'></div>
<div style='display:inline-flex;align-items:center;gap:0.75rem;font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;letter-spacing:0.15em;color:#888;margin-bottom:2rem;padding:0.6rem 1.2rem;border:1px solid #181818;'>
<span style='width:6px;height:6px;background:#E91E8C;border-radius:50%;animation:pulse 2s infinite;display:inline-block;'></span>
AI-Powered &nbsp;|&nbsp; Indian Legal Documents &nbsp;|&nbsp; Legal-Tech
</div>
<div style='overflow:hidden;'>
<div style='transform:translateY(115%);animation:slideUp 1.2s cubic-bezier(0.16,1,0.3,1) 0.3s forwards;font-family:Bebas Neue,sans-serif;font-size:clamp(4rem,10vw,8rem);line-height:0.9;color:#ffffff;'>YK</div>
</div>
<div style='overflow:hidden;'>
<div style='transform:translateY(115%);animation:slideUp 1.2s cubic-bezier(0.16,1,0.3,1) 0.5s forwards;font-family:Bebas Neue,sans-serif;font-size:clamp(4rem,10vw,8rem);line-height:0.9;color:#E91E8C;'>DRAFT</div>
</div>
<div style='overflow:hidden;margin-bottom:2rem;'>
<div style='transform:translateY(115%);animation:slideUp 1.2s cubic-bezier(0.16,1,0.3,1) 0.7s forwards;font-family:Bebas Neue,sans-serif;font-size:clamp(1.5rem,4vw,3rem);line-height:0.9;color:#888;'>Your Rights - Explicitly Defined</div>
</div>
<div style='display:inline-block;padding:2rem 3rem;border:1px solid #181818;'>
<div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#E91E8C;margin-bottom:0.5rem;'>SYSTEM STATUS</div>
<div style='font-family:Bebas Neue,sans-serif;font-size:3rem;color:#ffffff;line-height:1;'>READY</div>
<div style='font-family:Space Mono,monospace;font-size:0.65rem;color:#888;'>Precision in Every Paragraph</div>
</div>
</div>
<hr style='border-color:#181818;margin:0;'>
<div style='overflow:hidden;padding:1rem 0;border-bottom:1px solid #181818;'>
<div style='display:flex;width:max-content;animation:marquee 35s linear infinite;font-family:Space Mono,monospace;font-size:0.7rem;letter-spacing:0.1em;text-transform:uppercase;color:#444;white-space:nowrap;'>
<span style='padding:0 2rem;'>NDA</span><span style='color:#E91E8C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Employment Agreement</span><span style='color:#E91E8C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Legal Notice</span><span style='color:#E91E8C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Rental Agreement</span><span style='color:#E91E8C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>MOU</span><span style='color:#E91E8C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Service Agreement</span><span style='color:#E91E8C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Partnership Deed</span><span style='color:#E91E8C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Affidavit</span><span style='color:#E91E8C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Power of Attorney</span><span style='color:#E91E8C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>NDA</span><span style='color:#E91E8C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Employment Agreement</span><span style='color:#E91E8C;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Legal Notice</span><span style='color:#E91E8C;padding:0 1rem;'>◆</span>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
letter-spacing:0.2em;color:#888;margin:3rem 0 1rem 0;'>
01 / SELECT DOCUMENT TYPE
</div>
""", unsafe_allow_html=True)

doc_type = st.selectbox("", [
    "NDA — Non-Disclosure Agreement",
    "Employment Agreement",
    "Service Agreement",
    "Rental / Lease Agreement",
    "MOU — Memorandum of Understanding",
    "Legal Notice",
    "Partnership Deed",
    "Affidavit",
    "Power of Attorney",
    "Vendor Agreement",
    "Freelancer Agreement",
    "Loan Agreement",
    "Cease and Desist Letter",
    "Demand Letter",
    "Terms and Conditions",
    "Privacy Policy"
], label_visibility="collapsed")

st.markdown("""
<div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
letter-spacing:0.2em;color:#888;margin:2rem 0 1rem 0;'>
02 / DESCRIBE WHAT YOU NEED
</div>
""", unsafe_allow_html=True)

description = st.text_area("",
    placeholder="e.g. NDA between a startup and a freelance developer. The developer will work on a mobile app. Confidentiality period is 2 years. Based in Mumbai, Maharashtra.",
    height=120,
    label_visibility="collapsed"
)

st.markdown("""
<div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
letter-spacing:0.2em;color:#888;margin:2rem 0 1rem 0;'>
03 / SELECT GOVERNING LAW
</div>
""", unsafe_allow_html=True)

governing_law = st.selectbox("", [
    "Indian Law — General",
    "Maharashtra",
    "Delhi",
    "Karnataka",
    "Tamil Nadu",
    "Telangana",
    "Gujarat",
    "West Bengal",
    "Rajasthan",
    "Other State"
], label_visibility="collapsed", key="gov")

if st.button("📝 GENERATE LEGAL DOCUMENT →", use_container_width=True):
    if not description.strip():
        st.warning("Please describe what you need first!")
    else:
        with st.spinner("Drafting your legal document..."):

            draft_prompt = f"""You are an expert Indian lawyer. Draft a professional {doc_type} based on the following instructions.

Document Type: {doc_type}
Governing Law: {governing_law}
Instructions: {description}

Draft a complete, professional legal document that:
1. Follows Indian law and legal conventions
2. Includes all standard clauses for this document type
3. Is clear, precise and enforceable
4. Includes proper recitals, definitions, and signature blocks
5. Mentions governing jurisdiction and dispute resolution

Format it as a proper legal document with:
- Title
- Date placeholder
- Party details placeholders
- Numbered clauses
- Signature block

Make it comprehensive and ready to use."""

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": draft_prompt}],
                max_tokens=2000
            )
            draft = response.choices[0].message.content

        st.markdown("""
        <div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
        letter-spacing:0.2em;color:#888;margin:2rem 0 1rem 0;'>
        04 / YOUR DRAFT DOCUMENT
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style='border:1px solid #181818;padding:2rem;
        font-family:Space Mono,monospace;font-size:0.8rem;
        color:#ffffff;line-height:1.8;white-space:pre-wrap;'>
        {draft}
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<hr style='border-color:#181818;margin:2rem 0;'>", unsafe_allow_html=True)

        st.download_button(
            label="EXPORT DOCUMENT →",
            data=f"YK DRAFT — {doc_type.upper()}\n{'='*50}\nGoverning Law: {governing_law}\nInstructions: {description}\n\n{draft}",
            file_name=f"YKDraft_{doc_type.split('—')[0].strip().replace(' ','_')}.txt",
            mime="text/plain",
            use_container_width=True
        )

st.markdown("""
<div style='text-align:center;padding:1rem;font-family:Space Mono,monospace;
font-size:0.55rem;color:#333;text-transform:uppercase;letter-spacing:0.1em;'>
AI-drafted documents require review by a qualified lawyer before use.<br>Adv. Damini Yasodai — YK Legal
</div>
""", unsafe_allow_html=True)
