# Copyright 2022 MosaicML Diffusion authors
# SPDX-License-Identifier: Apache-2.0

"""Diffusion models."""

from diffusion.models.models import (build_autoencoder, build_diffusers_autoencoder, continuous_pixel_diffusion,
                                     discrete_pixel_diffusion, precomputed_text_latent_diffusion, stable_diffusion_2,
                                     stable_diffusion_xl, text_to_image_transformer)
from diffusion.models.noop import NoOpModel
from diffusion.models.pixel_diffusion import PixelDiffusion
from diffusion.models.precomputed_text_latent_diffusion import PrecomputedTextLatentDiffusion
from diffusion.models.stable_diffusion import StableDiffusion

__all__ = [
    'build_autoencoder',
    'build_diffusers_autoencoder',
    'continuous_pixel_diffusion',
    'discrete_pixel_diffusion',
    'NoOpModel',
    'PixelDiffusion',
    'precomputed_text_latent_diffusion',
    'stable_diffusion_2',
    'stable_diffusion_xl',
    'StableDiffusion',
    'PrecomputedTextLatentDiffusion',
    'text_to_image_transformer',
]
