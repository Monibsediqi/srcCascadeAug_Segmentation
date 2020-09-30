from .base import *
from .ade20k import ADE20KSegmentation
from .pcontext import ContextSegmentation

datasets = {
    'ade20k': ADE20KSegmentation,
    'pcontext': ContextSegmentation,
}

def get_segmentation_dataset(name, **kwargs):
    return datasets[name.lower()](**kwargs)
