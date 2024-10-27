from dash import html, dcc, _dash_renderer
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from charts import pizza, continuous, categoricals, fig_c, fig_e
_dash_renderer._set_react_version("18.2.0")

############################### components ###################################

Comp_A = dbc.Card(
    dbc.CardBody([
        html.H1("Candy Brands"),
        html.P("Visualizing the makeup of different cohorts", className="subtitle")
    ], className="titlecenter"), className="knucklepuck titlewidth"
)

Comp_B = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure={}, id="fig_b", className="height100p")
    ]), className="knucklepuck"
)

Comp_C = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_c, id="fig_c", className="height50p1")
    ]), className="knucklepuck"
)

Comp_D = dbc.Card(
    dbc.CardBody([
        html.Div([
            html.Div([
                html.Div([

                    dmc.Select(
                        label="Select",
                        description="Choose two variables to chart",
                        placeholder= "Ingredient",
                        data=[j for j in continuous if j not in "id"],
                        value=continuous[1],
                        id="dropdown1",
                        w=200,
                        mb=10,
                    )


                ], className="displaythisinline"),
                html.Div([

                    dmc.Select(
                        placeholder= "Ingredient",
                        data=[j for j in continuous if j not in "id"],
                        value=continuous[1],
                        id="dropdown2",
                        w=200,
                        mb=10,
                    )
                ], className="displaythisinline"),
            ], className="selectorleft flexdaddy"),
        ], className="flexdaddy height50p2")
    ]), className="knucklepuck"
)

Comp_DE = dbc.Card(
    dbc.CardBody([
        html.P(
            "This analysis charts cohorts of candy brands. From examining various X-by-Y combinations, it looks like the cohorts sometimes have unique attributes. However, it is difficult to fully segment by all the information in just a 2-D space. ", className="description"
            ),
    ]), className="knucklepuck",
)

Comp_E = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure=fig_e, id="fig_e")
    ]), className="knucklepuck",
)

            # html.Div([
            #     html.P(
            #         "This analysis examines composition of ingredients, by pizza brand. By charting X vs Y, one can see that there are cluster-like spaces, based on pizza brand, that are distinct."
            #     )
            # ],className="selectorright"),


############################### skeleton ###################################

atf = html.Div([
    html.Div([
        Comp_A
    ]),
    html.Div([
        html.Div([
            Comp_B
        ], className="atf_charts_left"),
        html.Div([
            html.Div([
                Comp_D,
                Comp_DE
            ], className="selector_component"),
            html.Div([
                Comp_C
            ], className="heatmap_chart"),
        ], className="flexdaddy atf_charts_right"),
    ], className="flexdaddy atf_charts"),
], className="flexdaddy biggest")

btf = html.Div([
    Comp_E
])


############################### aggregation ###################################


lyt = dmc.MantineProvider([
    atf,
    btf
])