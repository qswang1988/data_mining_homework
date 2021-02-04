#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : luis-eduardo@dsv.su.se
# Created Date: 2020/06/30
# =============================================================================
"""
Course: Data Mining for Computer and Systems Sciences
Lab 5: Model Deployment
Creates a web platform to interact with the webserver
"""
# =============================================================================
# Imports
# =============================================================================
import helper_dash_example

import dash
from dash.dependencies import Input, Output, State

from pathlib import Path
import numpy as np
import pandas as pd
import pickle

# =============================================================================
# Main
# =============================================================================

# Relative paths respect to current file
THIS_FILE_PATH = str(Path(__file__).parent.absolute())+"/"
filename_to_load = THIS_FILE_PATH + "trained_model_diabetes.pickle"

# Variables to create the data structure from the web interface
#['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age']
#dataset_colnames = ['P', 'G', 'BP', 'S', 'I', 'BMI','D','A']
dataset_colnames = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI', 'DiabetesPedigreeFunction', 'Age']
sample = None   # DataFrame with the data that the user has input in the webpage

# Load trained model
loaded_model = None
with open(filename_to_load, "rb") as readFile:
    loaded_model = pickle.load(readFile)

# Styling for HTML website
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Create web server
app = dash.Dash("dami_analytics_lab", external_stylesheets=external_stylesheets)

# In the additional file `helper_dash_example` is hidden all webpage' structure
app.layout = helper_dash_example.app_html_layout

# =============================================================================
# Callbacks to setup the interaction between webpage and controls
# The next syntax is specific from the dash library, documentation can be found
# on https://dash.plotly.com/
# =============================================================================

# Sliders
# Generic function to return the string from a change in the web app
def update_value(value):
    return str(value)


'''
#['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness','Insulin','BMI', 'DiabetesPedigreeFunction', 'Age']
# [P,G,BP,S,I,BMI,D,A]
[State('slider-P', 'value'),
    State('slider-G', 'value'),
    State('slider-BP', 'value'),
    State('slider-S', 'value'),
    State('slider-I', 'value'),
    State('slider-BMI', 'value'),
    State('slider-D', 'value'),
    State('slider-A', 'value'),
    ]
'''


@app.callback(
    Output(component_id='value-slider-P', component_property='children'),
    [Input(component_id='slider-P', component_property='value')]
)
def update_area(value):
    return update_value(value)

@app.callback(
    Output(component_id='value-slider-G', component_property='children'),
    [Input(component_id='slider-G', component_property='value')]
)
def update_perimeter(value):
    return update_value(value)

@app.callback(
    Output(component_id='value-slider-BP', component_property='children'),
    [Input(component_id='slider-BP', component_property='value')]
)
def update_compactness(value):
    return update_value(value)

@app.callback(
    Output(component_id='value-slider-S', component_property='children'),
    [Input(component_id='slider-S', component_property='value')]
)
def update_length_kernel(value):
    return update_value(value)

@app.callback(
    Output(component_id='value-slider-I', component_property='children'),
    [Input(component_id='slider-I', component_property='value')]
)
def update_width_kernel(value):
    return update_value(value)

@app.callback(
    Output(component_id='value-slider-BMI', component_property='children'),
    [Input(component_id='slider-BMI', component_property='value')]
)
def update_asymm_coeff(value):
    return update_value(value)

@app.callback(
    Output(component_id='value-slider-D', component_property='children'),
    [Input(component_id='slider-D', component_property='value')]
)
def update_length_kernel_groove(value):
    return update_value(value)


@app.callback(
    Output(component_id='value-slider-A', component_property='children'),
    [Input(component_id='slider-A', component_property='value')]
)
def update_length_kernel_groove(value):
    return update_value(value)


# Visualization
@app.callback(
    Output(component_id='graph-histogram', component_property='figure'),
    [Input(component_id='dropdown-histogram', component_property='value'),
    Input(component_id='submit', component_property='n_clicks')]
)
def update_histogram(colname, n_clicks):
    return helper_dash_example.update_histogram(colname, sample)

@app.callback(
    Output(component_id='graph-scatter', component_property='figure'),
    [Input(component_id='dropdown-scatter-1', component_property='value'),
    Input(component_id='dropdown-scatter-2', component_property='value'),
    Input(component_id='submit', component_property='n_clicks')]
)
def update_scatter(col1, col2, n_clicks):
    return helper_dash_example.update_scatter(col1, col2, sample)


# Classification Button
#['P', 'G', 'BP', 'S', 'I', 'BMI','D','A']
@app.callback(    
    Output(component_id='classification-result', component_property='children'),
    [Input(component_id='submit', component_property='n_clicks')],
    [State('slider-P', 'value'),
    State('slider-G', 'value'),
    State('slider-BP', 'value'),
    State('slider-S', 'value'),
    State('slider-I', 'value'),
    State('slider-BMI', 'value'),
    State('slider-D', 'value'),
    State('slider-A', 'value'),
    ]
)
def execute_classification(n_clicks,Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
    """
    Main method. Loads the trained model, applies the input data and returns a class
    """
    if(n_clicks == None): # When the application open
        return "Press below to execute the classification"
    else:
        # The sliders' values are already parsed to numeric values
        # Here we create a DataFrame with the input data
        data_from_user = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        global sample
        sample = pd.DataFrame(data=[data_from_user], columns=dataset_colnames)

        # Execute the prediction using the loaded trained model.
        prediction = loaded_model.predict(sample)

        # Return final message
        prediction_labels = ["Negative", "Positive"]
        return "The predicted class of the input data is: ["+ str(prediction[0]) +":" + prediction_labels[prediction[0]] + "]"


# Run the web server when this script is executed in Python
if __name__ == "__main__":
    app.run_server(debug=True)