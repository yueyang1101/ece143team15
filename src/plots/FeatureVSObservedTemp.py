import numpy as np
import pandas as pd
import plotly.graph_objects as go
from matplotlib import pyplot as plt

def plot_feature_VS_Observed(feature, df, linecolor):
    """
    This function plots the 1880-2004 time series plots for the selected feature and observed earth
    :param
        Input: df -- > The dataframe of each of the features,processed before
               feature --> The feature to compare with observed earth temperature
               linecolor --> The line color for this feature
        Output : the plot of feaure compared with observed earth temperature
    """
    assert isinstance(df,pd.DataFrame)
    assert isinstance(feature,str)
    assert isinstance(linecolor,str)
    
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
                x=df['Year'],
                y=df[feature],
                name=feature,
                line_color=linecolor,
                opacity=1))
    
    fig.add_trace(go.Scatter(
                x=df['Year'],
                y=df['Observed'],
                name="Observed",
                line_color='dimgray',
                opacity=0.5) )
    
    # Use date string to set xaxis range
    fig.update_layout(plot_bgcolor='rgba(0, 0, 0,0)',
                  xaxis_title="1880- 2005",
                    yaxis_title="Average Temp (K)",
                  title_text= feature + " vs Observed",
                 showlegend=True)
 
    fig.show()
