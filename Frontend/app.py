import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import db as db

lang_ms = db.key_ms[::2]
value_ms = db.key_ms[1::2]

lang_syd = db.key_syd[::2]
value_syd = db.key_syd[1::2]

app = dash.Dash()
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Melbourne/Sydney',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Twitter', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='Graph1',
        #button
        figure={  'data': [
                {'x': lang_ms, 'y': value_ms, 'type': 'bar', 'name': 'Melbourne'},
                {'x': lang_syd, 'y': value_syd, 'type': 'bar', 'name': u'Sydney'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                },
            'style' : {"height" : "25vh", "width" : "100vh"}
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
