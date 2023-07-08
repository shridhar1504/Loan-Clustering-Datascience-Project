# Loan-Clustering-Datascience-Project
This project uses Machine Learning to Cluster loan together based on their similarities. The project uses a dataeset of loan application which includes information about the Loan amount and Balance. The project then use the clustering algorithm to group the loan together based on the similarities.
## Problem Statement :
The main aim of the project is to group the clusters based on the loan amount and balance of the applicant's data. The clusters can be used to identify the similarities between the applicant's behaviourial pattern in repayment of the loan based on the provided data. 
## Solution Approach :
With the help of Structured Query Language (SQL), transforming the data with the bunch of datasets which has different informations on Customer's behaviourial pattern. By the following structural mapping, joining the datasets to get the final data.  


`image` ![Dataset SQL Formatting](https://github.com/shridhar1504/Loan-Classification-Datascience-Project/assets/113985416/984a2561-6d2f-4656-bfe2-e47f970c175d)

 K-Means Algorithm can be used to cluster the model and group it by the similarities between them. These models are trained on historical data of loan applications and using this data which learns with the relationship between loan amount and balance. Once a model is trained, the cluster can be grouped using the model for the futuristic data.
## Observations : 
The clustering model can vary depending on the dataset that is used to train the model. The Bank had given applicant's details in individual CSV Files. For the predictive modeling,by using SQL; the datasets should be joined or merged using various statements which can have all the necessary column to form the final data in a csv format. The individual datasets and details of the datasets are as follows:

 * Account - The dataset has account id, district id, frequency & date.
 * Card - The dataset has card id, disposition id, type & issued.
 * Client - The dataset has client id , birth number alomg with district id.
 * Disp - The dataset has disposition id, client id, account id, type.
 * District - The dataset has different factors such as A1 - A16 which includes much datas than the other datasets but not explained in a well manner.
 * Loan - The dataset has loan id, account id, date, amount, duartion, payment & status.
 * Order - The dataset has order id, account id, bank to, account to, amount, k_symbol.
 * Transaction Data - The dataset has transaction id, account id, date, type, operation, amount, balance, k_symbol, bank & account.
## Findings :
Loan clustering can be used to identify groups of borrowers with similar loan amounts and balances. This can be useful for lenders to target marketing campaigns or to develop new loan products. Loan clustering can also be used to identify borrowers who are at a higher risk of default.
## Insights :
Loan clustering can be used to improve the efficiency of loan lending by helping lenders to better understand their borrowers. Loan clustering can also be used to identify borrowers who are at a higher risk of default, which can help lenders to take steps to mitigate their risk. Loan clustering can be used to identify trends in the lending market. Loan clustering can be used to develop new risk models. Loan clustering can be used to improve the customer experience.
