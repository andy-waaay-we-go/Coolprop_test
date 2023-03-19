import streamlit as st
import matplotlib.pyplot as plt

def create_plot():
    # Create some data
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the data on the axis
    ax.plot(x, y)

    # Set the title and axis labels
    ax.set_title('My First Matplotlib Plot')
    ax.set_xlabel('X-axis Label')
    ax.set_ylabel('Y-axis Label')

    return fig

# Create a Streamlit app
st.title('My Streamlit App')
st.write('Here is a Matplotlib plot:')

# Call the create_plot function and pass the returned figure to st.pyplot
fig = create_plot()
st.pyplot(fig)
