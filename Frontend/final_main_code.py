import dash
import dash_html_components as html
import dash_core_components as dcc
import db as db

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config['suppress_callback_exceptions'] = True
# main data
lang_ms = db.key_ms[::2]
value_ms = db.key_ms[1::2]

lang_syd = db.key_syd[::2]
value_syd = db.key_syd[1::2]

lang_aurin_ms = db.aurin_ms[::2]
value_aurin_ms = db.aurin_ms[1::2]

lang_aurin_syd = db.aurin_syd[::2]
value_aurin_syd = db.aurin_syd[1::2]

# ar
aurin_ms_lang = ['ar_aurin', 'ar_twitter']
aurin_ms_value = [value_aurin_ms[0], value_ms[0]]

aurin_syd_lang = ['ar_aurin', 'ar_twitter']
aurin_syd_value = [value_aurin_syd[0], value_syd[0]]
# it
aurin_ms_lang_it = ['it_aurin', 'it_twitter']
aurin_ms_value_it = [value_aurin_ms[3], value_ms[3]]

aurin_syd_lang_it = ['it_aurin', 'it_twitter']
aurin_syd_value_it = [value_aurin_syd[3], value_syd[3]]
# de
aurin_ms_lang_de = ['de_aurin', 'de_twitter']
aurin_ms_value_de = [value_aurin_ms[1], value_ms[1]]

aurin_syd_lang_de = ['de_aurin', 'de_twitter']
aurin_syd_value_de = [value_aurin_syd[1], value_syd[1]]

##zh
aurin_ms_lang_zh = ['zh_aurin', 'zh_twitter']
aurin_ms_value_zh = [value_aurin_ms[4], value_ms[4]]

aurin_syd_lang_zh = ['zh_aurin', 'zh_twitter']
aurin_syd_value_zh = [value_aurin_syd[4], value_syd[4]]


