import inspect
import textwrap

import streamlit as st

from CoolProp.CoolProp import PropsSI

Refrigerant_Selection = st.selectbox(
     'Select Refrigerant',
    ('Nitrogen', 'Propane', 'R134a', 'R404a', 'R410a'))
st.write('You selected:', Refrigerant_Selection)

Temperature_Selection = st.slider(
'Select Temperature in degC',
     -20, 100, 0)
Temperature_K = Temperature_Selection + 273.15
st.write('Temperture in degC:', Temperature_Selection)

Pressure_Selection = st.slider(
'Select Pressure in BarA',
     0, 100, 5)
Pressure_Pa = Pressure_Selection * 100000
st.write('Pressure in BarA:', Pressure_Selection)

H = PropsSI('H','T',Temperature_K,'P',Pressure_Pa, Refrigerant_Selection)/1000
st.write('Enthalpy in kJ/kg', H)
print(H)

