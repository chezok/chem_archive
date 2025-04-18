import rdkit
from rdkit import Chem


class ESOLDataset:
    def __init__(self, dataset_path: str):
        self.dataset_path = dataset_path
        self.molecules = []
        self.labels = []
        self.load_data()

    def load_data(self):
        with open(self.dataset_path, 'r') as f:
            for line in f:
                parts = line.strip().split()
                smiles = parts[0]
                label = float(parts[1])
                mol = Chem.MolFromSmiles(smiles)
                if mol is not None:
                    self.molecules.append(mol)
                    self.labels.append(label)

    def __len__(self):
        return len(self.molecules)