import co2concentration_tem
import co2emission_tem
import correlationdata
import treemapdata

if __name__ == '__main__':
    """
    @Author Haoyang Ding
    main function
    generate data files for visualization
    """
    nameco2 = "co2-concentration-long-term.xlsx"
    nametem = "temperature-anomaly.xlsx"
    nameco2emi = "annual-co-emissions-by-region.xlsx"
    namegdp = "average-real-gdp-per-capita-across-countries-and-regions.xlsx"

    developed=["United States", "Japan", "United Kingdom", "Germany", "France", "Italy", "Canada", "Switzerland", "Belgium", "Netherlands", "Finland", "Norway", "Denmark", "Sweden", "Greece", "Iceland", "Portugal", "Spain", "Austria", "Australia", "Ireland", "South Africa"]
    developing=["Argentina", "Malaysia", "Panama", "Israel", "Sri Lanka", "Vietnam", "Cyprus", "Czechoslovakia", "Chile", "Greece", "Peru", "Nepal", "Egypt", "China", "South Korea", "Thailand", "Turkey", "Brazil", "India", "Philippines", "North Korea", "Bolivia"]

    co2concentration_tem.co2concentration_tem(nameco2, nametem)
    co2emission_tem.co2emission_tem(nameco2emi, nametem)
    correlationdata.correlationdata(nameco2emi, namegdp, developed, developing)

    africa = ["AFRICA", "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Cape Verde",
              "Central African Republic", "Chad", "Comoros", "Republic of the Congo",
              "Democratic Republic of the Congo", "Ivory Coast", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea",
              "Ethiopia", "Gabon", "The Gambia", "Ghana", "Guinea", "Guinea Bissau", "Kenya", "Lesotho", "Liberia",
              "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia",
              "Niger", "Nigeria", "Rwanda", "São Tomé and Príncipe", "Senegal", "Seychelles", "Sierra Leone", "Somalia",
              "South Africa", "South Sudan", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda",
              "Western Sahara", "Zambia", "Zimbabwe"]
    asia = ["ASIA", "Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia",
            "China", "Cyprus", "Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan",
            "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar",
            "Nepal", "North Korea", "Oman", "Pakistan", "Palestine", "Philippines", "Qatar", "Saudi Arabia",
            "Singapore", "South Korea", "Sri Lanka", "Syria", "Tajikistan", "Thailand", "Turkey", "Turkmenistan",
            "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"]
    europe = ["EUROPE", "Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria",
              "Croatia", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary",
              "Iceland", "Ireland", "Italy", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg",
              "North Macedonia", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "Norway", "Poland",
              "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden",
              "Switzerland", "Ukraine", "United Kingdom", "Vatican City"]
    na = ["NA", "Antigua and Barbuda", "Anguilla", "Aruba", "The Bahamas", "Barbados", "Belize", "Bermuda", "Bonaire",
          "British Virgin Islands", "Canada", "Cayman Islands", "Clipperton Island", "Costa Rica", "Cuba", "Curaçao",
          "Dominica", "Dominican Republic", "El Salvador", "Greenland", "Grenada", "Guadeloupe", "Guatemala", "Haiti",
          "Honduras", "Jamaica", "Martinique", "Mexico", "Montserrat", "Navassa Island", "Nicaragua", "Panama",
          "Puerto Rico", "Saba", "Saint Barthelemy", "Saint Kitts and Nevis", "Saint Lucia", "Saint Martin",
          "Saint Pierre and Miquelon", "Saint Vincent and the Grenadines", "Sint Eustatius", "Sint Maarten",
          "Trinidad and Tobago", "Turks and Caicos", "United States"]
    sa = ["SA", "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "French Guiana",
          "Guyana", "Paraguay", "Peru", "South Georgia and the South Sandwich Islands", "Suriname", "Uruguay",
          "Venezuela"]
    oceania = ["OCEANIA", "Australia", "Federated States of Micronesia", "Fiji", "Kiribati", "Marshall Islands",
               "Nauru", "New Zealand", "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu",
               "Vanuatu"]

    treemapdata.treemapdata(africa, asia, europe, na, sa, oceania)
