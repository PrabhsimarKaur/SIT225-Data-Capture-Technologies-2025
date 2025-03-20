import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load Gyroscope data from CSV
df = pd.read_csv("gyroscope_data.csv")  # Replace with your file
df["Index"] = df.index  # Add an index column for navigation

# Initialize Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Gyroscope Data Visualization", style={'textAlign': 'center' ,'fontSize': '100px','fontWeight': 'bold'}),

    # Dropdown for graph type
    html.Label("Select Graph Type:"),
    dcc.Dropdown(
        id="graph-type",
        options=[
            {"label": "Scatter Plot", "value": "scatter"},
            {"label": "Line Chart", "value": "line"},
            {"label": "Distribution Plot", "value": "dist"}
        ],
        value="line"
    ),

    # Dropdown for X, Y, Z variables selection
    html.Label("Select Variables:"),
    dcc.Dropdown(
        id="variable-select",
        options=[
            {"label": "X", "value": "x"},
            {"label": "Y", "value": "y"},
            {"label": "Z", "value": "z"}
        ],
        value=["x", "y", "z"],
        multi=True
    ),

    # Input for number of samples
    html.Label("Enter Number of Samples to Display:"),
    dcc.Input(id="num-samples", type="number", value=100, min=10, step=10),

    # Navigation Buttons
    html.Div([
        html.Button("Previous", id="prev-btn", n_clicks=0),
        html.Button("Next", id="next-btn", n_clicks=0)
    ], style={'margin': '10px'}),

    # Graph
    dcc.Graph(id="gyro-graph"),

    # Summary Table
    html.H3("Statistical Summary:"),
    html.Div(id="summary-table")
])

# Callback to update graph and table based on user input
@app.callback(
    [Output("gyro-graph", "figure"), Output("summary-table", "children")],
    [Input("graph-type", "value"),
     Input("variable-select", "value"),
     Input("num-samples", "value"),
     Input("prev-btn", "n_clicks"),
     Input("next-btn", "n_clicks")]
)
def update_graph(graph_type, selected_vars, num_samples, prev_clicks, next_clicks):
    start_idx = max(0, (prev_clicks - next_clicks) * num_samples)
    end_idx = min(len(df), start_idx + num_samples)
    filtered_df = df.iloc[start_idx:end_idx]

    # Create plot
    if graph_type == "scatter":
        fig = px.scatter(filtered_df, x="Index", y=selected_vars, title="Scatter Plot of Gyroscope Data")
    elif graph_type == "line":
        fig = px.line(filtered_df, x="Index", y=selected_vars, title="Line Chart of Gyroscope Data")
    else:  # Distribution plot
        fig = px.histogram(filtered_df, x=selected_vars, title="Distribution Plot of Gyroscope Data")

    # Compute summary statistics
    summary = filtered_df[selected_vars].describe().reset_index()
    table = html.Table([
        html.Tr([html.Th(col) for col in summary.columns])
    ] + [
        html.Tr([html.Td(value) for value in row]) for row in summary.values
    ])

    return fig, table

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
