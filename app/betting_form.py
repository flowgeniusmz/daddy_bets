import streamlit as st
import config.pagesetup as ps
import function.create_prompt as cp
from openai import OpenAI

client = OpenAI(api_key=st.secrets.OPENAI_API_KEY)
sports = ["NBA", "NFL", "MLB", "NHL", "NCAAF", "NCAAB"]
betting_markets = ["h2h", "spreads", "totals"]

def display_betting_form():
    ps.set_blue_header("Betting Information")
    select_sport = st.selectbox(
        label="Select Sport",
        options=sports,
        key="selected_sport"
    )

    select_betting_markets = st.selectbox(
        label="Select Betting Type",
        options=betting_markets,
        key="selected_betting_markets"
    )

    user_input = st.text_area(
        label="Betting Instructions",
        key="input_instructions"
    )

    submit_button = st.button(
        label="Submit",
        key="submit_button"
    )
    
    if submit_button:
        asst_prompt = cp.create_assistant_prompt(select_sport, select_betting_markets, user_input)
        st.markdown(asst_prompt)
        print(asst_prompt)
        

    st.divider()
