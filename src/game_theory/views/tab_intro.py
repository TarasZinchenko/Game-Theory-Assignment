"""
Introduction Tab View.
"""

import streamlit as st


def render_tab_intro() -> None:
    st.title("Introduction")
    st.write(
        """
        ##### Game Theory is all around us—whether we realize it or not. From negotiations and traffic decisions to sports strategies and even everyday choices, the way we interact with others follows strategic patterns. Our app is designed to bring these concepts to life through interactive experiences that let you explore, play, and learn at your own pace.

        ##### With our app, you won’t just read about Game Theory—you’ll experience it. Dive into classic strategic dilemmas and test your decision-making skills with our interactive modules:
        
        ##### The Prisoner’s Dilemma – A classic example of why cooperation is hard, even when it's beneficial.
        
        ##### IESDS (Iterated Elimination of Strictly Dominated Strategies) – A method to predict rational choices in strategic games.
        
        ##### The Stoplight Game – A real-world application of Nash Equilibrium in traffic decisions.
        
        ##### The Battle of the Sexes – Exploring mixed strategies and payoffs in coordination problems.
        
        ##### Penalty Kick Analyzer – How professional athletes use mixed strategies in real-life competition.
        
        ##### Take vs. Share Dilemma – Examining the tension between selfishness and cooperation.
        
        ##### Rock, Paper, Scissors – A simple game with deeper strategic implications.
        """
    )
