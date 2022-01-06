"""
    2022 Housing Advance Regression utils file
    Author: Rohan Deshpande
"""
import os
from collections import defaultdict
import pathlib

EPSILON = 1e-6

def true_project_directory():
    REPO_DIR = pathlib.Path(__file__).parent.absolute()
    return os.path.dirname(REPO_DIR)

def between(val ,a, b):
    low = min(a, b)
    high = max(a,b)
    return val >= low and val <= high

def interpret_skew_score(skew:float):
    """
        measures the lack of symmetry in data distribution.
    """
    if between(skew, -0.5, 0.5):
        return "Fairly Symmetrical"
    elif between(skew, -0.5, -1):
        return "Negative Skew and Moderately Skewed"
    elif between(skew, 0.5, 1):
        return "Postive Skew and Moderately Skewed"
    elif skew < -1:
        return "Negative Skew and Highly Skewed"
    elif skew > 1:
        return "Positive Skew and Highly Skewed"

def interpret_kurt_score(kurt:float):
    """
        measure of outliers present in the distribution.
    """
    if abs(kurt - 3) <= EPSILON:
        return "Mesokurtic: Similar to Normal Distrubution"
    elif kurt < 3:
        return "Platykurtic: Peak is lower and broader than Mesokurtic and thus Lack of outliers."
    elif kurt > 3:
        return "Leptokurtic: Peak is Higher and thinner than Mesokurtic and thus Lot of outliers."
        
def read_file(file: str):
    """
    Efficient way to read large text files seperated by \n
    """
    with open(file, "r") as file:
        for line in file:
            yield line.rstrip()


def map_feature_text_file_to_dict(project_directory: str, feature: str):
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
        if len(line_split) != 0:
            feature_dict[line_split[0]] = " ".join(line_split[1:])
    return feature_dict

if __name__ == "__main__":
    feature_dict = map_feature_text_file_to_dict('/Users/user/Applications/machine-learning/housing-prices', 'MSSubClass')
    print(feature_dict)