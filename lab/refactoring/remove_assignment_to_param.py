# By Kami Bigdely
# Remove assignment to method parameter.
class Distance:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value


class Mass:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit


def calculate_kinetic_energy(mass: Mass, distance: Distance, time: int) -> float:
    adjusted_distance = Distance(distance.value, distance.unit)
    if distance.unit != 'km':
        if distance.unit == "ly":  # [ly] stands for light-year (measure of distance in astronomy)
            # convert from light-year to km unit        
            in_km = distance.value * 9.461e12
            adjusted_distance = Distance(in_km, "km") 
        else:
            print ("unit is Unknown")
            return
    speed = adjusted_distance.value/time # [km per sec]

    adjusted_mass = Mass(mass.value, mass.unit)
    if mass.unit != 'kg':
        if mass.unit == "solar-mass":
            # convert from solar mass to kg
            value = mass.value * 1.98892e30 # [kg]
            adjusted_mass = Mass(value, 'kg')
        else:
            print ("unit is Unknown")
            return    
        
    kinetic_energy = 0.5 * adjusted_mass.value * speed ** 2
    return kinetic_energy

mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))