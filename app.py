import streamlit as st
import streamlit.components.v1 as components

def length_converter(value, from_unit, to_unit):
    units = {'meters': 1, 'kilometers': 0.001, 'centimeters': 100, 'millimeters': 1000, 'miles': 0.000621371, 'yards': 1.09361, 'feet': 3.28084, 'inches': 39.3701}
    if from_unit not in units or to_unit not in units:
        return None
    return value * (units[to_unit] / units[from_unit])

def weight_converter(value, from_unit, to_unit):
    units = {'grams': 1, 'kilograms': 0.001, 'milligrams': 1000, 'pounds': 0.00220462, 'ounces': 0.035274}
    if from_unit not in units or to_unit not in units:
        return None
    return value * (units[to_unit] / units[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversions = {
        ('Celsius', 'Fahrenheit'): lambda x: (x * 9/5) + 32,
        ('Fahrenheit', 'Celsius'): lambda x: (x - 32) * 5/9,
        ('Celsius', 'Kelvin'): lambda x: x + 273.15,
        ('Kelvin', 'Celsius'): lambda x: x - 273.15,
        ('Fahrenheit', 'Kelvin'): lambda x: (x - 32) * 5/9 + 273.15,
        ('Kelvin', 'Fahrenheit'): lambda x: (x - 273.15) * 9/5 + 32
    }
    return conversions.get((from_unit, to_unit), lambda x: None)(value)

st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
st.markdown("""
    <style>
        .stApp {
            background-color: #f4f4f4;
        }
        .stTextInput, .stSelectbox, .stButton>button {
            border-radius: 8px;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🔄 Unit Converter")
st.markdown("Convert between different units of measurement effortlessly.")
category = st.radio("Select Conversion Type", ["Length", "Weight", "Temperature"], horizontal=True)

if category == "Length":
    units = ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet', 'inches']
elif category == "Weight":
    units = ['grams', 'kilograms', 'milligrams', 'pounds', 'ounces']
elif category == "Temperature":
    units = ['Celsius', 'Fahrenheit', 'Kelvin']

value = st.number_input("Enter Value:", min_value=0.0, format="%.4f")
from_unit = st.selectbox("From Unit", units)
to_unit = st.selectbox("To Unit", units)

if st.button("Convert", use_container_width=True):
    if category == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif category == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif category == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)
    
    if result is not None:
        st.success(f"Converted Value: {result:.4f} {to_unit}")
    else:
        st.error("Invalid conversion units selected.")
