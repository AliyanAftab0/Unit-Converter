import streamlit as st

# Set page config
st.set_page_config(page_title="Unit Converter", page_icon="⚖️", layout="centered")

# Set page title
st.title("Unit Converter")

# Dropdown for unit types
unit_type = st.selectbox("Select Unit Type", ["Length"])

# Input value
try:
    value = st.number_input("Enter Value", min_value=0.0, value=0.0)
except Exception as e:
    st.error("Invalid input! Please enter a valid number.")
    value = 0.0  # Default value if input is invalid

# Length conversion factors (1 meter = X unit)
length_conversion = {
    "Metre": 1,
    "Kilometre": 1000,
    "Centimetre": 0.01,
    "Millimetre": 0.001,
    "Micrometre": 1e-6,
    "Nanometre": 1e-9,
    "Mile": 1609.34,
    "Yard": 0.9144,
    "Foot": 0.3048,
    "Inch": 0.0254,
    "Nautical mile": 1852,
}

# Dropdowns for "From" and "To" units
from_unit = st.selectbox("From", list(length_conversion.keys()))
to_unit = st.selectbox("To", list(length_conversion.keys()))

# Conversion logic
if unit_type == "Length":
    try:
        # Convert the value to meters first
        value_in_meters = value * length_conversion[from_unit]
        # Convert meters to the target unit
        result = value_in_meters / length_conversion[to_unit]
    except KeyError:
        st.error("Invalid unit selected. Please check your 'From' and 'To' units.")
        result = 0.0
    except ZeroDivisionError:
        st.error("Cannot divide by zero. Please check your conversion units.")
        result = 0.0
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        result = 0.0

# Display result
if st.button("Convert"):
    if value < 0:
        st.error("Value cannot be negative. Please enter a positive number.")
    elif result == 0.0:
        st.warning("Conversion failed. Please check your inputs.")
    else:
        st.success(f"**Result:** {value:.2f} {from_unit} = {result:.6f} {to_unit}")