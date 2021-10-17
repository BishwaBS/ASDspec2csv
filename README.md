This package basically converts spectral readings (*.asd) files to csv files. User can also choose to create "Wavelength" vs "Reflectance" graph. The package provides functionality where user can perform the task for a number of files at once.

**Limitations:**
This package has been tested for only .asd files. It is not sure if this package will work for other file formats of spectral reading data.

**How to use:**

**step1** ```Goto your desired google drive directory and create a new google colaboratory file```

**step2** Open the collab file and mount your google drive by typing 

```from google.colab import drive```

```drive.mount("/content/gdrive")```

**step3** Type the following command after mounting the file ```git clone https://github.com/BishwaBS/ASDspec2csv.git ```

**step4** Change the working directory to the clone directory by typing ```cd "ASDspec2csv" ```

**step5** Type the following

```import os``` 

```import asdspec2csv```

**Start using the package**

**Let's say we have 100 .asd files in folder named FOLDER**

**to convert each .asd file to csv file and save graph for each .asd file, type following**
```asdspec2csv.convert_individual(inputdir, outputdir, save_graph=Ture)```
e.g. ```asdspec2csv.convert_individual ("gdrive:\\documents\\folder_containing_asdfiles", "gdrive:\\documents\\result_folder", save_graph=True)```

You need to provide the path of your input and output directory as shown in the example above

you can choose to not save graph by setting ```save_graph=False``` 

**to average the reflectance values for all the .asd values in the folder and convert the averaged value to a csv file and save graph for averaged value**
```asdspec2csv.average_n_convert(inputdir, outputdir, save_graph=Ture)```
you can choose to not save graph by setting ```save_graph=False``` 


**to convert only specific .asd files in the folder to csv files and save graph for each .asd file**
```asdspec2csv.select_n_convert(inputdir, outputdir, individual_mode=True, save_graph=True)```

**to average only specific .asd files in the folder, convert the averaged value to a csv file, and save graph for averaged value**
```asdspec2csv.select_n_convert(inputdir, outputdir, individual_mode=False, save_graph=True)```
