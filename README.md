# Agent Naomi

Agent Naomi is your friendly neighbor, designed to hire suitable candidates based on your input questions and preferred or ranked responses. This package includes toolkits and adaptive learners that focuses at optimizing Llama3.1’s capabilities in interacting with users, analyzing data, and evolving its behavior based on the sample of candidates the agent communicates with and user’s direct feedback.

> 🚧 **This project is a work in progress and documentation is still ongoing.** 🚧

# Table of Contents

1. [Agent Naomi](#agent-naomi)
2. [Adaptive Interview and Quiz Platform](#adaptive-interview-and-quiz-platform)
    - [Adaptive Learner](#adaptive-learner)
    - [Generative LLM](#generative-llm)
3. [Dataset Overview](#dataset-overview)
    - [Local Dataset](#local-dataset)
    - [Cloud Dataset](#cloud-dataset)
4. [Package's Targets](#packages-targets)
5. [Installation](#installation)
6. [Dependency FAQs](#dependency-faqs)
7. [Extensions](#extensions)
    - [Future Extensions](#future-extensions)
    - [Current Plans](#current-plans)
8. [CLI Docs](#cli-docs)

## Installation

1. Clone the Repository:
    
    ```bash
    git clone https://github.com/mimipynb/agent-naomi.git
    cd agent-naomi
    ```
    
2. Pip installation
    
    ```jsx
    pip install agent-naomi
    ```
    
---

### Adaptive Interview and Quiz Platform

This Python package is designed to facilitate adaptive interviewing and scoring quizes especially long text responses. 

**Adaptive Learner**

The Adaptive Learner in /src/agentNaomi/models is updated per user session. 

- This is a hybrid model combining Self-Organizing Maps and Adjustable Policy Optimization parameters. These parameters leverage the algebraic properties derived from SVD iteration

Alternate Methods / Considerations:
- K-Means / Clustering using either Hamming or Cosine Distance (Default function is set to Cosine Distance)
- Recursive Linear Regression (or Kalmin Filtering)
 
**Generative LLM**

Agent Naomi leverages Llama 3.1, served through Ollama on **Lightning AI Studio**. The framework for setting up the studio is currently being refactored at [AgentHostess](/mimipynb). The template was initially designed for my experiments and use cases, with the primary goal of providing a roleplaying agent, chatbot development toolkit, and data handlers.

**Dataset Overview**

Dataset saved locally in directory path `/data` : 
- `/output`:
    - Yaml file storing the last K number Chat session $$k \in \mathhb{Z}$$
    - Pickle file storing model's last session model's output and metrics.
- `/input/`: 
    - Yaml file containing user's initial interviewing dataset (e.g. question and answer). 
- `/user/`: Yaml file containing the users introductory information stored as yaml file. Data handlers are configured in other repo: **AgentHostess**. Example of User's profile:
    ```yaml
    - Features related to the interview / scoring metrics / task at hand:
        - Likes
        - Dislikes
    - Features related to the user only:
        - Name
        - Likes
        - Dislikes
        - Fun faqs: e.g. I hate apples
    ```

Dataset saved on Cloud Platforms (which was intended to be built with components from the cloud's current setup and not this package. In saying that, you would also need to install AgentHostess to use this package. As I am writing this, I realised that I should probably packet both this and the other as one package. The intention was that I was hoping to use this package with other components containing 'light weighted' models and toolkits to run locally on a user's device presumably with the worst kind of compute metrics):
- All Synthetic text generation dataset
- Loggings associated with generative LLM 

---

## Features

The goals and features this package has to offer ATM.

- **Real-Time Adaptive Model**: incrementally improves a Discriminator from user’s starting inputs (pairs of Question and Answers) and candidates. From my experiments, three modelling techniques are suitable for this task.
- **Scoring and Compatibility**: Provides a calculated score for candidate suitability or compatibility based on their answers.
- **Customizable**: Fine-tunes Naomi’s Text generation model according to the user’s usage and their quiz / questionaire / interviewing participants / candidates.

---

## Dependency FAQs

Environemnts Dependencies resolved / handled by using Poetry and conda.
Template Reference: 

[https://github.com/laserkelvin/cookiecutter-pytorch-project/tree/main/{{cookiecutter.project_name}}](https://github.com/laserkelvin/cookiecutter-pytorch-project/tree/main/%7B%7Bcookiecutter.project_name%7D%7D)

## Future Extensions

- Automating Fine-tuner for Generative AI (Llama).
- Add more Visualization of the graph networks behind cached data from the llm and the agent’s chatting environment / platform. This would be good practice on handling knowledge graphs of Agents (helping me monitor the growth and perserved memories for a llm)

## Current Plans

Fun Part
- Refactor my code for other modelling approaches for learning real-time datasets.
- Add User direct Feedback to Naomi e.g.  $f(reward | x_{t = i}) = x_{t=i+1}$
- Improve the Cli functionality 
Boring Part
- Notion Database Integration
- Setup Text Generation manipulator

## CLI Docs

Command Line

```jsx
agent-naomi [command] 
```

Example

```jsx
agent-naomi --help
```

- Setting up connection with Lightning AI Studio with cli
    
    ```jsx
    agent-naomi setup_studio <studio_name> <teamspace> <username>
    ```
    
    Example:
    
    ```jsx
    agent-naomi setup_studio llm-ollama-container miplayground mimiphan
    ```

> 🚧 **This project is a work in progress and documentation is still ongoing.**🚧