

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


def select_n_convert(inputdir, outputdir, individual_save_mode=False, save_graph=False):
        if os.path.exists(inputdir) and os.path.exists(outputdir):
            specfiles=os.listdir(inputdir)
            os.makedirs(os.path.join(outputdir, "csvfolder"), exist_ok=True)
            os.makedirs(os.path.join(outputdir, "graphfolder"), exist_ok=True)
            csvfolderpath=os.path.join(outputdir, "csvfolder")
            graphfolderpath=os.path.join(outputdir, "graphfolder")
                        
            selected=input("Enter the filenames for which the conversion is needed separated by comma:")
            selected=selected.replace(" ", "")
            selected=selected.split(",")
            print(selected)

            if individual_save_mode:
 
                
                for specfile in specfiles:
                    if specfile in selected:
                        data = read_asd(os.path.join(inputdir, specfile), read_metadata=False)
                        df = data[0].iloc[:, 0]
                        df=pd.DataFrame(df).reset_index() 
                        df.columns=["wavelength", "value"]  
                        csvfilename = specfile.rsplit(".", 1)[0] + ".csv"
                        df.to_csv(os.path.join(csvfolderpath, csvfilename))
                        print("{} saved successfully".format(csvfilename))

                        if save_graph==True:
                            plt.figure()
                            plt.plot(df["wavelength"], df["value"])
                            plt.xlabel('Wavelength')
                            plt.ylabel('DN')
                            filename=specfile.rsplit(".", 1)[0] + ".png" 
                            plt.savefig(os.path.join(graphfolderpath, filename), bbox_inches = 'tight', format = 'png', dpi = 300)       
                            print("{} saved successfully".format(filename))

            elif individual_save_mode==False:

                dflist=[]
                for specfile in specfiles:
                    if specfile in selected:
                        data = read_asd(os.path.join(inputdir, specfile), read_metadata=False)
                        df = data[0].iloc[:, 0]
                        dflist.append(df)

                dfmerge=pd.concat(dflist, axis=1) 
                dfmerge['value']=dfmerge.mean(axis=1) 
                mean= dfmerge.iloc[:, -1]
                dfmerge=pd.DataFrame(mean).reset_index()
                dfmerge.columns=["wavelength", "value"] 
                dfmerge.to_csv(os.path.join(csvfolderpath, "meanCSV.csv"))
                print("meanCSV file saved successfully")

                if save_graph==True:
                    plt.figure()
                    plt.plot(dfmerge["wavelength"], dfmerge["value"])
                    plt.xlabel('Wavelength')
                    plt.ylabel('Reflectance')
                    # filename=specfile.rsplit(".", 1)[0] + ".png" 
                    plt.savefig(os.path.join(graphfolderpath, "meanGraph.png"), bbox_inches = 'tight', format = 'png', dpi = 300)       
                    print("meanGraph saved successfully")
        else:
            print("The above specified inputdirectory and/or outputdirectory doesn't exist")