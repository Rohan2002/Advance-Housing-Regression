"""
    2022 Housing Advance Regression plot file
    Author: Rohan Deshpande
"""
import seaborn as sns
import matplotlib.pyplot as plt
from src.utils import (
    interpret_skew_score,
    interpret_kurt_score,
    map_feature_text_file_to_dict,
)


class Plot:
    def __init__(self, train_df, project_directory):
        self.train_df = train_df
        self.project_directory = project_directory

    def display_summary_stat_for_categorical_data(
        self, categorical_feature: str, category_map: dict
    ):
        unique_categories_of_feature = self.train_df[categorical_feature].unique()
        print(f"Summary Statistics for categorical feature {categorical_feature}")
        for category in unique_categories_of_feature:
            category_sale_price = self.train_df["SalePrice"].loc[
                self.train_df[categorical_feature] == category
            ]
            print(
                f"Summary Statistics for categorical class {category_map[str(category)]}"
            )
            print(category_sale_price.describe())
            print(
                f"Skew Score: {category_sale_price.skew()} and Interpret: {interpret_skew_score(category_sale_price.skew())}"
            )
            print(
                f"Kurt Score: {category_sale_price.kurt()} and Interpret: {interpret_kurt_score(category_sale_price.kurt())}"
            )
            print(f"================================================================")
            print("\n")

    def display_summary_stat_for_numeric_data(self, numeric_data_feature):
        data = self.train_df[numeric_data_feature]
        print(f"Summary for numerical feature {numeric_data_feature}")
        print(data.describe())
        print(
            f"Skew Score: {data.skew()} and Interpret: {interpret_skew_score(data.skew())}"
        )
        print(
            f"Kurt Score: {data.kurt()} and Interpret: {interpret_kurt_score(data.kurt())}"
        )
        print(f"================================================================")
        print("\n")

    def plot_categorical(self, feature, rotate_x_labels):
        feature_dict = map_feature_text_file_to_dict(self.project_directory, feature)
        # print(dict(feature_dict))
        self.display_summary_stat_for_categorical_data(feature, feature_dict)
        mapped_col = f"{feature}_Mapping"
        self.train_df[mapped_col] = (
            self.train_df[feature].astype(str).replace(feature_dict)
        )
        plt.figure(figsize=(15, 20))
        plt.title(f"{feature} vs SalePrice")
        sns.violinplot(data=self.train_df, x=mapped_col, y="SalePrice")
        plt.xticks(rotation=rotate_x_labels)
        plt.show()

    def plot_numeric(self, feature):
        self.display_summary_stat_for_numeric_data(feature)
        plt.figure(figsize=(15, 20))
        plt.title(f"{feature} vs SalePrice")
        sns.scatterplot(data=self.train_df, x=feature, y="SalePrice")
        plt.show()

    def plot_individual_numeric(self, feature):
        self.display_summary_stat_for_numeric_data(feature)
        sns.displot(self.train_df[feature])
        plt.show()
    
    def plot_heatmap(self, dataframe):
        plt.figure(figsize=(15, 20))
        corrmat = dataframe.corr()
        sns.heatmap(corrmat, vmax=.8, square=True)
        plt.show()
