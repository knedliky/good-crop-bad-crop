import dash
import dash_leaflet as dl
from dash import dcc
from dash import html
from map import create_map

app = dash.Dash(__name__)

map = create_map(7680, 10240)

# HTML layout
app.layout = html.Div(id='container', children = [
    html.Div(id = 'header', children = [
        html.H1('Good Crop, Bad Crop'),
        html.P('Predicting sugarcane health near Prosperine, Queensland')]),
    html.Div(id = 'sidebar', children =[
        html.H2('Field Info'),
        html.P('Select health metric:'),]),
    html.Div(id = 'map', children = [
        map]),
    html.Div(id = 'chart', children = [
        html.H2('Chart')]),
])

# Callback functions


# Main
if __name__ == '__main__':
    app.run_server(debug = True)
