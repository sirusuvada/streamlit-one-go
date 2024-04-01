import streamlit as st

                  # Title
                                 # Markdown

st.success('Mounu Love you ra')                                  # Success

st.subheader('Bayanga unda nanna')                            # Radio Button
radioButton = st.radio('edo okati select chey nanna : ', ('no heroo ','ippudu kasta ok','chaala'))
if(radioButton == 'chaala'):
    st.write("Kanna anni saddukuntayi ra ,:)")
elif(radioButton == 'ippudu kasta ok'):
    st.write("idi click chestav ani expect cheyle ra")
elif(radioButton == 'no heroo'):
    st.write("idi click chestav ani expect cheyle ra")



st.subheader("click below one  ")                                  # Button
if(st.button('miss avtunna herrooo')):
    st.write([
    "Mounu, remember that your worth isn't determined by anyone's opinion ",
    "especially not by misunderstandings.",
    "You shine brightly, and those who truly see you will cherish you for who you are.3",
    "I promise to have a heartfelt conversation with my parents to clear up any misunderstandings."
])
st.subheader("click below once more ra ")  
if(st.button('touch me')):
  st.write(" i use chat gpt for all these to make you feel some what better ra , i know i cant do right now ,,but small try")

