def updatecountry(update, reference):
    """
    make sure the update and reference have the same keys(country)
    :param update: a dict {country: {year: data}}
    :param reference: a dict {country: {year: data}}
    :return: None
    """
    for i in list(update.keys()):
        if i not in list(reference.keys()):
            update.pop(i)


def updateyear(update, reference):
    """
    make sure each value in update and reference has the same keys(year)
    :param update: a dict {country: {year: data}}
    :param reference: a dict {country: {year: data}}
    :return: None
    """
    for i in list(update.keys()):
        temp1 = update[i]
        temp2 = reference[i]
        for j in list(temp1.keys()):
            if j not in temp2.keys() or temp1[j] == 0:
                temp1.pop(j)
        update[i] = temp1


def tempdata(data):
    """
    change the data style from {country: {year: data}} to {country: [data]}
    :param data: a dict {country: {year: data}}
    :return: a dict {country: [data]}
    """
    temp = {}
    for i in list(data.keys()):
        temp[i] = []
        for j in list(data[i].keys()):
            temp[i].append(data[i][j])
    return temp


def correlationdata(nameco2emi, namegdp):
    """
    calculate the correlation between co2 emission and gdp per capita of each country
    And write a file according to the correlation data of each country
    the file will be used for plotting word-cloud
    :param nameco2emi: annual-co-emissions-by-region.xlsx
    :param namegdp: average-real-gdp-per-capita-across-countries-and-regions.xlsx
    :return:
    """
    import xlrd
    import pandas as pd
    import os
    import dictproducer

    fileaddress = os.getcwd()
    co2address = os.path.join(fileaddress, "data", nameco2emi)
    gdpaddress = os.path.join(fileaddress, "data", namegdp)
    fileco2 = xlrd.open_workbook(filename=co2address)
    filegdp = xlrd.open_workbook(filename=gdpaddress)

    sheetco2 = fileco2.sheet_by_index(0)
    sheetgdp = filegdp.sheet_by_index(0)

    globalco2 = dictproducer.dictproducer_country(sheetco2)
    globalgdp = dictproducer.dictproducer_country(sheetgdp)

    # make sure these two datasets have same countries
    updatecountry(globalco2, globalgdp)
    updatecountry(globalgdp, globalco2)

    faddress = os.path.join(fileaddress, "visualization")
    f = open(faddress + "\\cleanglobalco2.txt", "w")
    f.write(str(globalco2))
    f.close()

    # make sure every country's data has same years
    updateyear(globalco2, globalgdp)
    updateyear(globalgdp, globalco2)

    # now the country and year are same
    # I want to calculate the correlation rate between the gdppc and co2data per country

    tempco2 = tempdata(globalco2)
    tempgdp = tempdata(globalgdp)

    # now I have two big dict, key: country, value: co2 and gdp per year
    correlation = {}
    correlation = correlation.fromkeys(list(tempco2.keys()))
    correlation.pop("Taiwan")
    correlation.pop("World")
    correlation.pop("Hong Kong")
    for i in list(correlation.keys()):
        temps1 = pd.Series(tempco2[i])
        temps2 = pd.Series(tempgdp[i])
        correlation[i] = temps1.corr(temps2)

    tempsort = sorted(correlation.items(), key=lambda item: item[1])
    corindex = {}

    for i in range(len(tempsort)):
        country = tempsort[i][0]
        tempcountry = country.split()
        country = "".join(tempcountry)
        corindex[country] = i + 1

    f = open(faddress + "\\wordcloud.txt", "w")
    for i in list(corindex.keys()):
        num = corindex[i] * 30
        for j in range(num):
            f.write(str(i))
            f.write(" ")
    f.close()
