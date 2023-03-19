import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')  # Set the backend for matplotlib to 'agg'
import numpy as np
import CoolProp.CoolProp as CP
import CoolProp.Plots as CPP

from CoolProp.Plots import PropertyPlot

# Create a PropertyPlot instance for R290 refrigerant
plot = PropertyPlot('R290', 'ph')

# Calculate and add isobars and isotherms to the plot
plot.calc_isolines()

# Set the axis labels and title for the plot
plot.xlabel('Specific enthalpy (kJ/kg)')
plot.ylabel('Pressure (bar)')
plot.title('R290 Refrigerant PH Diagram')

# Display the plot on terminal GUI
# plot.show()

# Display the plot in Streamlit
st.pyplot(plot.figure)