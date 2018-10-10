from field.create_field import *


def ship_size(data, cell):
    """
    (dict, tuple) -> (tuple)

    Returns the size of the ship with its coordinates.

    e.g. cell: ('C', 1)
    """
    if type(data) != dict:
        print('Wrong argument data')
        return None
    if type(cell) != tuple:
        print("Second argument must be a tuple")
        return None
    if type(cell[0]) != str:
        print("First element of the second argument must be a str - A..J")
        return None
    if type(cell[1]) != int:
        print("Second element of the second argument must be a number - 1..10")
        return None
    if type(cell[1]) == dict:
        print("Second element of the second argument is dictionary")
    if not has_ship(data, cell):
        return 0
    x = ord(cell[0].upper()) - 64
    y = cell[1]
    if x < 1 or x > 10:
        print('Wrong coordinate. Must be from A to J.')
        return None
    if y < 1 or y > 10:
        print('Wrong coordinate. Must be from 1 to 10.')
        return None
    size = 1
    coords = {(x, y)}
    if data[(x+1, y)] == 'damaged' or data[(x+1, y)] or data[(x-1, y)] == 'damaged' or data[(x-1, y)]:
        start = x
        while(data[(start-1, y)] == 'damaged' or data[(start-1, y)]):
            coords = coords | {(start-1, y)}
            size += 1
            start -= 1
            if start < 2:
                break
        start = x
        while(data[(start+1, y)] == 'damaged' or data[(start+1, y)]):
            coords = coords | {(start + 1, y)}
            size += 1
            start += 1
            if start > 10:
                break
    elif data[(x, y+1)] == 'damaged' or data[(x, y+1)] or data[(x, y-1)] == 'damaged' or data[(x, y-1)]:
        start = y
        while(data[(x, start-1)] == 'damaged' or data[(x, start-1)]):
            coords = coords | {(x, start - 1)}
            size += 1
            start -= 1
            if start < 1:
                break
        start = y
        while(data[(x, start+1)] == 'damaged' or data[(x, start+1)]):
            coords = coords | {(x, start + 1)}
            size += 1
            start += 1
            if start > 10:
                break
    return (size, coords)


def has_ship(data, coords):
    """
    (dict, tuple) -> (bool)

    Checks if there is a ship on the field on the given coordinates.
    Return bool value - True if ship exist, or False otherwise.

    e.g. coords: ('C', 1)
    """
    if type(data) != dict:
        print('Wrong type of first argument (data)')
        return None
    if type(coords) != tuple:
        print('Wrong type of second argument (coords)')
        return None
    x = ord(coords[0].upper()) - 64
    y = coords[1]
    if x < 1 or x > 10:
        print('Wrong coordinate. Must be from A to J.')
        return
    if y < 1 or y > 10:
        print('Wrong coordinate. Must be from 1 to 10.')
        return
    if data[(x, y)] or data[(x, y)] == 'damaged':
        return True
    else:
        return False

def check_size(data, coords):
    """
    (dict, tuple) -> (bool)
    
    Check the size of the ship
    """
    x = ord(coords[0].upper()) - 64
    y = coords[1]
    
    value = data[(x, y)]
    if len(value[0]) > 5 or len(value[0]) < 1 or len(value[1]) > 5:
        print("Incorrect values")
        return None
    
