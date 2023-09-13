import csv


court = 'Badminton Court.csv'
ch = 'Y'
list_index = 0
days = ['MONDAY', 'TUESDAY', 'WEDNESDAY',
        'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

while (ch == 'Y'):
    with open(court) as csvfile:
        csvreader = csv.reader(csvfile)
        court = court.rstrip('.csv')
        print(court, 'Booking')

        booking_date = input(
            '\nEnter day of the week to be booked: (Eg: Monday): ')
        list_index = days.index(booking_date.upper())
        day_index = list_index+2
        print('\nAvailable timeslots:\n')
        for row_list in csvreader:
            if (row_list[day_index] == 'Empty'):
                print(row_list[0], 'to', row_list[1])
        booking_start_time = input(
            '\nEnter time of the day to be booked: (Eg: 06:00): ')
        booking_time_int = int(
            booking_start_time[0:2])*100 + int(booking_start_time[3:])

        print('Confirming details:')
        print('Chosen day slot:', booking_date.title())
        print('Chosen time slot:', booking_start_time)
        ch = input('Confirm booking? (Y/N) ').upper()
        if (ch == 'N'):
            break
        id = input('Enter your ID Number: ').upper()
        name = input('Enter your Name: ')
        if (' ' in name and id[-1] == 'H' and len(id) == 13):
            print('Booking Confirmed')

    ch = input('Continue booking? (Y/N) ').upper()
    if (ch == 'N'):
        break
    print('1. Badminton Court')
    n = int(input('Enter index of court: '))
    if (n == 1):
        court = 'Badminton Court.csv'
    else:
        ch = 'N'
