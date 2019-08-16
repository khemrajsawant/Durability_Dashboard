# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Khemraj)s
"""
#from utils import Header
import dash
import dash_core_components as dcc
import dash_html_components as html
import preprocess

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id="stock_input",placeholder="Enter Title details"),
    html.Div(dcc.Graph(preprocess.fig)),
#    dcc.Upload(html.Button('Upload File')),
#    dcc.Dropdown(
#    options=[
#        {'label': 'New York City', 'value': 'NYC'},
#        {'label': 'Montréal', 'value': 'MTL'},
#        {'label': 'San Francisco', 'value': 'SF'}
#    ],
#    value='MTL'
#)


])

if __name__ == '__main__':
    app.run_server(debug=False)