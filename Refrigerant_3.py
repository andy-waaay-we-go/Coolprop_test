import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')  # Set the backend for matplotlib to 'agg'
import numpy as np
import CoolProp.CoolProp as CP
import CoolProp.Plots as CPP

from CoolProp.Plots import PropertyPlot
from CoolProp.Plots import SimpleCompressionCycle

pp = PropertyPlot('HEOS::R134a', 'PH', unit_system='EUR')
pp.calc_isolines(CoolProp.iQ, num=11)
cycle = SimpleCompressionCycle('HEOS::R134a', 'PH', unit_system='EUR')
T0 = 280
pp.state.update(CoolProp.QT_INPUTS,0.0,T0-15)
p0 = pp.state.keyed_output(CoolProp.iP)
T2 = 310
pp.state.update(CoolProp.QT_INPUTS,1.0,T2+10)
p2 = pp.state.keyed_output(CoolProp.iP)
cycle.simple_solve(T0, p0, T2, p2, 0.7, SI=True)
cycle.steps = 50
sc = cycle.get_state_changes()
import matplotlib.pyplot as plt
plt.close(cycle.figure)
pp.draw_process(sc)