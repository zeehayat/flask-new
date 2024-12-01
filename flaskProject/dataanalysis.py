import os.path

import pandas as pd
class DataAnalysis:

    def read_file(self, filename, column_to_find_keyword, keyword):
        # Find csv file in the directory... There should be only one..

        if os.path.exists(filename):
            df=pd.read_csv(filename)
            #ds_key=df[column_to_find_keyword].str.find(keyword)
            df.dropna(inplace=True)
            idx=df[column_to_find_keyword].str.contains(keyword)

            return df[idx].to_json()

            #f = open(filename, 'r')
            #return f.read()
        else:
            return 'No File Found'

    def search_for_titles_by_genre(self, genre):

        return ''
    def read_raw_csv_file_and_return_data(self,filename):
        if os.path.exists(filename):
            if(filename.endswith('.csv')):
                df=pd.read_csv(filename)

                return df.to_html()
            else:
                return 'CSV File Not found'
        else:
            return 'No File Found'


