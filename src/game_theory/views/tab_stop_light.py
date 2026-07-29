"""
Stop Light Game Tab View.
"""

import streamlit as st


def render_tab_stop_light() -> None:
    st.title("Nash Equilibrium: Stoplight Game")
    st.write("""
             Picture a situation. Two cars are approaching an intersection.
             If they both crash into each other they will get significantly delayed.

             If they both stop, they will both wait, but most likely not for so long.

             If one can go and the only wait it's the best scenario for both of them because they are not wasting their time.

             This is represented below:
             """)
    st.image("images/stop_light.jpg")

    st.write(
        "Nash equilibrium is a law that everyone would want to follow even in the absence of an effective police force."
    )
    st.write("The payoffs represent the consequences of their decisions.")

    st.write("### Nash Equilibria")
    st.write("- **(Go, Stop)**: If Player 1 goes and Player 2 stops, neither has an incentive to change.")
    st.image("images/stop_light_go_stop.jpg")
    st.write(
        """
        If player 1 stops instead of going, player 1 gets **-1** < **1**

        If player 2 goes instead of stopping, player 2 gets **-5** < **0**
        """
    )

    st.write("- **(Stop, Go)**: If Player 1 stops and Player 2 goes, neither has an incentive to change.")
    st.image("images/stop_light_stop_go.jpg")
    st.write(
        """
        If player 1 goes instead of stopping, player 1 gets **-5** < **0**

        If player 2 stops instead of going, player 2 gets **-1** < **1**
        """
    )
    st.write("These are the two Nash equilibria of the game:")
    st.image("images/stop_light_equilibria.jpg")
