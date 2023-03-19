import numpy as np
import matplotlib.pyplot as plt
from CoolProp.CoolProp import PropsSI

def vapor_compression_cycle_points(refrigerant, evap_temp=-5, cond_temp=45, subcooling=5, superheat=10):
    evap_pressure = PropsSI('P', 'T', evap_temp + 273.15, 'Q', 0, refrigerant) / 1e5  # bar
    cond_pressure = PropsSI('P', 'T', cond_temp + 273.15, 'Q', 0, refrigerant) / 1e5  # bar

    h1 = PropsSI('H', 'T', evap_temp + 273.15 + superheat, 'P', evap_pressure * 1e5, refrigerant) / 1e3  # kJ/kg
    h2 = PropsSI('H', 'P', cond_pressure * 1e5, 'S', PropsSI('S', 'H', h1 * 1e3, 'P', evap_pressure * 1e5, refrigerant), refrigerant) / 1e3  # kJ/kg
    h3 = PropsSI('H', 'T', cond_temp + 273.15 - subcooling, 'P', cond_pressure * 1e5, refrigerant) / 1e3  # kJ/kg
    h4 = PropsSI('H', 'P', evap_pressure * 1e5, 'S', PropsSI('S', 'H', h3 * 1e3, 'P', cond_pressure * 1e5, refrigerant), refrigerant) / 1e3  # kJ/kg

    return (h1, evap_pressure), (h2, cond_pressure), (h3, cond_pressure), (h4, evap_pressure)

def plot_ph_diagram(refrigerant):
     # Define pressure and enthalpy ranges
    T_min = PropsSI('Tmin', refrigerant) + 1
    T_max = PropsSI('Tcrit', refrigerant) - 1
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
    plt.contour(H, P, T, levels=20, cmap="coolwarm")
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

    # Return the figure instead of showing it
    return plt.gcf()
