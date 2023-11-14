
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
=======
# Example: Running test script in Conda environment on Windows command line.
1. Make edits within inds/invars.py file
```diff
"""
Set values for table names (future, StdVArs for Python)
"""
#------------------------------------------------
#START EDITS
#------------------------------------------------
- site = 'KPNW'
+ site = 'KPCO'
- lowest_count = 20
+ lowest_count = 6
#------------------------------------------------
#END EDITS
#------------------------------------------------
```
2. Make edits within prog/test_program.py file. 
```diff 
"""
#------------------------------------------------
#START EDITS
#------------------------------------------------
# !!!NOTE: SITE EDITS ARE ALSO NEEDED IN THE FILE invars.py (in the inds sub-directory)

#Ex: root = "//fsproj/cesrtop/PROJECTS/SAS_Alternatives/Programming/Python/python_test_package"
- root = "PATH TO DIRECTORY WHERE YOU UNZIPPED THIS PACKAGE"
+ root = "C:\Documents\SAS_Alternatives\Programming\Python\cesr_altsas_test"
#------------------------------------------------
```
3. Open terminal (CMD line example). Activate Conda environment.
```console
C:\Documents>conda activate pandas_2_0
```
4. Change directory to location of the project. (optional)
```console
C:\Documents>cd "C:\Documents\SAS_Alternatives\Programming\Python\cesr_altsas_test"
```
5. Execute python script.

```console
(pandas_2_0) C:\Documents\SAS_Alternatives\Programming\Python\cesr_altsas_test>python "prog\test_program.py" 
```
Output rendered in command line.
```
KPCO
6
demog
encounters
  gender_identity    mrn  birth_date sex_admin sex_at_birth race1 race2 race3 race4 race5 hispanic sexual_orientation1 sexual_orientation2 sexual_orientation3 needs_interpreter
0              FF  10006  01/01/1994         F            F    IN    UN    UN    UN    UN        N                   Q                   P                   O                 N
1              FF  10011  01/01/1990         F            F    UN    UN    UN    UN    UN        N                   M                   P                   O                 N
2              FF  10013  01/01/1938         F            F    IN    UN    UN    UN    UN        N                   M                   U                   D                 N
3              FF  10017  01/01/1975         F            F    MU    UN    UN    UN    UN        Y                   O                   Q                   P                 N
4              MM  10019  01/01/2014         M            M    AS    UN    UN    UN    UN        Y                   U                   P                   N                 N
 drg_version  drg_value    mrn  enc_id       adate       ddate  atime  dtime enctype encounter_subtype provider admitting_source discharge_status
0           A        416  10056  100375  01/01/1979  01/02/1979    720  49200      IP                AI      bob               IP               SN
1           C        454  42430  100969  01/01/1992  01/05/1992  76800  39300      IP                AI      bob               ED               EX
2           C        454  42430  100969  01/01/1992  01/03/1992  76800  39300      IP                AI      bob               ED               EX
3           B         64  42430  100969  01/01/1992  01/04/1992  76800  39300      IP                AI      bob               ED               EX
4           C       1304  41914  101361  01/01/1995  01/06/1995  65580  63900      IP                AI      bob               IP               RH
```

