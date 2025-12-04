INCHES_TO_CM = 2.54
CM_TO_METERS = 0.01
FEET_TO_INCHES = 12

def convert_height_to_meters(feet, inches):
    feet_inches = feet * FEET_TO_INCHES
    inches_cm = feet_inches * INCHES_TO_CM + (inches * INCHES_TO_CM)
    meter = inches_cm * CM_TO_METERS
    print(meter)


convert_height_to_meters(6, 4) # 1.9304 
convert_height_to_meters(6, 5) # 1.9304 
convert_height_to_meters(2, 8) # 1.9304 
convert_height_to_meters(10, 6) # 1.9304 
convert_height_to_meters(37, 5) # 1.9304 
