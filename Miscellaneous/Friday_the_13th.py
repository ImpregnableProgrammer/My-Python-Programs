
def Friday_13th(year):
    referenceYear = 2018
    referenceDays = {'January': 6, 'February': 2, 'March': 2, 'April': 5, 'May': 0, 'June': 3, 'July': 5, 'August': 1, 'September': 4, 'October': 6, 'Novemeber': 2, 'December': 4}
    past = -1 ** (referenceYear > year)
    for year in range(referenceYear + past, year + past, past):
        for month in referenceDays:
            referenceDays[month] = (referenceDays[month] + (1 + 1 * ((year % 4 < 1 and (month != 'January' or month != 'February')) or ((year - past) % 4 < 1 and (month == 'January' or month == 'February')))) * past) % 7
            print(year, month, referenceDays[month])
        print()
    for month in referenceDays:
        if referenceDays[month] % 7 == 5:
            print(month)

Friday_13th(int(input("Enter a year: ")))
        
