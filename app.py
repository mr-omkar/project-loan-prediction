import pandas as pd
import numpy as np

import streamlit as st
import dill





def get_form(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12):
    res = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12]
    # res_2 = [i3,i4,i5,i6,i7,i8,i9,i10,i11,i12]
    res_df = pd.DataFrame([[i3,i4,i5,i6,i7,i8,i9,i10,i11,i12]])
    res_df.columns=["Married","Dependents","Education","Self_Employed","ApplicantIncome","CoapplicantIncome","LoanAmount","Loan_Amount_Term","Credit_History","property_Area"]
    print(res_df)
    print(res_df.info())
    print("get form clicked")
    if all(res):
        print("all fields are ok")
        with open("loan_m1.pkl","rb") as f:
            p1 = dill.load(f)
            p1_res = p1.predict(res_df)
            print("output 1",p1_res)
    else:
        print("All Fields are mandatory")
        st.warning("All Fields are mandatory")


form = st.form("Loan_Details",clear_on_submit=True)
in_name  = form.text_input("Enter Your Name")
in_email = form.text_input("Enter Email")
inp_marst = form.radio("Married",("yes","No"))
inp_dep = form.radio("Dependents",(["0","1","2","3+"]))
inp_edu = form.radio("Education",("Graduate","Not Graduate"))
inp_emp = form.radio("Self Employed",("yes","no"))
inp_apinc = form.number_input("Applicant Income")
inp_coapinp = form.number_input("Co-applicant Income")
inp_lamt = form.number_input("Loan Amount")
inp_lamtTerm = form.selectbox("Loan Amount Term",["30.0", "10.0", "20.0", "15.0",  "5.0", "25.0", "40.0",  "3.0",  "7.0",  "1.0"])
inp_credit = form.selectbox("Credit History",["1.0","0.0"])
inp_prop = form.radio("Property Area",['Urban', 'Rural', 'Semiurban'])
form.form_submit_button("Submit",on_click=get_form(in_name,in_email,inp_marst,inp_dep,inp_edu,inp_emp,inp_apinc,inp_coapinp,inp_lamt,inp_lamtTerm,inp_credit,inp_prop))




