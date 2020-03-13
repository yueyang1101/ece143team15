
def plot_1_5_animation(df_historical_data, df15):
	'''
	This function plots the historical CO2 Emissions from 1900-2019 &
	plots the mitigation curves from 2000-2026 to meet +1.5C degrees 
	in an animation. The animation is also saved as a GIF.
	:param
		Input:  df_historical_data --> The dataframe of historical CO2 emissions
				df15 --> The dataframe of the mitigation rates for max +1.5C degrees
		Output: Plot of the curves and animated GIF
	'''
	import pandas as pd
	import matplotlib.pyplot as plt
	from matplotlib.animation import FuncAnimation
	degree = u'\N{DEGREE SIGN}'

	data_dict = {}
	for i in range(2000,2027):
		data_dict[i] = df15[['Year',str(i)]]


	fig, ax = plt.subplots()
	ax = plt.axes(xlim=(1900, 2100), ylim=(-5, 45))
	line1, = ax.plot([], [],lw=2, label = 'Year')
	line2, = ax.plot([], [],lw=2, label = 'CO2 Emissions (Gigatonnes)')
	year_text = ax.text(0.03, 0.905, '', fontsize = 14, transform=ax.transAxes)


	def init():
		line1.set_data([], [])
		line2.set_data([], [])
		year_text.set_text('')
		return line1, line2, year_text
	def animate(i):
		x = (data_dict[i+2000])['Year']
		y = (data_dict[i+2000])[str(i+2000)]
		line2.set_data(x,y)
		line1.set_data(df_historical_data['Year'], df_historical_data['Historical'])
		year_text.set_text(str(i+2000))


		return line1,line2, year_text

	anim = FuncAnimation(fig, animate, frames=len(data_dict), init_func=init, interval=200, blit=True)

	plt.xlabel('Year')
	plt.ylabel('CO2 Emissions (Gigatonnes)')

	plt.title('CO2 Emission Mitigation Curves to Limit Warming to 1.5'+ degree + 'C by 2100')
	plt.show()
	anim.save('1.5 Degrees Mitigation.gif', writer='imagemagick', fps=4)

def plot_1_5_2020(df_historical_data, df15):
	'''
	This function plots the historical CO2 Emissions from 1900-2019 &
	plots the mitigation curve starting at the beginning of 2020 to 
	meet +1.5C degrees.
	:param
		Input:  df_historical_data --> The dataframe of historical CO2 emissions
				df15 --> The dataframe of the mitigation rates for max +1.5C degrees
		Output: Plot of the curves on the same figure.
	'''
	import pandas as pd
	import matplotlib.pyplot as plt
	from matplotlib.animation import FuncAnimation
	degree = u'\N{DEGREE SIGN}'

	data_dict = {}
	for i in range(2000,2027):
		data_dict[i] = df15[['Year',str(i)]]
	ax = plt.gca()
	size = (20,15)
	df_historical_data.plot(kind='line',x='Year',y='Historical',ax=ax, color = [(0.3647058823,0.73725490196,0.82352941176)], legend = None, figsize = size,linewidth=2)
	data_dict[2019].plot(kind='line',x='Year',y=str(2019),ax=ax, color = 'red', legend = None, figsize = size,linewidth=2)
	plt.xticks(range(1900,2120,20))
	plt.xlabel('Year')
	plt.ylabel('CO2 Emissions (Gigatonnes)')
	plt.figure(1)
	plt.show()

