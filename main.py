import streamlit as st
import pandas as pd
import numpy as np
import joblib


manufacturer_dic = {'Audi':0,
 'BMW':1,
 'ford':2,
 'hyundi':3,
 'merc':4,
 'skoda':5,
 'toyota':6,
 'vauxhall':7,
 'volkswagen':8}
transmission_dic = {'Automatic':0,'Manual':1, 'Other':2, 'Semi-Auto':3}
fuelType_dic = {'Diesel':0, 'Electric':1, 'Hybrid':2, 'Other':3, 'Petrol':4}
model_dic = {' 1 Series': 0,
' 2 Series': 1,
' 3 Series': 2,
' 4 Series': 3,
' 5 Series': 4,
' 6 Series': 5,
' 7 Series': 6,
' A Class': 7,
' A1': 8,
' A3': 9,
' A4': 10,
' A5': 11,
' A6': 12,
' A7': 13,
' Adam': 14,
' Agila': 15,
' Amarok': 16,
' Ampera': 17,
' Antara': 18,
' Arteon': 19,
' Astra': 20,
' Auris': 21,
' Avensis': 22,
' Aygo': 23,
' B Class': 24,
' B-MAX': 25,
' Beetle': 26,
' C Class': 27,
' C-HR': 28,
' C-MAX': 29,
' CC': 30,
' CL Class': 31,
' CLA Class': 32,
' CLS Class': 33,
' Caddy': 34,
' Caddy Life': 35,
' Caddy Maxi': 36,
' Caddy Maxi Life': 37,
' Camry': 38,
' Caravelle': 39,
' Cascada': 40,
' Citigo': 41,
' Combo Life': 42,
' Corolla': 43,
' Corsa': 44,
' Crossland X': 45,
' E Class': 46,
' EcoSport': 47,
' Edge': 48,
' Eos': 49,
' Fabia': 50,
' Fiesta': 51,
' Focus': 52,
' GL Class': 53,
' GLA Class': 54,
' GLB Class': 55,
' GLC Class': 56,
' GLE Class': 57,
' GT86': 58,
' GTC': 59,
' Galaxy': 60,
' Golf': 61,
' Golf SV': 62,
' Grand C-MAX': 63,
' Grand Tourneo Connect': 64,
' Grandland X': 65,
' Hilux': 66,
' I10': 67,
' I20': 68,
' I30': 69,
' I40': 70,
' I800': 71,
' IQ': 72,
' IX20': 73,
' IX35': 74,
' Insignia': 75,
' Ioniq': 76,
' Jetta': 77,
' KA': 78,
' Ka+': 79,
' Kadjar': 80,
' Kamiq': 81,
' Karoq': 82,
' Kodiaq': 83,
' Kona': 84,
' Kuga': 85,
' Land Cruiser': 86,
' M Class': 87,
' Meriva': 88,
' Mokka': 89,
' Mokka X': 90,
' Mondeo': 91,
' Mustang': 92,
' Octavia': 93,
' PROACE VERSO': 94,
' Passat': 95,
' Polo': 96,
' Prius': 97,
' Puma': 98,
' Q2': 99,
' Q3': 100,
' Q5': 101,
' RAV4': 102,
' RS3': 103,
' RS4': 104,
' RS5': 105,
' Rapid': 106,
' Roomster': 107,
' S Class': 108,
' S-MAX': 109,
' S3': 110,
' S4': 111,
' SL CLASS': 112,
' SLK': 113,
' SQ5': 114,
' Santa Fe': 115,
' Scala': 116,
' Scirocco': 117,
' Sharan': 118,
' Shuttle': 119,
' Superb': 120,
' T-Cross': 121,
' T-Roc': 122,
' TT': 123,
' Tiguan': 124,
' Tiguan Allspace': 125,
' Touran': 126,
' Tourneo Connect': 127,
' Tourneo Custom': 128,
' Transit Tourneo': 129,
' Tucson': 130,
' Up': 131,
' Urban Cruiser': 132,
' V Class': 133,
' Veloster': 134,
' Verso': 135,
' Verso-S': 136,
' Viva': 137,
' Vivaro': 138,
' X-CLASS': 139,
' X1': 140,
' X2': 141,
' X3': 142,
' X4': 143,
' X5': 144,
' Yaris': 145,
' Yeti': 146,
' Yeti Outdoor': 147,
' Z4': 148,
' Zafira': 149,
' Zafira Tourer': 150,
' i3': 151,
' i8': 152,
'180': 153,
'200': 154,
'220': 155,
' E Class': 156}

