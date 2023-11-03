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
