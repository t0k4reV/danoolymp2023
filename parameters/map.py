import folium


map = folium.Map()

# Добавление точек на карту


# Волгоград
folium.CircleMarker(
    location=[48.707070, 44.516952],
    radius=0.2739183954054501 * 10,
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(map)

#
folium.CircleMarker(
    location=[51.660782, 39.200286],
    radius=0.3941927342008557 * 10,
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(map)

#
folium.CircleMarker(
    location=[56.838011, 60.597474],
    radius=0.624674309373954 * 10,
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(map)

#
folium.CircleMarker(
    location=[55.796125, 49.106400],
    radius=0.3632577715303158 * 10,
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(map)

#
folium.CircleMarker(
    location=[45.035470, 38.975313],
    radius=1.1489492964592172 * 10,
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(map)


#
folium.CircleMarker(
    location=[56.010552, 92.852531],
    radius=0.3766124274963144 * 10,
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(map)

#
folium.CircleMarker(
    location=[55.755829, 37.617627],
    radius=1.0288225340344523 * 10,
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(map)

#
folium.CircleMarker(
    location=[56.326793, 44.006437],
    radius=0.4409193050722999 * 10,
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(map)

#
folium.CircleMarker(
    location=[55.030280, 82.920383],
    radius=0.875021680112058 * 10,
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(map)

#
folium.CircleMarker(
    location=[54.989362, 73.368037],
    radius=0.4513783897379912 * 10,
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(map)

#
folium.CircleMarker(
    location=[58.010400, 56.229486],
    radius=0.3992855109649682 * 10,
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(map)

#
folium.CircleMarker(
    location=[47.222104,  39.720179],
    radius=0.3071795921806539 * 10,
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(map)

#
folium.CircleMarker(
    location=[53.195878, 50.100202],
    radius=0.4995097532904209 * 10,
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(map)

#
folium.CircleMarker(
    location=[59.938670, 30.314350],
    radius=1.946624664020497 * 10,
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(map)

#
folium.CircleMarker(
    location=[54.735148, 55.958596],
    radius=0.2229747155189327 * 10,
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(map)

#
folium.CircleMarker(
    location=[55.159902, 61.402554],
    radius=0.3129260128347927 * 10,
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(map)


map.save('map.html')