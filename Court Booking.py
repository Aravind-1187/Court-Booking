import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Madras123$",
    database="Court_Booking"
)

mycursor = mydb.cursor()
court = 'badminton'
while (True):

    print('1. Badminton Court')
    n = int(input('Enter index of court: '))
    print()
    if (n == 1):
        court = 'Badminton'
    else:
        break

    print(court.title(), 'Court Booking')

    booking_date = input(
        '\nEnter day of the week to be booked: (Eg: Monday): ').title()
    print('\nAvailable timeslots:\n')
    mycursor.execute("SELECT StartTime, EndTime FROM %s where %s = 'Empty';",
                     court, booking_date)  # Working on this error

    table = mycursor.fetchall()
    for rows in table:
        print(rows[0], rows[1], sep=' to ')
    booking_timeslot = input(
        '\nEnter time of the day to be booked: (Eg: 06:00): ')

    print('Confirming details:')
    print('Chosen day slot:', booking_date)
    print('Chosen time slot:', booking_timeslot)
    ch = input('Confirm booking? (Y/N) ').upper()
    if (ch == 'N'):
        break
    id = input('Enter your ID Number: ').upper()
    name = input('Enter your Name: ')
    if (' ' in name and id[-1] == 'H' and len(id) == 13):
        print('ID Confirmed.')
        mycursor.execute('UPDATE %s SET %s = %s WHERE StartTime = %s',
                         court, booking_date, id, booking_timeslot)
        print('Booking Confirmed.')

    ch = input('Continue booking? (Y/N) ').upper()
    if (ch == 'Y'):
        continue
    else:
        break

print('End of program.')
