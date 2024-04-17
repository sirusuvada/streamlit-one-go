import streamlit as st

                  # Title
                                 # Markdown

st.success('Mounu Love you ra')                                  # Success

hobbies = st.text_input('Write about your hobbies here:')
if hobbies:
    with open('hobbies.txt', 'a') as file:
        file.write(hobbies + '\n')
