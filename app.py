import numpy as np
import pandas as pd
import streamlit as st 
import pickle

model = pickle.load(open(r"C:\Users\Tharuni\Desktop\NIT\Aug month\20th-investment analysis\multilinear_regression_model.pkl",'rb'))

st.title("📊A Predictive Model for Investment Trends Using Regression Techniques")
digital = st.number_input("Digital Marketing Investment",min_value=0, max_value=1000000, step=1000)
promotion = st.number_input("Promotion Investment", min_value=0, max_value=1000000, step=1000)
research = st.number_input("Research & Development Investment", min_value=0, max_value=1000000, step=1000)
state = st.selectbox("Select State", ("Hyderabad", "Bangalore", "Chennai"))


if st.button("predict profit"):
     # Encode state (dummy variables, same as training with drop_first=True)
    if state == "Hyderabad":
        state_banglore, state_chennai =0,0
    elif state == "Bangalore" :
        state_bangalore, state_chennai = 1, 0
    else:  # Chennai
        state_bangalore, state_chennai = 0, 1   
    
    input_data = np.array([[digital,promotion,research,state_bangalore, state_chennai]])
    prediction = model.predict(input_data)
    st.success(f"💰 Estimated  Profit: ${prediction[0]:,.2f}")