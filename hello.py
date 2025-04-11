import pandas as pd
import plotly.express as px
from preswald import connect, get_df, plotly, query, slider, table, text

# Title and welcome
text("# Stock Market Simulator 📈")
text("Interactive analysis of synthetic market data.")

# Initialize Preswald connection
connect()

# Load the dataset (replace sample_csv with your actual dataset name on Preswald)
data = get_df("stock_market_simulation")

# Convert Date to string if needed
if "Date" in data.columns:
    data["Date"] = data["Date"].astype(str)

# Show preview table
text("Preview of Stock Data")
table(data.head(10), title="Preview of Stock Data")

# # --- Static Query: High Closing Prices --- It's Timing Out; Panda Filter can help 
# sql = "SELECT * FROM stock_market_simulation where Close>100"
# sql = "SELECT * FROM stock_market_simulation WHERE Close > 100 LIMIT 100"
# filtered_df = query(sql, "stock_market_simulation")
# table(filtered_df, title="High-Closing Stocks (> $100)")

# --- Static Query: Retrieveing Min Value for Close Prices
min_sql = "SELECT min(Close) FROM stock_market_simulation"
min_close_val = query(min_sql, "stock_market_simulation")

# --- Static Query: Retrieveing Max Value for Close Prices
max_sql = "SELECT max(Close) FROM stock_market_simulation"
max_close_val = query(max_sql, "stock_market_simulation")

# --- Interactive Slider: Close Price Threshold ---
threshold = slider("Minimum Close Price", min_val=int(min_close_val.iloc[0, 0]), max_val=int(max_close_val.iloc[0, 0]), default=int(min_close_val.iloc[0, 0]))
filtered_dynamic = data[data["Close"] > threshold]
table(filtered_dynamic, title=f"Stocks with Close Price > {threshold}")

# --- Line Chart: Close Prices Over Time by Company ---
fig = px.line(filtered_dynamic,
              x="Date",
              y="Close",
              color="Company",
              title="Stock Close Price Trends by Company",
              line_group="Company")
plotly(fig)

# --- Volume by Company ---
volume_fig = px.bar(data.groupby("Company")["Volume"].mean().reset_index(),
                    x="Company", y="Volume",
                    title="Average Trading Volume by Company")
plotly(volume_fig)
