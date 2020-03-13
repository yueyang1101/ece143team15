def plot(developed, developing):
    """
    @Author: Haoyang Ding
    plot the correlation rate scatter
    :param developed: a DataFrame {"developed countries' name", correlation rate}
    :param developing: a DataFrame {"developing countries' name", correlation rate}
    :return: None
    """
    import pandas as pd
    assert isinstance(developed, pd.DataFrame)
    assert isinstance(developing, pd.DataFrame)

    import matplotlib.pyplot as plt

    developedcountry, developedcorre, y1 = init(developed)
    developingcountry, developingcorre, y2 = init(developing)
    plt.scatter(y1, developedcorre, label="developed country", s=1500)
    plt.scatter(y2, developingcorre, label="developing country", s=1500)

    for i in range(len(y1)):
        plt.annotate(developedcountry[i], xy=(y1[i], developedcorre[i]), xytext=(y1[i] - 15, developedcorre[i] + 0.015),
                     fontsize=60)

    for i in range(len(y2)):
        plt.annotate(developingcountry[i], xy=(y2[i], developingcorre[i]),
                     xytext=(y2[i] - 15, developingcorre[i] + 0.01), fontsize=60)

    plt.title("Correlation between GDP and CO2 emission", fontsize=65)
    plt.legend(loc='lower right', prop={'size': 65})
    plt.rcParams['figure.figsize'] = (55.0, 35.0)
    plt.yticks([])
    plt.xlabel('Countries', fontsize=90)
    plt.ylabel('Correlation rate', fontsize=90)
    plt.rcParams['axes.facecolor'] = 'white'

    plt.savefig(r'Image\CO2_GDP\developed-ing.jpg')
    plt.show()


def init(developed):
    """
    @Author: Haoyang Ding
    init for plotting the correlation rate scatter
    :param developed:
    :return: two lists and a parameter
    """
    import pandas as pd
    assert isinstance(developed, pd.DataFrame)

    developedcountry = developed["country"]
    developedcountry = developedcountry.tolist()

    developedcorre = developed["correlation"]
    developedcorre = developedcorre.tolist()
    developedcorre = list(map(abs, developedcorre))

    y1 = list(range(len(developedcorre)))
    y1 = [item * 27 for item in y1]
    developedcorre = [item * item * item * item * item * item * item * item * item * item for item in developedcorre]

    return developedcountry, developedcorre, y1
