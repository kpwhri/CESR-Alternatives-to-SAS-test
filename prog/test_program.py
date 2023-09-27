
"""
Project: CESR: Alternatives to SAS
Contact: daniel.r.vaughn@kpchr.org
Date: 9/27/2023

Instructions:
    See workplan in the 'Document' folder of the zip package for full instructions.
    If you will be running this program from command line or in batch mode, please skip to step 5
    
    1. Make site edits below and in the invars.py file in the inds folder
    2. Run this program interactively or through command line interface. If you are new to Python,
        I recommend running interactively to start

"""

#------------------------------------------------
#START EDITS
#------------------------------------------------

# !!!NOTE: SITE EDITS ARE ALSO NEEDED IN THE FILE invars.py (in the inds sub-directory)

#Ex: root = "//fsproj/cesrtop/PROJECTS/SAS_Alternatives/Programming/Python/python_test_package"
root = "PATH TO DIRECTORY WHERE YOU UNZIPPED THIS PACKAGE"

#------------------------------------------------
#------------------------------------------------
#------------------------------------------------
#------------------------------------------------

#------------------------------------------------
#SET DIRECTORIES
#------------------------------------------------

inds = root + "/inds"
outlocal = root + "/local_only"
prog = root + "/prog"
outds = root + "/outds"


#------------------------------------------------
#IMPORT PACKAGES
#------------------------------------------------

#Call necessary packages
import pandas as pd
import os
import sys

#Set directory
os.chdir(root)

#Import variables
path = os.path.abspath(inds)
sys.path.append(path)

import invars

#Check that variables were set
print(invars.site)
print(invars.lowest_count)
print(invars.vdw_demographic)
print(invars.vdw_utilization)

#------------------------------------------------
#MAIN PROGRAM
#------------------------------------------------

#Read in CSV to dataframes
demog = pd.read_csv(inds + "/indata/" + invars.vdw_demographic + ".csv")
encounter = pd.read_csv(inds + "/indata/" + invars.vdw_utilization + ".csv")

#Check data if you like
print(demog.head())
print(encounter.head())

#Merge Demog/Enc
demog_enc_1 = demog.merge(encounter, on='mrn', how='left')

#Transform data----------------------------------

#Subset data
av_enc_all = demog_enc_1[demog_enc_1['admitting_source']=='AV']
#Set columns for output
av_enc_output = demog_enc_1[['mrn', 'gender_identity', 'birth_date', 'enctype', 'discharge_status']].copy()

#Output to csv
av_enc_output.to_csv(outds + "/av_encounters.csv", index=False)


#-----------------------------------------
#END PROGRAM
#-----------------------------------------





