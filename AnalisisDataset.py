pip install folium

%matplotlib inline
%pylab inline
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import folium 
from folium import plugins

df= pd.read_csv("/content/drive/MyDrive/Colab Notebooks/ChicagoCrime_dataset_2001.csv", nrows=10000)


df.rename(columns={'Case Number':'Case_Number',
                        'Primary Type':'Primary_Type',
                        'Location Description':'Location_Description',
                        'X Coordinate':'X_Coordinate',
                        'Y Coordinate':'Y_Coordinat',
                        'Updated On':'Updated_On'},inplace=True)

df.columns
#Cambio
df.describe(include=np.object)

df["Primary_Type"].unique()
