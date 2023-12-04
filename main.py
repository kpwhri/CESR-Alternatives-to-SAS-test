
"""
Project: CESR: Alternatives to SAS
Contact: daniel.r.vaughn@kpchr.org
Date: 9/27/2023

See the README.md for instructions on how to run this program.
"""

# read in a configuration script that sets variables


#------------------------------------------------
#MAIN PROGRAM
#------------------------------------------------

import sys
import os
# Call necessary packages
# write code to import a package living in a parent directory
sys.path.append('..')
from StdVars import *
import pandas as pd
import mdutils as md
import logging
from datetime import datetime, date
import shutil
import pyarrow

# create_package_output_folder(package_name, package_output_destination)
# print(share)
# logfile = os.path.join(share, f'{package_name}_{package_ver}_{datetime.now().strftime("%Y%m%d %H.%M.%S")}.log')

#------------------------------------------------
# IMPORT PACKAGES
#------------------------------------------------

# Initialize package variables
root = os.getcwd()
package_name = 'cesr_altsas_test'
package_ver = 0.2

# setup output destinations
pkg_dir, outlocal, share = create_package_output_folder(package_name, package_output_destination)

# Set up logs
logfile = os.path.join(share, f'{package_name}_{package_ver}_{datetime.now().strftime("%Y%m%d %H.%M.%S")}.log')
logging.basicConfig(filename=logfile, level=logging.INFO)
logging.info('Started')
logging.info('Creating output folder')
logging.info(f'Output folder created: {share}')
logging.info(f'Local folder created: {outlocal}')

#Set up input folder
inds = os.path.join(root, 'inds/indata')

#Read in CSV to dataframes
print(fake_vdw_vars['vdw_demographic'])
demog_df = pd.read_csv(os.path.join(inds,fake_vdw_vars['vdw_demographic'] + '.csv'))
encounter_df = pd.read_csv(os.path.join(inds,fake_vdw_vars['vdw_utilization'] + '.csv'))

dataframe_contents_list = [demog_df,encounter_df]


# Merge Demog/Enc
demog_enc_1 = demog_df.merge(encounter_df, on='mrn', how='left')  

# Transform data----------------------------------

# Subset data
av_enc_all = demog_enc_1.loc[demog_enc_1['admitting_source']=='AV'].reset_index()
# Set columns for output
output_columns = ['mrn', 'gender_identity', 'birth_date', 'enctype', 'discharge_status']
av_enc_output = av_enc_all[output_columns]

# Output to csv
output_csv = os.path.join(outlocal, 'av_encounters.csv')
av_enc_output.to_csv(output_csv, index=False)
# Output to parquet
output_parquet = os.path.join(share, 'av_encounters.parquet')
av_enc_output.to_parquet(output_parquet)

#name the dataframe
demog_df.name = 'Demographics'
encounter_df.name = 'Encounters'
av_enc_all.name = 'AV Encounters with Demographics'

# create markdown summaries
local_md = md.MdUtils(file_name=fr'{outlocal}/{package_name}_output.md', title='CESR: Alternatives to SAS')
local_md.new_header(level=1, title='Level 1 Analysis: Contents')
for df in dataframe_contents_list:
    local_md.new_header(level=2, title=f'{df.name}')
    local_md.write(f'\n{df.head().to_markdown()}')
# Create the markdown.
local_md.create_md_file()

logging.info('Create a share markdown file for the QA results')
# create a share markdown file for the QA results
share_md = md.MdUtils(file_name=fr'{share}/{package_name}_output.md', title='CESR: Alternatives to SAS')
share_md.new_header(level=1, title='Level 1 Analysis: Contents')
share_md.new_header(level=2, title=f'{av_enc_all.name}')
logging.info('Writing column names to markdown')
for col in av_enc_all.columns:
    share_md.write(f'1. {col}\n')

# check out gender identity by sex at birth
# create a pivot table of gender identity by sex_at_birth
logging.info('Creating pivot tables')
_gi_pivot = av_enc_all.pivot_table(index=['gender_identity'], columns=['sex_at_birth'], values=['mrn'],  aggfunc='count', fill_value=0)
_race1_pivot = av_enc_all.pivot_table(index=['race1'], columns=['sex_at_birth'], values=['mrn'],  aggfunc='count', fill_value=0)
_hispanic_pivot = av_enc_all.pivot_table(index=['hispanic'], columns=['sex_at_birth'], values=['mrn'],  aggfunc='count', fill_value=0)
_sexual_orientation1_pivot = av_enc_all.pivot_table(index=['sexual_orientation1'], columns=['sex_at_birth'], values=['mrn'],  aggfunc='count', fill_value=0)
_discharge_pivot = av_enc_all.pivot_table(index=['discharge_status'], columns=['sex_at_birth'], values=['mrn'],  aggfunc='count', fill_value=0)
logging.info('Pivot tables created')
# write the pivot tables to the share markdown file
logging.info('Writing pivot tables to markdown')
share_md.new_header(level=2, title='Gender Identity')
share_md.write(f'\n{_gi_pivot.to_markdown()}')
share_md.new_header(level=2, title='Race 1')
share_md.write(f'\n{_race1_pivot.to_markdown()}')
share_md.new_header(level=2, title='Hispanic')
share_md.write(f'\n{_hispanic_pivot.to_markdown()}')
share_md.new_header(level=2, title='Sexual Orientation 1')
share_md.write(f'\n{_sexual_orientation1_pivot.to_markdown()}')
share_md.new_header(level=2, title='Discharge Status')
share_md.write(f'\n{_discharge_pivot.to_markdown()}')
share_md.create_md_file()

# create a zip file of the output
logging.info('Creating zip file')
share_zip = os.path.join(pkg_dir, f'{package_name}_v{package_ver}_{local_config["site"]}_{date.today()}.zip')    
shutil.make_archive(share_zip, 'zip', share)
logging.info('Finished')
   
# END
