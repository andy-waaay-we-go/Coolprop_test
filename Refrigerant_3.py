import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')  # Set the backend for matplotlib to 'agg'
import numpy as np
import CoolProp.CoolProp as CP
import CoolProp.Plots as CPP

import CoolProp
from CoolProp.Plots import PropertyPlot
from CoolProp.Plots import SimpleCompressionCycle
pp = PropertyPlot('HEOS::R134a', 'PH', unit_system='EUR')
pp.calc_isolines(CoolProp.iQ, num=11)
cycle = SimpleCompressionCycle('HEOS::R134a', 'PH', unit_system='EUR')
Te = 265
Tc = 300
cycle.simple_solve_dt(Te, Tc, 10, 15, 0.7, SI=True)
cycle.steps = 50
sc = cycle.get_state_changes()
import matplotlib.pyplot as plt
plt.close(cycle.figure)
pp.draw_process(sc)

# Display the plot in Streamlit
st.pyplot(plt.figure)