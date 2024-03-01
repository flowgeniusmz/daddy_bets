import streamlit as st
from config import pagesetup as ps, sessionstates as ss


# 0. Page Config


with open( "config/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

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
