import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('/Users/meetshah/Documents/practise/diabetes/trained_model.sav','rb'))

def diabetes_prediction(input_data):
    

    input_data_as_numpy_array = np. asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape (1, -1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    
    
    print (prediction)
    
    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'


def main():
    
    #giving title
    st.title("Diabetic Predictor")
    
    #values of these columns
         
    pregnancies = st.text_input("No of Pregnancies: ")
    
    glucose = st.text_input("Enter Glucose Level: ")
    
    blood_pressure = st.text_input("Enter Blood Pressure Level: ")
    
    skinthickness = st.text_input("Enter Skin Thickness Value: ")
    
    insulin = st.text_input("Enter Insulin Level: ")
    
    bmi = st.text_input("Enter BMI : ")
    
    diabetes_Pedigree_Function = st.text_input("Enter  Diabetes Pedigree Function: ")
    
    age = st.text_input("Enter Age: ")


    diagnosis = '' 
    
    if st.button("Check If Diabetic"):
        diagnosis = diabetes_prediction([pregnancies,glucose,blood_pressure,skinthickness,insulin,bmi,diabetes_Pedigree_Function,age])
        
    
    st.success(diagnosis)
    
if __name__  == '__main__' :
    main()
        
    
    