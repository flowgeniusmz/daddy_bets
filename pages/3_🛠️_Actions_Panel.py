import streamlit as st
from config import pagesetup as ps

# 0. Page Config
ps.get_st_page_config()

# 1. Page Title
ps.get_title(3)
ps.display_background_image()
# 2. Page Overview
ps.get_overview(3)