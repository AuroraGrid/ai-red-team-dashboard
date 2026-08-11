import streamlit as st
import os

st.set_page_config(page_title="AI Red-Team Dashboard", layout="wide")
st.title("AI Red-Teaming & Decision Intelligence")

api_key = st.text_input("Enter GROQ API Key", type="password")
if api_key:
    os.environ["GROQ_API_KEY"] = api_key

tab1, tab2, tab3, tab4 = st.tabs(["Red-Team Scanner", "Bug Bounty Generator", "Startup Audit Generator", "Metaculus Forecaster"])

with tab1:
    st.write("PyRIT Multi-Turn Prompt Injection Tester")
    st.info("Run `python red_team_scan.py` in your terminal to execute the PyRIT memory containers.")

with tab2:
    st.write("Huntr / HackerOne Markdown Output")
    st.info("Run `python track1_bounty_gen.py` in your terminal to generate the MD report.")

with tab3:
    st.write("LinkedIn DM + Executive Summary")
    st.info("Run `python track2_audit_pitch.py` in your terminal to generate the outreach text.")

with tab4:
    st.write("Metaculus & Prediction Market Forecaster")
    st.info("Run `python track3_metaculus_engine.py` in your terminal to generate base rates and confidence intervals.")
