from smooth_plot import smooth_live_plot
from arduino_connection import get_latest_accel_data, start_arduino_updater

# Start the background thread that continuously receives data from Arduino IoT Cloud
start_arduino_updater()

# Start the Dash application to plot accelerometer data in real-time
smooth_live_plot(
    data_fn=get_latest_accel_data,
    labels=['Accel X', 'Accel Y', 'Accel Z'],
    buffer_size=100,
    update_interval=200,
    graph_title="Smooth Real-Time Accelerometer Data"
)
