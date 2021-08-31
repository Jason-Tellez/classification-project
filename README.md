# Classification Project
___


## Plan
### Objectives

- Document code, data-pipeline processes, results, and key takeaways.
- Create the necessary modules that allow for repeatable testing (.py files)
- Construct models to predict customer churn using classification techniques to find best model.
- Deliver brief presentation with walkthrough using final Jupyter Notebook; adjust presentation to target audience (Codeup Data Science team).
- Answer panel questions about code, process, findings, key takeaways, and model.


### Goals

- Find potential drivers for customer churn at Telco.
- Construct ML classification models that accurately predict customer churn rate.
- Document your process well enough to be presented or read like a report.
___

## Deliverables

- **Highly**-commented final Jupyter notebook that will be used for a final walkthrough
- .py mmodules that hold functions from Acquire and Prepare phases
- .csv file with customer_id, probability of churn, and prediction of churn (1=churn, 0=not_churn).
___

## Data Dictionary

|Target|Datatype|Definition|
|:-------|:-------|:----------|
|churn|7032 non-null: int64|0: no churn, 1: churn|

|Feature|Datatype|Definition|
|:-------|:-------|:----------|
senior_citizen                         | 7043 non-null: int64    | 0: not senior, 1: senior |
partner                                | 7043 non-null: int64    | 0: not partners, 1: has partners |
dependents                             | 7043 non-null: int64    | 0: no dep, 1: has dep |
tenure                                 | 7043 non-null: int64    | tenure in months |
phone_service                          | 7043 non-null: int64    | 0: no phone, 1: has phone |
multiple_lines                         | 7043 non-null: int64    | 0: doesnt have multiple lines, 1: has multiple lines |
online_security                        | 7043 non-null: int64    | 0: no online security, 1: has online security |
device_protection                      | 7043 non-null: int64    | 0: no device protection, 1: has device protection |
tech_support                           | 7043 non-null: int64    | 0: no tech support, has tech support |
streaming_tv                           | 7043 non-null: int64    | 0: no tv streaming, 1: has tv streaming |
streaming_movies                       | 7043 non-null: int64    | 0: no movie streaming, 1: has movie streaming |
paperless_billing                      | 7043 non-null: int64    | 0: no movie streaming, 1: has movie streaming |
monthly_charges                        | 7043 non-null: float64  | monthly customer charges in dollars and cents | 
total_charges                          | 7043 non-null: float64  | total customer charges in dollars and cents |
gender_Female                          | 7043 non-null: uint8    | 0: is female, 1: is male |
gender_Male                            | 7043 non-null: uint8    | 0: no DSL, 1: has DSL |
internet_service_type_DSL              | 7043 non-null: uint8    | 0: no  DSL, 1: has DSL |
internet_service_type_Fiber optic      | 7043 non-null: uint8    | 0: no Fiber, 1: has Fiber |
internet_service_type_None             | 7043 non-null: uint8    | 0: no internet, 1: has internet |
payment_type_Credit card (automatic)   | 7043 non-null: uint8    | 0: no auto credit card, 1: has auto credit card |
payment_type_Electronic check          | 7043 non-null: uint8    | 0: no movie streaming, 1: has movie streaming |
payment_type_Mailed check              | 7043 non-null: uint8    | 0: no movie streaming, 1: has movie streaming |
contract_type_One year                 | 7043 non-null: uint8    | 0: no movie streaming, 1: has movie streaming |
contract_type_Two year                 | 7043 non-null: uint8    | 0: no movie streaming, 1: has movie streaming |
___

## Hypotheses

**Hypothesis 1**

- H_{0}: churn and customer having tech support are independent
- H_{a}: churn and customer having tech support are dependent

alpha = 0.05

Result: We reject the null hypothesis! Churn and customer having tech support are dependent.


**Hypothesis 2**

- H_{0}: Monthly charge is the same with fiber optic internet
- H_{a}: Monthly charge is not the same with fiber optic internet

alpha = 0.05

Result: We reject the null hypothesis! Monthly charge is not the same with fiber optic internet.


**Hypothesis 3**

H_{0}: Mean of total charges of customers who are churned <= Mean total charges of all customers

H_{a}: Mean of total charges of customers who are churned > Mean total charges of all customers

