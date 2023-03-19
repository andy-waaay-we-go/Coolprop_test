import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')  # Set the backend for matplotlib to 'agg'
import numpy as np
import CoolProp.CoolProp as CP
import CoolProp.Plots as CPP

from CoolProp.Plots import PropertyPlot

# Create a PropertyPlot instance for R134a refrigerant
plot = PropertyPlot('HEOS::R134a', 'PH', unit_system='EUR', tp_limits='ACHP')

# Calculate and add isobars and isotherms to the plot
plot.calc_isolines()

# Set the axis labels and title for the plot
plot.xlabel('Specific enthalpy (kJ/kg)')
plot.ylabel('Pressure (bar)')
plot.title('R134a Refrigerant PH Diagram')

# Display the plot on terminal
plot.show()

# Display the plot in Streamlit
st.pyplot(plot.figure)