# Introduction

The purpose of this project was to create two Python scripts: 
- PyBank: Analyzing the financial records of a company
- PyPoll: Help a rural town modernize its vote-counting process

## PyBank

This folder contains:
- Resource Folder
  - budget_data.csv: The raw data file 
- Analysis Folder
  - pybank_main.py: The main script that runs the analysis
  - pybankanalysis.txt: The output textfile of the analysis

The Python script will analyze the records to calculate each of the following:
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The average of the changes in "Profit/Losses" over the entire period
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in losses (date and amount) over the entire period

The script will both print the analysis to the terminal and export a text file with the results.

## PyPoll

This folder contains:
- Resource Folder
  - election_data.csv: The raw data file 
- Analysis Folder
  - pypoll_main.py: The main script that runs the analysis
  - pypollanalysis.txt: The output textfile of the analysis

The Python script will analyze the votes and calculates each of the following:
- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote

The script will both print the analysis to the terminal and export a text file with the results.
