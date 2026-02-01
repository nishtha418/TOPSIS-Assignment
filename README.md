# TOPSIS Assignment

This repository contains the complete implementation of the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) method as required in the assignment. The assignment is implemented in three parts: a command-line program, a Python package, and a web service.

---

## Part-I: Command Line Implementation of TOPSIS

### Description
A Python-based command-line program that implements the TOPSIS algorithm using an input CSV file, user-defined weights, and impacts.

### Command Line Usage
python topsis.py <InputDataFile> <Weights> <Impacts> <OutputFileName>

### Example
python topsis.py data.csv "1,1,1,2,1" "+,+,-,+,+" output.csv

### Features
- Validates number of input arguments  
- Handles file not found exceptions  
- Ensures minimum three columns in input file  
- Validates numeric values in criteria columns  
- Validates weights and impacts  
- Supports benefit (+) and cost (-) criteria  
- Outputs TOPSIS score and rank in CSV format  

---

## Part-II: Python Package for TOPSIS

### Package Name
Topsis-Nishtha-102303805

### Description
The TOPSIS logic is implemented as a reusable Python package. The package can be installed locally using pip and executed directly from the command line.

### Installation
pip install ./Topsis-Nishtha-102303805

### Usage
python -m topsis data.csv "1,1,1,2,1" "+,+,-,+,+" output_pkg.csv

### Testing
The package was installed locally and tested using the above command. The output file successfully contains TOPSIS scores and ranks.

---

## Part-III: TOPSIS Web Service

### Description
A Flask-based web service that allows users to compute TOPSIS using a browser interface.

### Web Service Features
- Upload input CSV file  
- Enter weights and impacts  
- Enter email ID  
- Backend computes TOPSIS  
- Result file is sent to the user via email  

### Running the Web Service
cd topsis_web  
python app.py  

Open the browser and visit:  
http://127.0.0.1:5000

### Email Functionality
Email sending is implemented using SMTP. Due to Gmail security restrictions, an App Password is required for authentication.

---

## Input File Format
- First column: Alternatives (non-numeric)  
- Remaining columns: Criteria values (numeric only)  
- Minimum three columns required  

---

## Output File Format
- Original input data  
- Additional columns:  
  - Topsis Score  
  - Rank  

---

## Technologies Used
- Python  
- Pandas  
- NumPy  
- Flask  
- SMTP (Email)  
- GitHub  

---

## Author
Nishtha Goyal  
Roll Number: 102303805

