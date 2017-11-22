#!/usr/bin/python

def hex_to_rgb(value):
	"""Return (red, green, blue) for the color given as #rrggbb."""
	value = value.lstrip('#')
	lv = len(value)
	return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(red, green, blue):
	"""Return color as #rrggbb for the given color values."""
	return '#%02x%02x%02x' % (red, green, blue)

choice = input("Convert from rgb or hex? ")

if choice == "rgb":
    r = int(input("Red: "))
    g = int(input("Green: "))
    b = int(input("Blue: "))
    print(rgb_to_hex(r, g, b))
elif choice == "hex":
    hex = input("Hex: #")
    print(hex_to_rgb(hex))
