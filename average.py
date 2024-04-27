difference = 0
def average(first_number, second_number):
    if first_number > second_number:
        difference = first_number - second_number
    elif first_number < second_number:
        difference = second_number - first_number
    else:
        difference = 0
