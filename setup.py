#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
#

"""
XAI Tools, Explainer
"""
from pathlib import Path
from setuptools import setup

# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

ATTRIBUTIONS_PKGS = [
  'captum==0.6.0',
  'intel-tensorflow==2.13.0',
  'ipywidgets==7.8.1',
  'numpy==1.22.4; python_version<"3.10"',
  'numpy==1.24.3; python_version=="3.10"',
  'opencv-python==4.8.0.76',
  'plotly==5.17.0',
  'scikit-plot==0.3.7',
  'scipy==1.10.1; python_version=="3.8"',
  'scipy==1.11.2; python_version>"3.8"',
  'shap==0.42.1',
  'torch==2.0.1',
  'transformers==4.33.2',
  ]

CAM_PKGS = [
  'grad-cam==1.4.8',
  'matplotlib==3.7.3; python_version=="3.8"',
  'matplotlib==3.8.0; python_version>"3.8"',
  'numpy==1.22.4; python_version<"3.10"',
  'numpy==1.24.3; python_version=="3.10"',
  'opencv-python==4.8.0.76',
  'scipy==1.10.1; python_version=="3.8"',
  'scipy==1.11.2; python_version>"3.8"',
  'torch==2.0.1',
  ]

METRICS_PKGS =  [
  'matplotlib==3.7.3; python_version=="3.8"',
  'matplotlib==3.8.0; python_version>"3.8"',
  'pandas==1.5.3',
  'plotly==5.17.0',
  'scikit-learn==1.3.1',
  'seaborn==0.12.2',
]

MCG_PKGS = [
  'Jinja2==3.1.2',
  'absl-py==1.4.0',
  'attrs==21.4.0',
  'dataclasses==0.6',
  'grpcio-status==1.48.2',
  'intel-tensorflow==2.13.0',
  'joblib==1.3.2',
  'jsonschema[format-nongpl]==4.17.3',
  'plotly==5.17.0',
  'protobuf==3.20.3',
  'semantic-version==2.10.0',
  'tensorflow-data-validation==1.13.0; python_version<"3.10"',
  'tensorflow-data-validation==1.14.0; python_version=="3.10"',
  'tensorflow-model-analysis==0.44.0; python_version<"3.10"',
  'tensorflow-model-analysis==0.45.0; python_version=="3.10"',
  ]

PYTORCH_PKGS = [
  'torch==2.0.1',
  'torchvision==0.15.2',
  ]

REQUIRED_PKGS =  (
  ATTRIBUTIONS_PKGS +
  CAM_PKGS +
  METRICS_PKGS +
  MCG_PKGS
  )

TEST_PKGS = [
  'datasets==2.10.1; python_version<"3.10"',
  'datasets==2.14.4; python_version=="3.10"',
  'deepdiff==6.5.0',
  'pytest==7.4.2',
  'tensorflow-hub==0.14.0',
  ]

PACKAGES = [
  'explainer',
  'explainer.attributions',
  'explainer.cam',
  'explainer.metrics',
  'explainer.utils.model',
  'explainer.utils.graphics',
  'model_card_gen',
  'model_card_gen.analyze',
  'model_card_gen.datasets',
  'model_card_gen.docs',
  'model_card_gen.docs.examples',
  'model_card_gen.graphics',
  'model_card_gen.utils',
  ]


EXTRAS = {
  'pytorch': PYTORCH_PKGS,
  'test': TEST_PKGS + PYTORCH_PKGS,
  }

# Get version from version module.
with open('explainer/version.py') as fp:
  globals_dict = {}
  exec(fp.read(), globals_dict)  # pylint: disable=exec-used
__version__ = globals_dict['__version__']

setup(
    name='intel-xai',
    version=__version__,
    url='https://github.com/IntelAI/intel-xai-tools',
    license='Apache 2.0',
    author='IntelAI',
    author_email='IntelAI@intel.com',
    description='Intel® Explainable AI Tools',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=REQUIRED_PKGS,
    tests_require=TEST_PKGS,
    extras_require=EXTRAS,
    packages=PACKAGES,
    package_data={
        'model_card_gen': ['schema/**/*.json', 'template/**/*.jinja'],
        'model_card_gen.docs.examples': ['docs/examples/**/*.html',
                                         'docs/examples/**/*.json'],
    },
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.8',
    keywords='XAI, explainer',
)
