def dictproducer(sheet):
    """
    @Author Haoyang Ding
    produce a dictionary, key: year, value: data
    using in co2concentration_tem.py
    :param sheet: read the xlsx file as a sheet
    :return: dict[year]=data
    """
    temp = {}
    for i in range(1, sheet.nrows):
        row = sheet.row_values(i)
        temp[row[2]] = row[3]
    return temp


def dictproducer_co2emi(sheet):
    """
    @Author Haoyang Ding
    calculate the global cow emission in each year
    need to do a sum in this function
    :param sheet:
    :return: dict[year]=data
    """
    temp = {}
    for i in range(1, sheet.nrows):
        row = sheet.row_values(i)
        if (row[2] not in temp.keys()):
            temp[row[2]] = 0
        temp[row[2]] += row[3]  # sum the co2 emission data from different countries in the same year
    return temp


def dictproducer_country(sheet):
    """
    @Author Haoyang Ding
    return a dictionary like this: dict[country]={year: data}
    :param sheet:
    :return: {country: {year: data}}
    """
    temp = {}
    for i in range(1, sheet.nrows):
        row = sheet.row_values(i)
        if (row[0] not in temp.keys()):
            temp[row[0]] = {}
        temp[row[0]][row[2]] = row[3]
    return temp
