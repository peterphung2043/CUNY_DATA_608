from dash import html, dcc
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from final_project.dropdowns import generate_dropdowns

def generate_children(subject_array, country_dict, year_dict):
    meat_type_dropdown, country_dropdown, year_dropdown = generate_dropdowns(
        subject_array, 
        country_dict, 
        year_dict
        )
    children=[
        html.Div(
            children = [
                html.H1(children='GDP and Meat Consumption Per Capita Dash App',
                        className = "header-title",
                        style = {"text-align": "center",
                                    "fontSize": 40}),
                html.P(
                    children = (
                        "Exploration of GDP Per Capita collected from The World Bank"
                        " and meat consumption data collected from OECD. Created by"
                        " Peter Phung."
                    ),
                    className = "header-description",
                    style = {"fontSize": 20}
                ),
                html.Hr()
            ],
            className = "header"
        ),

    dbc.Container(
        [
            dbc.Row([dbc.Col(meat_type_dropdown), dbc.Col(country_dropdown)])
        ],
        fluid = True
    ),

    dmc.Grid([
        dmc.Col([
            dcc.Graph(
                figure={}, 
                id='ts_fig',
                style = {"border": "2px black solid"})
        ], span=6),
        dmc.Col([
            dcc.Graph(
                figure={}, 
                id='corr_fig',
                style = {"border": "2px black solid"})
        ], span=6)
    ]),

    dbc.Container(
        [
            dbc.Row([dbc.Col(year_dropdown)])
        ],
        fluid = True
    ),

    dmc.Grid([
        dmc.Col([
            dcc.Graph(
                figure={}, 
                id='gdp_fig_low',
                style = {"border": "2px black solid"})
        ], span=6),
        dmc.Col([
            dcc.Graph(
                figure={}, 
                id='gdp_fig_high',
                style = {"border": "2px black solid"})
        ], span=6)
    ]),
    ]

    return children
