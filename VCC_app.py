import streamlit as st
from plot_ph_diagram import plot_ph_diagram  # Assuming the plot_ph_diagram function is in a file called plot_ph_diagram.py

st.set_page_config(page_title="p-h Diagram", layout="wide")

st.title("Pressure-Enthalpy Diagram")

refrigerant = st.selectbox("Select refrigerant:", ["R134a", "R410A", "R22"])

# Call the plot_ph_diagram function and display the plot
ph_fig = plot_ph_diagram(refrigerant)
st.pyplot(ph_fig)