def plot(txtaddress, filepath):
    """
    @Author: Haoyang Ding
    plot the interactive treemap html
    :param txtaddress: txt file address, string
    :return: None
    """

    from pyecharts import TreeMap

    f = open(txtaddress, 'r')
    a = f.read()
    tree = eval(a)
    f.close()

    counter = 0
    for i in range(len(tree)):
        counter += tree[i]["value"]

    for i in range(len(tree)):
        tree[i]["value"] = tree[i]["value"] / counter

    # change the ratio from region to global
    for i in tree:
        for j in i["children"]:
            j["value"] = j["value"] * i["value"]
    bcounter = round(counter / pow(10, 9))

    def label(params):
        return params.name + "\n" + window.parseFloat(params.value * 100).toFixed(2) + r"%" + " " + "co2 emission"

    treemap = TreeMap(width=800, height=800, title_text_size=24, is_animation=True, renderer="canvas")
    treemap.add("Co2 emission in 10 years", tree, is_random=False, is_legend_show=True
                , line_opacity=0.5
                , is_label_show=True
                , label_pos="inside"
                , legend_orient="vertical"
                , label_formatter=label
                , is_more_utils=True
                , label_text_size=24)
    treemap.render(path=filepath)