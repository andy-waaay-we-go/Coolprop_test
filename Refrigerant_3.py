#pip install streamlit CoolProp modelicares

import inspect
import textwrap
import pandas as pd

import streamlit as st

from CoolProp.CoolProp import PropsSI

import streamlit as st

# Your code goes here

if __name__ == '__main__':
    st.set_page_config(page_title='PH Diagram for R134a Refrigerant')
    st.title('PH Diagram for R134a Refrigerant')
    # Your Streamlit app code goes here

import CoolProp.CoolProp as CP
import modelicares as mr

# Define the temperature range (in K)
T_min = CP.PropsSI('Tmin', 'R134a')
T_max = CP.PropsSI('Tcrit', 'R134a') - 1

# Define the pressure range (in Pa)
P_min = CP.PropsSI('Pmin', 'R134a')
P_max = CP.PropsSI('Pcrit', 'R134a') - 1000

# Create the PH diagram
ph_data = mr.plot_ph('R134a', P_min, P_max, T_min, T_max)

# Display the PH diagram on Streamlit
st.pyplot(ph_data.plot())
