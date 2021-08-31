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

## Acquire
