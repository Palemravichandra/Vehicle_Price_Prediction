import pandas as pd
import streamlit as st
import pickle
import sklearn
import numpy as np
import datetime

df=pd.read_csv('car_data.xls')
forest = open('Car_Price_prediction_model.pkl','rb')
model = pickle.load(forest)
st.title(':violet[VEHICLE PRICE PREDICTION APP]')
dict={'ritz': 90.0, 'sx4': 93.0, 'ciaz': 68.0, 'wagon_r': 96.0, 'swift': 92.0,'vitara_brezza': 95.0, 's_cross': 91.0, 'alto_800': 62.0, 'ertiga': 76.0, 'dzire': 73.0, 'alto_k10': 63.0,
      'ignis': 85.0, '800': 0.0, 'baleno': 65.0, 'omni': 89.0, 'fortuner': 81.0, 'innova': 86.0, 'corolla_altis': 71.0, 'etios_cross': 77.0, 'etios_g': 78.0, 'etios_liva': 80.0,
      'corolla': 70.0, 'etios_gd': 79.0, 'camry': 67.0, 'land_cruiser': 88.0, 'Royal_Enfield_Thunder_500': 49.0, 'UM_Renegade_Mojave': 56.0, 'KTM_RC200': 42.0, 'Bajaj_Dominar_400': 11.0,
      'Royal_Enfield_Classic_350': 46.0, 'KTM_RC390': 43.0, 'Hyosung_GT250R': 40.0, 'Royal_Enfield_Thunder_350': 48.0, 'KTM_390_Duke_': 41.0, 'Mahindra_Mojo_XT300': 44.0,
      'Bajaj_Pulsar_RS200': 17.0, 'Royal_Enfield_Bullet_350': 45.0, 'Royal_Enfield_Classic_500': 47.0, 'Bajaj_Avenger_220': 6.0, 'Bajaj_Avenger_150': 4.0, 'Honda_CB_Hornet_160R': 32.0,
      'Yamaha_FZ_S_V_2.0': 60.0, 'Yamaha_FZ_16': 58.0, 'TVS_Apache_RTR_160': 51.0, 'Bajaj_Pulsar_150': 14.0, 'Honda_CBR_150': 37.0, 'Hero_Extreme': 20.0, 'Bajaj_Avenger_220_dtsi': 7.0,
      'Bajaj_Avenger_150_street': 5.0, 'Yamaha_FZ__v_2.0': 57.0, 'Bajaj_Pulsar__NS_200': 12.0, 'Bajaj_Pulsar_220_F': 15.0, 'TVS_Apache_RTR_180': 52.0, 'Hero_Passion_X_pro': 26.0,
      'Bajaj_Pulsar_NS_200': 16.0, 'Yamaha_Fazer_': 61.0, 'Honda_Activa_4G': 31.0, 'TVS_Sport_': 54.0, 'Honda_Dream_Yuga_': 38.0, 'Bajaj_Avenger_Street_220': 8.0, 'Hero_Splender_iSmart': 28.0,
      'Activa_3g': 1.0, 'Hero_Passion_Pro': 25.0, 'Honda_CB_Trigger': 34.0, 'Yamaha_FZ_S_': 59.0, 'Bajaj_Pulsar_135_LS': 13.0, 'Activa_4g': 2.0, 'Honda_CB_Unicorn': 35.0, 'Hero_Honda_CBZ_extreme': 22.0,
      'Honda_Karizma': 39.0, 'Honda_Activa_125': 30.0, 'TVS_Jupyter': 53.0, 'Hero_Honda_Passion_Pro': 23.0, 'Hero_Splender_Plus': 27.0, 'Honda_CB_Shine': 33.0, 'Bajaj_Discover_100': 9.0,
      'Suzuki_Access_125': 50.0, 'TVS_Wego': 55.0, 'Honda_CB_twister': 36.0, 'Hero_Glamour': 21.0, 'Hero_Super_Splendor': 29.0, 'Bajaj_Discover_125': 10.0, 'Hero_Hunk': 24.0,
      'Hero__Ignitor_Disc': 19.0, 'Hero__CBZ_Xtreme': 18.0, 'Bajaj__ct_100': 3.0, 'i20': 84.0, 'grand_i10': 82.0, 'i10': 83.0, 'eon': 75.0, 'xcent': 97.0, 'elantra': 74.0, 'creta': 72.0,
      'verna': 94.0, 'city': 69.0, 'brio': 66.0, 'amaze': 64.0, 'jazz': 87.0}

#code to remove whitespace
def remove(string):
    return string.replace(" ", "_")

col1,col2=st.columns(2)
with col1:
    # For vehicle Type
    vehicle=st.selectbox(':blue[Select Vehicle]',df['Car_Name'].unique())
    if vehicle:
        veh=remove(vehicle)
        vehicle=dict[veh]
    #st.write(vehicle)

    # For price column
    price=st.text_input(':blue[Enter The Present Price of Vehicle in Lacks]')
    if price:
        present_price=int(price)


    # Seller Type
    seller = st.selectbox(':blue[Select Seller Type]', ['Dealer', 'Individual'])
    if seller == 'Dealer':
        Seller_Type = 0
    else:
        Seller_Type = 1
    # st.write(Seller_Type)


    # For Kilometers driven
    kilometers_driven = st.text_input(':blue[Enter the Number of Kilometers Driven]')
    if kilometers_driven:
        kilometers_driven = int(kilometers_driven)
    #st.write(kilometers_driven)



with col2:
    # For Transmission Type
    trans=st.selectbox(':blue[Select Transmission Type]',['Manual', 'Automatic'])
    if trans == 'Manual':
        Transmission=0
    else:
        Transmission = 1
    #st.write(Transmission)

    # For owner
    owner=st.text_input(':blue[Enter The Number Of Owners]')
    if owner:
        owner=int(owner)
    #st.write(owner)

     # For fuel column
    fuel = st.selectbox(':blue[Select Fuel Type]', ['Petrol', 'Diesel', 'CNG'])
    if fuel == 'Petrol':
        fuel_type = 0
    elif fuel == 'Diesel':
        fuel_type = 1
    else:
        fuel_type = 2
    # st.write(fuel_type)

    # For age column
    age=st.text_input(':blue[Enter The Registered Year of Vehicle]')
    if age:
        date_time = datetime.datetime.now()
        age= date_time.year-int(age)

    #st.write(age)

predict=st.button('predict')
if predict:
    prediction=model.predict([[vehicle,present_price, kilometers_driven, fuel_type, Seller_Type, Transmission, owner, age]])
    st.write("### :green[The predicted price of vehicle is]",int(prediction[0]))

st.write( f'<h5 style="color:rgb(0, 153, 153,0.35);">App Created by RAVI CHANDRA PALEM </h5>', unsafe_allow_html=True )


