#!/usr/bin/env python

import sys
import os.path
from os.path import join as PJ
from collections import OrderedDict
import re
import json
import numpy as np
from tqdm import tqdm
import igraph as ig
import jgf
import pandas as pd
from nilearn import input_data, connectome


configFilename = "config.json"
argCount = len(sys.argv)
if(argCount > 1):
		configFilename = sys.argv[1]

outputDirectory = "output"
outputFile = PJ(outputDirectory,"network.json.gz")

if(not os.path.exists(outputDirectory)):
		os.makedirs(outputDirectory)


with open(configFilename, "r") as fd:
		config = json.load(fd)

if("method" in config):
	methodName = config["method"]
else:
	methodName = "correlation"


timeseriesFilename = config["timeseries"]
metadataFilename = config["metadata"]

with open(metadataFilename, "r") as fd:
	metadata = json.load(fd)

timeSeries = pd.read_csv(timeseriesFilename,sep="\t")

columnNames = list(timeSeries.columns)


networkProperties = []

#{“covariance”, “correlation”, “partial correlation”, “tangent”, “precision”}
connobj = connectome.ConnectivityMeasure(kind=methodName)
connmat = connobj.fit_transform([timeSeries.to_numpy()])[0]

# remove diagonal
np.fill_diagonal(connmat, 0)




nodesProperties = OrderedDict()
nodesProperties["label"] = columnNames;
for nodeIndex,nodeInformation in enumerate(metadata):
	for key,value in nodeInformation.items():
		if(key not in nodesProperties):
			nodesProperties[key] = OrderedDict()
		nodesProperties[key][nodeIndex] = value


jgf.conmat.save([connmat],outputFile, compressed=True,
	label="network",
	networkProperties={"type":methodName},
	nodeProperties=nodesProperties)


