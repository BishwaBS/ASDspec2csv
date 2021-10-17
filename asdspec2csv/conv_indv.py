import pandas as pd
import os
import numpy as np
from os.path import abspath, expanduser, splitext, basename, join, split
import glob
from collections import OrderedDict
import json
import struct
import matplotlib.pyplot as plt
import operator

from .base_code import read_asd

def convert_individual(inputdir, outputdir, save_graph=False):
        if os.path.exists(inputdir) and os.path.exists(outputdir):
            specfiles=os.listdir(inputdir)
            os.makedirs(os.path.join(outputdir, "csvfolder"), exist_ok=True)
            os.makedirs(os.path.join(outputdir, "graphfolder"), exist_ok=True)
            csvfolderpath=os.path.join(outputdir, "csvfolder")
            graphfolderpath=os.path.join(outputdir, "graphfolder")


            for specfile in specfiles:
                data = read_asd(os.path.join(inputdir, specfile), read_metadata=False)
                df = data[0].iloc[:, 0]
                print(df)
                df=pd.DataFrame(df).reset_index() 
                df.columns=["wavelength", "value"]  
                csvfilename = specfile.rsplit(".", 1)[0] + ".csv"
                df.to_csv(os.path.join(csvfolderpath, csvfilename))
                print("{} saved successfully".format(csvfilename))

                if save_graph==True:
                    plt.figure()
                    plt.plot(df["wavelength"], df["value"])
                    plt.xlabel('Wavelength')
                    plt.ylabel('Reflectance')
                    filename=specfile.rsplit(".", 1)[0] + ".png" 
                    plt.savefig(os.path.join(graphfolderpath, filename), bbox_inches = 'tight', format = 'png', dpi = 300)       
                    print("{} saved successfully".format(filename))

        else:
            print("The above specified inputdirectory and/or outputdirectorydoesn't exist")