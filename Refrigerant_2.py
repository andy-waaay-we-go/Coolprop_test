import inspect
import textwrap
import pandas as pd

import streamlit as st

from CoolProp.CoolProp import PropsSI

Refrigerant_Selection = st.selectbox(
     'Select Refrigerant',
    ('Propane', 'R134a','R1234yf','R32', 'R404a', 'R410a'))

T_Evap = st.slider(
'Select Evaporator Temperature in °C',
     -20, 40, 0)
T_Evap_K = T_Evap + 273.15

Superheat = st.slider(
'Select Evaporator Superheat Value in K',
     0, 15, 5)

P_Evap = PropsSI('P','T',T_Evap_K,'Q',1,Refrigerant_Selection)
P_Evap_barA = P_Evap/100000

Pressure_drop = st.slider(
'Estimate Suction Line Pressure Drop in kPa',
     250, 1000, 500)
Pdrop_kPa = Pressure_drop*100

T_Cond = st.slider(
'Select Condenser Temperature in °C',
     10, 70, 35)
T_Cond_K = T_Cond + 273.15

Subcool = st.slider(
'Select Condenser Subcool Value in K',
     0, 15, 5)

P_Cond = PropsSI('P','T',T_Cond_K,'Q',0,Refrigerant_Selection)
P_Cond_barA = P_Cond/100000

Compressor_disp = st.number_input('Enter Compressor Size in CC',value=10.2)

Volumetric_eff = st.slider(
'Estimate Compressor Volumetric Efficiency',
     0, 100, 80)

Compressor_speed = st.slider(
'Enter Compressor Speed in RPM',
     1000, 7000, 2500)

D = PropsSI('D','T',T_Evap_K + Superheat,'P',P_Evap-Pdrop_kPa,Refrigerant_Selection)

mdot = (Compressor_speed*D*Volumetric_eff/100*(Compressor_disp/1000000))/60

Isentropic_eff = st.slider(
'Estimate Compressor Isentropic Efficiency',
     0, 100, 95)

Compressor_Entropy_in = PropsSI('S','T',T_Evap_K + Superheat,'P',P_Evap-Pdrop_kPa,Refrigerant_Selection)/1000

Compressor_Entropy_out = Compressor_Entropy_in/(Isentropic_eff/100)

Compressor_Temperature_out_est = PropsSI('T','P',P_Cond,'S',Compressor_Entropy_out*1000,Refrigerant_Selection)

H_Comp_out = PropsSI('H','T',Compressor_Temperature_out_est,'P',P_Cond,Refrigerant_Selection)

H_Cond_out = PropsSI('H','T',T_Cond_K - Subcool,'P',P_Cond,Refrigerant_Selection)

H_Evap_out = PropsSI('H','T',T_Evap_K + Superheat,'P',P_Evap,Refrigerant_Selection)

Q_Cond  =  mdot*(H_Comp_out-H_Cond_out)

Q_Evap  =  mdot*(H_Evap_out-H_Cond_out)

Mechanical_eff = st.slider(
'Estimate Compressor Mechanical Efficiency',
     0, 100, 90)

W_Comp  =  mdot*(H_Comp_out-H_Evap_out)*(Mechanical_eff/100)

COP_heating = Q_Cond/W_Comp

#st.write('Refrigerant Choice:', Refrigerant_Selection)
#st.write('Evaporator Temperture in °C:', T_Evap)
#st.write('Superheat in K:', Superheat)
#st.write('Evaporator Pressure in BarA:', P_Evap_barA)
#st.write('Suction Line Pressure Drop in kPa:', Pressure_drop)
#st.write('Condenser Temperature in °C:', T_Cond)
#st.write('Subcool in K:', Subcool)
#st.write('Condenser Pressure in BarA:', P_Cond_barA)
#st.write('Compressor Displacement in cc', Compressor_disp)
#st.write('Volumetric Efficiency%:', Volumetric_eff)
#st.write('Compressor Speed:', Compressor_speed)
#st.write('Suction Line Refrigerant Density in kg/m3:', D)
#st.write('Refrigerant Massflow Rate:', mdot)
#st.write('Isentropic Efficiency%:', Isentropic_eff)
#st.write('Compressor_Entropy_in J K−1', Compressor_Entropy_in)
#st.write('Compressor_Entropy_out J K−1', Compressor_Entropy_out)
#st.write('Estimate of Compressor Temperature Out', Compressor_Temperature_out_est-273.15)
#st.write('Enthalpy Refrigerant Compressor Discharge kJ/kg:', H_Comp_out/1000)
#st.write('Enthalpy Refrigerant Condenser outlet kJ/kg:', H_Cond_out/1000)
#st.write('Enthalpy Refrigerant Evaporator outlet in kJ/kg:', H_Evap_out/1000)
#st.write('Condenser Power in kW:', Q_Cond/1000)
#st.write('Evaporator Power in kW:', Q_Evap/1000)
#st.write('Mechanical Efficiency%:', Mechanical_eff)
#st.write('Compressor Work in kW:', W_Comp/1000)

# Update default settings to show 2 decimal place
pd.options.display.float_format = '{:.2f}'.format

# Create dataframe
df = pd.DataFrame({'Result Output': ['Refrigerant Choice', 'Evaporator Temperture', 'Superheat', 'Evaporator Pressure', 'Suction Line Pressure Drop', 
                    'Condenser Temperature', 'Subcool','Condenser Pressure','Compressor Displacement','Volumetric Efficiency','Compressor Speed',
                    'Suction Line Refrigerant Density','Refrigerant Massflow Rate','Isentropic Efficiency','Estimate of Compressor Temperature Out',                    
                    'Condenser Power','Evaporator Power','Mechanical Efficiency','Compressor Work','COP Heating'],
                   'Value': [Refrigerant_Selection, T_Evap, Superheat, float("{:.2f}".format(P_Evap_barA)), Pressure_drop, T_Cond, Subcool,
                    float("{:.2f}".format(P_Cond_barA)),Compressor_disp,Volumetric_eff,Compressor_speed,float("{:.2f}".format(D)),float("{:.4f}".format(mdot)),Isentropic_eff,float("{:.2f}".format(Compressor_Temperature_out_est-273.15)),
                    float("{:.2f}".format(Q_Cond/1000)),float("{:.2f}".format(Q_Evap/1000)),Mechanical_eff,float("{:.2f}".format(W_Comp/1000))float("{:.2f}".format(COP_heating/1000))],
                   'Units': ['-', '°C', 'K', 'BarA', 'kPa', '°C', 'K','BarA','cc','%',
                   'RPM','kg/m\u00b3','kg/s','%','°C','kW','kW','%','kW','']})


Results = df.astype(str)
st.table(Results)  

