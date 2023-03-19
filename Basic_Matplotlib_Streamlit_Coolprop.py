import streamlit as st
import matplotlib.pyplot as plt
from CoolProp.CoolProp import PropsSI

# Define the temperature and pressure ranges
T_min = -50
T_max = 200
P_min = 0.1
P_max = 10

# Define the refrigerant name
fluid = 'R134a'

# Define the data to plot
Ts_data = []
Ps_data = []
for T in range(T_min, T_max + 1, 5):
    for P in range(int(P_min * 1000), int(P_max * 1000) + 1, 10):
        T_actual = T + 273.15
        P_actual = P / 1000.0
        try:
            h = cp.PropsSI('H', 'T', T_actual, 'P', P_actual, fluid)
            s = cp.PropsSI('S', 'T', T_actual, 'P', P_actual, fluid)
            Ts_data.append((T_actual, s))
            Ps_data.append((P_actual, h / 1000.0))
        except:
            pass

# Create the plot
fig, ax = plt.subplots()
ax.plot([x[0] for x in Ts_data], [x[1] for x in Ts_data], label='Saturated Vapor Line')
ax.plot([x[0] for x in Ps_data], [x[1] for x in Ps_data], label='Saturated Liquid Line')
ax.set_xlabel('Temperature (K)')
ax.set_ylabel('Specific Entropy (kJ/(kg*K))')
ax.set_ylim(min([x[1] for x in Ts_data]), max([x[1] for x in Ts_data]))
ax.legend()

# Define the Streamlit app
st.set_page_config(page_title='PH Diagram for R134a', page_icon=':snowflake:')
st.title('PH Diagram for R134a')
st.pyplot(fig)
