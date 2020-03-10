import numpy as np
import pandas as pd

def processdata(tradeCO2, countrylist, year):
    '''
    Give the dataset with the given country list and years interested to study
    :param 
        Input: tradeCO2  -- > The dataframe of each of countries Trade CO2, reading it from the CSV final_metric
               countrylist  -- >a list of country names
               year -- > an int for year to study
    Output: :return: a dataframe with interested data information
    '''
    assert isinstance(tradeCO2, pd.DataFrame)
    assert isinstance(countrylist, list)
    assert isinstance(year, int)
    
    
    is_year = tradeCO2['Year'] >= year
    after_year = tradeCO2[is_year]
    interested_country = [item in countrylist  for item in after_year['Entity']]
    countrydata = after_year[interested_country]
    
    return countrydata
