def plot(csvaddress):
    """
    @Author: Haoyang Ding
    plot 6 countrys' co2 emission and gdp trends
    :param csvaddress: file address
    :return:
    """
    assert isinstance(csvaddress, str)
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    df2=pd.read_csv(csvaddress)
    sns.set(style="white")
    fig, ax=plt.subplots()
    fig.set_size_inches(15, 10)
    ax2=ax.twinx()
    sns.set(color_codes=True)
    sns.regplot(x="year", y="global co2 emission", data=df2, ax=ax, order=2, color="blue", marker="o", label="Global co2 emission")
    sns.regplot(x="year", y="temperature anomaly", data=df2, ax=ax2, order=2, color="orange", marker="o", label="Temperature anomaly")
    fig.legend(loc=2, bbox_to_anchor=(0.065, 0.82), prop = {'size':20})
    a=ax2.set_ylim(-1,1)

    ax.set_ylabel('Global co2 emission',fontsize=25)
    ax2.set_ylabel('Temperature anomaly',fontsize=25)
    ax.set_xlabel('year', fontsize=25)

    plt.savefig(r'Image\CO2_GDP\co2emission-tem.jpg', bbox_inches='tight')
    plt.show()