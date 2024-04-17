import streamlit as st

# Title
st.title("Mounu's Page")


# Subheader for hobbies
st.subheader('Tell me about your hobbies:')

# Text input for hobbies
hobbies = st.text_input('Write about your hobbies here:')



if hobbies:
    st.write("Hobbies entered:", hobbies)
    with open('hobbies.txt', 'a') as file:
        file.write(hobbies + '\n')
        st.write("Hobbies written to hobbies.txt")
