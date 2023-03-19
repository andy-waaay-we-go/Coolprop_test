import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import modelicares as mr

# Load the ModelicaRes library
mr.load_library("Modelica.Media.Water")

# Define a range of temperatures to plot
T_range = np.linspace(273.15, 373.15, 101)

# Calculate the specific enthalpy and specific entropy of water at each temperature
h = mr.ENTHALPY_WATER(T=T_range)
s = mr.ENTROPY_WATER(T=T_range)

# Create a Streamlit plot of specific enthalpy vs. specific entropy
st.pyplot(plt.plot(s, h))
