import glob
import csv
import pandas as pd

files = (glob.glob("output_A/*.csv"))
#print files
rows = []
for f in files:
    df = pd.read_csv(f)
    df.to_csv('outA.csv',mode="a")
    
