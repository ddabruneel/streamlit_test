import streamlit as st

st.title("Hello Bib!!! 👋")
st.markdown(
    """ 
Press the button... I know you want too... come on... press it!!!!! 
    """
)

if st.button("Send balloons!"):
    st.balloons()
