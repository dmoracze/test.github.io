import pandas as pd
import datetime
import argparse
from glob import glob

dict_cols = ['subject_id', 'site_id', 'age', 'sex', 'dob']

def checks(file):
    df = pd.read_csv(file)

    # check column names
    if not all(item in list(df.columns) for item in dict_cols):
        raise Exception('Column names do not match data dictionary!')
        
    # check age range
    if (min(df['age'] < 0)) or (max(df['age']) > 80):
        raise Exception('Ages are not in an appropriate range!')
        
    # check sex
    if not all([item==0 or item==1 for item in df['sex']]):
        raise Exception('Sex must be either 0 or 1')
        
    # check date of birth format
    try:
        dates = [datetime.date.fromisoformat(item) for item in df['dob']]
    except:
        print('Dates are not in an appropriate format')

def main():
    # parser
    parser = argparse.ArgumentParser()
    parser.add_argument('team_name', type=str)
    args = vars(parser.parse_args())

    # find file
    file = glob(f'./data/{args["team_name"]}/*_data.csv')

    # more than 1 data file?
    if len(file)>1:
        raise Exception('More than one data file found!')
    elif len(file)==0:
        raise Exception('No data file found!')
    else:
        print(f'Checking data file: {file[0]}')
        checks(file[0])

if __name__ == "__main__":
    main()