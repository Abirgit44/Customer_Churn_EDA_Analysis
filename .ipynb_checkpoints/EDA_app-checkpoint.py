import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
url = 'https://raw.githubusercontent.com/Abirgit44/Customer_Churn_EDA_Analysis/main/churn_dataset.csv'
df = pd.read_csv(url)



st.title('Customer Churn EDA Dashboard 📊')

# Sidebar with selectbox for page navigation
st.sidebar.markdown("<h1 style='text-align: center; color: violetblue;'>🚀 Select a Page 🚀</h1>", unsafe_allow_html=True)
page = st.sidebar.selectbox(
    "",
    ["🏠 Home", "📊 Data", "📈 EDA", "🧑‍💻 About Me"],
    #format_func=lambda x: x.split()[1]  # Remove emojis from display
)

# Instructions with emoji icons for page navigation
instructions_html = """
    <div style='padding: 10px; background-color: #33ffff; border-radius: 10px;'>
        <h2 style='color: violetblue;'>📌 Instructions:</h2>
        <ul>
            <li style='color: #330066;'>👇 Use the selectbox to navigate to different pages:</li>
        </ul>
        <div style='padding-left: 20px;'>
            <p style='color: #330066;'>Select a page to view its content.</p>
        </div>
        <div style='text-align: center; padding: 10px;'>
            <span style='font-size: 24px;'>🏠</span>
            <span style='font-size: 24px;'>📊</span>
            <span style='font-size: 24px;'>📈</span>
            <span style='font-size: 24px;'>🧑‍💻</span>
        </div>
    </div>
"""
st.sidebar.markdown(instructions_html, unsafe_allow_html=True)

# Define the content for each page
page_content = {
    "🏠 Home": "Hi, in this page I have given a brief description and Outlook of the Project.",
    "📊 Data": "This is the data page where you can see the dataI have used and some basic summary of it.",
    "📈 EDA": "This is the EDA page content where I have performed all the Exploratory Data Visualizations that I could generate to present them sophisticatedly.",
    "🧑‍💻 About Me": "This is the page where you will find all basic details about the man who created the project i.e. Me."
}
# Display the content based on the selected page
if page in page_content:
    st.sidebar.title(f"{page.split()[1]} Page")
    st.sidebar.write(page_content[page])




# Home Page
if page == "🏠 Home":
    st.header("About this Project")
    st.write("This is an EDA dashboard for customer churn prediction. Explore the data and visualizations to gain insights.")

# Data Page
elif page == "📊 Data":
    st.header("View the Data")

    # Adding an option to filter data by Contract type
    contract_filter = st.selectbox('Filter by Contract Type', df['Contract'].unique())
    filtered_data = df[df['Contract'] == contract_filter]
    # Displaying the dataset with 'SeniorCitizen' values replaced
    st.write("<pre style='background-color: rgba(2, 2, 55, 0.68);'><span style='font-style: italic; font-weight: bold;'>Displaying 'SeniorCitizen' as 'Yes' and 'No' instead of '1' and '0' for clarity:</span></pre>", unsafe_allow_html=True)
    filtered_data['SeniorCitizen'] = filtered_data['SeniorCitizen'].replace({0: 'No', 1: 'Yes'})
    st.write(f"Showing data for Contract Type: {contract_filter}")
    st.write(filtered_data)

   # Summary statistics for filtered data
    st.subheader("Summary Statistics for Filtered Data")
   # Create a styled table for summary statistics
    summary_stats = filtered_data.describe()
    st.table(summary_stats.style.applymap(lambda x: f'background-color: rgba(173, 212, 238, 0.23)' if x >= 0 else ''))


