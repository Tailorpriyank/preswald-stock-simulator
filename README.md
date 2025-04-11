# 📈 Preswald Stock Simulator

An interactive stock market dashboard built using [Preswald](https://preswald.com), pandas, and Plotly. This simulator demonstrates real-time filtering, querying, and visualization of synthetic stock market data — all in one dynamic notebook environment.

---

## 📖 Project Story

Simulating and understanding financial data can be challenging — especially when tools are either too simple or too complex. This project bridges that gap using **Preswald**, creating a lightweight, flexible, and interactive stock market analysis tool.

**Objective**: Allow users to explore synthetic stock data, filter it interactively, and uncover trends in closing prices and trading volume — directly in the notebook.

---

## 🚀 Features

- 🧮 **Interactive Filtering**: Use sliders to dynamically adjust the minimum closing price and update the table + graphs in real time.
- 📊 **Line Chart**: Visualizes how the closing price evolves over time for each company.
- 📉 **Volume Analysis**: Explore average trading volumes across different companies.
- 🧠 **SQL + Python Integration**: Uses Preswald’s native SQL queries combined with pandas for advanced data wrangling.
- ⚡ **Notebook-native UI**: Clean, fast, and runs entirely in-browser.

---

## 🔍 Preview

### 📅 Stock Closing Price Trends

<img src="images/close_price_linechart.png" width="600"/>

### 📦 Average Volume by Company

<img src="images/volume_barchart.png" width="600"/>

---

## 🛠️ Tech Stack

- [Preswald](https://preswald.com) – SQL-powered data notebook  
- [pandas](https://pandas.pydata.org/) – Data manipulation  
- [Plotly Express](https://plotly.com/python/plotly-express/) – Visualization  
- SQL – For interactive data querying  

---

## 📂 File Structure

├── data/                     # Synthetic stock data
├── images/                   # Visualizations used in README
├── hello.py                  # Main app logic
├── preswald.toml             # Preswald config
├── pyproject.toml            # Project metadata
├── secrets.toml              # (Empty or sanitized!)


---

## 👤 Author

**Priyank Tailor**  
M.S. in Data Analytics and Visualization  
[LinkedIn](#) | [GitHub](https://github.com/Tailorpriyank)

---

## ⭐ Acknowledgements

- Thanks to **Structured Labs** and **Amrutha Gujjar** for the opportunity.  
- If you liked the project, [drop a ⭐ on Preswald’s GitHub repo](https://github.com/StructuredLabs/preswald)!
