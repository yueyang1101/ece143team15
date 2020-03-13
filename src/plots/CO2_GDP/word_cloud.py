def plot(txtaddress):
    """
    @Author: Haoyang Ding
    plot the word cloud image
    :param txtaddress: file address, string
    :return: None
    """

    assert isinstance(txtaddress, str)
    import numpy as np
    from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
    import matplotlib.pyplot as plt
    from PIL import Image
    import os

    f=open(txtaddress).read()
    earthpath=os.path.abspath(os.path.join(os.getcwd(), 'Data\VisualizationData\CO2_GDP', 'Equal_Earth_projection_SW2.jpg'))
    earthfig=np.array(Image.open(earthpath))
    stopwords = set(STOPWORDS)
    stopwords.add("said")
    wordcloud = WordCloud(background_color="white", mask=earthfig, stopwords=stopwords, collocations=False).generate(f)
    fig, axes = plt.subplots(1, 1)
    fig.set_size_inches(55, 50)
    image_colors = ImageColorGenerator(earthfig)
    axes.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    axes.set_axis_off()
    plt.savefig(r'Image\CO2_GDP\wordcloud.jpg', bbox_inches='tight')
    plt.show()