alpha = 0.05

Result: We fail to reject the null hyposthesis! The mean of total charges of customers who are churned <= Mean total charges of all customers
___

## Executive Summary

- I found that the main drivers of churn were price,
    - On average, customers that churned paid a higher monthly fees than the retained counterparts
- I used three different models and all performed better than my baseline
    - I chose my Logistic Regression Model as my MVP

**Recommendations**
- Since month-to-month users have the highest churn rate of all, consider giving discounts to those with more service
- Consider making tech support standard for ll customers

**Next Steps**
- tune adjusting hyperparamets of models
- pruning the columns more
- scaled the data, if necessary
___

## Data Science Pipeline

### Plan
- Create README.md file detailing
    - DS pipeline process
    - instructions on how to repeat pipeline process
    - initial hypotheses and conclusions
    - key findings, recommendations, and takeaways
- Create Jupyter Notebook documenting and commenting necessary
    - code
    - reasoning
    - findings
    - takeaways
- Create modules that hold useful functions
- Create CSV file with customer_id, probability of churn, and prediction of churn (1=churn, 0=not_churn).
- Present final notebook to Codeup Data Science team
- Answer questions stoically 
- Identify key drivers of customer churn from Telco
- Create ML models to predict customer churn
- Document process

### Acquire
In Your acquire.py module:
- Store functions that are needed to acquire data from the customers table from the telco_churn database on the Codeup data science database server; make sure your module contains the necessary imports to run your code. You will want to join some tables as part of your query.
- Your final function should return a pandas DataFrame.
In Your Notebook:
- Import your acquire function from your acquire.py module and use it to acquire your data in your notebook.
- Complete some initial data summarization (.info(), .describe(), .value_counts(), ...).
- Plot distributions of individual variables.

### Prepare
In Your prepare.py module

- Store functions that are needed to prepare your data; make sure your module contains the necessary imports to run your code. Your final function should do the following:
- Split your data into train/validate/test.
- Handle Missing Values.
- Handle erroneous data and/or outliers you wish to address.
- Encode variables as needed.
- Create any new features, if you decided to make any for this project.
In Your Notebook
- Explore missing values and document takeaways/action plans for handling them.
- Is 'missing' equivalent to 0 (or some other constant value) in the specific case of this variable?
- Should you replace the missing values with a value it is most likely to represent, like mean/median/mode?
- Should you remove the variable (column) altogether because of the percentage of missing data?
- Should you remove individual observations (rows) with a missing value for that variable?
- Explore data types and adapt types or data values as needed to have numeric represenations of each attribute.
- Create any new features you want to use in your model.
- Create a new feature that represents tenure in years.

### Explore
In Your Notebook
- Answer key questions, your initial hypotheses from , and figure out the drivers of churn. You are required to run at least 2 statistical tests in your data exploration. Make sure you document your hypotheses, set your alpha before running the tests, and document your findings well.
- Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). The goal is to identify features that are related to churn (your target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
- Summarize your conclusions, provide clear answers to your specific questions, and summarize any takeaways/action plan from the work above.

### Model & Evaluate 
In Your Notebook
- You are required to establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
- Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
- Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
- Feature Selection (optional): Are there any variables that seem to provide limited to no additional information? If so, remove them.
- Based on the evaluation of your models using the train and validate datasets, choose your best model that you will try with your test data, once.
- Test the final model on your out-of-sample data (the testing dataset), summarize the performance, interpret and document your results.

### Deliver
- Introduce yourself and your project goals at the very beginning of your notebook walkthrough.
- Summarize your findings at the beginning like you would for an Executive Summary. Just because you don't have a slide deck for this presentation, doesn't mean you throw out everything you learned from Storytelling.
- Walk us through the analysis you did to answer our questions and that lead to your findings. Relationships should be visualized and takeaways documented. Please clearly call out the questions and answers you are analyzing as well as offer insights and recommendations based on your findings.
- Finish with key takeaways, recommendations, and next steps and be prepared to answer questions from the data science team about your project.
- Practice.
___

## How to recreate
1. Download this README.md file for instructions and purpose of report
2. Import tour own credentials to env.py file for access to SQL database
3. Import acquire.py, prepare.py, and explore.py(optional)
4. Download final_notebook.ipynb
5. Compare results