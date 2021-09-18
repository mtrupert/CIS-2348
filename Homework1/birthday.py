# Name: Michael Rupert
# PSID: 1855121

print('Birthday Calculator')
print('Current day')
month = int(input('Month:'))
day = int(input('Day:'))
year = int(input('Year:'))
print('Birthday')
b_month = int(input('Birthday Month:'))
b_day = int(input('Birthday Day:'))
b_year = int(input('Birthday Year:'))
if (b_month == month) and (b_day == day):
    print('Happy Birthday!')

age = year - b_year
print('You are', age, 'old.')