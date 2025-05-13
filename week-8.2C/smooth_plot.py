from collections import deque
import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.graph_objs as go
import time

def smooth_live_plot(
    data_fn,
    labels=['X', 'Y', 'Z'],
    buffer_size=100,
    update_interval=200,
    graph_title="Live Data Stream"
):
    """
    Smooth real-time Dash plot for continuous data.
    """
    # Create buffers to store recent values for each label
    buffers = {label: deque([0]*buffer_size, maxlen=buffer_size) for label in labels}
    # Create a buffer for timestamps
    timestamps = deque([time.time()]*buffer_size, maxlen=buffer_size)

    # Initialize Dash app
    app = dash.Dash(__name__)

    # Define the layout of the web page
    app.layout = html.Div([
        html.H2(graph_title, style={'textAlign': 'center'}),
        dcc.Graph(id='live-graph'),
        dcc.Interval(id='interval', interval=update_interval, n_intervals=0)
    ])

    # Callback to update the graph at regular intervals
    @app.callback(Output('live-graph', 'figure'),
                  Input('interval', 'n_intervals'))
    def update_graph(n):
        new_data = data_fn()
        now = time.time()

        # Update buffers with new data
        for label, val in zip(labels, new_data):
            buffers[label].append(val)
        timestamps.append(now)

        # Create the figure with line traces for each label
        fig = go.Figure()
        for label in labels:
            fig.add_trace(go.Scatter(
                x=list(timestamps),
                y=list(buffers[label]),
                mode='lines',
                name=label
            ))

        # Update graph layout
        fig.update_layout(
            xaxis_title="Time",
            yaxis_title="Acceleration",
            template="plotly_dark",
            margin=dict(l=40, r=20, t=40, b=40),
            uirevision=True
        )
        return fig

    # Run the Dash app
    app.run(debug=True)
