"""
IESDS Concept Tab View.
"""

import streamlit as st


def render_tab_iesds() -> None:
    st.title("Game Theory Concepts: Strict Dominance and IESDS")

    st.header("Strict Dominance")
    st.write("""
        - Strategy 'x' strictly dominates strategy 'y' for a player if 'x' generates a greater payoff than 'y' regardless of what the other players do.
        - Rational players never play strictly dominated strategies. \n
        -- Why play 'y' when you can play 'x' instead?
    """)
    st.image("images/IESDS1.png")
    st.write(
        "Regardless of what strategy P2 chooses, it is always in the best interest of P1 to confess, as the payout is bigger in any case, therefore the 'Confess' strategy strictly dominates 'Keep Quiet'"
    )

    st.header("Iteration Elimination of Strictly Dominated Strategies (IESDS)")
    st.write("""
        IESDS is a method where we iteratively remove strategies that are strictly dominated by other strategies,
        simplifying the game to find the optimal strategies for the players.
    """)
    st.image("images/IESDS2.png")
    st.write(" - If you ever see a strictly dominated strategy eliminate it immediately. \n - Order does not matter.")
