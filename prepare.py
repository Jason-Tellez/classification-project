import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split



################### Get value counts for object columns ###################
def check_v_counts(df):
    '''
    This function shows value counts for all columns by looping though each column, checking dtype, and shows appropriate stats
    '''
    x = []
    y = []
    for i in range(len(df.columns)):
        if df[df.columns[i]].dtype == 'object':
            print(f'{df.columns[i]}:\n{df[df.columns[i]].sort_values().value_counts()}\n')
            print('----------\n')
        elif df[df.columns[i]].dtype == 'int64':
            print(f'{df.columns[i]}:\n{df[df.columns[i]].value_counts(bins=5, sort=False)}\n')
            print('----------\n')
            
            

################### Prepare dataframe by editing columns ###################
def  prep_data(df):
    '''
    This function prepares and cleans the data by:
        - adds '.00' to all total_charges values then cast column values as float dtype
        - replaces "Yes" or "No" values with 1 or 0, respectively
        - converts categorical vars to dummy vars then deletes first newly created dummy variable
            > combines dummy columns with original df
        - repeats same dummy var process with deleting any new columns
            > combines dummy columns with original df
        - drops any existing duplicate rows
        - drops unsuable or unnecessary columns
    '''
    # replace empty spaces with 0.00 and convert total_charges to float dtype
    df['total_charges'] = df.total_charges.replace(' ', '0.00').astype(float)
    
    # replace yes/no with 1/ 0
    yes_no_cols = ['paperless_billing', 'partner', 'dependents', 'phone_service', 'churn']
    other_cols = ['online_security', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies']
    for i in yes_no_cols:
        df.replace({i: {'Yes': 1, 'No': 0}}, inplace=True)
    for j in other_cols:
        df.replace({j: {'Yes': 1, 'No': 0, 'No internet service': 0}}, inplace=True)
    df.replace({'multiple_lines': {'Yes': 1, 'No': 0, 'No phone service': 0}}, inplace=True)

    # creates dummy vars for gender and payment_type, drops first new var, concats dummy vars with original df
    dummy_df = pd.get_dummies(df[['gender','payment_type']], dummy_na=False, drop_first=True) 
    df = pd.concat([df, dummy_df], axis=1)

    # creates dummy vars for internet_service_type and contract_type then concats dummy vars with original df
    dummy_df = pd.get_dummies(df[['internet_service_type', 'contract_type']], dummy_na=False)
    df = pd.concat([df, dummy_df], axis=1)

    # drops unusable or unecessary columns and columns with new dummy vars
    df.drop(columns=['customer_id', 'gender', 'contract_type','payment_type', 'internet_service_type', 'contract_type_Two year'], inplace=True)
    
    return df



###################  ###################




###################  ###################




###################  ###################




###################  ###################




###################  ###################




###################  ###################