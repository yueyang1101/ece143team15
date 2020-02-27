import geopandas as gpd
import pandas as pd
from bokeh.io import output_notebook, show, output_file, export_png
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar
from bokeh.palettes import brewer
import json
import os
import imageio
from IPython.display import HTML
import random

shapefile = 'data/countryshapes/ne_110m_admin_0_countries.shp'
# Read shapefile using Geopandas
gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]
# Rename columns.
gdf.columns = ['country', 'country_code', 'geometry']
# import temperature dataset
datafile = 'data/temperature/hadcrut-surface-temperature-anomaly.csv'
df = pd.read_csv(datafile, names=['country', 'code', 'year', 'temperature'], skiprows=1)


def get_figure(year: int):
    '''
    create bokeh figure object
    :param year: year
    :return: figure
    '''
    df_year = df[df['year'] == year]
    # Merge dataframes gdf and df_2016.
    merged = gdf.merge(df_year, left_on='country_code', right_on='code')

    # Read data to json.
    merged_json = json.loads(merged.to_json())
    # Convert to String like object.
    json_data = json.dumps(merged_json)

    # Input GeoJSON source that contains features for plotting.
    geosource = GeoJSONDataSource(geojson=json_data)
    # Define a sequential multi-hue color palette.
    palette = brewer['RdBu'][11]
    # Reverse color order so that dark blue is highest obesity.
    # Instantiate LinearColorMapper that linearly maps numbers in a range, into a sequence of colors.
    color_mapper = LinearColorMapper(palette=palette, low=-2, high=2)
    # Define custom tick labels for color bar.
    tick_labels = {'0': '0°C',
                   '-0.5': '-0.5°C',
                   '-1': '-1°C',
                   '-1.5': '-1.5°C',
                   '-2': '-2°C',
                   '0.5': '0.5°C',
                   '1': '1°C',
                   '1.5': '1.5°C',
                   '2': '2°C'}
    # Create color bar.
    color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8, width=500, height=20,
                         border_line_color=None, location=(0, 0), orientation='horizontal',
                         major_label_overrides=tick_labels)
    # Create figure object.
    p = figure(title='Surface temperature anomaly (degrees celcius), ' + str(year), plot_height=600, plot_width=950,
               toolbar_location=None)
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    # Add patch renderer to figure.
    p.patches('xs', 'ys', source=geosource, fill_color={'field': 'temperature', 'transform': color_mapper},
              line_color='black', line_width=0.25, fill_alpha=1)
    # Specify figure layout.
    p.add_layout(color_bar, 'below')
    return p


def save_figure(year: int, filename: str):
    '''
    save figure to filename
    :param year: int
    :param filename: str
    :return: 
    '''
    p = get_figure(year)
    export_png(p, filename=filename)


def show_figure(year: int):
    '''
    show figure in ipython
    :param year: int
    :return: void
    '''
    p = get_figure(year)
    output_notebook()
    show(p)


def generate_gif(plots_directory: str, file_path: str, start: int, end: int, step: int = 1, fps: int = 5):
    '''
    geterate gif from plots
    :param plots_directory: str path
    :param file_path: str path
    :param start: start year
    :param end: end year
    :param step: step of year between gif
    :param fps: fps of gif
    :return: 
    '''
    file_names = sorted((fn for fn in os.listdir(plots_directory) if fn.endswith('png')))
    images = []
    count = 0
    for filename in file_names:
        year = int(filename.split('.')[0])
        if year >= start and year <= end:
            if count == step:
                count = 0
            if count == 0:
                images.append(imageio.imread(plots_directory + filename))
            count += 1
    imageio.mimsave(file_path, images, fps=fps)


def show_gif(file_path):
    '''
    show gif in ipython
    :param file_path: gif file path
    :return: 
    '''
    return HTML('<img src="' + file_path + '?invalidateCache=' + str(random.random()) + '">')