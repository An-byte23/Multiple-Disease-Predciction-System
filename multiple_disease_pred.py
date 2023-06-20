# streamlit run multiple_disease_pred.py
import warnings
# Settings the warnings to be ignored
warnings.filterwarnings('ignore')
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading saved model
diabetes_model = pickle.load(open("diabetes_model.sav","rb"))
diabetes_standardized = pickle.load(open("diabetes_standard.sav","rb"))

heart_model = pickle.load(open("heart_model.sav","rb"))

parkinson_model = pickle.load(open("parkinson_model.sav","rb"))
parkinson_standardized = pickle.load(open("parkinson_standard.sav","rb"))

def diabetes_prediction(input_data):

    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshape=input_data_as_numpy_array.reshape(1,-1)
    std_data=diabetes_standardized.transform(input_data_reshape)
    pred=diabetes_model.predict(std_data)
    if(pred[0]==0):
        return "The patient is Non-Diabetic"
    else:
        return "The patient is Diabetic"

def parkinsion_func(input_data):
    input_data_asnumpyarray=np.asarray(input_data)
    input_data_reshaped=input_data_asnumpyarray.reshape(1,-1)
    input_data_standard=parkinson_standardized.transform(input_data_reshaped)
    output=parkinson_model.predict(input_data_standard)
    if(output[0]==1):
        return "The person has Parkinson's Disease"
    else:
        return "The person does not have Parkinson's Disease"

# creatring sidebar for navigation

with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                        ['Diabetes Prediction',
                        'Heart Disease Prediction',
                        'Parkinsons Prediction'],
                        icons=['activity','heart','person'],
                        default_index=0)


# Diabetes Prediction Page
if(selected=='Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')

    # getting input data from user
    # columns for input fields
    col1,col2,col3=st.columns(3)
    with col1:
        pregnancies=st.text_input('Number of Pregnancies')
    with col2:
        glucose=st.text_input('Blood Glucose Level')
    with col3:
        bp=st.text_input('Blood Pressure Value')
    with col1:
        skin_thick=st.text_input('Skin Thickness Value')
    with col2:
        insulin=st.text_input('Insulin Level')
    with col3:
        bmi=st.text_input('BMI (Body Mass Index) Value')
    with col1:
        dpf=st.text_input('Diabetes Pedigree Function Value')
    with col2:
        age=st.text_input('Age of the patient')

    #code for prediction
    diab_diagnosis = ''
    # creating button for prediction
    if st.button("Get Diabetes Test Result"):
        diab_diagnosis=diabetes_prediction([pregnancies,glucose,bp,skin_thick,insulin,bmi,dpf,age])

    st.success(diab_diagnosis)


# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Sex')
        
    with col3:
        cp = st.number_input('Chest Pain types')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    


# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)',format="%.6f")
        
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)',format="%.6f")
        
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)',format="%.6f")
        
    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)',format="%.6f")
        
    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)',format="%.6f")
        
    with col1:
        RAP = st.number_input('MDVP:RAP',format="%.6f")
        
    with col2:
        PPQ = st.number_input('MDVP:PPQ',format="%.6f")
        
    with col3:
        DDP = st.number_input('Jitter:DDP',format="%.6f")
        
    with col4:
        Shimmer = st.number_input('MDVP:Shimmer',format="%.6f")
        
    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)',format="%.6f")
        
    with col1:
        APQ3 = st.number_input('Shimmer:APQ3',format="%.6f")
        
    with col2:
        APQ5 = st.number_input('Shimmer:APQ5',format="%.6f")
        
    with col3:
        APQ = st.number_input('MDVP:APQ',format="%.6f")
        
    with col4:
        DDA = st.number_input('Shimmer:DDA',format="%.6f")
        
    with col5:
        NHR = st.number_input('NHR',format="%.6f")
        
    with col1:
        HNR = st.number_input('HNR',format="%.6f")
        
    with col2:
        RPDE = st.number_input('RPDE',format="%.6f")
        
    with col3:
        DFA = st.number_input('DFA',format="%.6f")
        
    with col4:
        spread1 = st.number_input('spread1',format="%.6f")
        
    with col5:
        spread2 = st.number_input('spread2',format="%.6f")
        
    with col1:
        D2 = st.number_input('D2',format="%.6f")
        
    with col2:
        PPE = st.number_input('PPE',format="%.6f")
        
    
    #code for prediction
    parkinsons_diagnosis = ''
    # creating button for prediction
    if st.button("Get Parkinsions Disease Test Result"):
        parkinsons_diagnosis=parkinsion_func([fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE])

    st.success(parkinsons_diagnosis)
