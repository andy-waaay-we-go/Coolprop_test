import streamlit as st
from ph_diagram import display_ph_diagram, get_results

st.set_page_config(page_title="p-h Diagram", layout="wide")

st.title("Pressure-Enthalpy Diagram")

refrigerant, T_Evap, Superheat, P_Evap_barA, Pressure_drop, T_Cond, Subcool, P_Cond_barA, Compressor_disp, Volumetric_eff, Compressor_speed, D, mdot, Isentropic_eff, Compressor_Temperature_out_est, Q_Cond, Q_Evap, Mechanical_eff, W_Comp, COP_heating = get_results()

ph_fig = display_ph_diagram(refrigerant, T_Evap, Superheat, P_Evap_barA, Pressure_drop, T_Cond, Subcool, P_Cond_barA, Compressor_disp, Volumetric_eff, Compressor_speed, D, mdot, Isentropic_eff, Compressor_Temperature_out_est, Q_Cond, Q_Evap, Mechanical_eff, W_Comp, COP_heating)
st.pyplot(ph_fig)

Results = get_results(refrigerant, T_Evap, Superheat, P_Evap_barA, Pressure_drop, T_Cond, Subcool,P_Cond_barA, Compressor_disp, Volumetric_eff, Compressor_speed, D, mdot, Isentropic_eff, Compressor_Temperature_out_est, Q_Cond, Q_Evap, Mechanical_eff, W_Comp, COP_heating)
st.table(Results)
