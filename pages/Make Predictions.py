import streamlit as st
import numpy as np
import pandas as pd

from helper import predict_linreg

# set page titie so that it doesnt use my python filename
st.set_page_config(
    page_title="Make Predictions",
    page_icon="😈"
)
st.title("Energy Consumption Predictions")

# load the model
@st.cache_resource
def load_model():
    data = np.load('./training/multiRegressionModel.npz', allow_pickle=True)
    beta = data['beta']
    means = data['means']
    stds = data['stds']
    feature_columns = data['feature_columns']
    return beta, means, stds, feature_columns

beta, means, stds, feature_columns = load_model()



# obtain user inputs
userInputs = {}
with st.form("predict", clear_on_submit=True):
    # make it 2 columns for compactness
    col1, col2 = st.columns(2)
    with col1:
        temp = st.number_input("Temperature (°C)", step=0.1, format="%.1f")
        humidity = st.number_input("Humidity (%)", step=0.1, format="%.1f")
        sqft = st.number_input("Square Footage", step=1.0)
        occupancy = st.number_input("Occupancy", step=1)
        renewable = st.number_input("Renewable Energy (kWh)", step=0.1)

    with col2:
        hvac = st.radio("HVAC Usage", ["On", "Off"], help="HVAC refers to Heater, Ventilator and Air-Con Appliances")
        lighting = st.radio("Lighting Usage", ["On", "Off"], help="Select On if your lighting is currently on")
        day = st.selectbox("Day of Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        holiday = st.radio("Holiday", ["Yes", "No"])

    submitted = st.form_submit_button("Predict")

# store data into session state
if submitted:
    st.session_state["inputs"] = {
    "Temperature": temp,
    "Humidity": humidity,
    "SquareFootage": sqft,
    "Occupancy": occupancy,
    "RenewableEnergy": renewable,
    "HVACUsage_On": 1 if hvac == "On" else 0,
    "LightingUsage_On": 1 if lighting == "On" else 0,
    "DayOfWeek_Monday": int(day == "Monday"),
    "DayOfWeek_Tuesday": int(day == "Tuesday"),
    "DayOfWeek_Wednesday": int(day == "Wednesday"),
    "DayOfWeek_Thursday": int(day == "Thursday"),
    "DayOfWeek_Friday": int(day == "Friday"),
    "DayOfWeek_Saturday": int(day == "Saturday"),
    "DayOfWeek_Sunday": int(day == "Sunday"),
    "Holiday_Yes": 1 if holiday == "Yes" else 0
}

# rebuild the input vector asimilar to how we dump into the model for prediction
inputFeatures = []
for col in feature_columns:
    value = st.session_state.get("inputs", {}).get(col, 0)
    inputFeatures.append(value)

# convert to numpy array
inputFeatures = np.array(inputFeatures).reshape(1, -1)

# predictions
prediction = predict_linreg(inputFeatures, beta, means, stds)

st.success(f"🔮 Predicted Energy Consumption: **{prediction.item():.2f} kWh**")