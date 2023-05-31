# Intel® Explainable AI Tools

This repository provides tools for data scientists and MLOps engineers that have requirements specific to AI model interpretability.

## Overview

The Intel Explainable AI Tools are designed to help users detect and mitigate against issues of fairness and interpretability, while running best on Intel hardware.
There are two Python* components in the repository:

* [Model Card Generator](model_card_gen)
  * Creates interactive HTML reports containing model performance and fairness metrics
* [Explainer](explainer)
  * Runs post-hoc model distillation and visualization methods to examine predictive behavior for both TensorFlow* and PyTorch* models via a simple Python API including the following modules:
    * [Attributions](explainer/attributions/): Visualize negative and positive attributions of tabular features, pixels, and word tokens for predictions
    * [CAM (Class Activation Mapping)](explainer/cam/): Create heatmaps for CNN image classifications using gradient-weight class activation CAM mapping
    * [Metrics](explainer/metrics/): Gain insight into models with the measurements and visualizations needed during the machine learning workflow

## Get Started

### Requirements
* Linux system or WSL2 on Windows (validated on Ubuntu* 20.04/22.04 LTS)
* Python 3.9
* Install required OS packages with `apt-get install build-essential python3-dev`
* git (only required for the "Developer Installation")

### Create and activate a Python3 virtual environment
We encourage you to use a python virtual environment (virtualenv or conda) for consistent package management.
There are two ways to do this:

a. Using `virtualenv`:
   ```
   python3.9 -m virtualenv xai_env
   source xai_env/bin/activate
   ```

   Or `conda`:
   ```
   conda create --name xai_env python=3.9
   conda activate xai_env
   ```

### Basic Installation
```
pip install intel-xai
```
### Developer Installation
Use these instructions to install the Intel Explainable AI Tools with a clone of the
GitHub repository. This can be done instead of the basic pip install, if you plan
on making code changes.

1. Clone this repo and navigate to the repo directory:
   ```
   git clone https://github.com/IntelAI/intel-xai-tools.git

   cd intel-xai-tools
   ```
2. Install the Intel Explainable AI Tools using the following command:
   ```
   make install
   ```

## Running Notebooks

The following links have Jupyter* notebooks showing how to use the Explainer and Model Card Generator APIs in various ML domains and use cases:
* [Model Card Generator Notebooks](/model_card_gen/notebooks)
* [Explainer Notebooks](notebooks/)

## Support

The Intel Explainable AI Tools team tracks bugs and enhancement requests using
[GitHub issues](https://github.com/intelai/intel-xai-tools/issues). Before submitting a
suggestion or bug report, search the existing GitHub issues to see if your issue has already been reported.

*Other names and brands may be claimed as the property of others. [Trademarks](http://www.intel.com/content/www/us/en/legal/trademarks.html)

#### DISCLAIMER: ####
These scripts are not intended for benchmarking Intel platforms. For any performance and/or benchmarking information on specific Intel platforms, visit https://www.intel.ai/blog.
 
Intel is committed to the respect of human rights and avoiding complicity in human rights abuses, a policy reflected in the Intel Global Human Rights Principles. Accordingly, by accessing the Intel material on this platform you agree that you will not use the material in a product or application that causes or contributes to a violation of an internationally recognized human right.
 
#### License: ####
Intel® Explainable AI Tools is licensed under Apache License Version 2.0.
 
#### Datasets: ####
To the extent that any public datasets are referenced by Intel or accessed using tools or code on this site those datasets are provided by the third party indicated as the data source. Intel does not create the data, or datasets, and does not warrant their accuracy or quality. By accessing the public dataset(s) you agree to the terms associated with those datasets and that your use complies with the applicable license. [DATASETS](DATASETS.md)
 
Intel expressly disclaims the accuracy, adequacy, or completeness of any public datasets, and is not liable for any errors, omissions, or defects in the data, or for any reliance on the data.  Intel is not liable for any liability or damages relating to your use of public datasets.
