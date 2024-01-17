# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""
Finetune a large language model (LLaMA) w/ ``torchtune``!
=============================

This is a walkthrough of how to get started finetuning models using the ``torchtune`` library.
"""

# %%
# Installation
# ------------------
#
# Our recommended installation is via ``pip``:

pip install torchtune

# However, you can also install from source by running:
# ..code-block:: bash
# git clone https://github.com/pytorch/torchtune.git
# cd torchtune
# pip install -e .

# %%
# Understanding your environment
# ------------------------------
#
# Your environment will dictate the size of your model and dataset, PEFT methods you should use, your optimizer, batch size, training speed, and more.
# See below for a table showing common model architectures along w/ the hardware setup and training speed.
#
# | Model | GPU Model | Min # GPUs Needed to Avoid OOM | Batch Size | Training Speed |
# | --- | --- | --- | --- | --- |
# | Llama2-7B | RTX 4090 24G | 2 | 16 | 1000 samples/s |
# | Llama2-7B |
# | Mistral-7B |
# | Mistral MoE |

#
#
#
#
# CPU Offload
#
# If you start your script and see an OOM (out-of-memory), please see our OOM guide here (<LINK>)
#


# %%
# Downloading a model
# --------------------
#
#

# %%
# Updating your config
# --------------------

# %%
# Running your finetuning script
# ------------------------------
