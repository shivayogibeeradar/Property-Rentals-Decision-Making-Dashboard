import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input , Output


import plotly.graph_objs as graph_objs
import folium
import dash_table_experiments as dt 
import flask
import dash
import dash_html_components as html

server = flask.Flask(__name__)

@server.route('/')
def index():
   return 'Hello Flask app'

app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/'
)


app.layout=html.Div([


html.H1("New York Housing Heatmap"),
html.Iframe(id="map",srcDoc=open("maps.html","r").read(),width="100%",height="650")	])
if __name__ == '__main__':
    app.run_server(debug=True)  