#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : luis-eduardo@dsv.su.se
# Created Date: 2020/06/30
# =============================================================================
"""
Creation of HTML webpage with Dash and visualization with Plotly.
This file is called from the `dash_example_web.py`, and its main goal
is to make the main code more readable.
"""
# =============================================================================
# Imports
# =============================================================================

import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.express as px

from pathlib import Path
import pandas as pd


# =============================================================================
# Functions
# =============================================================================

def update_histogram(colname = None, sample=None):
#def update_histogram(colname, sample=None):
    """
    Draws a histogram plot from the original dataset and puts the value
    from the `sample` that the user has input in the website.
    """
    fig = px.histogram(data,
                    x=colname,
                    color="Outcome",
                    labels={k:v for k,v in zip(colnames,column_labels)},
                    template="ggplot2")
    fig.update_layout(
        legend = dict(title="Class",
                orientation="h",
                y=1, yanchor="bottom",
                x=0.5, xanchor="center"
                )
    )
    # Show a black line with the current value of the sample
    if (sample is not None):
        fig.add_shape(type="line", line_color="black",
                    line_width = 3, 
                    xref='x', yref='paper',
                    x0 = float(sample[colname]), x1 = float(sample[colname]),
                    y0 = 0, y1 = 1)
    return fig

def update_scatter(col1=None, col2=None, sample=None):
#def update_scatter(col1, col2, sample=None):
    """
    Draws a scatter plot from the original dataset and puts the value
    from the `sample` that the user has input in the website.
    """
    fig = px.scatter(data,
                    x=col1, 
                    y=col2, 
                    color="Outcome",
                    labels={k:v for k,v in zip(colnames,column_labels)},
                    template="simple_white")

    fig.update_layout(
        legend = dict(
                    title="Class",
                )
    )
     
    if (sample is not None):
        fig.add_annotation( # add a text callout with arrow
            text="SAMPLE!", x=float(sample[col1]), y=float(sample[col2]),
            arrowhead=3, showarrow=True, startarrowsize=3
        )
    return fig

# =============================================================================
# Main
# =============================================================================


#############
"""
Load and simple processing of the original dataset for visualization
purposes in the web application.
"""

# Relative paths respect to current file
# DO NOT MODIFY: Relative path prefix to be able to find the dataset
THIS_FILE_PATH = str(Path(__file__).parent.absolute())+"/"
FOLDER_PATH = THIS_FILE_PATH + "../datasets/"

# Load original dataset file
dataset_filename = FOLDER_PATH + "diabetes.csv"
data = pd.read_csv(dataset_filename)

# Structure to map df column names to meaningful labels
colnames = data.columns
colnames = colnames.drop('Outcome').values
column_labels = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness','Insulin','BMI', 'DiabetesPedigreeFunction', 'Age']

# Initialization of plots when the website is loaded the first time
#  [P,G,BP,S,I,BMI,D,A]
fig_histogram = update_histogram("Pregnancies")
fig_scatter = update_scatter("Pregnancies","BloodPressure")

