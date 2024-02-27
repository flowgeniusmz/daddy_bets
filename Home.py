# 0. Import Libraries
import streamlit as st
from config import pagesetup as ps
from openai import OpenAI
import time
from app import assistant_chat as asst, background_image as bckim, betting_form as bf

# 1. Set Page Config
app_name = "Daddy Bets"
page_title = "Daddy Bets"
page_subtitle = "Betting Assistant" 
page_icon = "https://storage.googleapis.com/production-domaincom-v1-0-8/048/1724048/4RBifvGs/dfc737c8f0d640cfa7e8623583bfcf5e"
page_description = "Is a gambler's best friend. It is capable of taking your Odds Assistant odds and analyzing the smart bets for you."
overview_header = "Overview"
overview_text = f"**{page_subtitle}** {page_description.lower()}"

# with open('config/style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# 2. Set Page Title
ps.set_title(varTitle=page_title, varSubtitle=page_subtitle)

# 3. Set Page Overview
ps.set_page_overview(varHeader=overview_header, varText=overview_text)

# 4. Set assistant chat
bckim.display_background_image()
bf.display_betting_form()
asst.app_chat()
