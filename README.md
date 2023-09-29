# Customer Churn Analysis and Prediction

![Churn Analysis](https://user-images.githubusercontent.com/111905512/216779696-2b8101d8-77e6-45f1-9543-153fd00303e3.png)

## Overview

Welcome to my project on **Telecom Customer Churn Analysis and Prediction**! In this project, I've harnessed the power of data science to explore and predict customer churn in the telecom industry. Leveraging the Telecom Customer Churn dataset from Kaggle, I performed Exploratory Data Analysis (EDA) and built predictive models using popular data science libraries. If you're interested in the fascinating world of churn analysis and prediction, you're in the right place!

### Key Skills Applied

This project allowed me to hone my skills in a variety of areas, including:

- **Data Cleaning**: I ensured the dataset was pristine and ready for analysis.
- **Python**: The primary programming language I used throughout this project.
- **Pandas and NumPy**: These libraries were instrumental for data manipulation.
- **Data Visualization**: I utilized Seaborn and Matplotlib to create engaging visualizations.
- **Jupyter Notebook**: My interactive environment for data exploration and model development.
- **Machine Learning**: I employed TensorFlow, Keras, and Scikit-Learn to build predictive models.

## **Project Overview and  Explore the app live**:


Dive deeper into the project by visiting the [Project Link](https://bit.ly/3DU5NRz). There, you'll find comprehensive details about the dataset, my analysis, and the predictive models I've developed. This project provides valuable insights into the world of customer churn, and I encourage you to explore it in greater depth.

Explore the Streamlit based web application built to show the EDA visualizations and Predictive modeling together from clicking the icon below:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://telecom-customer-analysis-by-abir.streamlit.app/)

## Churn Analysis Insights

Here are some key insights I've gleaned after meticulously cleaning and exploring the data:

- The dataset reveals that out of 5,174 customers, 1,869 are churning, resulting in an approximate churn rate of 27%.
- The majority, approximately 73%, are loyal, non-churning customers.
- A closer look at customer service tenure reveals that the highest number of customers stayed for 1 year (2,175 individuals), followed by those with service spanning 5 to 6 years (1,407 individuals).

## Exploratory Data Analysis (EDA)

In this section of the app, we perform Exploratory Data Analysis to gain insights into the telecom customer data. The EDA process involves univariate and bivariate analysis, revealing patterns and trends that can help us better understand the dataset and the factors influencing customer churn.

### Univariate Analysis

#### Gender Distribution

We start with a bar chart that displays the distribution of customers by gender. This visualization helps us understand the gender balance within our customer base.

#### Senior Citizen Distribution

The next chart shows the distribution of senior citizens among our customers. It distinguishes between customers who are senior citizens (Yes) and those who are not (No).

#### Internet Service Distribution

This visualization represents the distribution of customers by their internet service type. It helps us understand which internet service options are most popular among our customers.

#### Monthly Charges Distribution

To analyze the distribution of monthly charges incurred by customers, we use a histogram. This chart provides insights into the range and frequency of monthly charges.

#### Total Charges Distribution

Similar to the monthly charges, this histogram displays the distribution of total charges across all customers. It reveals the spread of total charges incurred.

#### Tenure Distribution

This chart visualizes the distribution of customer tenure, which is the duration of service. It helps us understand how long customers have been with the telecom company.

### Bivariate Analysis

#### Custom Variable Selection

We introduce custom widgets that allow users to select the X and Y variables for bivariate analysis. These selections enable users to explore relationships between different factors in the dataset.

#### Bivariate Analysis Plots

Depending on the user's selections, we create various types of bivariate analysis plots:
- For categorical variables, we generate grouped bar plots. These plots show how one variable's distribution differs by categories of another variable.
- For numeric variables, we create scatter plots. These plots help us visualize relationships between two numeric variables while considering the churn status.

### Additional Interactive Visualizations

#### Monthly Charges Distribution by Churn

This interactive histogram displays the distribution of monthly charges for customers, categorized by churn status (Churn). It allows users to see how monthly charges vary between customers who have churned and those who haven't.

#### Contract vs. Churn

This interactive bar plot shows the distribution of customer contracts, categorized by churn status (Churn). It helps us understand the impact of contract type on customer churn.

#### Tenure by Payment Method and Churn

An interactive box plot illustrates the tenure (duration of service) of customers based on their payment methods. It also considers the churn status (Churn). This visualization helps us analyze how payment methods influence customer churn.

#### Interactive Scatter Matrix

The interactive scatter matrix provides insights into the relationships between tenure, monthly charges, and total charges. Each point represents a customer, color-coded by churn status (Churn). This matrix helps us identify patterns and correlations within these numeric variables.

These visualizations collectively offer a comprehensive understanding of the customer data and are instrumental in identifying key factors influencing customer churn.


## Model Building

I've also ventured into predictive modeling to identify potential churners. I've employed the following approaches:

**Artificial Neural Network (ANN) with TensorFlow and Keras:** I've harnessed the capabilities of TensorFlow and Keras to construct a robust ANN model. This model was trained on preprocessed data to predict customer churn.

Curious about how this model performs in practice? You can explore my web-based **Churn Prediction Model**, developed using Streamlit. Don't miss the opportunity to test its predictive power from the shared app link above.


## Main Insights

The overarching aim of this project is to draw meaningful insights from the dataset and construct predictive models to identify potential churners. Here are a few of the standout findings:

1. **Payment Method Matters:** Customers using the Electronic check payment method exhibit the highest churn rate.
2. **Monthly Contracts Lead to Churn:** Customers with monthly contracts are more likely to churn due to the absence of long-term commitments.
3. **The Importance of Security and Support:** Categories with no Online Security or Tech Support tend to have higher churn rates.
4. **Age as a Factor:** Non-senior citizens are more likely to churn compared to senior citizens.

For more detailed information, engaging visualizations, and deeper insights from the models, I invite you to explore the project link. If you have any questions or comments, please don't hesitate to reach out.

Thank you for your interest in my Customer Churn Analysis and Prediction project!

---
