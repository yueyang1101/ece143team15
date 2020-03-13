def processFeatures(feature, observed):
    """
    This function takes two data frames files and merge two datasets together
    :param
        Input: feature-- > The dataframe of each of the feature info,  reading it from the CSV final_metric
               observed --> The dataframe of each of the observed earth temperature, reading it from the CSV final_metric
        Output : a dataframe with desired infomation
    """
    assert isinstance(feature,pd.DataFrame)
    assert isinstance(observed, pd.DataFrame)
    
    #select the 1880-2005
    trueyears =  feature['Year'] >= 1880
    nfeature = feature[trueyears]
    trueyear =  observed['Year'] <= 2005
    nobserved  = observed[trueyear]
    
    #get the mean from features
    means = nfeature.mean(axis = 0)
    
    nfeature['avg_solar'] = nfeature['Solar']- means['Solar']
    nfeature['avg_human'] =  nfeature['Human']- means['Human'] 
    nfeature['avg_natural'] = nfeature['Natural']- means['Natural'] 
    nfeature['avg_GHG'] = nfeature['Greenhouse gases']- means['Greenhouse gases'] 
    nfeature['avg_Volcanic'] = nfeature['Volcanic'] - means['Volcanic'] 
    nfeature['avg_land'] = nfeature['Land use']- means['Land use'] 
    nfeature['avg_Orbital'] = nfeature['Orbital changes'] - means['Orbital changes'] 
    nfeature['avg_Ozone'] = nfeature['Ozone']- means['Ozone'] 
    
    nfeature1 = pd.merge(nfeature, nobserved, on='Year')
    
    #generate columns for easier graphing
    nfeature1['Observed']= nfeature1['Annual_Mean'] 
    nfeature1['Solar']= nfeature1['avg_solar'] 
    nfeature1['Volcanic']= nfeature1['avg_Volcanic'] 
    nfeature1['Deforestation']= nfeature1['avg_land'] 
    nfeature1['Ozone']= nfeature1['avg_Ozone'] 
    nfeature1['Greenhouse Gas']= nfeature1['avg_GHG'] 
    
    nfeature1.to_csv('TempFeature.csv') 

    return nfeature1
