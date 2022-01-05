"""
    2022 Housing Advance Regression utils file
    Author: Rohan Deshpande
"""
import os
from collections import defaultdict

def read_file(file: str):
    """
    Efficient way to read large text files seperated by \n
    """
    with open(file, "r") as file:
        for line in file:
            yield line.rstrip()


def map_feature_text_file_to_dict(feature: str):
    """
    This function will read categorical variable file where
    each line in the file will have the format of variable - meaning.

    Suppose variable is Type of Sale

    File will contain
        WD 	Warranty Deed - Conventional
       CWD	Warranty Deed - Cash

    The returned dict will be like the following:

    dict["WD"] = "Warranty Deed - Conventional"
    dict["CWD"] = "Warranty Deed - Cash"

    """
    path_to_feature_dict_mapping = os.path.join(
        project_directory, "notebooks", "dict_mapping_features"
    )
    file_name = os.path.join(path_to_feature_dict_mapping, f"{feature}.txt")

    if not os.path.exists(file_name):
        raise FileNotFoundError(
            f"Your {feature}.txt file is not located in the dict_mapping directory!"
        )

    line_reader = read_file(file_name)
    feature_dict = defaultdict(str)
    for line in line_reader:
        line_split = line.strip().split()
        feature_dict[line_split[0]] = " ".join(line_split)[1:]
    return feature_dict
