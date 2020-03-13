def co2emission_tem(nameco2emi, nametem):
    """
    @Author Haoyang Ding
    Produce the clean co2 emissions-temperature data for visualization
    produce a csv file in "visualization" folder
    :param nameco2: annual-co-emissions-by-region.xlsx
    :param nametem: temperature-anomaly.xlsx
    :return: None
    """
    import xlrd
    import pandas as pd
    import os
    import dictproducer

    fileaddress = os.getcwd()
    co2address = os.path.join(fileaddress, "data", nameco2emi)
    temaddress = os.path.join(fileaddress, "data", nametem)
    fileco2 = xlrd.open_workbook(filename=co2address)
    filetem = xlrd.open_workbook(filename=temaddress)

    sheetco2 = fileco2.sheet_by_index(0)
    sheettem = filetem.sheet_by_index(0)

    globaltem = dictproducer.dictproducer(sheettem)
    temp = dictproducer.dictproducer_co2emi(sheetco2)

    # we need to find the relationship between last year's global co2 emission data and this year's temperature
    # so we need to clean the global co2 emission data (the temperature dataset is smaller than the dataset of co2 emission)

    globalco2emi = {}
    for i in range(len(globaltem)):
        year = list(globaltem.keys())[i]
        if year - 1 in temp.keys():
            globalco2emi[year] = temp[year - 1]

    df = pd.DataFrame({"year": list(globalco2emi.keys()),
                       "global co2 emission": list(globalco2emi.values()),
                       "temperature anomaly": list(globaltem.values())
                       })

    fileaddress = os.path.join(fileaddress, "visualization")
    df.to_csv(fileaddress + "\\co2emission-temperature.csv")
