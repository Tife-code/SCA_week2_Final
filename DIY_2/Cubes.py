Cubes = []

#calculating and storing the cube value of integers from 1 to 10
for value in range(1, 11):
    cube = value ** 3
    Cubes.append(cube)

#printing each cubic value in the list
for cube_value in Cubes:
    print(cube_value)