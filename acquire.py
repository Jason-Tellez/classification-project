import os
from env import host, user, password
import numpy as np
import pandas as pd


################### Connects to Sequel Ace using credentials ###################

def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    It takes in a string name of a database as an argument.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

    
################### Create new dataframe from SQL db ###################
    
def new_telco_data():
    '''
    This function reads the telco data from the Codeup db into a df,
    writes it to a csv file, and returns the df.
    '''

    # Create SQL query.
    sql_query = """
           SELECT c.customer_id,
                c.gender, 
                c.senior_citizen,
                c.partner,
                c.dependents,
                c.tenure,
                c.phone_service,
                c.multiple_lines,
                c.online_security,
                c.device_protection,
                c.tech_support,
                c.streaming_tv,
                c.streaming_movies,
                c.paperless_billing,
                c.monthly_charges,
                c.total_charges,
                c.churn,
                ct.contract_type,
                i.internet_service_type,
                p.payment_type
            FROM customers as c
            JOIN contract_types as ct USING (contract_type_id)
            JOIN internet_service_types as i USING (internet_service_type_id)
            JOIN payment_types as p USING (payment_type_id);
                """
    
    # Read in DataFrame from Codeup's SQL db.
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    
    return df


################### Acquire existing csv file ###################

def get_telco_data():
    '''
    This function reads in telco data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('telco_df.csv'):
        
        # If csv file exists, read in data from csv file.
        df = pd.read_csv('telco_df.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame.
        df = new_telco_data()
        
        # Write DataFrame to a csv file.
        df.to_csv('telco_df.csv')
        
    return df


################### Dataframe overview ###################

def gen_view(df):
    '''
    This function will give a general overview of a dataframe.
    This includes:
        - statistical description of the df's numerical values
        - info about df's columns and their values
        - dimensions (rows x columns) of df
        - if any null values exist in each column
        - if any observations/rows are duplicated
        - return columns value counts
    '''
    print('------------------------------')
    print('General overview of dataframe.')
    print('------------------------------\n')
    print('Descriptive stats:\n')
    print(df.describe())
    print('\n')
    print('Column and row info:')
    print(df.info())
    print('\n')
    print('Dimensions of df:')
    print(df.shape)
    print('\n')
    print('Null values:')
    print(df.isnull().sum())
    print('\n')
    dups = df['customer_id'].duplicated().any()
    print('Any duplicates:', dups)
    print('\n')
    for i in range(len(df.columns)):
        if df[df.columns[i]].dtype == 'object':
            print(f'{df.columns[i]}:\n{df[df.columns[i]].value_counts().sort_values()}\n')
            print('----------\n')
        elif df[df.columns[i]].dtype == 'int64':
            print(f'{df.columns[i]}:\n{df[df.columns[i]].value_counts(bins=5, sort=False)}\n')
            print('----------\n')
            
            
################### Plots histograms of column-distributions ###################

def plot_dist(quant_vars, cat_vars):
    '''
    Function loops through all columns and plot each distribution.
    '''
    for col in df.columns[1:]:
        plt.title(f'Histogram for {col}')
        sns.histplot(x=df[col], hue=df.churn, bins=10)
        plt.show()