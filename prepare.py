import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

            

################### Prepare dataframe by editing columns ###################
def  prep_data(df):
    '''
    This function prepares and cleans the data by:
        - drops rows with empty total_charges values
        - replaces "Yes" or "No" values with 1 or 0, respectively
        - converts categorical vars to dummy vars then deletes first newly created dummy variable
            > combines dummy columns with original df
        - repeats same dummy var process with deleting any new columns
            > combines dummy columns with original df
        - drops any existing duplicate rows
        - drops unsuable or unnecessary columns
        - creates new column 'tenure_years'
    '''
    # replace empty spaces with 0.00 and convert total_charges to float dtype
    df.drop(index=df[df.total_charges==' '].index.values.tolist(), inplace=True)
    df['total_charges'] = df.total_charges.astype(float)
    
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
    
    # adds tenure years column
    df['tenure_years'] = round(df.tenure / 12, 1)
    
    return df



################### Train, validate, and test ###################
def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate.churn)
    return train, validate, test