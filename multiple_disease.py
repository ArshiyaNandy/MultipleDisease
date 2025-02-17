
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model=pickle.load(open('diabetes_model.sav','rb'))

heart_disease_model=pickle.load(open('heart_model.sav','rb'))

parkinsons_model=pickle.load(open('parkinsons_model.sav','rb'))





#sidebar for navigation

with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinsons Prediction'
                          ],
                         
                          icons=['activity','heart','person'],
                          default_index=0)
                          
  # Diabetes Prediction page
if (selected=='Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction using ML')
    #gettinginput from user
    
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
    with col2:
        Glucose=st.text_input('Glucose Level')
    with col3:
        BloodPresure=st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness=st.text_input('Skin Thickness Value')
    with col2:
        Insulin=st.text_input('Insulin Level')
    with col3:
        BMI=st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age=st.text_input('Age of the person')
    
    #code for Prediction
    diab_diagnosis=''
    
    #creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPresure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        # Example if diab_prediction is a scikit-learn model:
        if (diab_prediction[[0]] == 1):
    

            diab_diagnosis='The person is Diabetic'
            
        else:
            diab_diagnosis='The person is not Diabetic'
    
    st.success(diab_diagnosis)
            
              
if (selected=='Heart Disease Prediction'):
     #page title
     st.title('Heart Disease Prediction using ML')
     
     col1,col2=st.columns(2)
     
     with col1:
         age=st.text_input('Age')
     with col2:
         sex=st.text_input('1 for Male,0 for Female')
     with col1:
         cp=st.text_input('Chest Pain Types')
     with col2:
         trestbps=st.text_input('Resting Blood Pressure')
     with col1:
         chol=st.text_input('Serum Cholesterol in mg/dl')
     with col2:
         fbs=st.text_input('Fasting Blood sugar>120 mg/dL')
     with col1:
         restecg=st.text_input('Resting Electrocardiographic results')
     with col2:
         thalach=st.text_input('Maximum Heart Rate Achieved')
     with col1:
         exang=st.text_input('Exercise Induced Angina')
     with col2:
         oldpeak=st.text_input('ST depression induced by exercise')
     with col1:
         slope=st.text_input('Slope of the peak exercise ST segment')
     with col2:
         ca=st.text_input('Number of Major Vessels Colored by Flourosopy')
     with col1:
         thal=st.text_input('Thalassemia')
         
     #code for Prediction
     heart_diagnosis=''
     
     #creating a button for prediction
     
     if st.button('Heart Test Result'):
         heart_prediction=heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
         
         # Example if diab_prediction is a scikit-learn model:
         if (heart_prediction[[0]] == 1):
             heart_diagnosis='The person has Heart Disease'
     
         else:
             heart_diagnosis='The person does not have Heart Disease'
     
     st.success(heart_diagnosis)    
     
if (selected=='Parkinsons Prediction'):
     #page title
     st.title('Parkinsons Disease Prediction using ML')
     st.markdown("#### **Fundamental Frequency Features**")
       
     col1,col2,col3=st.columns(3)
     with col1:
          MDVP_Fo_Hz = st.number_input("MDVP:Fo(Hz) - Average fundamental frequency", min_value=50.0, max_value=300.0, step=0.1)
     with col2:
          MDVP_Fhi_Hz = st.number_input("MDVP:Fhi(Hz) - Maximum fundamental frequency", min_value=50.0, max_value=600.0, step=0.1)
     with col3:
          MDVP_Flo_Hz = st.number_input("MDVP:Flo(Hz) - Minimum fundamental frequency", min_value=50.0, max_value=300.0, step=0.1)
     
     st.markdown("#### **Variation in Fundamental Frequency**")
     col1,col2,col3=st.columns(3)
     with col1:
         MDVP_Jitter = st.number_input("MDVP:Jitter(%)", min_value=0.0, max_value=0.1, step=0.0001, format="%.4f")
     with col2:
         MDVP_Jitter_Abs = st.number_input("MDVP:Jitter(Abs)", min_value=0.0, max_value=0.005, step=0.0001, format="%.4f")
     with col3:
         MDVP_RAP = st.number_input("MDVP:RAP", min_value=0.0, max_value=0.1, step=0.0001, format="%.4f")
     with col1:
         MDVP_PPQ = st.number_input("MDVP:PPQ", min_value=0.0, max_value=0.1, step=0.0001, format="%.4f")
     with col2:
         Jitter_DDP = st.number_input("Jitter:DDP", min_value=0.0, max_value=0.1, step=0.0001, format="%.4f")
     
     st.markdown("#### **Variation in Amplitude**")
     col1,col2,col3=st.columns(3)
     with col1:
         MDVP_Shimmer = st.number_input("MDVP:Shimmer", min_value=0.0, max_value=1.0, step=0.01)
     with col2:
         MDVP_Shimmer_dB = st.number_input("MDVP:Shimmer(dB)", min_value=0.0, max_value=10.0, step=0.1)
     with col3:
         Shimmer_APQ3 = st.number_input("Shimmer:APQ3", min_value=0.0, max_value=1.0, step=0.01)
     with col1:
         Shimmer_APQ5 = st.number_input("Shimmer:APQ5", min_value=0.0, max_value=1.0, step=0.01)
     with col2:
         MDVP_APQ = st.number_input("MDVP:APQ", min_value=0.0, max_value=1.0, step=0.01)
     with col3:
         Shimmer_DDA = st.number_input("Shimmer:DDA", min_value=0.0, max_value=1.0, step=0.01)
     
     
     st.markdown("#### **Noise-to-Harmonics Ratio**")
     col1,col2=st.columns(2)
     with col1:
         NHR = st.number_input("NHR - Noise-to-Harmonics Ratio", min_value=0.0, max_value=1.0, step=0.01)
     with col2:
         HNR = st.number_input("HNR - Harmonics-to-Noise Ratio", min_value=0.0, max_value=50.0, step=0.1)
    
     st.markdown("#### **Nonlinear Dynamical Complexity Measures**")
     col1,col2,col3=st.columns(3)
     with col1:
     
         RPDE = st.number_input("RPDE - Recurrence Period Density Entropy", min_value=0.0, max_value=1.0, step=0.01)
     with col2:
         D2 = st.number_input("D2 - Correlation Dimension", min_value=0.0, max_value=5.0, step=0.1)
     with col3:
         DFA = st.number_input("DFA - Detrended Fluctuation Analysis", min_value=0.0, max_value=1.0, step=0.01)

     st.markdown("#### **Nonlinear Measures of Fundamental Frequency Variation**")
     col1,col2,col3=st.columns(3)
     with col1:
         spread1 = st.number_input("Spread1", min_value=-10.0, max_value=0.0, step=0.01)
     with col2:
         spread2 = st.number_input("Spread2", min_value=0.0, max_value=1.0, step=0.01)
     with col3:
         PPE = st.number_input("PPE - Pitch Period Entropy", min_value=0.0, max_value=1.0, step=0.01)
   
     parkinsons_diagnosis=''
     if st.button("Parkinsons Test Result"):
         parkinsons_prediction=parkinsons_model.predict([[MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter, MDVP_Jitter_Abs, 
                            MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, 
                            Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, 
                            RPDE, D2, DFA, spread1, spread2, PPE]])


         if (parkinsons_prediction[[0]] == 1):
             parkinsons_diagnosis='The person has Parkinsons'
              
         else:
             parkinsons_diagnosis='The person is Healthy'
      
     st.success(parkinsons_diagnosis)
              
   
    
                              
