Inputs:
value - Float
in_low - Float
in_high - Float
out_low - Float
out_high - Float
clamp - Boolean

Outputs:
output - Float

Script:
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
a mapping node.

map a value from one range to another range.
((value - in_low) * (out_high - out_low)) / (in_high - in_low) + out_low
((value - inlow) * (outhigh - outlow)) / (inhigh - inlow) + outlow

"""


def map(value, in_low, in_high, out_low, out_high):
    """map."""
    result = None

    # based on http://arduino.cc/en/Reference/Map
    result = ((value - in_low) * (out_high - out_low)) / \
        (in_high - in_low) + out_low

    # http://stackoverflow.com/a/5650012/574981
    # result = out_low + \
    #     ((out_high - out_low) * (value - in_low)) / \
    #     (in_high - in_low)

    return result


def map_bound(value, in_low, in_high, out_low, out_high):
    """map with high and low bound handling."""
    result = None

    if value <= in_low:
        result = out_low
    else:
        if value >= in_high:
            result = out_high
        else:
            # http://stackoverflow.com/a/5650012/574981
            result = out_low + \
                (out_high - out_low) * (value - in_low) / (in_high - in_low)
    return result

# set output to None
output = None
# check if clamp is used:
if clamp:
    output = map_bound(value, in_low, in_high, out_low, out_high)
else:
    output = map(value, in_low, in_high, out_low, out_high)
