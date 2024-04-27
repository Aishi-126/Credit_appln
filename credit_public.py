

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained Random Forest model
with open("rf_classifier.pkl", 'rb') as file:
    model = pickle.load(file)

def main():
    # Front end elements of the web page
    st.title('Credit Score Prediction App')

    # Add inputs for user to enter data
    age = st.slider("Age", min_value=0, max_value=100, step=1)
    annual_income = st.number_input("Annual Income")
    delay_from_due_date = st.number_input("Delay from Due Date")
    num_of_delayed_payment = st.number_input("Number of Delayed Payments", min_value=0, max_value=100, step=1)
    outstanding_debt = st.number_input("Outstanding Debt")
    credit_history_age = st.number_input("Credit History Age")
    payment_of_min_amount = st.selectbox("Payment of Minimum Amount", ['Yes', 'No'])
    total_emi_per_month = st.number_input("Total EMI per Month")
    payment_behaviour = st.slider("Payment Behaviour", min_value=1, max_value=6, step=1)
    monthly_balance = st.number_input("Monthly Balance")
    
    # Get the selected occupation
    occupation = st.selectbox("Occupation", ['Accountant', 'Architect', 'Developer', 'Doctor', 'Engineer',
                                             'Entrepreneur', 'Journalist', 'Lawyer', 'Manager', 'Mechanic',
                                             'Media_Manager', 'Musician', 'Scientist', 'Teacher', 'Writer'])

    # Convert the selected occupation to one-hot encoding
    occupation_columns = ['Occupation_' + o.replace(' ', '_') for o in ['Accountant', 'Architect', 'Developer', 'Doctor', 'Engineer',
                                                                        'Entrepreneur', 'Journalist', 'Lawyer', 'Manager', 'Mechanic',
                                                                        'Media_Manager', 'Musician', 'Scientist', 'Teacher', 'Writer']]
    occupation_values = [1 if occupation_columns[i] == 'Occupation_' + occupation.replace(' ', '_') else 0 for i in range(len(occupation_columns))]
    
    # Store user input data into a DataFrame
    user_data = pd.DataFrame({
        'Age': [age],
        'Annual_Income': [annual_income],#[19114.12],
        'Delay_from_due_date': [delay_from_due_date],#[3],
        'Num_of_Delayed_Payment':[num_of_delayed_payment],# [9],
        'Outstanding_Debt': [outstanding_debt],#[809.98],
        'Credit_History_Age': [credit_history_age],#[22.10],
        'Payment_of_Min_Amount': [1 if payment_of_min_amount == 'Yes' else 2],
        'Total_EMI_per_month':[total_emi_per_month],# [49.574949],#[total_emi_per_month],
        'Payment_Behaviour': [payment_behaviour],#[5],# [payment_behaviour],
        'Monthly_Balance': [monthly_balance],#[361.444004],
        #'occupation': ,
        # Add occupation columns
       #**dict(zip(occupation_columns, occupation_values))
    })
    
    
    #f=open('Dataset\\train_train1.csv')
    df=pd.read_csv('Dataset\\train_train1.csv')
    d=dict(zip(occupation_columns, occupation_values))
    for k in d:
        df[k]=d[k]
    #print(dict(zip(occupation_columns, occupation_values)))
    print(df)
    print(df.iloc[[1]])
    print(df.columns)
    #print(user_data)
    # Make predictions
    if st.button('Predict'):
        credit_score = model.predict(df)[4]
        st.success(f'Predicted Credit Score: {credit_score}')

if __name__ == '__main__':
    main()
