import streamlit as st
import config.pagesetup as ps


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

    st.divider()
