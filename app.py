"""
Shiny Histogram App

This app allows users to interactively generate a histogram based on random data. 
Users can select the number of bins via a slider, choose the bar color from a dropdown menu, 
and toggle gridlines on or off. The histogram dynamically updates based on user input, 
providing a visual representation of the data distribution.

Features:
- Input slider to select the number of bins (0-100).
- Dropdown menu for selecting bar color.
- Checkbox to show/hide gridlines.
- Histogram displayed using Matplotlib with density normalization.

Author: Nick Elias
Date: 10/25/2024
"""


import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Setting page options, adding a title
ui.page_opts(title="Nick's Interactive Histogram")

# Customizing sidebar options
with ui.sidebar():

    # Add an input slider to choose number of bins
    ui.input_slider(
        "selected_number_of_bins",  # Unique string ID for bins
        "Number of Bins",  # Label for the slider
        0,  # Minimum number of bins
        100,  # Maximum number of bins
        20,  # Default number of bins
    )

    # Add options to change histogram color
    ui.input_select(
        "bar_color",  # Unique string ID for bar color option
        "Choose Bar Color",  # Label for bar color selection dropdown
        choices=[
            "black",
            "blue",
            "red",
            "green",
            "orange",
            "purple",
            "cyan",
            "yellow",
        ],  # Correct parameter
        selected="blue",  # Default selection
    )

    # Add checkbox to show gridlines
    ui.input_checkbox("show_grid", "Show Grid", True)


# Render the histogram plot onto the page
@render.plot(alt="A histogram")  # Add alternative text for accessibility
def histogram():
    # Random number generator for sample set
    np.random.seed(19680801)
    random_data = 100 + 15 * np.random.randn(437)

    # Plot the histogram with user-selected parameters
    plt.hist(
        random_data,
        input.selected_number_of_bins(),
        color=input.bar_color(),
        density=True,
    )

    # Add a title to the histogram
    plt.title("Data Distribution with Selected Number of Bins")

    # Add x and y labels
    plt.xlabel("Value")
    plt.ylabel("Density")

    # Show gridlines when checkbox selected
    plt.grid(input.show_grid())
