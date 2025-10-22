from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app
import plotly.graph_objects as go



fig = go.Figure()
fig.update_layout(template="plotly", paper_bgcolor="rgba(220, 220, 220, 1)")

map = dbc.Row([
                dcc.Graph(id="map-graph", figure=fig)
            ], style={"height": "70vh"})