print('What is the radius of the cone?')
radius = int(input())
print('What is the height of the cone?')
height = int(input())
PI = 3.141592653589793
result = (PI * radius ** 2 * height) / 3
print('The volume of the cone is: ' + str(result))