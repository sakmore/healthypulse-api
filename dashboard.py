import streamlit as st
import requests
import time

API_URL = "https://healthypulse-api.onrender.com/vitals"  # use your Render URL here

st.title("🏥 HealthPulse - Live Patient Vitals")

placeholder = st.empty()

while True:
    try:
        response = requests.get(API_URL)
        data = response.json()

        with placeholder.container():
            st.metric("Heart Rate (bpm)", data['heart_rate'])
            st.metric("Blood Pressure", data['blood_pressure'])
            st.metric("Temperature (°F)", data['temperature'])
            st.metric("SpO2 (%)", data['spo2'])

        time.sleep(5)  # updates every 5 seconds

    except:
        st.warning("Waiting for API response...")
        time.sleep(5)
