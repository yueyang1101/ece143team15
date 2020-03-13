def countrytrend(countryname, co2address, gdpaddress):
    """
    @Author: Haoyang Ding
    Clean the data for Co2-GDP visualization
    :param countryname: The country you need
    :param co2address:  annual-co2-emissions-by-region
    :param gdpaddress: average-real-gdp-percapita-across-countries-and-regions
    :return:
    """

    import xlrd
    import pandas as pd
    import os
    import dictproducer
    import correlationdata

    #co2address=r"C:\Users\74019\Desktop\ece143team15\OriginalData\annual-co-emissions-by-region.xlsx"
    #gdpaddress=r"C:\Users\74019\Desktop\ece143team15\OriginalData\average-real-gdp-per-capita-across-countries-and-regions.xlsx"
    fileco2 = xlrd.open_workbook(filename=co2address)
    filegdp = xlrd.open_workbook(filename=gdpaddress)

    sheetco2 = fileco2.sheet_by_index(0)
    sheetgdp = filegdp.sheet_by_index(0)

    globalco2 = dictproducer.dictproducer_country(sheetco2)
    globalgdp = dictproducer.dictproducer_country(sheetgdp)

    # make sure these two datasets have same countries
    correlationdata.updatecountry(globalco2, globalgdp)
    correlationdata.updatecountry(globalgdp, globalco2)

    correlationdata.updateyear(globalco2, globalgdp)
    correlationdata.updateyear(globalgdp, globalco2)

    countryco2=globalco2[countryname]
    countrygdp=globalgdp[countryname]

    co2str=countryname + " co2 emission"
    gdpstr=countryname + " gdp"

    countrydf=pd.DataFrame({"year": list(countryco2.keys()),
                       co2str: list(countryco2.values()),
                       gdpstr: list(countrygdp.values())
                       })

    fileaddress = os.path.join(os.path.pardir, "VisualizationData")
    filename="\\" + countryname + "-co2-gdp.csv"
    countrydf.to_csv(fileaddress + filename)