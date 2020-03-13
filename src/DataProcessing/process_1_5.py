import pandas as pd
def process1_5(df15 = pd.read_csv("Data/OriginalData/mitigation_curves_1.5C_191203_data.csv")):
	'''
	This function takes a data frame file and returns a dataframe of 
	historical carbon emissions data and a dataframe with migitation 
	values from 2000-2026 for maximum +1.5 Degrees warming.
	:param
		Input: df15 --> The dataframe of the orginal data in the file
						mitigation_curves_1.5C_191203_data.csv which 
						contains historical carbon emissoins data and 
						mitigation curves for 1.5 degrees
		Output: a list with just the historical data dataframe and 
				mitigation curves data in a dataframe
	'''
	assert isinstance(df15,pd.DataFrame)


	indexNames = df15[ df15['Year'] < 1900 ].index
	df15.drop(indexNames , inplace=True)

	df_historical_data = df15[['Year','Historical']]

	df_historical_data.to_csv('Data/FinalData/Historical_CO2_Emissions_Data.csv')

	df15.to_csv('Data/FinalData/1.5_Mitigation_Curves_Data.csv')

	return [df_historical_data, df15]
process1_5()
