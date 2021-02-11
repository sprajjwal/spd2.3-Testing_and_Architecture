# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

def print_distance(xc1, xc2, yc1, yc2):
    # Calculate the distance between the two circle
    distance = math.sqrt((xc1-xc2)**2 + (yc1 - yc2)**2)
    print('distance', distance)

def print_length(xa, xb, ya, yb):
    # calcualte the length of vector AB vector which is a vector between A and B points.
    length = math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))
    print('length', length)

if __name__ == "__main__":
    xc1 = 4
    yc1 = 4.25

    xc2 = 53
    yc2 = -5.35
    print_distance(xc1, xc2, yc1, yc2)

    xa = -36
    ya = 97

    xb = .34
    yb = .91
    print_length(xa, xb, ya, yb)