import pandas as pd
import plotly.graph_objects as go
import os

BASE_DIR = os.path.dirname(__file__)

def plot(FILE):

    df = pd.read_csv(FILE)

    # ---------------------------------------------------
    # TRUE CONTINUOUS SERPENTINE REORDERING
    # ---------------------------------------------------

    # IMPORTANT:
    # We assume points arrive in scan order.
    # We rebuild lines in chunks of 5.

    CHUNK = 5

    traces = []

    for i in range(0, len(df), CHUNK):

        block = df.iloc[i:i+CHUNK].copy()

        # Reverse every alternate block (zig-zag)
        if (i // CHUNK) % 2 == 1:
            block = block.iloc[::-1]

        traces.append(go.Scatter3d(
            x=block["x"],
            y=block["y"],
            z=block["z"],
            mode='lines+markers',
            line=dict(width=4),
            marker=dict(
                size=3,
                color=block["z"],
                colorscale='Viridis'
            ),
            showlegend=False
        ))

    fig = go.Figure(data=traces)

    fig.update_layout(
        title="Drone Terrain Map (TRUE Continuous Zig-Zag)",
        scene=dict(
            xaxis_title="X (Sweep)",
            yaxis_title="Y (Drone Path)",
            zaxis_title="Elevation",
            aspectmode='data'
        )
    )

    fig.show()

plot(os.path.join(BASE_DIR, "processed_points.csv"))