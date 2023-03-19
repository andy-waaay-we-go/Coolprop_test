import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from CoolProp.CoolProp import PropsSI

from CoolProp.Plots import PropsPlot

ph_plot = PropsPlot('R410A', 'Ph')
ph_plot.show()
