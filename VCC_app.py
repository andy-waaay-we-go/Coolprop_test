import inspect
import textwrap
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from CoolProp.CoolProp import PropsSI

import streamlit as st

st.set_page_config(page_title="p-h Diagram", layout="wide")

st.title("Pressure-Enthalpy Diagram")

refrigerant = st.selectbox("Select refrigerant:", ["R134a","R1234yf", "R290", "R600a", "R410A", "R32", "R404a"])

T_Evap = st.slider(
'Select Evaporator Temperature in °C',
    -20, 40, 0)
T_Evap_K = T_Evap + 273.15

Superheat = st.slider(
'Select Evaporator Superheat Value in K',
    0, 15, 5)

P_Evap = PropsSI('P','T',T_Evap_K,'Q',1, refrigerant)
P_Evap_barA = P_Evap/100000

Pressure_drop = st.slider(
'Estimate Suction Line Pressure Drop in Bar',
    0.0, 0.25, 0.0)
Pdrop_kPa = Pressure_drop*100

T_Cond = st.slider(
'Select Condenser Temperature in °C',
    10, 70, 50)
T_Cond_K = T_Cond + 273.15

Subcool = st.slider(
'Select Condenser Subcool Value in K',
    0, 15, 5)

Compressor_disp = st.number_input('Enter Compressor Size in CC',value=10.2)

Volumetric_eff = st.slider(
'Estimate Compressor Volumetric Efficiency',
    0, 100, 80)

Compressor_speed = st.number_input('Enter Compressor Speed in RPM',value=3000)

Isentropic_eff = st.slider(
'Estimate Compressor Isentropic Efficiency',
    0, 100, 95)

Mechanical_eff = st.slider(
'Estimate Compressor Mechanical Efficiency',
    0, 100, 90)

def vapor_compression_cycle_points(refrigerant, evap_temp=T_Evap, cond_temp=T_Cond, subcooling=Subcool, superheat=Superheat):
    evap_pressure = PropsSI('P', 'T', evap_temp + 273.15, 'Q', 0, refrigerant) / 1e5  # bar
    cond_pressure = PropsSI('P', 'T', cond_temp + 273.15, 'Q', 0, refrigerant) / 1e5  # bar

    h1 = PropsSI('H', 'T', evap_temp + 273.15 + superheat, 'P', evap_pressure * 1e5, refrigerant) / 1e3  # kJ/kg
    h2 = PropsSI('H', 'P', cond_pressure * 1e5, 'S', PropsSI('S', 'H', h1 * 1e3, 'P', evap_pressure * 1e5, refrigerant), refrigerant) / 1e3  # kJ/kg
    h3 = PropsSI('H', 'T', cond_temp + 273.15 - subcooling, 'P', cond_pressure * 1e5, refrigerant) / 1e3  # kJ/kg
    h4 = h3 # kJ/kg

    return (h1, evap_pressure), (h2, cond_pressure), (h3, cond_pressure), (h4, evap_pressure)

def plot_ph_diagram(refrigerant):
    # Define pressure and enthalpy ranges
    T_min = T_Evap_K - 10
    T_max = T_Cond_K + 5
    p_min = PropsSI('P', 'T', T_min, 'Q', 0, refrigerant) / 1e5  # bar
    p_max = PropsSI('P', 'T', T_max, 'Q', 0, refrigerant) / 1e5  # bar
    h_min = PropsSI('H', 'T', T_min, 'Q', 0, refrigerant) / 1e3  # kJ/kg
    h_max = PropsSI('H', 'T', T_max, 'Q', 1, refrigerant) / 1e3  # kJ/kg

    pressures = np.linspace(p_min, p_max, 200)
    enthalpies = np.linspace(h_min, h_max, 200)

    H, P = np.meshgrid(enthalpies, pressures)

    # Calculate saturation lines
    T_sat = np.linspace(T_min, T_max, 100)
    h_sat_liq = [PropsSI('H', 'T', T, 'Q', 0, refrigerant) / 1e3 for T in T_sat]
    h_sat_vap = [PropsSI('H', 'T', T, 'Q', 1, refrigerant) / 1e3 for T in T_sat]

    # Calculate temperature grid
    T = np.zeros_like(H)
    for i, p in enumerate(pressures):
        for j, h in enumerate(enthalpies):
            try:
                T[i, j] = PropsSI('T', 'P', p * 1e5, 'H', h * 1e3, refrigerant) - 273.15  # °C
            except ValueError:
                T[i, j] = np.nan

    # Create the p-h diagram
    plt.figure(figsize=(10, 6))
    contour_plot = plt.contour(H, P, T, levels=20, cmap="coolwarm")
    plt.clabel(contour_plot, inline=1, fontsize=8, fmt='%1.0f')  # Add labels to the contour lines
    plt.plot(h_sat_liq, [PropsSI('P', 'T', T, 'Q', 0, refrigerant) / 1e5 for T in T_sat], 'k--', label="Saturation Liquid")
    plt.plot(h_sat_vap, [PropsSI('P', 'T', T, 'Q', 1, refrigerant) / 1e5 for T in T_sat], 'k-.', label="Saturation Vapor")

    # Get the vapor compression cycle points
    points = vapor_compression_cycle_points(refrigerant)

    # Add the vapor compression cycle points to the plot
    plt.plot([points[0][0], points[1][0]], [points[0][1], points[1][1]], 'go-') #label="Compression"
    plt.plot([points[1][0], points[2][0]], [points[1][1], points[2][1]], 'go-')
    plt.plot([points[2][0], points[3][0]], [points[2][1], points[3][1]], 'go-')
    plt.plot([points[3][0], points[0][0]], [points[3][1], points[0][1]], 'go-')

    plt.xlabel('Enthalpy [kJ/kg]')
    plt.ylabel('Pressure [bar]')
    plt.title(f'Pressure-Enthalpy Diagram for {refrigerant}')
    plt.legend()
    plt.grid()
    return plt.gcf()

