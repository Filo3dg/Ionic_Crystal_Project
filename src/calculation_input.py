#from mp_api import MPRester
#import crystal_functions.file_readwrite as cffr
#import db_query as bset
#import os
#import json
#import sys

# This class will read the csv used as input and update the status database with the new structures to run
class Status_db_control:

    def __init__(self):
        pass

    # This function will take the input file and compare it with a csv copy of the status database and in such case
    # they'll be added to such database
    def read_csv(self, ipt: str):
        import pandas as pd
        import sys

        try:
            ipt = open(ipt, 'r')
            data = open(self, 'a+')
            ipt_lines = ipt.readlines()
            print('ipt:', ipt_lines)
            data.seek(0)
            data_lines = data.readlines()
            print('data:', data_lines)
            ipt_len = len(ipt_lines)
            data_len = len(data_lines)
            len_diff = ipt_len-data_len
            starting_index = ipt_len-len_diff

            if len_diff > 0:
                for indexes in range(starting_index, ipt_len):
                    data_lines.append(ipt_lines[indexes])
                    print('data_lines:', data_lines)

                for index in range(data_len, len(data_lines)):
                    data.seek(data_len)
                    data.write(data_lines[index])

            ipt.close()
            data.close()

            self.status = pd.read_csv(self, sep='\s+')

        except:
            print('Try again with a csv file!')
            sys.exit(1)

        for i in range(len(self.index)):
            if self.status['TORUN'][i] == '-':
                self.status['TORUN'][i] = True

            if self.status['OPTCONV'][i] == '-':
                self.status['OPTCONV'][i] = 'To run'

            if self.status['FREQCONV'][i] == '-':
                self.status['FREQCONV'][i] = 'To run'

            if self.status['FREQVIRT'][i] == '-':
                self.status['FREQVIRT'][i] = 'To run'

        return self

    # This function will update the database with the newly added structure
    # the input has to be a pandas Dataframe
    def database_update(self):

        import db_query

        data = self.status

        conn = db_query.connect_db('status/status.db')
        data.to_sql('Status', conn, if_exists='replace', index=False)
        conn.close()

    # This function will update the csv form of the status database
    # to its latest form for the daily update of the structure to run
    def daily_update(self):

        data = self.status
        data.to_csv('data_track.csv', sep='\s+')


# This class will process the database and generate the stucture for the
# ones that have been recently added to the database
class Structure_gen:

    def __init__(self):
        pass

    def torun_check(self):

        data = self.status

        self.torun = data.loc[data['TORUN' == True]]

        return self
