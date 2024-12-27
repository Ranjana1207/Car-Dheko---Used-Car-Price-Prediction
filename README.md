# Car-Dheko--Used-Car-Price-Prediction
We have historical data on used car prices from CarDekho, including various features such as make, model, year, fuel type, transmission type, and other relevant attributes from different cities.

## Domain:

Automotive Industry , Data Science, Machine Learning

## Introduction:

In this project, the task is to enhancing the customer experience and optimizing the pricing process for used cars by developing a machine learning model. This model, based on historical car price data, will take into account various features such as the car's make, model, year, fuel type, and transmission type. The goal is to predict the prices of used cars accurately and integrate this model into an interactive web application using Streamlit.

## Skills take away From This Project:
* Data Cleaning and Preprocessing
* Exploratory Data Analysis
* Machine Learning Model Development
* Price Prediction Techniques
* Model Evaluation and Optimization
* Model Deployment
* Streamlit Application Development
* Documentation and Reporting

## Regression Algorithms Explained
1. Linear Regression

Imagine drawing a straight line through a scatter plot of points that best represents the overall trend.

Concept: Finds the best straight line to fit the data.

Pros: Simple, interpretable.

Cons: Assumes a linear relationship, which isn't always true.

Use when: You have a roughly linear relationship between variables.

2. Random Forest

Picture a forest where each tree gives a prediction, and the final prediction is the average of all trees.

Concept: Builds multiple decision trees and averages their predictions.

Pros: Handles non-linear relationships, less prone to overfitting.

Cons: Less interpretable than linear regression.

Use when: You have complex relationships and want a robust model.

3. XGBoost (eXtreme Gradient Boosting)

Think of a team of weak learners that gradually improve by focusing on the mistakes of previous learners.

Concept: Builds trees sequentially, each correcting the errors of the previous ones.

Pros: Often provides high accuracy, handles various data types.

Cons: Can overfit if not tuned properly, less interpretable.

Use when: You want high performance and have time to tune parameters.

4. Gradient Boosting Regressor

Similar to XGBoost, it's like a team learning from its mistakes, but with a different learning strategy.

Concept: Builds trees sequentially, each focusing on the residuals of the previous ones.

Pros: High performance, can handle different types of data.

Cons: Can overfit, requires careful tuning.

Use when: You want high accuracy and interpretability is less important.

Remember, the best algorithm often depends on your specific dataset and problem. It's common to try several and compare their performance.

## Results:

##  XGBoost (eXtreme Gradient Boosting):

Achieved the best performance with the highest R² and the lowest MSE/MAE, making it the chosen model for deployment.

Hyperparameter Tuning: Grid Search was employed to identify the optimal parameters, such as n_estimators and max_depth. By systematically testing a range of values for these parameters, Grid Search helped in determining the best combination that enhances the Random forest model's performance.

## Streamlit Application Development:

Deploying the predictive model through the Streamlit application revolutionizes the user experience at CarDekho by delivering swift and reliable price estimates for used cars.

## Home Page
![Home Page](https://github.com/user-attachments/assets/0d087656-bdb7-48bd-86f7-db8168bc9ac0)


## Car Price Prediction
![Car new predict](https://github.com/user-attachments/assets/3cbc3616-da72-4192-be3a-57fd4f3dbaea)

![Car new predict ans](https://github.com/user-attachments/assets/d29c6bf4-34d1-4964-ab1e-babd78babfac)






