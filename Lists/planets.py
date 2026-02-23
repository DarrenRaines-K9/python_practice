planet_list = ['Mercury', 'Venus', 'Earth']

def add_planet(planet):
    planet_list.append(planet)
    print(f"Planet '{planet}' added.")

def add_planets(planets):
    planet_list.extend(planets)
    print(f"Planets '{', '.join(planets)}' added.")

def insert_planet(index, planet):
    planet_list.insert(index, planet)
    print(f"Planet '{planet}' inserted at index {index}.")

def remove_planet(planet):
    if planet in planet_list:
        planet_list.remove(planet)
        print(f"Planet '{planet}' removed.")
    else:
        print(f"Planet '{planet}' not found.")

add_planet('Mars')
add_planets(['Jupiter', 'Saturn'])
insert_planet(2, 'Venus')

def display_planets():
    print("Planets in the list:")
    for planet in planet_list:
        print(f"- {planet}")

display_planets()

def rocky_planets():
    planets = []

    for planet in planet_list:
        if planet in ['Mercury', 'Venus', 'Earth', 'Mars']:
            planets.append(planet)
    return planets

rocky_planetslist = rocky_planets() 
print("Rocky Planets:")
for planet in rocky_planetslist:
    print(f"- {planet}")

# List of spacecraft and the planets they visited
spacecraft = [
    ("Mariner 10", ["Mercury", "Venus"]),
    ("MESSENGER", ["Mercury", "Venus"]),
    ("Venera 1-16", ["Venus"]),
    ("Mariner 2", ["Venus"]),
    ("Mariner 5", ["Venus"]),
    ("Pioneer Venus 1 and 2", ["Venus"]),
    ("Vega 1 and 2", ["Venus"]),
    ("Magellan", ["Venus"]),
    ("Venus Express", ["Venus"]),
    ("Parker Solar Probe", ["Venus"]),
    ("Mariner 4", ["Mars"]),
    ("Mariner 6 and 7", ["Mars"]),
    ("Mariner 9", ["Mars"]),
    ("Viking 1 and 2", ["Mars"]),
    ("Mars Pathfinder", ["Mars"]),
    ("Mars Odyssey", ["Mars"]),
    ("Spirit", ["Mars"]),
    ("Opportunity", ["Mars"]),
    ("Phoenix", ["Mars"]),
    ("Dawn", ["Mars"]),
    ("Curiosity", ["Mars"]),
    ("InSight", ["Mars"]),
    ("Perseverance", ["Mars"]),
    ("Pioneer 10 and 11", ["Jupiter"]),
    ("Voyager 1 and 2", ["Jupiter", "Saturn"]),
    ("Ulysses", ["Jupiter"]),
    ("Galileo", ["Venus", "Jupiter"]),
    ("Cassini", ["Venus", "Jupiter", "Saturn"]),
    ("New Horizons", ["Jupiter", "Pluto"]),
    ("Juno", ["Jupiter"]),
    ("Pioneer 11", ["Jupiter", "Saturn"]),
    ("Voyager 2", ["Jupiter", "Saturn", "Uranus", "Neptune"]),
]

# Iterate over spacecraft, and for each one, print which planets it visited
for craft, planets in spacecraft:
    print(f"{craft} has visited")
    print("-----------------------")
    for planet in planets:
        print(planet)
    print()  # Add a newline for better readability