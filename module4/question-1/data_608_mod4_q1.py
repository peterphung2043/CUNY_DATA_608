from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

## Get all the boroughs in the dataset

boro_url = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?' +\
            '$query=select distinct boroname').replace(' ', '%20')
distinct_boroughs = pd.read_json(boro_url)

## Get all of the distinct species in a dataset

spc_common_url = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?' +\
            '$query=select distinct spc_common').replace(' ', '%20')
distinct_spc_common = pd.read_json(spc_common_url)

app = Dash(__name__)

server = app.server

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Dropdown(id='boro_selection', options=[
    {'label': x, 'value': x} for x in distinct_boroughs['boroname']
    ],
            value = 'Bronx'),
            
    dcc.Dropdown(id='spc_selection', options=[
    {'label': x, 'value': x} for x in distinct_spc_common['spc_common']
    ],
            value = 'black walnut'),

    dcc.Graph(
        id='example-graph'
    )
])

@app.callback(Output('example-graph', 'figure'),
              [Input('boro_selection', 'value'),
               Input('spc_selection', 'value')])

def update_figure(boro_selection, spc_selection):
    soql_url = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?' +\
            '$select=health,count(tree_id)' +\
            '&$where=boroname=\'{}\'&spc_common=\'{}\''.format(boro_selection, spc_selection) +\
            '&$group=health').replace(' ', '%20')

    soql_trees = pd.read_json(soql_url)

    soql_trees['proportion'] = round(soql_trees['count_tree_id']/soql_trees['count_tree_id'].sum(), 2)
    soql_trees = soql_trees.sort_values('proportion')

    fig = px.bar(
        soql_trees, 
        x="health", 
        y="proportion",
        text_auto=True,
        title = 'Proportion of {} Trees In Good, Fair, or Poor Health for the {} Borough'.format(spc_selection, boro_selection)
        )

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )

    return fig


if __name__ == '__main__':
    app.run_server()