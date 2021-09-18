# Name: Michael Rupert
# PSID: 1855121

lemon_juice = float(input('Enter amount of lemon juice (in cups):'"\n"))
water = float(input('Enter amount of water (in cups):'"\n"))
agave_nectar = float(input('Enter amount of agave nectar (in cups):'"\n"))
servings = float(input('How many servings does this make?'"\n"))

print("\n"'Lemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(lemon_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave_nectar), 'cup(s) agave nectar'"\n")

servings2 = int(input('How many servings would you like to make?'"\n"))
factor = servings2/servings
mod_lemon = factor * lemon_juice
mod_water = factor * water
mod_agave = factor * agave_nectar

print("\n"'Lemonade ingredients - yields {:.2f}'.format(servings2),'servings')
print('{:.2f}'.format(mod_lemon), 'cup(s) lemon juice')
print('{:.2f}'.format(mod_water), 'cup(s) water')
print('{:.2f}'.format(mod_agave), 'cup(s) agave nectar'"\n")

print('Lemonade ingredients - yields {:.2f}'.format(servings2),'servings')
gallon_lemon = mod_lemon / 16
gallon_water = mod_water / 16
gallon_agave = mod_agave / 16
print('{:.2f}'.format(gallon_lemon), 'gallon(s) lemon juice')
print('{:.2f}'.format(gallon_water), 'gallon(s) water')
print('{:.2f}'.format(gallon_agave), 'gallon(s) agave nectar')



