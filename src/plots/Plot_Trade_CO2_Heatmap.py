import numpy as np
import pandas as pd
import holoviews as hv
import hvplot.pandas
from holoviews.ipython.magics import OptsMagic


def plot_TradeCO2_heatmap(tradedata, feature):
    '''
    Plot the heat map
    :param tradedata: a processed data frame
    :param feature: the vairable for the plot
    :return: a heatmap lpot
    '''
    assert isinstance(tradedata, pd.DataFrame)
    assert isinstance(feature, str)
    
    newtradedata = tradedata.dropna()
    
    edata = hv.Dataset(data =newtradedata,kdims=['Entity','Year'])
    
    om = OptsMagic()
    
    
    return edata.to(hv.HeatMap,['Year','Entity'],feature, label = feature)
