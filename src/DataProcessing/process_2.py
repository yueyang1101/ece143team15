import pandas as pd
def process2(df2 = pd.read_csv("Data/OriginalData/mitigation_curves_2.0C_191203_data.csv")):
	'''
	This function takes a data frame file and returns a dataframe 
	with migitation values from 2000-2026 for maximum +2 Degrees 
	warming.
	:param
		Input: df2 --> The dataframe of the orginal data in the file
						mitigation_curves_2.0C_191203_data.csv which 
						contains mitigation curves for 2 degrees
		Output: returns a mitigation curves data in a dataframe 
	'''
	assert isinstance(df2,pd.DataFrame)


	indexNames = df2[ df2['Year'] < 1900 ].index
	df2.drop(indexNames , inplace=True)


	df2.to_csv('Data/VisualizationData/2_Mitigation_Curves_Data.csv')
process2()