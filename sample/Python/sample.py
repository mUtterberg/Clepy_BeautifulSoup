# Sample Python script for code snippet presentation methods

# -*- coding: utf-8 -*-

# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xml.etree.ElementTree as ET

# Importing the dataset
tree = ET.parse('xml-compilation.xml')
branches = tree.
root = tree.getroot()

# Exploring root information
root.tag
root.attrib

data = []
for neighbor in root.findall("occupation"):
    name = neighbor.find("title")
    nameStr = neighbor.find("title").text
    print(nameStr)
    data.append(nameStr)
 

hierarchy = []
for neighbor in tree.iter():
    name = neighbor.tag
    hierarchy.append(name)
print(hierarchy)


frame = pd.DataFrame(data)
frame.to_csv("occupations.csv")

hFrame = pd.DataFrame(hierarchy)
hFrame.to_csv("contents.csv")