app.layout =html.Div([
    html.H1("Top Language Comparison", style={'textAlign': 'center',
                                          'color': '#0000ff',
                                          'font-size':50}),
    html.Hr(),
    html.Div(children='Comparison between Melbourne & Sydney based on top four languages other than English', style={
        'textAlign': 'center','font-size':36}),
    html.Hr(),
    dcc.Tabs([
        # first tab
        dcc.Tab(label='Arabic', children=[

            dcc.Graph(
                figure={
                      'data': [{'x': aurin_ms_lang, 'y': aurin_ms_value, 'type': 'bar', 'name': 'Melbourne'},
                               {'x': aurin_syd_lang, 'y': aurin_syd_value, 'type': 'bar', 'name': u'Sydney'}],
                      'layout': {'xaxis': dict(title='Arabic Language From Aurin & Twitter', titlefont=dict(family='Helvetica, monospace', size=20, color='black')),
                                 'yaxis': dict(title='Tweet Count', titlefont=dict(family='Helvetica, monospace', size=20, color='black')),
                                  'autosize':False,
                                  'width':1800,'height':900,
                                  'margin':dict(l=400),
                                  }

                }
            ),
            html.Div(children='Conclusion from the Bar-Graph', style={'font-size':35}),
            html.H4('In this graph, the ratio of the Arabic people in Aurin and twitter data remains constant. According to the Aurin data, the number of Arabic people from Sydney are more than Melbourne which is also proven from the twitter data. ', 
                    style={'textAlign': 'left','font-size':30,'color':'#787d7c'}),
            html.Br(),
             html.Div(children='Conclusion from the Maps', style={'font-size':35}),
            html.H4('All tweets shown comes either from commerical areas or tourist spots. Thus Melbourne sees a good number of Arabic workers as well as tourists.', 
                    style={'textAlign': 'left','font-size':30,'color':'#787d7c'}),
            html.H4('Less Arabic people seem to be populated in Sydney. Who ever are there, seem to be most populated in the busiest areas of Sydney.', style={
                 'textAlign': 'left','font-size':30,'color':'#787d7c'}),
            html.Br(),
            html.Br(),

            ##maps
            html.Div([
                html.Div([
                    html.H3("Melbourne Maps", style={
                        'textAlign': 'center'}),
                    html.Hr(),
                    html.Div([
                        html.H3('Aurin Map',
                                style={'marginLeft': 100,'textAlign':'center'}),
                        html.Iframe(src="/static/melbourne/Arabic/qgis_melb/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100,
                                           'marginRight': 100, 'marginBottom': 100,
                                           'fixedrange': True,
                                           }
                                    ),
                    ], className="five columns"),

                    html.Div([
                        html.H3('Twitter Map',
                                style={'marginLeft': 100,'textAlign':'center'}),
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
                    html.H3("Sydney Maps",style={
                        'textAlign': 'center'}),
                    html.Hr(),
                    html.Div([
                        html.H3('Aurin Map', style={'marginLeft': 100,'textAlign':'center'}),
                        html.Iframe(src="/static/Sydney/Arabic/qgis_syd/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100, 'marginRight': 100, 'marginBottom': 100})
                    ], className="five columns"),

                    html.Div([
                        html.H3('Twitter Map',
                                style={'marginLeft': 100,'textAlign':'center'}),
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
                                 'yaxis': dict(title='Tweet Count', titlefont=dict(family='Helvetica, monospace', size=20, color='black')),
                                 'autosize':False,
                                  'width':1800,'height':900,
                                  'margin':dict(l=400),
                                 }

                }
            ),
            html.Div(children='Conclusion from the Bar-Graph', style={'font-size':35}),
            html.H4('Comparing Aurin and Twitter data we can see that number of people speaking Italian in Sydney are more than Melbourne.', style={
                 'textAlign': 'left','font-size':30,'color':'#787d7c'}),
            html.Br(),
             html.Div(children='Conclusion from the Maps', style={'font-size':35}),
            html.H4('Most Italians seems to locate in the commercial areas where it is easier to commute to their work places', style={
                 'textAlign': 'left','font-size':30,'color':'#787d7c'}),
            html.H4('Most of the data comes from the areas where you would find either offices or colleges which are in the centre in Sydney', style={
                 'textAlign': 'left','font-size':30,'color':'#787d7c'}),
            html.Br(),
            html.Br(),

            html.Div([
                html.Div([
                    html.H3("Melbourne Maps", style={
                        'textAlign': 'center'}),
                    html.Hr(),
                    html.Div([
                        html.H3('Aurin Map', style={'marginLeft': 100,'textAlign':'center'}),
                        html.Iframe(src="/static/melbourne/Italian/qgis_melb/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100,
                                           'marginRight': 100, 'marginBottom': 100}

                                    ),
                    ], className="five columns"),

                    html.Div([
                        html.H3('Twitter Map',
                                style={'marginLeft': 100,'textAlign':'center'}),
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
                        html.H3('Aurin Map', style={'marginLeft': 100,'textAlign':'center'}),
                        html.Iframe(src="/static/Sydney/Italian/qgis_syd/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100, 'marginRight': 100, 'marginBottom': 100})
                    ], className="five columns"),

                    html.Div([
                        html.H3('Twitter Map',
                                style={'marginLeft': 100,'textAlign':'center'}),
                        html.Iframe(src="/static/Twitter_map/it_maps_twitter/qgis_syd/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100, 'marginRight': 100, 'marginBottom': 100})
                    ], className="five columns"),
                ]),
            ])

        ]),
        # third tab
        dcc.Tab(label='German', children=[

            dcc.Graph(
                figure={
                      'data': [{'x': aurin_ms_lang_de, 'y': aurin_ms_value_de, 'type': 'bar', 'name': 'Melbourne'},
                               {'x': aurin_syd_lang_de, 'y': aurin_syd_value_de, 'type': 'bar', 'name': u'Sydney'}],
                      'layout': {'xaxis': dict(title='German Language From Aurin & Twitter', titlefont=dict(family='Helvetica, monospace', size=20, color='black')),
                                 'yaxis': dict(title='Tweet Count', titlefont=dict(family='Helvetica, monospace', size=20, color='black')),
                                 'autosize':False,
                                  'width':1800,'height':900,
                                  'margin':dict(l=400),
                                 }

                }
            ),
            html.Br(),
            html.Div(children='Conclusion from the Bar-Graph', style={'font-size':35}),
            html.H4('Comparing the number of German people in Melbourne & Sydney, we notice that the number has increased in Sydney but has decreased in Melbourne', style={
                 'textAlign': 'left','font-size':30,'color':'#787d7c'}),
            html.Br(),
             html.Div(children='Conclusion from the Maps', style={'font-size':35}),
            html.H4('As seen from both the maps, german tweets seem to be populated around central Melbourne.', style={
                 'textAlign': 'left','font-size':30,'color':'#787d7c'}),
            html.H4('For Sydney,the tweets seem to be denser in the inner suburbs and seem to get lower as we move towards the outer suburbs.', style={
                 'textAlign': 'left','font-size':30,'color':'#787d7c'}),
            html.Br(),
            html.Br(),

            html.Div([
                html.Div([
                    html.H3("Melbourne Maps", style={
                        'textAlign': 'center'}),
                    html.Hr(),
                    html.Div([
                        html.H3('Aurin Map',
                                style={'marginLeft': 100,'textAlign':'center'}),
                        html.Iframe(src="/static/melbourne/German/qgis_melb/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100,
                                           'marginRight': 100, 'marginBottom': 100}

                                    ),
                    ], className="five columns"),

                    html.Div([
                        html.H3('Twitter Map',
                                style={'marginLeft': 100,'textAlign':'center'}),
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
                        html.H3('Aurin Map', style={'marginLeft': 100,'textAlign':'center'}),
                        html.Iframe(src="/static/Sydney/German/qgis_syd/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100, 'marginRight': 100, 'marginBottom': 100})
                    ], className="five columns"),

                    html.Div([
                        html.H3('Twitter Map',
                                style={'marginLeft': 100,'textAlign':'center'}),
                        html.Iframe(src="/static/Twitter_map/de_maps_twitter/qgis_syd/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100, 'marginRight': 100, 'marginBottom': 100})
                    ], className="five columns"),
                ]),
            ])

        ]),
        ##fourth tab
        dcc.Tab(label='Chinese', children=[

            dcc.Graph(
                figure={
                      'data': [{'x': aurin_ms_lang_zh, 'y': aurin_ms_value_zh, 'type': 'bar', 'name': 'Melbourne'},
                               {'x': aurin_syd_lang_zh, 'y': aurin_syd_value_zh, 'type': 'bar', 'name': u'Sydney'}],
                      'layout': {'xaxis': dict(title='Chinese Language From Aurin & Twitter', titlefont=dict(family='Helvetica, monospace', size=20, color='black')),
                                 'yaxis': dict(title='Tweet Count', titlefont=dict(family='Helvetica, monospace', size=20, color='black')),
                                 'autosize':False,
                                  'width':1800,'height':900,
                                  'margin':dict(l=400),
                                 }

                }
            ),
            html.Br(),
            html.Div(children='Conclusion from the Bar-Graph', style={'font-size':35}),
            html.H4('The number of Chinese speaking people in Melbourne is almost the same as the past data but there is a drastic reduction between the past and present data of Sydney.', style={
                 'textAlign': 'left','font-size':30,'color':'#787d7c'}),
            html.Br(),
             html.Div(children='Conclusion from the Maps', style={'font-size':35}),
            html.H4('All Chinese speaking people in the Aurin data seem to be located everywhere in the Melbourne but in the twitter data the Chinese people seem to move from the outer suburbs to the central area of the city.', style={
                 'textAlign': 'left','font-size':30,'color':'#787d7c'}),
            html.H4(' For Sydney, we just have one coordinate location which seems to be coming from the area which is one of the denser areas of the Aurin maps.', style={
                 'textAlign': 'left','font-size':30,'color':'#787d7c'}),
            html.Br(),
            html.Br(),

            html.Div([
                html.Div([
                    html.H3("Melbourne Maps", style={
                        'textAlign': 'center'}),
                    html.Hr(),
                    html.Div([
                        html.H3('Aurin Map',
                                style={'marginLeft': 100,'textAlign':'center'}),
                        html.Iframe(src="/static/melbourne/Chinese/qgis_melb/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100,
                                           'marginRight': 100, 'marginBottom': 100}

                                    ),
                    ], className="five columns"),

                    html.Div([
                        html.H3('Twitter Map',
                                style={'marginLeft': 100,'textAlign':'center'}),
                        html.Iframe(src="/static/Twitter_map/zh_maps_twitter/qgis_melb/index.html",
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
                        html.H3('Aurin Map', style={'marginLeft': 100,'textAlign':'center'}),
                        html.Iframe(src="/static/Sydney/Chinese/qgis_syd/index.html",
                                    height='700px', width='700px',
                                    style={'marginLeft': 100, 'marginRight': 100, 'marginBottom': 100})
                    ], className="five columns"),

                    html.Div([
                        html.H3('Twitter Map',
                                style={'marginLeft': 100,'textAlign':'center'}),
                        html.Iframe(src="/static/Twitter_map/zh_maps_twitter/qgis_syd/index.html",
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
