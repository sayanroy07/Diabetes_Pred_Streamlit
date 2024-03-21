import streamlit as st
import pickle


#Sidebar Details
with st.sidebar:
    st.markdown('''
    # About the Model:
    The purpose of this application is to be able to correctly predict whether you have Diabetes or not
    - Model - XGBoost Classifier
    - Threshold - 0.39
    - ROC - 97.4
    - Recall - 0.77
    - Dataset - https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset
    - My Github Link - https://github.com/sayanroy07
    ''')
    st.write("Developed by Sayan Roy")

def prediction(age, ht1, hd1, bmi, hb, bgl, g_m1, g_t1, s_p1, s_c1):
    final = model.predict([[age, ht1, hd1, bmi, hb, bgl, g_m1, g_t1, s_p1, s_c1]])
    print(final)
    return final
st.title("Diabetes Prediction Application")
st.write("Please enter below details to check if you have Diabetes?")



age = st.number_input("Age", key='age')
bmi = st.number_input("Body Mass Index {https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm}",key='bmi')
hb = st.number_input("HBA1C level {https://www.ncbi.nlm.nih.gov/books/NBK549816/#:~:text=Diagnostic%20Tests&text=For%20an%20HbA1c%20test%20to,HbA1c%20of%206.5%25%20or%20higher.}",key='hb')
bgl = st.number_input("Blood Glucose level",key='bgl')
st.write("Please tick wherever applicable")
g_m = st.checkbox("Gender = Male",key='g_m')
if g_m is True:
    g_m1=1
else:
    g_m1=0
g_t = st.checkbox("Gender = Trans",key='g_t')
if g_t is True:
    g_t1=1
else:
    g_t1=0
ht = st.checkbox("Hyper Tension", key='ht')
if ht is True:
    ht1=1
else:
    ht1=0
hd = st.checkbox("Heart Disease",key='hd')
if hd is True:
    hd1=1
else:
    hd1=0
s_p = st.checkbox("Past Smoker",key='s_p')
if s_p is True:
    s_p1 = 1
else:
    s_p1 = 0
s_c = st.checkbox("Current Smoker", key='s_c')
if s_c is True:
    s_c1 = 1
else:
    s_c1 = 0
#s_c = st.number_input("Please enter whether you are a current Smoker?")
pred = st.button("Predict", type="primary")

def reset():
    st.session_state.age = 0
    st.session_state.bmi = 0
    st.session_state.hb = 0
    st.session_state.bgl = 0
    st.session_state.g_m = 0
    st.session_state.g_t = 0
    st.session_state.ht = 0
    st.session_state.hd = 0
    st.session_state.s_p = 0
    st.session_state.s_c = 0

reset = st.button('Reset', on_click=reset, type="primary")
result = 0
model = pickle.load(open("model.pkl","rb"))
if pred:
    result = prediction(age, ht1, hd1, bmi, hb, bgl, g_m1, g_t1, s_p1, s_c1)

if result is not None:
    if result == 0:
        st.success('Good News, You are not Diabetic:smile')
    else:
        st.success('Bad News, You have Diabetes')



def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
if __name__ == '__main__':
    print_hi('PyCharm')






