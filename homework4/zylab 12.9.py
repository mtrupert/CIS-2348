#Michael Rupert
#1855121

parts = input().split()
name = parts[0]

while name != '-1':
    try:
        age = int(parts[1]) + 1
        print('{} {}'.format(name, age))
    except ValueError:
        print('{} {}'.format(name, 0))

    parts = input().split()

    name = parts[0]
