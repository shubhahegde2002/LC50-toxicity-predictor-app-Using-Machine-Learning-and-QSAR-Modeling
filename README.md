# Prediction of LC50 value QSAR models
Prediction of LC50 value using Quantitative structure activity relationship models (QSAR models) Prediction of LC50 value using Quantitative structure-activity relationship models (QSAR models) 
Develop quantitative regression QSAR models to predict acute aquatic toxicity towards the fish fathead minnow ( Pimephales promelas ) on a set of 908 chemicals based on 6 molecular descriptors using multiple Regressor Models:
K-Nearest Neighbours
Multiple Linear Regression
XGBooost Regressor
Support Vector Machine Regressor
Random Forest Regressor
Bayesian Ridge Regressor

Calculate Training time, Prediction time, R squared value, MAE value, RMSE value for every model, save results to csv file and serialize most optimal model using pickle dump.
Dyanmically load data into  database by integrating Python with MySQL and setting up a Flask Web Application for Model Deployment Using Heroku.
