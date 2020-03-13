def plot(csvaddress, countryname):
    """
    @Author: Haoyang Ding
    plot 6 countrys' co2 emission and gdp trends
    :param csvaddress: file address, string
    :param countryname: country name, string
    :return: None
    """
    assert isinstance(csvaddress, str)
    assert isinstance(countryname, str)

    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import os

    df = pd.read_csv(csvaddress)
    sns.set(style="white")
    fig, ax = plt.subplots()
    fig.set_size_inches(15, 10)
    ax2 = ax.twinx()

    sns.set(color_codes=True)
    yco2name = countryname + " co2 emission"
    ygdpname = countryname + " gdp"

    # United States is too long, change it to USA
    if countryname == "United States":
        countryname = "USA"

    labelco2name = countryname + " co2 emission"
    labelgdpname = countryname + " gdp per capita"
    order1 = 5
    order2 = 2
    xlim1 = 1800
    xlim2 = 2025
    if countryname == "China":
        order1 = 2
        order2 = 2
        xlim1 = 1920
        xlim2 = 2020
    elif countryname == "Germany":
        order1 = 3
        order2 = 2
        xlim1 = 1850
        xlim2 = 2025
    elif countryname == "India":
        order1 = 2
        order2 = 2
        xlim1 = 1875
        xlim2 = 2020
    elif countryname == "Japan":
        order1 = 5
        order2 = 2
        xlim1 = 1870
        xlim2 = 2020
    elif countryname == "Brazil":
        order1 = 2
        order2 = 2
        xlim1 = 1900
        xlim2 = 2020

    sns.regplot(x="year", y=yco2name, data=df, ax=ax, order=order1, color="blue", marker="o",
                label=labelco2name)
    sns.regplot(x="year", y=ygdpname, data=df, ax=ax2, order=order2, color="orange", marker="o",
                label=labelgdpname)
    fig.legend(loc=2, bbox_to_anchor=(0.065, 0.83), prop={'size': 20})

    plt.title(countryname, fontsize=25)
    plt.xlim(xlim1, xlim2)
    ax.set_ylabel(labelco2name, fontsize=25)
    ax2.set_ylabel(labelgdpname, fontsize=25)
    ax.set_xlabel('year', fontsize=25)

    figname = countryname + "co2emission-gdp.png"
    figpath = os.path.abspath(os.path.join(os.getcwd(), "Image/CO2_GDP", figname))
    plt.savefig(figpath, bbox_inches='tight')
    plt.show()
