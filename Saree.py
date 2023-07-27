import numpy as np
import pandas as pd
import matplotlib.pyplot as mpt
import sklearn
from IPython.display import display, Image, SVG, Math, YouTubeVideo
from IPython.core.display import HTML
from sklearn.metrics import pairwise_distances
from sklearn.linear_model import LinearRegression


def path_to_image_html(path):
    return '<img src="' + path + '" width="60" >'


lis = []

df = pd.read_csv("Myntra_Women_Clothing_Dataset.csv")
df.dropna(inplace=True)

reg = LinearRegression.fit(df.[[]])

print(lis)
