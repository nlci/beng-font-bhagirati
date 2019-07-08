#!/usr/bin/python3

from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)

# Modify UFO
double = font['doubledanda']
double.name = 'dandadbl'

# Save UFO
font.changed()
font.save()
font.close()
