plane_1 = ("Boeing-747", "AE56-977", 2010, 360)
plane_2 = ("Boeing-747", "TTY-66545", 2021, 360)
plane_3 = ("Aerobus-A320", "TYU-009-4", 2015, 320)
plane_4 = ("Sesna-172", "WW66443", 2019, 172)

planes = [plane_1, plane_2, plane_3, plane_4]

for plane in planes:
    if plane[2] > 350:
        print(plane[1])

print("--------------------")
plane_11 = {"model": "Boeing-747", "number": "AE56-977", "year": 2010, "sits": 360}
plane_12 = {"model": "Boeing-747", "number": "TTY-66545", "year": 2021, "sits": 360}
plane_13 = {"model": "Aerobus-A320", "number": "TYU-009-4", "year": 2015, "sits": 320}
plane_14 = {"model": "Sesna-172", "number": "WW66443", "year": 2019, "sits": 172}

planes_2 = [plane_11, plane_12, plane_13, plane_14]

for plane in planes_2:
    if plane["sits"] > 350:
        print(plane["number"])


print("--------------------")
from collections import namedtuple


Plane = namedtuple("Plane", ["model", "number", "year", "sits"])
plane_21 = Plane("Boeing-747", "AE56-977", 2010, 360)
plane_22 = Plane("Boeing-747", "TTY-66545", 2021, 360)
plane_23 = Plane("Aerobus-A320", "TYU-009-4", 2015, 320)
plane_24 = Plane("Sesna-172", "WW66443", 2019, 172)

planes_3 = [plane_21, plane_22, plane_23, plane_24]

for plane in planes_3:
    if plane.sits > 350:
        print(plane[1])
