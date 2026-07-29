"""
Battle of the Sexes Tab View.
"""

import streamlit as st


def render_tab_battle_sexes() -> None:
    st.title("Mixed strategies and Payoffs")
    st.header("Battle of sexes")
    st.write("So far the strategy has only been pure. This means that the players will always stick to one strategy.")
    st.write("In the following case Ballet-Ballet and Fight-Fight are the equalibria.")
    st.image("images/sexes.jpg")
    st.write("What if we combine more strategies?")

    st.header("Mixed strategy")
    st.write("In this strategy the players will mix both of their strategies with a probability P")
    st.subheader("Algorithm for solving mixed strategies:")
    st.write("Since both players can have the same decisions, for simplification let's now refer to these decisions as the following:")
    st.image("images/mixed_strategies.jpg")
    st.write("Firstly, we must solve for Player 1's mixed strategy and therefore we isolate Player 2's decisions.")

    st.image("images/p1s_mixed_strategy.jpg")
    st.write("""
                If Player 1 does a mixed strategy:
              
                Player 2 will receive **2** with the probability **P_Ballet** and **0** with the probability **(1 - P_Ballet)**
                """)
    st.write("To quantify this we use a metric called EU (Expected Utilization)")
    st.write("Player 2's EU when she goes left is the following:")
    st.latex(r"EU_{left} = (P_{up})*(2) + (1 - P_{up})*(0)")
    st.write("Player 2's EU when she goes right is the following:")
    st.latex(r"EU_{right} = (P_{up})*(0) + (1 - P_{up})*(0)")

    st.write("Now the whole idea of mixed strategy is to optimize our strategy to make it indifferent for the other player what decision they make.")
    st.write("We do that by finding with what probability the EUs are equal to each other.")
    st.latex(r"EU_{left} = EU_{right}")
    st.latex(r"(P_{up})*(2) + (1 - P_{up})*(0) = (P_{up})*(0) + (1 - P_{up})*(0)")
    st.latex(r"P_{up} = 1/3")

    st.write("This means, that if P1 decides to use a mixed strategy, they will go to the **ballet (up)** with the probability of **1/3** and to the **fight (down)** with the probability of **2/3**")

    st.write("Then we can do the same for the Player 2's mixed strategy:")
    st.latex(r"EU_{up}=EU_{down}")
    st.latex(r'(P_{left})(1) + (1 - P_{left})(0) = (P_{left})(0) + (1-P_{left})(2)')
    st.latex(r'P_{left} = 2/3')
    st.write("This means that Player 2 will go to the ballet (left) with probability 2/3 and to the fight (right) with probability 1/3")
    st.image("images/mixed_strat_complete.jpg")

    st.subheader("Payoffs")
    st.write("The strategy we have identified before is ensures that both players going to have the same Expected Utilization, however that doesn't mean that such strategy will be optimal.")
    st.write("To validate, it is necessary to calculate the payoffs for each outcome.")
    st.write("To calculate the payoff we need to multiply the outcome with the multiplication and sum all the products.")
    st.write("That gives us the following matrix for Player 1:")
    st.image("images/player1_payoffs.jpg")
    st.latex(r"EU_1 = (1)(1/3)(2/3) + (0)(2/3)(2/3) + (0)(1/3)(1/3) + (2)(2/3)(1/3)")
    st.latex(r"EU_1 = 2/3")
    st.write("And for player 2:")
    st.latex(r"EU_2 = (2)(1/3)(2/3) + (0)(2/3)(2/3) + (0)(1/3)(1/3) + (1)(2/3)(1/3)")
    st.latex(r"EU_2 = 2/3")

    st.write("This means that the mixed strategy is worse than a pure strategy. With pure strategy the players will achieve at worse the outcome of 1, whereas with mixed it will be only 2/3.")
    st.write("This is caused by the fact that the couple often end up in going to different places which drags down the payoffs.")
