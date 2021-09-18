# Name: Michael Rupert
# PSID: 1855121

height = int(input('Enter wall height (feet):'"\n"))
width = int(input('Enter wall width (feet):'"\n"))
area = height * width

print('Wall area:', area, 'square feet')

paint = area / 350
print('Paint needed:', '{:.2f}'.format(paint), 'gallons')

paint_can = round(paint)
print('Cans needed:', paint_can, 'can(s)'"\n")

color_prices = {'red': 35, 'blue': 25, 'green': 23}
color_choice = (input('Choose a color to paint the wall:'"\n"))
print('Cost of purchasing', color_choice, 'paint: ${}'.format(color_prices[color_choice] * paint_can))