#categorical values list
manufacturer_list = ['Audi',
 'BMW',
 'ford',
 'hyundi',
 'merc',
 'skoda',
 'toyota',
 'vauxhall',
 'volkswagen']
transmission_list = ['Automatic', 'Manual', 'Other', 'Semi-Auto']
fuelType_list = ['Diesel', 'Electric', 'Hybrid', 'Other', 'Petrol']

st.set_page_config(page_title="Car Price Prediction")

cars = pd.read_csv('CleanedCarReport.csv')

def find_model(manf):
    models = cars[cars['Manufacturer'] == manf]['model']
    return list(models)

@st.cache_data
def model_loader(path):
    models = joblib.load(path)
    return models

with st.spinner('.... The app is retrieving !! ...'):
    forest_model = model_loader("RF_Car_ModeLPredict.pkl")


st.markdown("<h2 style = 'text-align: center;'> Car Price Prediction Tool </h2>", unsafe_allow_html=True )

col1, col2 = st.columns(2)

mileage = col1.number_input(label="Enter Mileage")
year = col1.slider("Enter the year, eg: 2005", 1980, 2020, 2025)

manufacturer_inp = col1.selectbox(label="Select Manufacturer", options=manufacturer_list)
manufacturer = manufacturer_dic[manufacturer_inp]

fuelType_inp = col1.selectbox(label="Select Fuel Type", options = fuelType_list)
fuelType = fuelType_dic[fuelType_inp]

engsize = col2.number_input(label="Enter Engine Size, eg: 1.0", max_value=6.0)
engsize = float(engsize)

transmission_inp = col2.selectbox(label="Select Transmission Type", options = transmission_list)
transmission = transmission_dic[transmission_inp]

if manufacturer_inp == 'Audi':
    model_inp = col2.selectbox("Select the Car Model", options = find_model('Audi'))
    model = model_dic[model_inp]
elif manufacturer_inp == 'BMW':
    model_inp = col2.selectbox("Select the Car Model", options = find_model('BMW'))
    model = model_dic[model_inp]
elif manufacturer_inp == 'ford':
    model_inp = col2.selectbox("Select the Car Model", options = find_model('ford'))
    model = model_dic[model_inp]
elif manufacturer_inp == 'hyundi':
    model_inp = col2.selectbox("Select the Car Model", options = find_model('hyundi'))
    model = model_dic[model_inp]
elif manufacturer_inp == 'merc':
    model_inp = col2.selectbox("Select the Car Model", options = find_model('merc'))
    model = model_dic[model_inp]
elif manufacturer_inp == 'skoda':
    model_inp = col2.selectbox("Select the Car Model", options = find_model('skoda'))
    model = model_dic[model_inp]
elif manufacturer_inp == 'toyota':
    model_inp = col2.selectbox("Select the Car Model", options = find_model('toyota'))
    model = model_dic[model_inp]
elif manufacturer_inp == 'vauxhall':
    model_inp = col2.selectbox("Select the Car Model", options = find_model('vauxhall'))
    model = model_dic[model_inp]
elif manufacturer_inp == 'volkswagen':
    model_inp = col2.selectbox("Select the Car Model", options = find_model('volkswagen'))
    model = model_dic[model_inp]

tax = col2.number_input(label="Enter the Tax Amount, eg: 140")
mpg = col2.number_input(label="Enter the MilesPerGallon, eg: 160")


imp_array = np.array([[mileage, year, manufacturer, fuelType, engsize, transmission, model, tax, mpg]])

predict = col1.button('Predict')

if predict:
    pred = forest_model.predict(imp_array)
    if pred < 0:
        st.error("Please check your input values and try again !")
    pred = round(float(pred),2)
    write = "The predicted car amount in $ is:"+ " " + str(pred)
    st.success(write)
    st.balloons()



