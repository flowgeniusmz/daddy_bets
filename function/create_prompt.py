import streamlit as st


def create_assistant_prompt(varSport: str, varMarket: str, varFreeText: str):

    prompt = f"""Provide the best bets for the following requirements:
    1. Sport = {varSport}
    2. Betting Market = {varMarket}
    3. User Requested Details = {varFreeText}
    NOTE: Be sure to follow your instructions, perform any simulations, and return the best bets possible.
    """

    return prompt