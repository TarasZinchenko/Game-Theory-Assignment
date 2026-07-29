"""
Game Theory Suite - Main Streamlit Application Entrypoint.
"""

import sys
from pathlib import Path

# Ensure src/ directory is on sys.path
src_dir = Path(__file__).resolve().parent / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

import streamlit as st
from game_theory.views.tab_intro import render_tab_intro
from game_theory.views.tab_prisoners import render_tab_prisoners
from game_theory.views.tab_iesds import render_tab_iesds
from game_theory.views.tab_stop_light import render_tab_stop_light
from game_theory.views.tab_battle_sexes import render_tab_battle_sexes
from game_theory.views.tab_penalty import render_tab_penalty
from game_theory.views.tab_take_share import render_tab_take_share
from game_theory.views.tab_rps import render_tab_rps
from game_theory.views.tab_credits import render_tab_credits


def main() -> None:
    st.set_page_config(page_title="Game Theory Suite", layout="wide")
    st.title("Game Theory Application Suite")

    (
        tab_intro,
        tab_prison,
        tab_iesds,
        tab_stop_light,
        tab_sexes,
        tab_penalty,
        tab_take_share,
        tab_rps,
        tab_credits,
    ) = st.tabs([
        "Introduction",
        "Prisoner's dilema",
        "IESDS",
        "Stop light",
        "Battle of sexes",
        "Penalty Kick Analyzer",
        "Take vs. Share Dilemma",
        "Rock Paper Scissors",
        "Credits",
    ])

    with tab_intro:
        render_tab_intro()

    with tab_prison:
        render_tab_prisoners()

    with tab_iesds:
        render_tab_iesds()

    with tab_stop_light:
        render_tab_stop_light()

    with tab_sexes:
        render_tab_battle_sexes()

    with tab_penalty:
        render_tab_penalty()

    with tab_take_share:
        render_tab_take_share()

    with tab_rps:
        render_tab_rps()

    with tab_credits:
        render_tab_credits()


if __name__ == "__main__":
    main()
