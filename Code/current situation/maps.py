import plotly.express as px
from dataset_info import case

palette = ["#FFC300", "#9D0208", "#1E2328"]


def draw_map(continent):
    print("Monkeypox origins in " + continent + " :")

    fig = px.choropleth(data_frame=case,
                        locations="Country",
                        locationmode="country names",
                        color="Confirmed_Cases",
                        color_continuous_scale=palette,
                        height=600,
                        scope=str.lower(continent),
                        labels={"Confirmed_Cases": "Confirmed Cases"})

    title = "Origins of Confirmed Monkeypox Cases in " + continent
    fig.update_layout(title={"text": title,
                             "y": 0.95,
                             "x": 0.5,
                             "xanchor": "center",
                             "yanchor": "top"})
    fig.show()


# uncomment to see the corresponding map
# draw_map("Asia")
# draw_map("Africa")
# draw_map("Europe")
# draw_map("North America")
# draw_map("South America")
draw_map("world")
