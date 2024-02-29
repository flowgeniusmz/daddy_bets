import streamlit as st
from config import pagesetup as ps
from openai import OpenAI
import time
from app import assistant_chat as asst, background_image as bckim, betting_form as bf
with open( "config/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

# 1. Set Page Config
app_name = "Daddy Bets"
page_title = "Daddy Bets"
page_subtitle = "Betting Assistant" 
page_icon = "https://storage.googleapis.com/production-domaincom-v1-0-8/048/1724048/4RBifvGs/dfc737c8f0d640cfa7e8623583bfcf5e"
page_description = "Is a gambler's best friend. It is capable of taking your Odds Assistant odds and analyzing the smart bets for you."
overview_header = "Overview"
overview_text = f"**{page_subtitle}** {page_description.lower()}"
#st.set_page_config(page_icon=page_icon, layout="wide")

from config import pagesetup as ps, sessionstates as ss

>>>>>>> c9c34f2 (mz push)

# 0. Page Config
ps.get_st_page_config()

with open( "config/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

<<<<<<< HEAD
# 4. Set assistant chat
bckim.display_background_image()
bf.display_betting_form()
asst.app_chat()
=======
# 1. Page Title
ps.get_title(0)

# 2. Page Overview
ps.get_overview(0)

# 3. Session State Initalization
ss.get_initial_session_states()

# 4. Set Page Background
ps.display_background_image()

# 5. Page Links
link_container = st.container(border=True)
with link_container:
    link_columns = st.columns(2)
    with link_columns[0]:
        ps.get_page_link(1)
        ps.get_page_link(3)
    with link_columns[1]:
        ps.get_page_link(2)
        ps.get_page_link(4)
>>>>>>> c9c34f2 (mz push)
