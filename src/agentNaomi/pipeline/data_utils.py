
import yaml
from pathlib import Path
from typing import List, Dict
from dataclasses import dataclass, field 

src_path = Path(__file__).parents[1].joinpath("data")
print(src_path)

@dataclass
class DataHandler:
    """Yaml data handler."""
    
    file_name: str
    data: List[str] = field(init=False)
    file_path: Path = field(init=False)

    def __post_init__(self):
        """Initialize paths and load the file."""
        self.file_path = get_data_paths()['subfolder']['input'].joinpath(self.file_name)
        self.loader()

    def loader(self):
        """Load data from the file."""
        if not self.file_path.exists():
            raise FileNotFoundError(f"File {self.file_name} not found at path {self.file_path}")

        with self.file_path.open('r') as f:
            data = yaml.safe_load(f)

        if not data or 'inputs' not in data:
            raise ValueError(
                f"File {self.file_name} does not contain the expected key: `inputs`. "
                f"Loaded file from path {self.file_path}\nData: {data}"
            )

        self.data = data['inputs']
        """
        for entry in data['inputs']:
            if not set(['question', 'answer']).issubset(entry.keys()):
                raise ValueError(f'Each entry in the file must contain both `question` and `answer` keys. {entry}')
            # self.question += [entry.get('question', [])]
            # self.answers += [entry.get('answer', [])]
        
        # assert len(self.question) == len(self.answers), "Number of questions and answers must be equal."
        """ 
        
    def save(self):
        """Save the current data to the file."""
        with self.file_path.open('w') as f:
            yaml.dump({"inputs": self.data}, f, default_flow_style=False, sort_keys=False)
        print(f"Data saved to {self.file_path}")
    
    def update(self, question: str, answer: str):
        """Update the data with a new question and answer."""
        
        self.data += [
            {
                'question': question,
                'answer': answer
            }
        ]

def markdown_table(data: dict):
    """Convert a dictionary to a markdown table"""
    return " ".join([f"{i+1}. {row['question']}\n" for i, row in enumerate(data)])

if __name__ == '__main__':
    holder = DataHandler('example.yaml')
    print(holder.data)