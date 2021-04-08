from datetime import date

# convert string date into date object
def get_date_from_string(input_date : str):
    year, month, day = input_date.split('-')
    formatted_date = date(int(year), int(month), int(day))
    return formatted_date