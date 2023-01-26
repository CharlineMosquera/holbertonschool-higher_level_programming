#!/usr/bin/python3
for dig_1 in range(0, 10):
    for dig_2 in range(dig_1+1, 10):
        if dig_1 == 8:
            print(f"{dig_1}{dig_2}")
        else:
            print(f"{dig_1}{dig_2}", end=", ")
