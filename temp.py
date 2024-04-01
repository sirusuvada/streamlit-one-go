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



st.subheader("click it ")                                  # Button
if(st.button('miss avtunna herrooo')):
    st.write('Kanna nenu kuda ra')

