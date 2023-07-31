import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

# Load the climate data
climate = pd.read_csv('climate.csv')
climate_new = climate[['Year', 'Disaster Group', 'Disaster Type', 'Continent', 'Country', 'Region', 'Start Month', 'End Month', 'Location']]
climate_f = climate_new.dropna()

# Plotly Figure 1: histplot
fig1 = px.histogram(climate_f, x='Continent', y='Year', color='Disaster Type',title='Different Type of Disaster occured in Different Continent with respect to Year')
fig1.update_layout(height=600, width=1000)  # Set the desired size

# Plotly Figure 2: countplot
fig2 = px.histogram(climate_f, x='Year', title='Most Disaster Year',color_discrete_sequence=['green'])
fig2.update_layout(height=600, width=1000)  # Set the desired size

# Plotly Figure 3: scatterplot
fig3 = px.scatter(climate_f, x='Year', y='Region', color='Disaster Group',title='Natural & Technolgical Disaster Occured in Different Region with respect to Year ')
fig3.update_layout(height=600, width=1000)  # Set the desired size

# Plotly Figure 4: histplot
fig4 = px.histogram(climate_f, x='Year', y='Region', color='Disaster Type',title='Different Disaster Occured in Different Region with respect to s')
fig4.update_layout(height=600, width=1000)  # Set the desired size

# Plotly Figure 5: Pie Chart
top_n = 9
top_categories = climate_f['Disaster Type'].value_counts().nlargest(top_n)
other_frequency = climate_f['Disaster Type'].value_counts().sum() - top_categories.sum()
reduced_df = pd.concat([top_categories, pd.Series({'Other': other_frequency})])
fig5 = px.pie(reduced_df, names=reduced_df.index, values=reduced_df.values, title='Disaster Group Pie Chart')
fig5.update_layout(height=600, width=1000)  # Set the desired size

# Initialize Dash app
app = dash.Dash(__name__)

# Create Dashboard Layout
app.layout = html.Div(children=[
    html.H1('Climate Disaster Dashboard'),

    # Grid Layout for Plots
    html.Div(className='row', children=[
        html.Div(className='col-6', children=[
            # Plotly Figure 1: histplot
            dcc.Graph(id='plot-1', figure=fig1),
        ]),
        html.Div(className='col-6', children=[
            # Plotly Figure 2: countplot
            dcc.Graph(id='plot-2', figure=fig2),
        ]),
    ]),

    html.Div(className='row', children=[
        html.Div(className='col-4', children=[
            # Plotly Figure 3: scatterplot
            dcc.Graph(id='plot-3', figure=fig3),
        ]),
        html.Div(className='col-4', children=[
            # Plotly Figure 4: histplot
            dcc.Graph(id='plot-4', figure=fig4),
        ]),
        html.Div(className='col-4', children=[
            # Plotly Figure 5: Pie Chart
            dcc.Graph(id='plot-5', figure=fig5),
        ]),
    ]),
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
