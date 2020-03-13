def co2concentration_tem(nameco2, nametem):
    """
    @Author Haoyang Ding
    Produce the clean co2concentration-temperature data for visualization
    produce a csv file in "visualization" folder
    :param nameco2: co2-concentration-long-term.xlsx
    :param nametem: temperature-anomaly.xlsx
    :return: None
    """
    assert isinstance(nameco2, str)
    assert isinstance(nametem, str)

    import xlrd
    import pandas as pd
    import os
    import dictproducer
    # read files
    # fileaddress is the Outermost file directory
    fileaddress = os.path.abspath(os.path.join(os.getcwd(), "../../.."))
    co2address = os.path.join(fileaddress, "Data\OriginalData", nameco2)
    temaddress = os.path.join(fileaddress, "Data\OriginalData", nametem)
    fileco2 = xlrd.open_workbook(filename=co2address)
    filetem = xlrd.open_workbook(filename=temaddress)

    sheetco2 = fileco2.sheet_by_index(0)
    sheettem = filetem.sheet_by_index(0)

    globaltem = {}
    globalco2 = dictproducer.dictproducer(sheetco2)
    temp = dictproducer.dictproducer(sheettem)

    # we need to find the relationship between last year's co2 concentration and this year's temperature
    # so we need to clean the global temperature data
    for i in range(len(globalco2)):
        year = list(globalco2.keys())[i]
        if year + 1 in temp.keys():
            globaltem[year] = temp[year + 1]

    globalco2.popitem()  # we do not have temperature data for 2020, so we do not need co2 concentration data for 2019

    df = pd.DataFrame({"year": list(globaltem.keys()),
                       "co2 concentration": list(globalco2.values()),
                       "temperature anomaly": list(globaltem.values())
                       })

    fileaddress=os.path.join(fileaddress, "Data\VisualizationData\CO2_GDP")
    fileaddress=os.path.abspath(os.path.join(fileaddress, "co2concentration-temperature.csv"))
    df.to_csv(fileaddress)
