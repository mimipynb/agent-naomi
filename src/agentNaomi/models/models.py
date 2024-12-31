
"""
models.py

This module is intended for *composed* models; i.e.
ready to training/usage, based off of layers defined in
either `torch`, other packages, or in `agentNaomi.layers`.
"""

import torch
import torch.nn as nn 
from datetime import datetime 

# import wandb
# import pytorch_lightning as pl
# from agentNaomi import layers

import joblib 
from lightning_sdk import Studio
from torch.utils.data import IterableDataset
from sentence_transformers import SentenceTransformer

# from agentNaomi.client import setup_studio
from agentNaomi.utils import get_data_paths, get_studio_keys

studio_keys = get_studio_keys()
path = get_data_paths()
memory = joblib.Memory(path['subfolder']['output'], verbose=0)

class Basement(SentenceTransformer):
    MODEL_CARD = "all-MiniLM-L6-v2"
    PROCESSING_PARAMS = {
        'normalize_embeddings': True,
        'similarity_type': 'dot', 
        'threshold': 0.5
    }
    MEMORY_PARAMS = {
        'output_path': path['subfolder']['output'],
        'time_window': 5,
    }
    """Sets Up preprocessing class module"""
    
    def __init__(self, **kwargs):
        """inputs: list of strings e.g. preferred candidate answers"""
        super().__init__(self.MODEL_CARD)
        
        if kwargs:
            for keys, values in kwargs.items():
                if keys in self.PROCESSING_PARAMS:
                    self.PROCESSING_PARAMS[keys] = values
                if keys in self.MEMORY_PARAMS:
                    self.MEMORY_PARAMS[keys] = values
                    
        self.crypt = {}
    
    @memory.cache
    def find_threshold(self, target: str, inputs: list):
        """Find the threshold for the target"""
        
        if target not in self.crypt:
            target_emb = self.encode([target], normalize_embeddings=self.PROCESSING_PARAMS['normalize_embeddings'])
            self.crypt[target] = target_emb
        else:
            target_emb = self.crypt[target]
        
        others = self.encode(inputs, normalize_embeddings=self.PROCESSING_PARAMS['normalize_embeddings'])
        sims_scores = self.similarity(target_emb, others)
        
        return sims_scores 
    
class TormentChamber(IterableDataset):
    def __init__(self, data, **kwargs):
        super(TormentChamber, self).__init__()
        
        self.studio = Studio(
            name=studio_keys['studio_name'],
            teamspace=studio_keys['teamspace'],
            user=studio_keys['username'] 
        )
        self.base = Basement(**kwargs)
        self.data = data 
        self.embeddings = dict(zip(self.data, self.base.encode(self.data, self.base.PROCESSING_PARAMS['normalize_embeddings'])))
    
    @memory.cache
    def __iter__(self):
        try:
            for entry in self.data: 
                pos = self.studio.findmylover(entry)
                opp = self.studio.findmyhater(entry)
                
                yield pos, opp, self.base.find_threshold(entry, pos), self.base.find_threshold(entry, opp)
                
        except Exception as e:
            print(f"Error: {str(e)}")
            raise e

if __name__ == "__main__":
    chamber = TormentChamber(['I like romantic films like Titanic', 'I like movies like Titanic'])
    