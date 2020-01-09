#!/usr/bin/python3

import numpy as np
import argparse

parser=argparse.ArgumentParser(description='Prints nxn table')
parser.add_argument('--rows','-x',default=10)
parser.add_argument('--columns','-y',default=10)
args=parser.parse_args()


x=int(args.rows)
y=int(args.columns)

table=np.random.rand(x,y)

for i in range(x):
    for j in range(y):
        print("%.6f" %table[i][j],end='\t')
    print()
