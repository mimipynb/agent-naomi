

from pathlib import Path
from typing import Dict, Type

src_path = Path(__file__) # src/agentNaomi/utils.py

def get_data_paths() -> Dict[str, Type[Path]]:
    """
    Retrieve a dictionary containing the absolute paths
    for this project. This provides a simple method for
    traversing and referencing files outside the current
    working directory, particularly for scripts and notebooks.
    """
    data_path = {
        'main_path': src_path.parents[2].joinpath("data"),
        'subfolder': {}
    }
    
    data_path['main_path'].mkdir(exist_ok=True)
    
    for subfolder in ['user', 'agent', 'input', 'output']:
        data_path['subfolder'][subfolder] = data_path['main_path'].joinpath(subfolder)
        data_path['subfolder'][subfolder].mkdir(exist_ok=True)
    
    return data_path

def read_input_dir() -> Dict[str, str]:
    """
    Read all files in the input directory and return a dictionary
    of file names and their contents.
    """
    
    path = get_data_paths()
    
    for file in path['subfolder']['input'].iterdir():
        if file.is_file() and file.suffix == '.txt':
            try:
                with open(file, 'r') as f:
                    yield from f.read().strip().split('\n')
                    
            except Exception as e:
                print(f"Error reading file {file.name}: {e}")

def get_studio_keys():
    import yaml 
    
    with open(src_path.parents[2].joinpath(".lightning_var", "config.yaml"), "r") as f:
        return yaml.safe_load(f)
     
class MockData:
    correct_sample = ['I like romantic films like Titanic', 'I like movies like Titanic']
    incorrect_sample = ['I like horror films', 'I like movies like marvel']
