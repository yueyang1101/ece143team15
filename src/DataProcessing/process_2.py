def process2(df2):
	'''
	This function takes a data frame file and returns a dataframe 
	with migitation values from 2000-2026 for maximum +1.5 Degrees 
	warming.
	:param
		Input: df2 --> The dataframe of the orginal data in the file
						mitigation_curves_1.5C_191203_data.csv which 
						contains historical carbon emissoins data and 
						mitigation curves for 1.5 degrees
		Output: returns a mitigation curves data in a dataframe 
	'''
	assert isinstance(df2,pd.DataFrame)
	import pandas as pd

	indexNames = df2[ df2['Year'] < 1900 ].index
	df2.drop(indexNames , inplace=True)


	df2.to_csv('2_Mitigation_Curves_Data.csv')
