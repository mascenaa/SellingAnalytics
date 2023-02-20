from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app


list_of_loc = {
    "All": 0,
    "Manhattan": 1,
    "Bronx": 2,
    "Brooklyn": 3,
    "Queens": 4,
    "Staten Island": 5,
}

slider_size = [100, 500, 1000, 10000, 10000000]


controlers = dbc.Row([
    html.H3("Venda de Imóveis - New York City",
            style={"margin-top": "2rem", "color": "white"}),
    html.P("Utilize esse dashboard para conferir as vendas ocorridas em nova york durante um ano!"),


    html.H4("""Borough""", style={
            "margin-top": "4rem", "margin-bottom": "2rem", "color": "white"}),
    dcc.Dropdown(
        id="drop",
        options=[{"label": i, "value": j} for i, j in list_of_loc.items()],
        value=0,
        placeholder="Select a district"
    ),
    html.H4("""Metragem""", style={
            "margin-top": "4rem", "margin-bottom": "2rem", "color": "white"}),
    dcc.Slider(
        id="slider",
        min=0,
        max=4,
        marks={
            i: str(j) for i, j in enumerate(slider_size)
        },
    ),
    html.H4("""Control""", style={
            "margin-top": "4rem", "margin-bottom": "2rem", "color": "white"}),
        dcc.Dropdown(
        id="control",
        options=[
            {'label': 'YEAR BUILT', 'value': 'YEAR BUILT'},
            {'label': 'TOTAL UNITS', 'value': 'TOTAL UNITS'},
            {'label': 'SALE PRICE', 'value': 'SALE PRICE'},
        ],
        value="SALE PRICE",
    ),

])
