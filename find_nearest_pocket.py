#
# This program is for calculating the distance between the deepsite center coordinates
# and the hotspot wizard pocket centers
#
# run with python version 3.9
# run with the command:
# python3 find_nearest_pocket.py


from math import dist


def calculate_distances_from_pockets(coordinate, pocket_center_list):
    for i, coords in enumerate(pocket_center_list):
        print("Pocket", i + 1, dist(coordinate, coords))


if __name__ == '__main__':
    #
    print("Distances to 4JJX pocket centers")
    deepsite_4JJX = tuple((-27.44000, -22.69000, 24.93000))
    pocket_centers_4JJX = [(-17, -31, 23), (-20, -21, 30), (-22, -19, 23), (-12, -21, 25), (-30, -26, 24),
                           (-27, -13, 21), (-14, -33, 16), (-28, -31, 17), (-39, -24, 28), (-27, -23, 14)]
    calculate_distances_from_pockets(deepsite_4JJX, pocket_centers_4JJX)
    print()

    print("Distances to 5BTR pocket centers")
    deepsite_5BTR = tuple((-20.66, 64.5, 12.8))
    # Only 12 of the 21 pockets are compared because the relevance drops to 10% at pocket 13, and copying the
    # coordinates is done by hand
    pocket_centers_5BTR = [(-8, 62, -1), (-22, 59, 13), (2, 66, -12), (-13, 62, 10), (-25, 68, 3), (0, 81, -7),
                           (-21, 78, -1), (-4, 69, -18), (-14, 78, 11), (-2, 84, 4), (-2, 46, 14), (-8, 65, 16)]
    calculate_distances_from_pockets(deepsite_5BTR, pocket_centers_5BTR)
