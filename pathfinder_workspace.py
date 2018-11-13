from PIL import Image
import random

"""Make the take the info in elevation_small and make it a list of lists"""

with open('elevation_small.txt') as file:
    stripped_lines = [line.strip() for line in file.readlines()]
    listed_lines = [line.split(' ') for line in stripped_lines]
    numbered_pixels = [[int(x) for x in line] for line in listed_lines]

"""Find the max and min elevation in the whole list"""

def find_max_elevation(data):
    max_elevation = max([max(row) for row in data])
    return max_elevation

max_elevation = find_max_elevation(numbered_pixels)

# print(max_elevation)

def find_min_elevation(data):
    min_elevation = min([min(row) for row in data])
    return min_elevation

min_elevation = find_min_elevation(numbered_pixels)

# print(min_elevation)

"""Divide all the (data minus the min of max) in the list by the max, then multiply by 255,
 getting an new list of integers"""

def convert_to_RBG_num(data, max, min):
    divide_by_max = [[int(((num-min)/(max-min) * 255)) for num in row] for row in data]
    return divide_by_max

RBG_num_list = convert_to_RBG_num(numbered_pixels, max_elevation, min_elevation)

# print(RBG_num_list[0])

"""Transfer all of the adjusted data from the new list into a .png file"""

def make_picture(data):
    height = len(data)
    width = len(data[0])
    image2 = Image.new('RGB', (height, width))
    for y, row in enumerate(data):
        for x, num in enumerate(row):
            image2.putpixel((x, y), (num, num, num))
    return image2.save("middlepath.png")

make_picture(RBG_num_list)

def red_pixel_start(xit, yit):
    from PIL import Image
    pixel_canvas = Image.open('middlepath.png')
    pixel_canvas.putpixel((xit, yit), (255, 0, 0))
    pixel_canvas.save('middlepath.png')
    # pixel_canvas.show()
    pixel_canvas.close()


# red_pixel_start(0, 300)

def choose_one():
    return random.choice([1, 2])

def where_to_go(data):
    x_axis = 0
    y_axis = 300
    while x_axis <= 600:
        print(x_axis)
        start_point = data[x_axis][y_axis]

        np_1 = data[x_axis + 1][y_axis + 1]
        np_2 = data[x_axis + 1][y_axis]
        np_3 = data[x_axis + 1][y_axis - 1]

        opt1 = abs(start_point - np_1)
        opt2 = abs(start_point - (np_2))
        opt3 = abs(start_point - (np_3))

        if opt1 < opt2 and opt1 < opt3:
            # print('happened1')
            x_axis += 1
            y_axis += 1
            red_pixel_start(x_axis, y_axis)

            continue
        elif opt2 < opt1 and opt2 < opt3:
            # print('happened2')
            x_axis += 1
            red_pixel_start(x_axis, y_axis)
            continue
        elif opt3 < opt1 and opt3 < opt2:
            # print('happened3')
            x_axis += 1
            y_axis -= 1
            red_pixel_start(x_axis, y_axis)
            continue
        elif opt1 == opt2 and opt1 < opt3:
            # print('tiehappened1')
            x_axis += 1
            red_pixel_start(x_axis, y_axis)
            continue
        elif opt2 == opt3 and opt2 < opt1:
            # print('tiehappened2')
            x_axis += 1
            red_pixel_start(x_axis, y_axis)
            continue
        elif opt3 == opt1 and opt3 < opt2:
            if choose_one() == 1:
                # print('hardchoice1')
                x_axis += 1
                y_axis -= 1
                red_pixel_start(x_axis, y_axis)
                continue
            else:
                # print('hardchoice2')
                x_axis += 1
                y_axis += 1
                red_pixel_start(x_axis, y_axis)
                continue
        elif opt3 == opt1 and opt1 == opt2:
            # print('allthreethesame')
            x_axis += 1
            red_pixel_start(x_axis, y_axis)
            continue

where_to_go(RBG_num_list)