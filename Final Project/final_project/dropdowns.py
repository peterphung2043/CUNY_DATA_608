from dash import dcc, html
from numpy import sort
from pandas import DataFrame

def generate_dropdowns(
        subject_array: list[str], 
        country_dict: dict[str, str], 
        year_dict: dict[str, str]
        ) -> list[html.Div]:

    meat_type_dropdown = html.Div(
                [
                    "Select Meat Type For Time Series Figure Below:",
                    dcc.RadioItems(
                    options=subject_array, 
                    value='BEEF', 
                    id='subject_selection'), 
                ],
                style={"width": 250,
                    "font-size": "15px"},
            )

    country_dropdown = html.Div(
            [
                "Select Country For Time Series and Correlation Figure Below:",
                dcc.Dropdown(
                id='country_selection', 
                options=[
                {'label': x, 'value': x} for x in sort(df['Country'].unique())
                ],
                value = 'Australia'),
            ],
            style={"width": 250,
                "font-size": "15px"},
        )

    year_dropdown = html.Div(
            [
                "Select Year For Bar Plots Below:",
                dcc.Dropdown(
                id='year_selection', 
                options=[
                {'label': x, 'value': x} for x in sort(df['Year'].unique())
                ],
                value = '2021'
                ),
            ],
            style={"width": 250,
                "font-size": "15px"},
        )
    
    return [meat_type_dropdown, country_dropdown, year_dropdown]