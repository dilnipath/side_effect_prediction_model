# Side Effect Prediction Model

# Overview

Drugs are first tested on animals whose side effects may be extremely different from those for humans (Perel, etal, 2006). This study aims to create a model that could predict side effects for humans before clinical trials are run. This could allow clinicians to be prepared to address potential health risks for the patients in the trial.

# Research Question

Can a model be trained to predict the side effects of drugs based on its usage, chemical composition and other features?

# Replication Instructions

Install [MiniForge](https://github.com/conda-forge/miniforge). Download all files from this repository to a folder and navigate to it. Run the following commands in Miniforge to download necessary libraries and activate environment:

```
$ conda env create -f environment.yml
$ conda activate ml
```
Download the additional dependencies: 
+ [pytorch](https://pytorch.org/get-started/locally/)
+ [Transformers](https://huggingface.co/docs/transformers/en/installation)
+ [sklearn](https://scikit-learn.org/stable/install.html)
+ [bs4](https://pypi.org/project/beautifulsoup4/)
+ [Claude AI API](https://platform.claude.com/login?returnTo=%2F%3F)

In order to run the split_side_effects_fewshot.py, you will need your own Claude AI API key.
Run model.py to train model on a dataset and get results.

# Data

### DrugBank ([https://go.drugbank.com/])
Dataset containing properties, characteristics, and descriptions of 15,000+ drugs.

### MedlinePlus ([https://medlineplus.gov/])
Online health resource ran by US government containing descriptions and side effects of approved drugs.

## Data Collection 

First, drug names were collected from DrugBank and MedlinePlus individually. The drug names were then compared to finding drug names in common. From DrugBank, features, such as description and toxicity, were collected for each drug. From MedlinePlus, the side effects were collected for each drug. These side effects were unstandardized (Example: “difficulty swallowing or breathing” vs “difficulty breathing or swallowing”). Side effects were then split up into smallest possible units using Claude AI (Example: "difficult swallow and breathing" --> "difficulty swallowing", "difficulty breathing"). These side effects were then generalized by hand (Example: “bone pain", "severe bone pain", "pain in bones", "increased bone pain", "pain in bone"→ “bone pain”).

# Model

BioBERT Embeddings were created using the drugs, features and side effects. Further, Multi-Label Classification was implemented where each side effect was a label. The data was then split into train and testing datasets to use in the model.

The model is a Sequential Model with three linear layers, dropout, and LeakyReLU for activation function. The loss function used was Binary Focal Loss and additionally Binary Cross Entropy specifically for Generalized Side Effects. These activation and loss functions were aimed to help with the unbalanced labels. The model was trained for 300 epochs with early stopping implemented. 

# Future Directions

Our model had a higher recall when there were less side effects, so for future steps we first would like to continue to generalize side effects. Additionally, we would like to add more features and determine which set of features gives the best results. Further, we would like to implement hyperparameter optimization and experiment with new models.

# Contributions

[Grace Kenney](https://github.com/gkenney1598)