ph_fig = plot_ph_diagram(refrigerant)
st.pyplot(ph_fig)

P_Cond = PropsSI('P','T',T_Cond_K,'Q',0,refrigerant)
P_Cond_barA = P_Cond/100000

D = PropsSI('D','T',T_Evap_K + Superheat,'P',P_Evap-Pdrop_kPa,refrigerant)

mdot = (Compressor_speed*D*Volumetric_eff/100*(Compressor_disp/1000000))/60

Compressor_Entropy_in = PropsSI('S','T',T_Evap_K + Superheat,'P',P_Evap-Pdrop_kPa,refrigerant)/1000

Compressor_Entropy_out = Compressor_Entropy_in/(Isentropic_eff/100)

Compressor_Temperature_out_est = PropsSI('T','P',P_Cond,'S',Compressor_Entropy_out*1000,refrigerant)

H_Comp_out = PropsSI('H','T',Compressor_Temperature_out_est,'P',P_Cond,refrigerant)

H_Cond_out = PropsSI('H','T',T_Cond_K - Subcool,'P',P_Cond,refrigerant)

H_Evap_out = PropsSI('H','T',T_Evap_K + Superheat,'P',P_Evap,refrigerant)

Q_Cond  =  mdot*(H_Comp_out-H_Cond_out)

Q_Evap  =  mdot*(H_Evap_out-H_Cond_out)

W_Comp  =  mdot*(H_Comp_out-H_Evap_out)/(Mechanical_eff/100)

COP_heating = Q_Cond/W_Comp

# Update default settings to show 2 decimal place
pd.options.display.float_format = '{:.2f}'.format

# Create dataframe
df = pd.DataFrame({'Result Output': ['Refrigerant Choice', 'Evaporator Temperture', 'Superheat', 'Evaporator Pressure', 'Suction Line Pressure Drop', 
                    'Condenser Temperature', 'Subcool','Condenser Pressure','Compressor Displacement','Volumetric Efficiency','Compressor Speed',
                    'Suction Line Refrigerant Density','Refrigerant Massflow Rate','Isentropic Efficiency','Estimate of Compressor Temperature Out',                    
                    'Condenser Power','Evaporator Power','Mechanical Efficiency','Compressor Work','COP Heating'],
                'Value': [refrigerant, T_Evap, Superheat, float("{:.2f}".format(P_Evap_barA)), Pressure_drop, T_Cond, Subcool,
                    float("{:.2f}".format(P_Cond_barA)),Compressor_disp,Volumetric_eff,Compressor_speed,float("{:.2f}".format(D)),float("{:.4f}".format(mdot)),Isentropic_eff,float("{:.2f}".format(Compressor_Temperature_out_est-273.15)),
                    float("{:.2f}".format(Q_Cond/1000)),float("{:.2f}".format(Q_Evap/1000)),Mechanical_eff,float("{:.2f}".format(W_Comp/1000)),float("{:.2f}".format(COP_heating))],
                'Units': ['-', '°C', 'K', 'BarA', 'kPa', '°C', 'K','BarA','cc','%',
                'RPM','kg/m\u00b3','kg/s','%','°C','kW','kW','%','kW','']}) 

Results = df.astype(str)
st.table(Results) 

