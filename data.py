import pandas as pd
import numpy as np

import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem


class MoleculeDataset:
    def __init__(self, dataset_path: str):
        self.dataset_path = dataset_path
        self.load_data()
        
        

    def load_data(self):
        df = pd.read_csv(self.dataset_path)
        self.smiles = df['smiles'].tolist()
        self.labels = df['label'].tolist()
        self.mols = [Chem.MolFromSmiles(smiles) for smiles in self.smiles]
        self.adj = [np.array(AllChem.GetAdjacencyMatrix(mol)) for mol in self.mols]
        

    
    def __len__(self):
        return len(self.smiles)

    def __getitem__(self, idx):
        return self.smiles[idx], self.labels[idx]