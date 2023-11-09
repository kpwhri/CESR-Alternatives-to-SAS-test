# select an output destination for the package
# - use forward slashes ONLY: you'll be OK Windows people.

package_output_destination = '//server.name.institution.org/where/output/lives'

################################################
# DO NOT EDIT BELOW THIS LINE
################################################

# create a function that checks if the package exists in the package_output_destination, if it does not exist, create a new folder with the package_name, otherwise do nothing
def create_package_output_folder(package_name, package_output_destination):
    import os
    global tar_dir, outlocal, share
    tar_dir = os.path.join(package_output_destination, package_name)
    outlocal = os.path.join(tar_dir,'local_only')
    share = os.path.join(tar_dir,'share')
    if os.path.exists(tar_dir):
        print('Package already exists')        
    else:
        os.mkdir(tar_dir)
        os.mkdir(outlocal)
        os.mkdir(share)
        print(f'Package created {tar_dir}')
    print(f'Package location: {tar_dir}')
    print(f'Package outlocal: {outlocal}')
    print(f'Package share: {share}')
    return tar_dir, outlocal, share


# create a dictionary that contains the attributes required to read/write data
# the attributes are:
# - database_type: the type of database to be used to determine the database connection string
# - connection_string: the connection string to the database
# - table_name: the name of the table in the database
# - common_name: the official HCSRN table_name to be used in distributed code
# - columns: a dictionary of columns in the table
# - columns_type: the types of the columns of the table in the database
# - table_columns_names: the friendly names of the columns of the table in the database

local_config = {'site'              :   'KPNW',
                'lowest_count'      :   20,
}



#------------------------------------------------
#SET FAKE VDW VARIABLES
#------------------------------------------------
fake_vdw_vars = {  'vdw_demographic'   :   'demog',
                   'vdw_utilization'   :   'encounters',
                   'vdw_px'            :   'px',}