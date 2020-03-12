import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
degree = u'\N{DEGREE SIGN}'

df2 = pd.read_csv("mitigation_curves_2.0C_191203_data.csv")
indexNames = df2[ df2['Year'] < 1900 ].index
df2.drop(indexNames , inplace=True)

df_historical_data = df2[['Year','Historical']]

data_dict = {}
for i in range(2000,2027):
	data_dict[i] = df2[['Year',str(i)]]


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

plt.title('CO2 Emission Mitigation Curves to Limit Warming to 2'+ degree + 'C by 2100')
plt.show()
#anim.save('animation.gif', writer='imagemagick', fps=4)