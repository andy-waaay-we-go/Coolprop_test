import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from CoolProp.CoolProp import PropsSI

def get_results():
    # Place the entire main code here, but remove the Streamlit related code
    # Return the necessary variables as a tuple

    def display_ph_diagram(refrigerant, T_Evap, Superheat, P_Evap_barA, Pressure_drop, T_Cond, Subcool, P_Cond_barA, Compressor_disp, Volumetric_eff, Compressor_speed, D, mdot, Isentropic_eff, Compressor_Temperature_out_est, Q_Cond, Q_Evap, Mechanical_eff, W_Comp, COP_heating):
    # Move the plot_ph_diagram function here, but remove the Streamlit related code
    # Return the ph_fig

        def get_results_dataframe(refrigerant, T_Evap, Superheat, P_Evap_barA, Pressure_drop, T_Cond, Subcool, P_Cond_barA, Compressor_disp, Volumetric_eff, Compressor_speed, D, mdot, Isentropic_eff, Compressor_Temperature_out_est, Q_Cond, Q_Evap, Mechanical_eff, W_Comp, COP_heating):
   
    # Update default settings to show 2 decimal places
            pd.options.display.float_format = '{:.2f}'.format

    # Create dataframe
    df = pd.DataFrame({'Result Output': ['Refrigerant Choice', 'Evaporator Temperture', 'Superheat', 'Evaporator Pressure', 'Suction Line Pressure Drop', 
                    'Condenser Temperature', 'Subcool','Condenser Pressure','Compressor Displacement','Volumetric Efficiency','Compressor Speed',
                    'Suction Line Refrigerant Density','Refrigerant Massflow Rate','Isentropic Efficiency','Estimate of Compressor Temperature Out',                    
                    'Condenser Power','Evaporator Power','Mechanical Efficiency','Compressor Work','COP Heating'],
                'Value': [refrigerant, T_Evap, Superheat, float("{:.2f}".format(P_Evap_barA)), Pressure_drop, T_Cond, Subcool,
                    float("{:.2f}".format(P_Cond_barA)),Compressor_disp,Volumetric_eff,Compressor_speed,float("{:.2f}".format(D)),float("{:.4f}".format(mdot)),Isentropic_eff,float("{:.2f}".format(Compressor_Temperature_out_est-273.15)),
                    float("{:.2f}".format(Q_Cond/1000)),float("{:.2f}".

.format(Q_Evap/1000)),Mechanical_eff,float("{:.2f}".format(W_Comp/1000)),float("{:.2f}".format(COP_heating))],
                'Units': ['-', '°C', 'K', 'BarA', 'kPa', '°C', 'K','BarA','cc','%',
                'RPM','kg/m³','kg/s','%','°C','kW','kW','%','kW','']})

    Results = df.astype(str)
    return Results

