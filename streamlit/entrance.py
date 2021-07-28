import streamlit as st

def app():
    st.title('Welcome to app')
    
    st.header('''
    In this app by taking photo of leaf we can find whether it is having one for the following::
    
        1) combinations: one of the below classes
    
        2) healthy
    
        3) rust
    
        4) scab
    ''')
    st.subheader('go to side bar where you can upload the photo and get the prediction.')
    st.write('Thank you for the visit!')