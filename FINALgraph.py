import dash
from dash import html
from dash import dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

# Load the CSV files
it_df = pd.read_csv('it.csv')
bandf = pd.read_csv('pharma.csv')
finance_df = pd.read_csv('finance.csv')
bank_df=pd.read_csv('BANKING.csv')
media_df=pd.read_csv('media.csv')

# Create the Dash app instance with external CSS stylesheet
external_stylesheets = ['nn.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Define the layout of the app
app.layout = html.Div([
        html.Div([
            html.H1(children='Relative Rotation Graph', style={'textAlign': 'center'}),
            html.H2(children='Unique Visualisation Tool', style={'textAlign': 'center'}),
        ], className='header'),
    dcc.DatePickerRange(
        id='date-picker',
        min_date_allowed=min(it_df['Date']),
        max_date_allowed=max(it_df['Date']),
        start_date=min(it_df['Date']),
        end_date=max(it_df['Date']),
    ),
    html.Div([
        html.Label('Select a sector:', style={'margin-right': '10px'}),
        html.Div(style={'display': 'flex'}, children=[
            html.Div(style={"flex": "1"}, children=[
                dcc.Dropdown(
                    id='sector-dropdown',
                    options=[
                        {'label': 'Pharma Sector', 'value': 'PHARMA'},
                        {'label': 'Finance Sector', 'value': 'FINANCE'},
                        {'label': 'IT Sector', 'value': 'IT'},
                        {'label': 'Media Sector', 'value': 'MEDIA'},
                        {'label': 'Banking Sector', 'value': 'BANKING'}
                    ],
                    style={"width": "70%"},
                ),
            ]),
            html.Div(style={'flex': '1'}, children=[
                html.Label('Benchmark:', style={'margin-left': '10px'}),
                dcc.Dropdown(
                    options=[{'label': 'Nifty 50', 'value': 'Nifty 50'}],
                    value='Nifty 50',
                    searchable=False,
                    style={"width": "70%", "height": "40px"},
                    placeholder="Benchmark"
                ),
            ]),
        ]),
        # Update button for updating the graph and table components
        html.Button('Update', id='update-button', n_clicks=0),
        # Graph for displaying the stock prices
        dcc.Graph(id='sector-graph1'),
        # Graph for displaying the RS and RM values
        dcc.Graph(id='sector-graph2'),
        # Table for displaying the top 5 stock prices
        html.Table(
            id='sector-table',
            className='table'
        ),
    ]),
])




# Define the callback function to update the graph and table components
@app.callback(
    [Output('sector-graph2', 'figure'),
     Output('sector-graph1', 'figure'),
     Output('sector-table', 'children')],
    Input('update-button', 'n_clicks'),
    State('date-picker', 'start_date'),
    State('date-picker', 'end_date'),
    [Input('sector-dropdown', 'value')]
)
def update_sector(n_clicks, start_date, end_date, sector):
    if sector == 'PHARMA':
        df = bandf
        col1='symbol'
        col2 = 'name'
        col3 = 'price'
        col4 = '%chg'
        col5 = 'volume'
    elif sector == 'IT':
        df = it_df
        col1 = 'symbol'
        col2 = 'name'
        col3 = 'price'
        col4 = '%chg'
        col5 = 'volume'
    elif sector == 'BANKING':
        df = bank_df
        col1 = 'symbol'
        col2 = 'name'
        col3 = 'price'
        col4 = '%chg'
        col5 = 'volume'
    elif sector == 'MEDIA':
        df = media_df
        col1 = 'symbol'
        col2 = 'name'
        col3 = 'price'
        col4 = '%chg'
        col5 = 'volume'
    else:
        df = finance_df
        col1 = 'symbol'
        col2 = 'name'
        col3 = 'price'
        col4 = '%chg'
        col5 = 'volume'
    # Filter the data based on the selected date range
    df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    # Create the plotly figure for displaying the stock prices
    fig1 = go.Figure(data=go.Scatter(x=df['name'], y=df['price'], mode='lines',
                                     marker=dict(size=10, colorscale='Viridis', showscale=True)))
    # Create the plotly figure for displaying the RS and RM values
    fig1.update_layout(title='Stock Prices',
                       xaxis_title='Stock',
                       yaxis_title='Price')
    grouped = df.groupby('Symbol')
    traces = []
    for symbol, data in grouped:
        # Get the index of the last data point in this trace
        last_index = len(data) - 1
        # Create a list of marker sizes for this trace
        marker_sizes = [8] * last_index + [16]  # Make the last marker size bigger
        # Modify the marker size of the last data point
        marker_sizes[-1] = 15
        traces.append(go.Scatter(x=data['RS'], y=data['RM'], name=symbol, mode='lines+markers',
                                 marker=dict(size=marker_sizes)))

    fig2 = go.Figure(data=traces)
    fig2.update_layout(title='RS-RM Graph', xaxis_title='RS', yaxis_title='RM')

    # add annotations

    fig2.add_annotation(xref='paper', yref='paper', x=0.05, y=0.9, text="Improving", font=dict(color='blue', size=16), showarrow=False)
    fig2.add_annotation(xref='paper', yref='paper', x=0.95, y=0.9, text="Leading", font=dict(color='green', size=16), showarrow=False)
    fig2.add_annotation(xref='paper', yref='paper', x=0.05, y=0.1, text="Lagging", font=dict(color='red', size=16), showarrow=False)
    fig2.add_annotation(xref='paper', yref='paper', x=0.95, y=0.1, text="Weakning", font=dict(color='orange', size=16), showarrow=False)

    fig2.update_xaxes(range=[0, 200])
    fig2.update_yaxes(range=[0, 200])
    fig2.add_shape(type='line',
                   x0=100,
                   y0=0,
                   x1=100,
                   y1=200,
                   line=dict(color='black', width=2))

    fig2.add_shape(type='line',
                   x0=0,
                   y0=100,
                   x1=200,
                   y1=100,
                   line=dict(color='black', width=2))


# Create the table with the stock prices

    table_rows = []
    for index, row in df.iloc[:5].iterrows():
        table_rows.append(html.Tr([
            html.Td(row[col1]),
            html.Td(row[col2]),
            html.Td(row[col3]),
            html.Td(row[col4]),
            html.Td(row[col5])
        ]))

    table = html.Table([
        html.Thead(html.Tr([
            html.Th(col1, className='table-header'),
            html.Th(col2, className='table-header'),
            html.Th(col3, className='table-header'),
            html.Th(col4, className='table-header'),
            html.Th(col5, className='table-header')
        ])),
        html.Tbody(table_rows)
    ])

    container = html.Div(children=[
        html.H1('My Table'),
        table
    ], className='container')

    return fig1, fig2, table


#

if __name__ == '__main__':
    app.run_server(debug=True)
