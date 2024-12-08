"""
This is a boilerplate pipeline 'data_preparation'
generated using Kedro 0.19.9
"""

from kedro.pipeline import Pipeline, node
from .nodes import clean_and_rename_data , transform_data, select_features

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=clean_and_rename_data,
            inputs="base_clientes_monopoly",
            outputs="cleaned_data",
            name="clean_and_rename_data_node",
        ),
        node(
            func=transform_data,
            inputs="cleaned_data",
            outputs="transformed_data",
            name="transform_data_node"
        ),
        node(
            func=select_features,
            inputs="transformed_data",
            outputs="prepared_data",
            name="select_features_node"
        ),
    ])
