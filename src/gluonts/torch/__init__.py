# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

__all__ = [
    "PyTorchLightningEstimator",
    "PyTorchPredictor",
    "DeepNPTSEstimator",
    "DeepAREstimator",
    "SimpleFeedForwardEstimator",
    "TemporalFusionTransformerEstimator",
    "WaveNetEstimator",
    "DLinearEstimator",
    "PatchTSTEstimator",
    "LagTSTEstimator",
]
import torch
from .model.estimator import PyTorchLightningEstimator
from .model.predictor import PyTorchPredictor
from .model.deep_npts import DeepNPTSEstimator
from .model.deepar import DeepAREstimator
from .model.simple_feedforward import SimpleFeedForwardEstimator
from .model.tft import TemporalFusionTransformerEstimator
from .model.wavenet import WaveNetEstimator
from .model.d_linear import DLinearEstimator
from .model.patch_tst import PatchTSTEstimator
from .model.lag_tst import LagTSTEstimator


from . import prelude as _  # noqa


if torch.cuda.is_available():
    torch.multiprocessing.set_start_method("spawn", force=True)
