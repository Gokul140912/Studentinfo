import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load data from an Excel file with a specific sheet
excel_file_path = r'C:\Users\gokulnath.s\Documents\Test file.xlsx'
sheet_name = 'Sheet1'  # Replace with the actual sheet name

try:
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
except Exception as e:
    print(f"Error loading data from Excel file: {e}")
    df = pd.DataFrame()  # Create an empty DataFrame to avoid further errors

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Student Marks Dashboard'),

    dcc.Graph(
        id='bar-chart',
        figure=px.bar(df, x='Name', y='marks', title='Student Marks')
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
