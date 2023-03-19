import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from CoolProp.CoolProp import PropsSI
from CoolProp.CoolProp import PhaseSI
from CoolProp.CoolProp import saturation_ancillary

# Specify the range of pressures and temperatures to use
T_values = np.linspace(-100, 300, 100)
P_values = np.linspace(0.1, 7, 100) * 1e6

# Generate the data for the phase boundary
data = []
for P in P_values:
    Tsat = PropsSI('T', 'P', P, 'Q', 0, 'R134a')
    hsatL = saturation_ancillary('H', ('P', P), ('Q', 0))
    ssatL = saturation_ancillary('S', ('P', P), ('Q', 0))
    hsatV = saturation_ancillary('H', ('P', P), ('Q', 1))
    ssatV = saturation_ancillary('S', ('P', P), ('Q', 1))
    data.append((Tsat, hsatL, ssatL, hsatV, ssatV))

# Plot the phase boundary
fig, ax = plt.subplots()
ax.plot([d[1] for d in data], [d[0] for d in data], 'b-', label='Liquid')
ax.plot([d[3] for d in data], [d[0] for d in data], 'r-', label='Vapor')
ax.set_xlabel('Specific enthalpy (J/kg)')
ax.set_ylabel('Pressure (Pa)')
ax.legend()

# Define the Streamlit app
st.set_page_config(page_title='PH Diagram for R134a', page_icon=':snowflake:')
st.title('PH Diagram for R134a')
st.pyplot(fig)
