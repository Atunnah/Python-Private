import math

def read_coordinates(file_path):
    """This function is to read coordinates from file and return coordinates of A and B"""
    with open(file_path, 'r') as file:
        content = file.read().split()
    coordinates = {'A': (float(content[1]), float(content[2])), 'B': (float(content[4]), float(content[5]))}
    return coordinates

def calculate_distance(coordiantes):
    """This function is to calculate distance between A and B"""
    point_a = coordiantes['A']
    point_b = coordiantes['B']
    distance = math.sqrt((point_b[0] - point_a[0])**2 + (point_b[1] - point_a[1])**2)
    return round(distance, 2)

def write_coordinates(file_path, coordinates, distance):
    """This function is to write result to output.txt file"""
    with open(file_path, 'w') as file:
        file.write(f"A({coordinates['A'][0]} {coordinates['A'][1]}) B({coordinates['B'][0]} {coordinates['B'][1]}) AB = {distance}")

input_file_path = 'input.txt'
coordinates = read_coordinates(input_file_path)
distance = calculate_distance(coordinates)
output_file_path = 'output.txt'
write_coordinates(output_file_path, coordinates, distance)
print("Doc va ghi ket qua ra tep thanh cong!!!")
