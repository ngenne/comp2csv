# comparison
A little program to be able to compare 2 CSV files between them and to see where the differences are.

# Files

Please find a description of the files below :

 - [comparison.py](https://github.com/ngenne/comp2csv/blob/master/comparison.py)
 - _build_/comparaison_v2
 - _dist_

All files included in __build__ and __dist__ directories are necessary to load the program which working on Windows (all versions).
Please pay attention to have installed Python3 on your system to make the script working.


# Usage
You need to compare differences between two CSV files about their content. So use this script to make it.
## Python script
Open a Terminal or a CMD prompt and write this command :

	> python3 comparison.py file1 file2
Make sure to write the abolute path (between double quotes " ") to the _file1_ and _file2_.
This command will create an output file named "output.txt" in place of the directory you launched the script. The file will contain the number of differences between the files.

## Windows executable
Open a CMD prompt (on Windows) and write this command :

	> comparison.exe file1 file2
Make sure to write the abolute path (between double quotes " ") to the _file1_ and _file2_.
Same as Python script part above, it will create an output file named "output.txt" in place of the directory you launched the exe file.

