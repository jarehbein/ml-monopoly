"""
This is a boilerplate pipeline 'data_understanding'
generated using Kedro 0.19.9
"""

from kedro.pipeline import Pipeline, node
from .nodes import explore_data_in_chunks

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=explore_data_in_chunks,
                inputs="base_clientes_monopoly",
                outputs=None,
                name="explore_data",
            ),
        ]
    )
