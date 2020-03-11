import numpy as np
import pandas as pd
import holoviews as hv
import hvplot.pandas
hv.extension('bokeh')


def plot_TradeCO2_heatmap(tradedata, feature):
    '''
    Plot the heat map
    :param tradedata: a processed data frame
    :param feature: the vairable for the plot
    :return: a heatmap lpot
    '''
    assert isinstance(tradedata, pd.DataFrame)
    assert isinstance(varaiable, str)
    
    newtradedata = tradedata.dropna()
    edata = hv.Dataset(data =newtradedata,kdims=['Entity','Year'])
    
    if feature == 'netCO2':
        %%opts HeatMap [colorbar=True,width=600,height=500,xrotation=60,tools=['hover'], symmetric=True ]( cmap='RdYlBu')
    else: 
        %%opts HeatMap [colorbar=True,width=600,height=500,xrotation=60,tools=['hover']] 
    
    return edata.to(hv.HeatMap,['Year','Entity'],feature, label = feature)
