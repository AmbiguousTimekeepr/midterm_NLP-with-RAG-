import pandas as pd
import numpy as np
import re
import string
import torch
import gensim
import seaborn as sns
import matplotlib.pyplot as plt
from underthesea import word_tokenize

from underthesea import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from tqdm import tqdm

import numpy as np
import pandas as pd
