# -*- coding: utf-8 -*-

"""
Getting started with Torchtune!
===============================

This is a walkthrough of how to get started finetuning models using the ``torchtune`` library.

.. grid:: 2
    .. grid-item-card:: :octicon:`mortar-board;1em;` What you will learn
      * How to install Torchtune
      * How to download a model and dataset
      * How to finetune your first model with Torchtune
    .. grid-item-card:: :octicon:`list-unordered;1em;` Prerequisites
      * PyTorch >= 2.0

"""

# %%
# Installation
# ------------
#
# Our recommended installation is via ``pip``:

pip install torchtune

# However, you can also install from source by running:
# ..code-block:: bash
# git clone https://github.com/pytorch/torchtune.git
# cd torchtune
# pip install -e .


# %%
# Downloading a model
# -------------------
#
# We need a base model so let's use Meta's [Llama2-7B model](LINK).
# Because of Llama2's license, you'll need to visit the [official website]() and accept
# terms and conditions in order to access the model weights. Once you've done that,
# keep an eye out for an email from the team with a link to download the weights. When
# that email comes through, you'll want to navigate to the [meta-llama]() repo on HuggingFace.
# If your HuggingFace email is the same as the one you used to accept the terms and conditions,
# you should be able to download the model weights with the following command:
#

pip install huggingface_hub
python scripts/download.py --repo meta-llama/Llama-2-7b-hf --output-dir /tmp/llama2-7b

# Then you can convert the model to work with the internal Torchtune format. By default,
# the model is in `float16` format, so if your hardware doesn't support it, you can provide
# a `dtype` argument to convert the model to `bfloat16` or `float32`.

python scripts/convert_checkpoint.py --checkpoint /tmp/llama2-7b --dtype float32

# Note:
#   Read more about the concept of recipes in our post: 'What is a recipe???'

# %%
# Running your first finetuning recipe
# ------------------------------------
#
# Now that we have a model, we can run our first finetuning recipe.
# At it's core, a recipe is a script that
