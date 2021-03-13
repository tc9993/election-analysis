counties = ["Arapahoe","Denver","Jefferson"]

if 'El Paso' in counties:
    print('El Paso is in the list of counties')
else:
    print('El Paso is NOT in the list of counties')

if 'Arapahoe' in counties or 'El Paso' in counties:
    print("One or both are in the list of counties")
else:
    print('One or both are NOT in the list of counties')

if 'Arapahoe' in counties and 'El Paso' not in counties:
    print('Only Arapahoe is in the list of counties')
else:
    print('Arapahoe is in the list of counties and El Paso is not in the list')


for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

print(len(counties))

counties_tuple = ("Arapahoe","Denver","Jefferson")

for i in range(len(counties_tuple)):
    print(counties_tuple[i])

for county in counties_tuple:
    print(county)