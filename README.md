# Prediction of LC50 value QSAR models

Prediction of LC50 value using Quantitative structure activity relationship models ( QSAR models ).
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

![arch](https://user-images.githubusercontent.com/73905298/152676791-24a6b9d1-2056-4b3b-b64d-8a81ffa1a36e.jpg)


Calculate Predictions, Training time, Prediction time, R squared value, MAE value, RMSE value for every model, save results to csv file and serialize most optimal model using pickle dump.

Dynamically load data into  database by integrating Python with MySQL; Save logging times of code to a database in MySQL.

Setting up a Flask Web Application

Front-End Development of Website using HTML and CSS, Jinja for Templating Engine 

Model Deployment Using Heroku.

![toxicity](https://user-images.githubusercontent.com/73905298/151829778-fac911d8-dab4-433c-8024-24dff5bc54b1.jpg)

