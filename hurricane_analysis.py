# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
print("Exercise 1: Clean Damages Data (2)\n")
conversion = {"M": 1000000,
              "B": 1000000000}
updated_damages = []
def update_damage(lst):
  for ea in lst:
    if ea.find("M") != -1:
      ea_float = float(ea.strip("M"))
      ea_float = ea_float * conversion["M"]
      updated_damages.append(ea_float)
    elif ea.find("B") != -1:
      ea_float = float(ea.strip("B"))
      ea_float = ea_float * conversion["B"]
      updated_damages.append(ea_float)
    else:
      updated_damages.append(ea)

# test function by updating damages
update_damage(damages)
print("Cleaned Damages List:\n", updated_damages)
print("\n *** End Exercise 1 *** \n")
# 2
# Create a Table
print("Exercise 2: Create Hurricanes Dictionary (3)\n")
hurricanes = {}
# Create and view the hurricanes dictionary
def populate_hurricanes(lst1, lst2, lst3, lst4, lst5, lst6, lst7):
  counter = 0
  for ea in lst1:
    hurricanes[ea] = {}
    hurricanes[ea]["Name"] = lst1[counter]
    hurricanes[ea]["Month"] = lst2[counter]
    hurricanes[ea]["Year"] = lst3[counter]
    hurricanes[ea]["Max Sustained Wind"] = lst4[counter]
    hurricanes[ea]["Areas Affected"] = lst5[counter]
    hurricanes[ea]["Damage"] = lst6[counter]
    hurricanes[ea]["Death"] = lst7[counter]
    counter +=1

populate_hurricanes(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricanes)
print("\n *** End Exercise 2 *** \n")
# 3
# Organizing by Year
print("Exercise 3: Organise by Year\n")
# create a new dictionary of hurricanes with year and key
hurricanes_by_year = {}

def populate_hurr_year(lst):
  for ea in lst:
    for item in lst[ea]:
      if item == "Year":
        newkey = lst[ea]["Year"]
        newval = lst[ea]
    if hurricanes_by_year.get(newkey) == None:
      hurricanes_by_year[newkey] = [newval]
    else:
      hurricanes_by_year[newkey].append(newval)

populate_hurr_year(hurricanes)
print(hurricanes_by_year)

print("\n *** End Exercise 3 *** \n")
# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
print("Exercise 4: Frequency of Damage (5)\n")
areas_frequency = {}
def populate_frequency(lst):
  areas_raw = []
  for ea in lst:
      for itm in ea:
        areas_raw.append(itm)
  for entry in areas_raw:
    if entry in areas_frequency:
      areas_frequency[entry] += 1
    else:
      areas_frequency[entry] = 1

populate_frequency(areas_affected)
print(areas_frequency)

print("\n *** End Exercise 4 *** \n")

# 5
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
print("Exercise 5: Most Affected Area (6)\n")

def determine_most_affected(lst):
  max_area = "None"
  max_incidence = 0
  for ea in lst:
    #print(lst[ea])
    if lst[ea] > max_incidence:
      max_incidence = lst[ea]
      max_area = ea
  return(print("The most affected area is", max_area, "with an incidence of", max_incidence, "hurricanes."))

determine_most_affected(areas_frequency)

print("\n *** End Exercise 5 *** \n")

# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths
print("Exercise 6: Most Deadly Hurricane (7)\n")

def determine_most_deadly(lst):
  max_deaths = 0
  max_deadly_name = "None"
  for ea in lst.items(): #hurricanes{}
    tmp_death = ea[1]["Death"]
    tmp_name = ea[1]["Name"]
    if tmp_death > max_deaths:
      max_deaths = tmp_death
      max_deadly_name = tmp_name
  return(print("The most deadly hurricane is", max_deadly_name, "with", max_deaths, "deaths."))

determine_most_deadly(hurricanes)

print("\n *** End Exercise 6 *** \n")

# 7
# Rating Hurricanes by Mortality
print("Exercise 7: Hurricane Mortality Ratings (8)\n")
# categorize hurricanes in new dictionary with mortality severity as key
hurricane_mortality = {}
hurricane_mortality[0] = []
hurricane_mortality[1] = []
hurricane_mortality[2] = []
hurricane_mortality[3] = []
hurricane_mortality[4] = []
hurricane_mortality[5] = []

def populate_mortality(lst):
    for ea in lst.items(): #hurricanes{}
      tmp_death = ea[1]["Death"]
      tmp_name = ea[1]["Name"]
      if tmp_death == 0:
        hurricane_mortality[0].append(tmp_name)
      elif tmp_death >0 and tmp_death <= 100:
        hurricane_mortality[1].append(tmp_name)
      elif tmp_death >100 and tmp_death <=500:
        hurricane_mortality[2].append(tmp_name)
      elif tmp_death >500 and tmp_death <=1000:
        hurricane_mortality[3].append(tmp_name)
      elif tmp_death >1000 and tmp_death <=1000:
        hurricane_mortality[4].append(tmp_name)
      elif tmp_death >10000:
        hurricane_mortality[5].append(tmp_name)

populate_mortality(hurricanes)
print(hurricane_mortality)

print("\n *** End Exercise 7 *** \n")
# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost

print("Exercise 8: Most Expensive Hurricane (9)\n")

def determine_most_expensive(lst):
  max_cost = 0.0
  max_cost_name = "None"
  for ea in lst.items(): #hurricanes{}
    tmp_cost = ea[1]["Damage"]
    tmp_name = ea[1]["Name"]
    if tmp_cost == "Damages not recorded":
      continue
    elif tmp_cost > max_cost:
      max_cost = tmp_cost
      max_cost_name = tmp_name
  return(print("The most expensive hurricane is", max_cost_name, "costing", max_cost, "USD."))

determine_most_expensive(hurricanes)

print("\n *** End Exercise 8 *** \n")

# 9
# Rating Hurricanes by Damage

print("Exercise 9: Hurricane Cost Severity Ratings (10)\n")
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

# categorize hurricanes in new dictionary with damage severity as key

hurricane_damage_scale = {}
for k in damage_scale:
    hurricane_damage_scale[k] = []
hurricane_damage_scale[5] = []

def populate_damagescale(lst):
    for ea in lst.items(): #hurricanes{}
      tmp_cost = ea[1]["Damage"]
      tmp_name = ea[1]["Name"]
      if tmp_cost == "Damages not recorded":
        continue
      elif tmp_cost == 0:
        hurricane_damage_scale[0].append(tmp_name)
      elif tmp_cost >0 and tmp_cost <= 100000000:
        hurricane_damage_scale[1].append(tmp_name)
      elif tmp_cost > 100000000 and tmp_cost <= 1000000000:
        hurricane_damage_scale[2].append(tmp_name)
      elif tmp_cost > 1000000000 and tmp_cost <= 10000000000:
        hurricane_damage_scale[3].append(tmp_name)
      elif tmp_cost > 10000000000 and tmp_cost <= 100000000000:
        hurricane_damage_scale[4].append(tmp_name)
      elif tmp_cost > 50000000000:
        hurricane_damage_scale[5].append(tmp_name)

populate_damagescale(hurricanes)
print(hurricane_damage_scale)

print("\n *** End Exercise 9 *** \n")
