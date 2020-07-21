# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:37:45 2020

@author: dkochar1
"""

import os
import pandas as pd
import numpy as np

def transfrom_openscape_queue_report():
    
    # Select xls files from files list
    files_xls = [f for f in os.listdir(os.getcwd()) if f[-3:] == 'xls']
    
    # Initialize empty dataframe
    df = pd.DataFrame()
    
    #Create counter for date_id
    date_id_counter = 1
    
    # Loop over files list to append to empty dataframe
    for f in files_xls:
        # Read in Excel to get report date
        dte = pd.read_excel ( f, header = 1, usecols = "B", nrows = 1, encoding = 'utf-8' )
        # Rename column
        dte.columns = ['report_date_range']   
        # Add date_id field to use in subsequent join
        dte['date_id'] = date_id_counter
        # Format date values
        dte['report_begin_date'] = dte['report_date_range'].str.replace('to', '').str[0:10].str.strip()
        dte['report_end_date']   = dte['report_date_range'].str.replace('to', '').str[-10:].str.strip()

        # Read in Excel to get report data
        data = pd.read_excel ( f, header = [0, 1], skiprows = 8, skipfooter = 3, encoding = 'utf-8' )
        # combine multi-level header columns to one level for header row, and clean header row
        data.columns = (pd.Series(data.columns.get_level_values(0)).apply(str)
                     + '_'
                     + pd.Series(data.columns.get_level_values(1)).apply(str)).str.strip().str.lower().str.replace(' ', '_').str.replace('unnamed:_0_level_0_', '').str.replace('unnamed:_1_level_0_', '').str.replace('unnamed:_2_level_0_', '').str.replace('unnamed:_3_level_0_', '')
        #Create defaulted report type attribute
        data['report_type'] = 'Queue, Historical'   
        #Add file name column
        data['file_name'] = f 
        #Create Company Attribute
        data['company'] = np.where(data.name_0 == 'HAP', 'HAP', None)
        data['company'] = data.groupby('file_name')['company'].fillna(method = 'pad')
        #Create start time attribute
        data['start_time'] = '08:00:00 AM'
        #Create end time attribute
        data['end_time'] = '11:59:00 PM'
        #Create time interval attribute
        data['time_interval'] = '15 Minute'
        #Create timezone attribute
        data['time_zone'] = 'Central reporting site'
        #Remove Company Roll-up row
        data = data[data.name_0 != 'HAP'] 
        #Remove odd characters from queue name column
        data['name_0'] = data['name_0'].str.replace ( '’', '\'' )
        #Rename columns from multi-level header combining
        data['service_level'] = data['received_contacts_service_level']
        data['abandon_rate'] = data['received_contacts_abandon_rate']
        # Add date_id field to use in subsequent join
        data['date_id'] = date_id_counter
        #Join dates and raw data dataframes
        df_inner = pd.merge(data, dte, on = 'date_id', how = 'inner', sort = False)
        #Create call time column
        df_inner['call_time'] = np.where ( df_inner['name_0'].str.contains(':'), df_inner['name_0'], None )
        #Create call date column for files with multi-day date range
        df_inner['call_dt'] = np.where ( df_inner['name_0'].str.contains('/'), df_inner['name_0'],
                              np.where ( df_inner['report_begin_date'] == df_inner['report_end_date'], df_inner['report_begin_date'], None ))
        #Select only valid names for name column
        df_inner['name_0'] = np.where ( ~df_inner['name_0'].str.contains(':') & ~df_inner['name_0'].str.contains('/'), df_inner['name_0'], None )     
        #Fill null name values with previous value
        df_inner['name_0'] = df_inner.groupby('file_name')['name_0'].fillna(method = 'pad')
        #Fill null call date values with previous value
        df_inner['call_dt'] = df_inner.groupby(['file_name', 'name_0'])['call_dt'].fillna(method = 'pad')
        #Select only rows with elapsed time
        df_inner = df_inner[df_inner.call_time.notnull()]
        #Append joined dataframes
        df = df.append(df_inner, sort = True)
        #Increment date id counter
        date_id_counter += 1
    
    # Drop unneeded columns
    df = df.drop(['date_id', 'report_begin_date', 'report_end_date', 'file_name'], 1)
    #Re-order dataframe columns
    df = df[[ 'report_type', 'report_date_range', 'start_time', 'end_time', 'time_interval', 'time_zone', 'company',
	          'name_0', 'call_dt', 'call_time', 'received_contacts_all', 'service_level', 'abandon_rate', 
              'abandoned_contacts_abandoned', 'average_wait_time_answered', 'answered_contacts_all', 
			  'user_involvement_time_average', 'user_involvement_time_total', 'maximum_wait_time_answered' ]]
    # Write appended dataframes to csv
    df.to_csv('Queue_Report.csv', encoding = 'utf-8', index = False)
   
if __name__ == '__main__':
    transfrom_openscape_queue_report()
