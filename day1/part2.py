import math

def calculate_fuel(mass):
  fuel_required = math.floor(mass/3)-2
  if fuel_required <= 0:
    return 0
  else:
    return fuel_required + calculate_fuel(fuel_required)

sum = 0
with open('input.txt','r') as file:
  for raw_value in file.readlines():
    if not raw_value:
      continue
    value = int(raw_value.strip())
    sum += calculate_fuel(value)

print(sum)