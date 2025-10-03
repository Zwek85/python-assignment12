from dash import Dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Load Gapminder dataset
df = px.data.gapminder()

# Get the list of unique countries (no duplicates), sorted alphabetically
countries = df['country'].drop_duplicates().sort_values()

app = Dash(__name__)
server = app.server  # Added ths line 

# Layout with dropdown and graph
app.layout = html.Div([
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in countries],
        value='Canada'  # Default selected country
    ),
    dcc.Graph(id='gdp-growth')
])

# Callback
@app.callback(
    Output('gdp-growth', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    # Filter dataframe for the selected country only
    filtered_df = df[df['country'] == selected_country]

    # Create line plot of GDP per capita over years
    fig = px.line(
        filtered_df,
        x='year',
        y='gdpPercap',
        title=f'GDP per Capita Over Time for {selected_country}'
    )
    return fig

# Running the app
if __name__ == '__main__':
    app.run(debug=True)

