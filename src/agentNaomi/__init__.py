"""
Agent Naomi is an adaptive learning system designed for interview candidate evaluation. It processes long-form text responses, dynamically updates classifiers and discriminators based on new data, and provides refined scoring metrics to assess candidate performance effectively. This package leverages machine learning to continuously improve its evaluation criteria, ensuring fair and insightful feedback for each interviewee.

"""

from agentNaomi.utils import get_data_paths, read_input_dir, MockData, get_studio_keys
from agentNaomi import models, pipeline, client
