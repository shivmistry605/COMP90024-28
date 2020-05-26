import dash
import dash_html_components as html
import dash_core_components as dcc
import db as db

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config['suppress_callback_exceptions'] = True

lang_ms = db.key_ms[::2]
value_ms = db.key_ms[1::2]

lang_syd = db.key_syd[::2]
value_syd = db.key_syd[1::2]
##ar
aurin_ms_lang = ['Ar_aurin', 'Ar_twitter']
aurin_ms_value = [1123.4, value_ms[0]]

aurin_syd_lang = ['Ar_aurin', 'Ar_twitter']
aurin_syd_value = [4011.7, value_syd[0]]
##it
aurin_ms_lang_it = ['It_aurin', 'It_twitter']
aurin_ms_value_it = [804.56, value_ms[3]]

aurin_syd_lang_it = ['It_aurin', 'It_twitter']
aurin_syd_value_it = [496.55, value_syd[3]]
##de
aurin_ms_lang_de = ['De_aurin', 'De_twitter']
aurin_ms_value_de = [135.71, value_ms[1]]

aurin_syd_lang_de = ['De_aurin', 'De_twitter']
aurin_syd_value_de = [131.97, value_syd[1]]

app.layout = html.Div([
    html.H1("Language Comparison", style={'textAlign': 'center'}),
    html.Hr(),
    html.Div(children='Comparison between Melbourne & Sydney based on top three languages other than English', style={
             'textAlign': 'center'}),
    html.Hr(),
    dcc.Tabs([
        # first tab
        dcc.Tab(label='Arabic', children=[

            dcc.Graph(
                figure={
                    'data': [{'x': aurin_ms_lang, 'y': aurin_ms_value, 'type': 'bar', 'name': 'Melbourne'},
                             {'x': aurin_syd_lang, 'y': aurin_syd_value, 'type': 'bar', 'name': u'Sydney'}],
                    'layout': {'xaxis': dict(title='Arabic Language From Aurin & Twitter', titlefont=dict(family='Helvetica, monospace', size=20, color='black')),
                               'yaxis': dict(title='Tweet Count', titlefont=dict(family='Helvetica, monospace', size=20, color='black'))}

                }
            ),
            html.Br(),
            html.Div(children='Comparing Aurin and Twitter data we can see that number of people speaking Arabic in Melbourne are less than that of number of Arabic speaking people in Sydney, Which is proved by the Twitter data as well.', style={
                     'textAlign': 'center'}),
            html.Br(),
            html.Br(),

            html.Div([
                html.Div([
                    html.H3("Melbourne Maps", style={'textAlign': 'center'}),
                    html.Hr(),
                    html.Div([
                        html.H3('Melbourne Aurin Map',
                                style={'marginLeft': 100}),
                        html.Iframe(src="/static/melbourne/Arabic/qgis_melb/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100,
                                           'marginRight': 100, 'marginBottom': 100}

                                    ),
                    ], className="five columns"),

                    html.Div([
                        html.H3('Melbourne Twitter Map',
                                style={'marginLeft': 100}),
                        html.Iframe(src="/static/Twitter_map/ar_maps_twitter/melb_qgis/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100,
                                           'marginRight': 100, 'marginBottom': 100}

                                    ),
                    ], className="five columns")
                ], className="row"),
            ]),
            html.Div([
                html.Div([
                    html.H3("Sydney Maps", style={'textAlign': 'center'}),
                    html.Hr(),
                    html.Div([
                        html.H3('Sydney Aurin Map', style={'marginLeft': 100}),
                        html.Iframe(src="/static/Sydney/Arabic/qgis_syd/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100, 'marginRight': 100, 'marginBottom': 100})
                    ], className="five columns"),

                    html.Div([
                        html.H3('Sydney Twitter Map',
                                style={'marginLeft': 100}),
                        html.Iframe(src="/static/Twitter_map/ar_maps_twitter/syd_qgis/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100, 'marginRight': 100, 'marginBottom': 100})
                    ], className="five columns"),
                ]),
            ])

        ]),
        # second tab
        dcc.Tab(label='Italian', children=[

            dcc.Graph(
                figure={
                    'data': [{'x': aurin_ms_lang_it, 'y': aurin_ms_value_it, 'type': 'bar', 'name': 'Melbourne'},
                             {'x': aurin_syd_lang_it, 'y': aurin_syd_value_it, 'type': 'bar', 'name': u'Sydney'}],
                    'layout': {'xaxis': dict(title='Italian Language From Aurin & Twitter', titlefont=dict(family='Helvetica, monospace', size=20, color='black')),
                               'yaxis': dict(title='Tweet Count', titlefont=dict(family='Helvetica, monospace', size=20, color='black'))}

                }
            ),
            html.Br(),
            html.Div(children='Comparing Aurin and Twitter data we can see that number of people speaking Italian in Sydney are more than Melbourne.'
                     , style={'textAlign': 'center'}),
            html.Br(),
            html.Br(),

            html.Div([
                html.Div([
                    html.H3("Melbourne Maps", style={'textAlign': 'center'}),
                    html.Hr(),
                    html.Div([
                        html.H3('Melbourne Aurin Map',
                                style={'marginLeft': 100}),
                        html.Iframe(src="/static/melbourne/Italian/qgis_melb/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100,
                                           'marginRight': 100, 'marginBottom': 100}

                                    ),
                    ], className="five columns"),

                    html.Div([
                        html.H3('Melbourne Twitter Map',
                                style={'marginLeft': 100}),
                        html.Iframe(src="/static/Twitter_map/it_maps_twitter/qgis_melb/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100,
                                           'marginRight': 100, 'marginBottom': 100}

                                    ),
                    ], className="five columns")
                ], className="row"),
            ]),
            html.Div([
                html.Div([
                    html.H3("Sydney Maps", style={'textAlign': 'center'}),
                    html.Hr(),
                    html.Div([
                        html.H3('Sydney Aurin Map', style={'marginLeft': 100}),
                        html.Iframe(src="/static/Sydney/Italian/qgis_syd/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100, 'marginRight': 100, 'marginBottom': 100})
                    ], className="five columns"),

                    html.Div([
                        html.H3('Sydney Twitter Map',
                                style={'marginLeft': 100}),
                        html.Iframe(src="/static/Twitter_map/it_maps_twitter/qgis_syd/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100, 'marginRight': 100, 'marginBottom': 100})
                    ], className="five columns"),
                ]),
            ])

        ]),
        #third tab
        dcc.Tab(label='German', children=[

            dcc.Graph(
                figure={
                    'data': [{'x': aurin_ms_lang_de, 'y': aurin_ms_value_de, 'type': 'bar', 'name': 'Melbourne'},
                             {'x': aurin_syd_lang_de, 'y': aurin_syd_value_de, 'type': 'bar', 'name': u'Sydney'}],
                    'layout': {'xaxis': dict(title='German Language From Aurin & Twitter', titlefont=dict(family='Helvetica, monospace', size=20, color='black')),
                               'yaxis': dict(title='Tweet Count', titlefont=dict(family='Helvetica, monospace', size=20, color='black'))}

                }
            ),
            html.Br(),
            html.Div(children='Comparing the number of German people in Melbourne & Sydney, we notice that the number has increased in Sydney but has decreased in Melbourne'
                     , style={'textAlign': 'center'}),
            html.Br(),
            html.Br(),

            html.Div([
                html.Div([
                    html.H3("Melbourne Maps", style={'textAlign': 'center'}),
                    html.Hr(),
                    html.Div([
                        html.H3('Melbourne Aurin Map',
                                style={'marginLeft': 100}),
                        html.Iframe(src="/static/melbourne/German/qgis_melb/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100,
                                           'marginRight': 100, 'marginBottom': 100}

                                    ),
                    ], className="five columns"),

                    html.Div([
                        html.H3('Melbourne Twitter Map',
                                style={'marginLeft': 100}),
                        html.Iframe(src="/static/Twitter_map/de_maps_twitter/qgis_melb/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100,
                                           'marginRight': 100, 'marginBottom': 100}

                                    ),
                    ], className="five columns")
                ], className="row"),
            ]),
            html.Div([
                html.Div([
                    html.H3("Sydney Maps", style={'textAlign': 'center'}),
                    html.Hr(),
                    html.Div([
                        html.H3('Sydney Aurin Map', style={'marginLeft': 100}),
                        html.Iframe(src="/static/Sydney/German/qgis_syd/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100, 'marginRight': 100, 'marginBottom': 100})
                    ], className="five columns"),

                    html.Div([
                        html.H3('Sydney Twitter Map',
                                style={'marginLeft': 100}),
                        html.Iframe(src="/static/Twitter_map/de_maps_twitter/qgis_syd/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100, 'marginRight': 100, 'marginBottom': 100})
                    ], className="five columns"),
                ]),
            ])

        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