#############
"""
Structure of the HTML webpage using Dash library
"""
app_html_layout = html.Div([

    html.Center(html.H1("DAMI HW3 - DIABETES")),

    html.Div("This app classifies two variaties of diabetes from eight real-value attributes"),

    #html.Div(['More information about dataset:', 
        #html.A('https://archive.ics.uci.edu/ml/datasets/seeds')
    #]),

    html.H3('Classification with Trained Model'),


    #['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness','Insulin','BMI', 'DiabetesPedigreeFunction', 'Age']
    # [P,G,BP,S,I,BMI,D,A]

    # Create the table to put input values
    html.Table([ html.Tbody([
        # Pregnancies
        html.Tr([
            html.Td( html.B('Pregnancies (P):', style={'font-size':'9pt'}), style={'width':'25%'} ),
            html.Td( dcc.Slider(id='slider-P',
                    min=0,
                    max=17,
                    step=1,
                    value=6,
                ), style={'width':'55%'} ),
            html.Td( html.P(id='value-slider-P',children=''), style={'width':'10%'} ),
            ]),
        # Glucose
        html.Tr([
            html.Td( html.B('Glucose (G):', style={'font-size':'9pt'}), style={'width':'25%'} ),
            html.Td( dcc.Slider(id='slider-G',
                    min=44,
                    max=199,
                    step=1,
                    value=88,
                ), style={'width':'55%'} ),
            html.Td( html.P(id='value-slider-G',children=''), style={'width':'20%'} ),
            ]),
        # BloodPressure
        html.Tr([
            html.Td( html.B('BloodPressure (BP):', style={'font-size':'9pt'}), style={'width':'25%'} ),
            html.Td( dcc.Slider(id='slider-BP',
                    min=24,
                    max=122,
                    step=1,
                    value=67,
                ), style={'width':'55%'} ),
            html.Td( html.P(id='value-slider-BP',children=''), style={'width':'20%'} ),
            ]),
        # SkinThickness
        html.Tr([
            html.Td( html.B('SkinThickness (S):', style={'font-size':'9pt'}), style={'width':'25%'} ),
            html.Td( dcc.Slider(id='slider-S',
                    min=7,
                    max=99,
                    step=1,
                    value=55,
                ), style={'width':'55%'} ),
            html.Td( html.P(id='value-slider-S',children=''), style={'width':'20%'} ),
            ]),
        # Insulin
        html.Tr([
            html.Td( html.B('Insulin (I):', style={'font-size':'9pt'}), style={'width':'25%'} ),
            html.Td( dcc.Slider(id='slider-I',
                    min=10,
                    max=846,
                    step=1,
                    value=130,
                ), style={'width':'55%'} ),
            html.Td( html.P(id='value-slider-I',children=''), style={'width':'20%'} ),
            ]),
        # BMI
        html.Tr([
            html.Td( html.B('BMI (BMI):', style={'font-size':'9pt'}), style={'width':'25%'} ),
            html.Td( dcc.Slider(id='slider-BMI',
                    min=18,
                    max=67,
                    step=1,
                    value=35,
                ), style={'width':'55%'} ),
            html.Td( html.P(id='value-slider-BMI',children=''), style={'width':'20%'} ),
            ]),
        # 'DiabetesPedigreeFunction'
        html.Tr([
            html.Td( html.B('DiabetesPedigreeFunction (D):', style={'font-size':'9pt'}), style={'width':'25%'} ),
            html.Td( dcc.Slider(id='slider-D',
                    min=0.05,
                    max=2.5,
                    step=0.01,
                    value=1.13,
                ), style={'width':'55%'} ),
            html.Td( html.P(id='value-slider-D',children=''), style={'width':'20%'} ),
            ]), 

        # 'Age'
        html.Tr([
            html.Td( html.B('Age (A):', style={'font-size':'9pt'}), style={'width':'25%'} ),
            html.Td( dcc.Slider(id='slider-A',
                    min=1,
                    max=90,
                    step=1,
                    value=50,
                ), style={'width':'55%'} ),
            html.Td( html.P(id='value-slider-A',children=''), style={'width':'20%'} ),
            ]),
        ]), 
    ], style={'width':'100%', 'padding':'0', 'margin':'0'}),

   
    html.Center( 
        html.Div([
            html.Br(),
            html.H4(html.B('Classification result', id='classification-result', style={'color':'#983e0f'})),
            html.Button('Execute Classification', id='submit', style={'margin':'0 auto', 'width':'30%'}),
        ])
    ),

    html.Br(),

    html.Center(html.B('Possible classes: [0:Negative], [1:Positive]', style={'color':'blue'})),

    html.Hr(),

    html.H3('Dataset Visualization'),

    html.Div('The next plots show some characteristics of the original dataset. Note that the values from the SAMPLE that was input above will be highlighted in the plot according to the selected variables.'),

#  #['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness','Insulin','BMI', 'DiabetesPedigreeFunction', 'Age']
   
    # Layout for plots
    html.Table([
        html.Tbody([
            # Create the cell for the first plot
            html.Tr([
                html.Td([
                    
                    html.H5('Histogram per class of a variable'),

                    html.Label("Choose a variable:"),

                    dcc.Dropdown(id='dropdown-histogram',
                        options=[{"label":l, 'value':v} for l,v in zip(column_labels,colnames)],
                        value='Pregnancies'
                    ),

                    dcc.Graph(
                        id='graph-histogram',
                        figure = fig_histogram
                    ),
                ], style={'width':'40%'} ),

                html.Td([
                    
                    html.H5('Scatter plot of two variables'),

                    html.Label("Choose two variables to plot:"),

                    dcc.Dropdown(id='dropdown-scatter-1',
                        options=[{"label":l, 'value':v} for l,v in zip(column_labels,colnames)],
                        value='Pregnancies'
                    ),

                    dcc.Dropdown(id='dropdown-scatter-2',
                        options=[{"label":l, 'value':v} for l,v in zip(column_labels,colnames)],
                        value='BloodPressure'
                    ),

                    dcc.Graph(
                        id='graph-scatter',
                        figure = fig_scatter
                    ),
                ], style={'width':'60%'} )
            ])
        ])
    ], style={'width': '100%'}),
    
], style={'columnCount': 1})