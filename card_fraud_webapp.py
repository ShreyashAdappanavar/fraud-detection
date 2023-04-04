import streamlit as st
import pickle
import sklearn
import pandas
import matplotlib
import numpy
import scipy


final_model = pickle.load(open('final_model.pkl', 'rb'))
def classify(num):
    if num<0.5:
        return 'Not Fraudulent!'
    else:
        return 'Fraudulent!!!'

def main():
    st.title('Predicting Credit Card Frauds')
    html_temp = """
        <div style="background-color:teal ;padding:10px">
        <h2 style="color:white;text-align:center;">Enter Transaction Details</h2>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.spinner("Hello!")
    V3  = st.slider('V3 Value', -48.3, 9.3)
    V4  = st.slider('V4 Value', -5.6, 16.8)
    V7  = st.slider('V7 Value', -43.5, 120.5)
    V10 = st.slider('V10 Value', -24.5, 23.7)
    V11 = st.slider('V11 Value', -4.7, 12.0)
    V12 = st.slider('V12 Value', -18.6, 7.8)
    V14 = st.slider('V14 Value', -19.2, 10.5)
    V16 = st.slider('V16 Value', -14.1, 17.3)
    V17 = st.slider('V17 Value', -25.1, 9.254)

    inputs = [[V3, V4, V7, V10, V11, V12, V14, V16, V17]]

    if st.button('Fraudulent?'):
        st.success(classify(final_model.predict(inputs)))


if __name__=='__main__':
    main()