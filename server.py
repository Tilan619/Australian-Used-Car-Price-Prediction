import pickle
import numpy as np
#from flask import (Flask,request, jsonify)

import streamlit as st


model = pickle.load(open('rf_regressor_model_AUS_car.pickle', 'rb'))

st.title('Australian Used Car Price Predictor')


Year = st.number_input("Manufactured Year", 2000,2030)
Transmission = st.selectbox("Transmission Type", ['Automatic','Manual'])
DriveType = st.selectbox("Drive type", ['4WD','AWD','Front','Rear'])
FuelType = st.selectbox("Fuel type", ['Diesel','Electric','Hybrid','Premium','Unleaded'])
FuelConsumption = float(st.number_input("Fuel Consumption Per 100 km in litres", 0,50))
Kilometres = st.number_input("Kilometres Driven", 5000,400000)
CylindersinEngine = st.slider("Number of Cylinders in Engine",0,12)
BodyType = st.selectbox("Body type", ['Commercial','Convertible','Coupe','Hatchback','SUV','Sedan','Ute / Tray','Wagon'])
Doors = st.slider("Number of Doors",0,5)
Seats = st.slider("Number of Seats",0,10)

def get_estimated_price(Year,Transmission,DriveType,FuelType,FuelConsumption,Kilometres,CylindersinEngine,BodyType,Doors,Seats):
        dict ={'Transmission':{'Automatic': 0, 'Manual': 1},
        'DriveType':{'4WD': 0, 'AWD': 1, 'Front': 2, 'Rear': 3},
        'FuelType':{'Diesel': 0, 'Electric': 1, 'Hybrid': 2, 'Premium': 3, 'Unleaded': 4},
        'BodyType':{'Commercial': 0, 'Convertible': 1, 'Coupe': 2, 'Hatchback': 3, 'SUV': 4, 'Sedan': 5, 'Ute / Tray': 6,
         'Wagon': 7}}
        x = np.zeros(10)
        x[0] = Year
        x[1] = dict['Transmission'][Transmission]
        x[2] = dict['DriveType'][DriveType]
        x[3] = dict['FuelType'][FuelType]
        x[4] = FuelConsumption
        x[5] = Kilometres
        x[6] = CylindersinEngine
        x[7] = dict['BodyType'][BodyType]
        x[8] = Doors
        x[9] = Seats

        return round(model.predict([x])[0],2)
price = 0
if st.button('Predict'):
    price= get_estimated_price(Year,Transmission, DriveType, FuelType, FuelConsumption, Kilometres,
                        CylindersinEngine, BodyType, Doors,Seats)
st.success(price)
