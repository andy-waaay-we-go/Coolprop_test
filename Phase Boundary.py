import numpy as np
import matplotlib.pyplot as plt
from CoolProp.CoolProp import PropsSI

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
    plt.xlabel('Enthalpy [kJ/kg]')
    plt.ylabel('Pressure [bar]')
    plt.title(f'Pressure-Enthalpy Diagram for {refrigerant}')
    plt.legend()
    plt.grid()
    plt.show()

# Plot the p-h diagram for R134a
plot_ph_diagram('R134a')
