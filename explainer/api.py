"""Module that defines the explainer API and Explanation object
"""
import os
from abc import ABC, abstractmethod, abstractproperty
from typing import Any
from numpy.typing import ArrayLike
import shap

shap.initjs()


class Explanation(ABC):
    """_summary_

    Raises:
        Exception: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    labels = {
        "MAIN_EFFECT": "SHAP main effect value for\n%s",
        "INTERACTION_VALUE": "SHAP interaction value",
        "INTERACTION_EFFECT": "SHAP interaction value for\n%s and %s",
        "VALUE": "SHAP value (impact on model output)",
        "GLOBAL_VALUE": "mean(|SHAP value|) (average impact on model output magnitude)",
        "VALUE_FOR": "SHAP value for\n%s",
        "PLOT_FOR": "SHAP plot for %s",
        "FEATURE": "Feature %s",
        "FEATURE_VALUE": "Feature value",
        "FEATURE_VALUE_LOW": "Low",
        "FEATURE_VALUE_HIGH": "High",
        "JOINT_VALUE": "Joint SHAP value",
        "MODEL_OUTPUT": "Model output value",
    }

    def __init__(self, shap_values: Any, max_display=10):
        pass


explainers_folder = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "explainers"))


class Explainer:
    """Explainer API base class
    """

    def __init__(self,  model: Any) -> None:
        """takes any type of model

        Args:
            model (Any): any instance of any type of model
        """
        self._explainer = shap.Explainer(model)

    def explainers(self) -> list:
        """Return the explainers available for the model

        Returns:
            list: list of explainers
        """
        r_var: list = []
        for filename in os.listdir(explainers_folder):
            if filename.endswith(".py"):
                r_var.append(filename[4:-3])
        r_var.sort()
        return r_var

    @property
    def explainer(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self._explainer

    @property
    def expected_value(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self._explainer.expected_value

    def explain(self, data: ArrayLike) -> Explanation:
        """takes data and forwards to internal explainer 

        Args:
            data (ArrayLike): _description_

        Returns:
            Explanation: explainable objects
        """
        return self.explainer(data)

    def visualize(self, *args: str, **kwargs: str) -> None:
        """_summary_
        """
