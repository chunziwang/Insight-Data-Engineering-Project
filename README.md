# Insight-Data-Engineering-Project

This project is a coding challenge by Insight Data Science Program. You can find the detailed problem statement and instructions [Here](https://github.com/InsightDataScience/h1b_statistics).

## Problem

Calculate **Top 10 Occupations** and **Top 10 States** for each year's certified H1B visa applications. The code should be modular, reusable, and could scale to handle large dataset.

## Approach

* I used csv reader to load the input data.
* Since different years have different column names, after careful inspection I used regular expression to find the target columns.
* I created two dictionaries, one for occupation and one for state. I filtered rows to keep the ones that are certified and count the number of each occupation/state.
* In the looping process of every row, I also kept track of the total row counts for calculating the percentage later.
* After that I select the top 10 key and value pairs from the dictionary, calculate percentage by dividing total row counts, and then sort them in descending order of value and ascending order of name, and store the records in a new output file.

## Run Instructions

The script can be found at `./src/h1b_counting.py`. You can run the script using `./run.sh`. 

I have tested it with `./insight_testsuite/run_tests.sh`. If you put `H1B_FY_2014.csv, H1B_FY_2015.csv, H1B_FY_2016.csv` into the input folder and change the file names accordingly (`h1b_input.csv`), it will run successfully too.