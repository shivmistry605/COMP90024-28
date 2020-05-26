import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import db as db
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


app = dash.Dash()
app.config['suppress_callback_exceptions'] = True
app.config.suppress_callback_exceptions = True

lang_ms = db.key_ms[::2]
value_ms = db.key_ms[1::2]

lang_syd = db.key_syd[::2]
value_syd = db.key_syd[1::2]

aurin_ms_lang = ['ar', 'de', 'el', 'it', 'zh']
aurin_ms_value = [11234, 13571, 60919, 80456, 17984]

aurin_syd_lang = ['ar', 'de', 'el', 'it', 'zh']
aurin_syd_value = [40117, 13571, 44697, 49655, 29208]

colors = {
    'background': '#111111',
    'background2': '#cccccc',
    'text': '#000000'
}

app.layout = html.Div(style={'backgroundColor': colors['background2']}, children=[
    html.Br(),

    html.H1(
        children='Melbourne/Sydney',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'id':'graph',
            'font-family':'Sans-serif',
            'font-size':36
        }
    ),
    html.Div(children='Twitter', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.Br(),
    html.Button('Bar Graph', id='button1',
                type='submit', n_clicks_timestamp=0),
    html.Button('Bar Graph 2', id='button2',
                type='submit', n_clicks_timestamp=0),
    html.Div(id='p_section'),
    html.Button('Melbourne Map', id='mapbutton1',
                type='submit', n_clicks_timestamp=0),
    html.Button('Sydney Map', id='mapbutton2',
                type='submit', n_clicks_timestamp=0),
    # dcc.Graph(
    #   id='bar-graph',figure={})
    html.Br(),
    html.Br(),
    html.Div(id='map_area', style={
             'position': 'absolute', 'top': '80%', 'left': '30%'}),


])


@app.callback(
    dash.dependencies.Output('p_section', 'children'),
    [dash.dependencies.Input('button1', 'n_clicks_timestamp'),
     Input('button2', 'n_clicks_timestamp')
     ])
def update_chart(btn1, btn2):
    btn_state = [int(btn1), int(btn2)]
    if all(v == 0 for v in btn_state):
        return html.H1(
            children=' ',
            style={
                'textAlign': 'center',
                'color': colors['text'],
            }
        )
    max_index = btn_state.index(max(i for i in btn_state if i is not None))
    if max_index == 0:
        fig = dcc.Graph(
            id='bar-graph',
            figure={
                'data': [{'x': lang_ms, 'y': value_ms, 'type': 'bar', 'name': 'Melbourne'},
                         {'x': lang_syd, 'y': value_syd, 'type': 'bar', 'name': u'Sydney'}],
                'layout': {'title': 'Twitter Data', 'xaxis': dict(title='Language', titlefont=dict(family='Courier New, monospace', size=20, color='blue')),
                           'yaxis': dict(title='Tweet Count', titlefont=dict(family='Helvetica, monospace', size=20, color='blue'), range=[0, 1000], tick=20, autorange=False)}
            })
        return fig
    else:
        fig = dcc.Graph(
            id='bar-graph',
            figure={
                'data': [{'x': aurin_ms_lang, 'y': aurin_ms_value, 'type': 'bar', 'name': 'Melbourne'},
                         {'x': aurin_syd_lang, 'y': aurin_syd_value, 'type': 'bar', 'name': u'Sydney'}],
                'layout': {'title': 'Aurin-Data', 'xaxis': dict(title='Language', titlefont=dict(family='Courier New, monospace', size=20, color='blue')),
                           'yaxis': dict(title='Tweet Count', titlefont=dict(family='Helvetica, monospace', size=20, color='blue'), range=[0, 50000], tick=20, autorange=False)}
            })
        return fig


@app.callback(
    dash.dependencies.Output('map_area', 'children'),
    [dash.dependencies.Input('mapbutton1', 'n_clicks_timestamp'),
     Input('mapbutton2', 'n_clicks_timestamp')])
def update_chart(btn1, btn2):
    btn_state = [int(btn1), int(btn2)]
    if all(v == 0 for v in btn_state):
        return html.H1(
            children=' ',
            style={
                'textAlign': 'center',
                'color': colors['text'],
            }
        )
    max_index = btn_state.index(max(i for i in btn_state if i is not None))
    if max_index == 0:
        fig = html.Iframe(src="static/melbourne/melb.html",
                          height='700px', width='800px')
        return fig
    else:
        return html.Iframe(src="/static/Sydney/Sydney.html", height='700px', width='800px')


if __name__ == '__main__':
    app.run_server(debug=False, dev_tools_ui=False,
                   dev_tools_props_check=False)
