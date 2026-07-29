"""
Credits and Documentation Tab View.
"""

import streamlit as st


def render_tab_credits() -> None:
    st.header("Project Credits & Documentation")

    with st.container(border=True):
        st.subheader("Team Members")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            - **Taras Zinchenko**
            - **Tim Huijbens**
            - **Jan Jelínek**
            """)
        with col2:
            st.markdown("""
            - **Žygimantas Mickavičius**
            - **Jaden Mannes**
            """)

    with st.container():
        st.subheader("References")
        st.markdown("""
        - [William Spaniel - YouTube Guide Playlist](https://youtu.be/NSVmOC_5zrE?si=h5rLcX6NBepf4TNU)
        - [Game Theory 101 by William Spaniel](https://gametheory101.com/courses/game-theory-101/)
        """)
