def leap_yr(yr):
    return yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0)

def convert_day_to_date(days, yr):
    days_in_months = {
        1: (31, "January"),
        2: (29 if leap_yr(yr) else 28, "February"),
        3: (31, "March"),
        4: (30, "April"),
        5: (31, "May"),
        6: (30, "June"),
        7: (31, "July"),
        8: (31, "August"),
        9: (30, "September"),
        10: (31, "October"),
        11: (30, "November"),
        12: (31, "December"),
    }

    month = 1
    while days > days_in_months[month][0]:
        days -= days_in_months[month][0]
        month += 1
    return f"{days} {days_in_months[month][1]}, {yr}"


input_day = 256
input_year = 2021
output_date = convert_day_to_date(input_day, input_year)
print(output_date)  