# EDA Page
elif page == "📈 EDA":
    st.header("Exploratory Data Analysis")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Remove the "CustomerID" column from the dataset
    df.drop(columns=['customerID'], inplace=True)

    # Univariate Analysis
    st.subheader("Univariate Analysis")

    # Gender distribution
    gender_counts = df['gender'].value_counts()
    fig_gender = px.bar(gender_counts, x=gender_counts.index, y=gender_counts.values, labels={'x': 'Gender', 'y': 'Count'}, title='Gender Distribution')
    st.plotly_chart(fig_gender)

    # Senior Citizen distribution
    senior_counts = df['SeniorCitizen'].value_counts()
    fig_senior = px.bar(senior_counts, x=senior_counts.index, y=senior_counts.values, labels={'x': 'Senior Citizen', 'y': 'Count'}, title='Senior Citizen Distribution')
    st.plotly_chart(fig_senior)

    # Internet Service distribution
    internet_counts = df['InternetService'].value_counts()
    fig_internet = px.bar(internet_counts, x=internet_counts.index, y=internet_counts.values, labels={'x': 'Internet Service', 'y': 'Count'}, title='Internet Service Distribution')
    st.plotly_chart(fig_internet)

    # Monthly Charges distribution
    fig_monthly_charges = px.histogram(df, x='MonthlyCharges', title='Monthly Charges Distribution', labels={'x': 'Monthly Charges'})
    st.plotly_chart(fig_monthly_charges)

    # Total Charges distribution
    fig_total_charges = px.histogram(df, x='TotalCharges', title='Total Charges Distribution', labels={'x': 'Total Charges'})
    st.plotly_chart(fig_total_charges)

    # Tenure distribution using
    fig_tenure = px.histogram(df, x='tenure', title='Tenure Distribution', labels={'x': 'Tenure'})
    st.plotly_chart(fig_tenure)

    # Bivariate Analysis
    st.subheader("Bivariate Analysis")

    # Custom widgets for selecting X and Y variables
    x_variable = st.selectbox('Select X-axis variable:', df.columns[1:], key='x_variable')  # Exclude CustomerID
    y_variable = st.selectbox('Select Y-axis variable:', df.columns[1:], key='y_variable')  # Exclude CustomerID

    # Create bivariate analysis plots based on user selection
    if x_variable != y_variable:
        if df[x_variable].dtype == 'object' and df[y_variable].dtype == 'object':
            # Create a grouped bar plot for categorical variables
            fig_bivariate = px.bar(df, x=x_variable, color=y_variable, title=f'{x_variable} by {y_variable}', labels={x_variable: x_variable, y_variable: y_variable})
        else:
            # Create a scatter plot for numeric variables
            fig_bivariate = px.scatter(df, x=x_variable, y=y_variable, color='Churn', title=f'{x_variable} vs. {y_variable} (Churn)', labels={x_variable: x_variable, y_variable: y_variable})

        st.plotly_chart(fig_bivariate)
    else:
        st.warning("Please choose different X and Y variables for bivariate analysis.")


    # Interactive histogram for Monthly Charges by Churn
    fig1 = px.histogram(df, x='MonthlyCharges', color='Churn', title='Monthly Charges Distribution by Churn',
                        labels={'MonthlyCharges': 'Monthly Charges'}, marginal='box')
    st.plotly_chart(fig1)

    # Interactive bar plot for Contract vs. Churn
    contract_churn = df.groupby(['Contract', 'Churn']).size().reset_index(name='Count')
    fig2 = px.bar(contract_churn, x='Contract', y='Count', color='Churn',
                  title='Contract vs. Churn', labels={'Count': 'Count'})
    st.plotly_chart(fig2)


    # Interactive box plot for Tenure by Payment Method and Churn
    fig3 = px.box(df, x='PaymentMethod', y='tenure', color='Churn',
                  title='Tenure by Payment Method and Churn',
                  labels={'tenure': 'Tenure', 'PaymentMethod': 'Payment Method'})
    st.plotly_chart(fig3)

    # Interactive scatter matrix for Tenure, Monthly Charges, and Total Charges
    st.subheader('Interactive Scatter Matrix')
    fig4 = px.scatter_matrix(df, dimensions=['tenure', 'MonthlyCharges', 'TotalCharges'], color='Churn',
                                                                  labels={'tenure': 'Tenure',
                                                                         'MonthlyCharges': 'Monthly Charges',
                                                                         'TotalCharges': 'Total Charges'})
    st.plotly_chart(fig4)
# About Me Page
elif page == "🧑‍💻 About Me":
    st.header("About Me 🧑‍💻")

    # Your name
    st.subheader("My Name:")
    st.write("Your Name")

    # GitHub link
    st.subheader("GitHub:")
    st.markdown("[![GitHub](https://github.com/favicon.ico)](https://github.com/YourGitHubUsername)")

    # LinkedIn link
    st.subheader("LinkedIn:")
    st.markdown("[![LinkedIn](https://www.linkedin.com/favicon.ico)](https://www.linkedin.com/in/YourLinkedInUsername)")

    # Tableau link
    st.subheader("Tableau:")
    st.markdown("[![Tableau](https://www.tableau.com/favicon.ico)](https://www.tableau.com/en-us/mytableau/account)")

    # Bio
    st.subheader("Bio:")
    st.write("Write a brief bio about yourself here.")

    # Contact information
    st.subheader("Contact:")
    st.write("You can reach out to me at")
    st.markdown("[![Gmail](https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico)](mailto:your@email.com)")

