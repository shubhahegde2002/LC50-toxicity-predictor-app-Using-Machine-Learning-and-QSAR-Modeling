# Prediction of LC50 value QSAR models
Prediction of LC50 value using Quantitative structure activity relationship models (QSAR models).
Develop quantitative regression QSAR models to predict acute aquatic toxicity towards the fish fathead minnow ( Pimephales promelas ) on a set of 908 chemicals based on 6 molecular descriptors.
Dataset: https://archive.ics.uci.edu/ml/datasets/QSAR+fish+toxicity 

LC50 data, which is the concentration that causes death in 50% of test fish over a test duration of 96 hours, was used as model response. The model comprised 6 molecular descriptors: MLOGP (molecular properties), CIC0 (information indices), GATS1i (2D autocorrelations), NdssC (atom-type counts), NdsCH ((atom-type counts), SM1_Dz(Z) (2D matrix-based descriptors). Regressor Models used: 

K-Nearest Neighbours

Multiple Linear Regression

XGBoost Regressor

Support Vector Machine Regressor

Random Forest Regressor

Bayesian Ridge Regressor

## After Model Development
Calculate Training time, Prediction time, R squared value, MAE value, RMSE value for every model, save results to csv file and serialize most optimal model using pickle dump.

Dynamically load data into  database by integrating Python with MySQL and setting up a Flask Web Application for Model Deployment Using Heroku.
