# CESR_ALTSAS_TEST
The purpose of this workplan is to test the python ALTSAS package. The package completes the following tests:
1. Share code via GitHub that requires no editing of file paths
1. Create a requirements.txt file and run
1. Create and import a StdVars analog for site-specific environment variables
1. Create a destination folder for the output files
1. Write data to a parquet file
1. Write data to a csv file
1. Write a log file
1. Write a markdown file


## Package maintainer contacts
Contact information for the package maintainers is listed below. Please contact the maintainers if you have questions about the package or the workplan.
Workgroup lead:
* Primary contact: Dan Vaughn
* Institution: KPCHR
* Email: Daniel.R.Vaughn@kpchr.org

Package contact:
* Author 1: Al Derus
* Institution: KPWHRI
* Email: Alphonse.Derus@kp.org

## Project Stage
Please run this code and return results.

## Workplan Timeline
Please complete the workplan by December 20, 2023.

## Workplan Package

Number and Type of Files to be Returned: 
1 zip file containing:
1. 1 log file
1. 1 parquet file
1. 1 markdown file


> **IMPORTANT**
> Prior to running the plan, you'll need to do the following:
1. Create a centralized folder to contain VDW scripts. This allows us to clone repositories directly into the folder and run the code without having to update file paths in distributed code.
1. Copy [StdVars.py](\document\StdVars.py) to the centralized folder. This file contains the standard variables used in all VDW workplans.


# Running this workplan
1. Clone this repository into the centralized folder.
1. Run the requirements.txt file to install the necessary packages.

> **NOTE**
> This code allows the package to read StdVars.py.
```python
sys.path.append('..')
from StdVars import *
```

> **Important**
> Open a command line and navigate to the folder containing the workplan. Run the following command:
```python
pip install -r requirements.txt
```

 Review the log for ERRORS or WARNINGS.  If there are problems, please send a full log to the workgroup leads (contact info at top of workplan), after first making sure the log is redacted of PHI and any site-specific information that your site does not want released. If there are no ERRORS or WARNINGS, please send an email to the workgroup leads stating that the log was reviewed and that there were no problems.

Directions to transfer data:
* Upload the zip file to the HCSRN folder on the [KP Washington SFT](https://projects.kpwashingtonresearch.org/SFT/main/login.aspx)