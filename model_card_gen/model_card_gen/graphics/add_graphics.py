# Add Plotly visualizations to Model Card
from ..model_card import ModelCard, Graphic, Dataset, GraphicsCollection
from .plotly_graphics import *
# Typing
from typing import Sequence, Text, Tuple, Union, Optional
import tensorflow_model_analysis as tfma
from tensorflow_metadata.proto.v0 import statistics_pb2

OVERVIEW_GRAPHS = [OverallPerformanceAtThreshold]
PLOTS_GRAPHS = [ConfusionMatrixAtThresholdsGraphs]
SLICING_METRIC_GRAPHS = [SlicingMetricGraphs]
DATASTAT_GRAPHS = [DataStatsGraphs]

def add_overview_graphs(model_card: ModelCard,
                        eval_result: tfma.EvalResult) -> None:
    """Adds plots for every graph in OVERVIEW_GRAPHS.

    Args:
        model_card: The model card object.
        eval_result: A `tfma.EvalResult`.
    """
    # Get all metric and slice names
    plots = set()
    for slicing_metric in eval_result.plots:
        if slicing_metric[1]:
            for output_name in slicing_metric[1]:
                for sub_key in slicing_metric[1][output_name]:
                    plots.update(slicing_metric[1][output_name][sub_key].keys())

    if plots:
        # Generate graphs for plots
        graphs = [graph.generate_figure(eval_result.plots)
            for graph in OVERVIEW_GRAPHS
            # Check metric name is in plots
            if graph.eval_result_keys[0] in plots]
        # Add graphs to modle card
        model_card.model_details.graphics.collection.extend([
                Graphic(name=None, html=graph.html_content)
                for graph in graphs
        ])

def add_dataset_feature_statistics_plots(
        model_card: ModelCard,
        data_stats: Sequence[statistics_pb2.DatasetFeatureStatisticsList]) -> None:
    """Adds Dataset objects to model card with all graphs in
         DATASTAT_GRAPHS
    """
    
    for i, (name, stats) in enumerate(data_stats.items()):
        graphs = [graph.generate_figure(name, stats, color_index=i)
        for graph in DATASTAT_GRAPHS]
        model_card.model_parameters.data.append(
            Dataset(
                name=name.title(),
                graphics=GraphicsCollection(collection=[
                    Graphic(name=graph.name, html=graph.html_content)
                        for graph in graphs])))

def add_eval_result_slicing_metrics(model_card: ModelCard,
                                    eval_result: tfma.EvalResult) -> None:
    """Adds plots for every graph in SLICING_METRIC_GRAPHS
    and every metric in eval_result.slicing_metrics.

    Args:
        model_card: The model card object.
        eval_result: A `tfma.EvalResult`.
    """
    if eval_result.get_metric_names():
        graphs = [graph.generate_figure(eval_result.slicing_metrics)
            for graph in SLICING_METRIC_GRAPHS]
        model_card.quantitative_analysis.graphics.collection.extend([
                Graphic(name=graph.name, html=graph.html_content)
                for graph in graphs
        ])

def add_eval_result_plots(model_card: ModelCard,
                          eval_result: tfma.EvalResult) -> None:
    """Add visualizations for every plot in eval_result.plots.

    This function generates plots encoded as html text
    strings, and appends them to
    model_card.quantitative_analysis.graphics.collection.

    Args:
        model_card: The model card object.
        eval_result: A `tfma.EvalResult`.
    """

    # get all metric and slice names
    plots = set()
    for slicing_metric in eval_result.plots:
        if slicing_metric[1]:
            for output_name in slicing_metric[1]:
                for sub_key in slicing_metric[1][output_name]:
                    plots.update(slicing_metric[1][output_name][sub_key].keys())

    # generate graphs for plots
    if plots:
        graphs = [graph.generate_figure(eval_result.plots)
            for graph in PLOTS_GRAPHS
            # Check metric name is in plots
            if graph.eval_result_keys[0] in plots]
        model_card.quantitative_analysis.graphics.collection.extend([
                Graphic(name=None, html=graph.html_content)
                for graph in graphs
        ])

def get_slice_key(
    slice_key: Union[Tuple[()],
                     Tuple[Tuple[Text, Union[Text, int, float]], ...]]
) -> Tuple[Text, Text]:
    """Returns a tuple of joined keys and values accross slice_key
    """

    if not len(slice_key):
        return ('Overall', 'Overall')

    keys, values = zip(*slice_key)

    return (', '.join([u'{}'.format(key) for key in keys]),
            ', '.join([u'{}'.format(value) for value in values]))
