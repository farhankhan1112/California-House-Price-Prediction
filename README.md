# California House Price Prediction

## Overview
This is a Streamlit-based web application that predicts house prices in California using a trained Linear Regression model.

## Features
- Predicts house prices based on input features like income, house age, and number of rooms.
- Converts predicted prices from USD to INR.
- Simple and interactive UI built with Streamlit.

## Requirements
Install dependencies using:
```sh
pip install -r requirements.txt
```

## Usage
Run the application using:
```sh
streamlit run app.py
```

## Inputs Required
- Median Income
- House Age
- Total Rooms
- Total Bedrooms
- Population
- Households

## Output
The predicted house price is displayed in both USD and INR.

## Model
The application uses a pre-trained Linear Regression model stored as `linear_regression_california.pkl`. Ensure this file is available in the same directory.


