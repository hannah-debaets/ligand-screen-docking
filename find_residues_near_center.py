##
## find_residues_near_center.py pdb_file_path distance_allowed center_x_coordinate center_y_coordinate center_z_coordinate
##
##
##


import pandas as pd
from math import dist
import sys


def read_in_args():
    """Confirms that the correct number of arguments are provided and that they are compatible datatypes."""
    if len(sys.argv) != 6:
        print("Error: Incorrect number of parameters.")
        print("USAGE: find_residues_near_center.py pdb_file_path distance_allowed "
              "center_x_coordinate center_y_coordinate center_z_coordinate")
        exit(1)
    else:
        file_path, distance, x, y, z = sys.argv[1:]
        return file_path, float(distance), float(x), float(y), float(z)


def read_in_pdb(file_name):
    """Reads the ATOM lines of the pdb file into a dataframe structure and returns the dataframe."""
    with open(file_name, "r") as filer:
        df_to_be = []
        for line in filer:
            if line.startswith("ATOM"):
                line_list = line.split()
                # line list = ["ATOM", atom_num, atom_role, residue, chain, residue_num, x, y, z, junk, junk, element]
                to_be_row = {"residue": line_list[3], "chain": line_list[4],
                             "residue_number": int(line_list[5]), "x_coordinate": float(line_list[6]),
                             "y_coordinate": float(line_list[7]), "z_coordinate": float(line_list[8])}
                df_to_be.append(to_be_row)
    df = pd.DataFrame(df_to_be)
    return df


def calculate_distance(row, center_coordinate):
    """Calculates distance from one atom to the center coordinates.
     For use with apply. Use with apply(axis=1) because this takes in a row as input."""
    atom_coordinate = tuple((row.x_coordinate, row.y_coordinate, row.z_coordinate))
    # Euclidean distance
    return dist(atom_coordinate, center_coordinate)


def make_filename(coordinates, distance, starting_file):
    """Creates a string that stores enough data to reproduce the results."""
    base_name = starting_file.split('.pdb')[0]
    distance_string = "_" + str(distance) + "ang_"
    coordinate_string = "from_" + "_".join(str(val) for val in coordinates)
    return base_name + distance_string + coordinate_string + ".csv"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Validate input
    file_path, distance, x, y, z = read_in_args()
    coord_pdb = read_in_pdb(file_path)
    center_deepsite = tuple((x, y, z))
    # Calculate distance from center
    coord_pdb["distance_from_center"] = coord_pdb.apply(calculate_distance, axis=1,
                                                        center_coordinate=center_deepsite)
    # The distance is the MIN distance to the center
    close_residues = coord_pdb[coord_pdb.distance_from_center < distance].groupby(["chain", "residue",
                                                                                   "residue_number"]).min()
    # Sort by residue number to make it easier for humans to skim
    to_save = close_residues.reset_index()[["chain", "residue_number", "residue",
                                            "distance_from_center"]].sort_values(by="residue_number")
    to_save_filename = make_filename(center_deepsite, distance, file_path)
    # writes the df of close residues to a csv file
    to_save.to_csv(to_save_filename, index=False)
