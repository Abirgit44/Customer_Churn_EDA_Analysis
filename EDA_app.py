import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load the dataset
url = 'https://raw.githubusercontent.com/Abirgit44/Customer_Churn_EDA_Analysis/main/churn_dataset.csv'
df = pd.read_csv(url)



st.title('Customer Churn EDA Dashboard 📊')

# Sidebar with selectbox for page navigation
st.sidebar.markdown("<h1 style='text-align: center; color: violetblue; margin-top: 0; padding-top: 0px;'>🚀 Select a Page 🚀</h1>", unsafe_allow_html=True)

# Instructions with emoji icons for page navigation
instructions_html = """
    <div style='padding: 10px; background-color: #33ffff; border-radius: 10px;'>
        <h2 style='color: #330060;'>📌 Instructions:</h2>
        <ul>
            <li style='color: #330066;'>👇 Use the selectbox to navigate to different pages:</li>
        </ul>
        <div style='padding-left: 20px;'>
            <p style='color: #330066;'>Select a page to view its content.</p>
        </div>
    </div>
"""
st.sidebar.markdown(instructions_html, unsafe_allow_html=True)

page = st.sidebar.selectbox(
    "",
    ["🏠 Home", "📊 Data", "📈 EDA", "🧑‍💻 About Me"],
    #format_func=lambda x: x.split()[1]  # Remove emojis from display
)
# Define the content for each page
page_content = {
    "🏠 Home": "Hi, in this page I have given a brief description and outlook of the Project.",
    "📊 Data": "This is the data page where you can see the data that I have used and some basic summary of it.",
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
    content="""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                background-color: #f2f4f7; /* Light blue background color */
                padding: 20px; /* Add padding for content */
            }
            .home-content {
                text-align: center;
                font-size: 24px;
                line-height: 1.5;
                padding: 20px; /* Add space around the text */
                background-color: rgba(231, 130, 231, 0.2); /* Semi-transparent white background */
                border-radius: 10px; /* Rounded edges */
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Box shadow for a card-like effect */
            }
            .highlight {
                color: #CEEE28; /* Dark purple text color */
                font-weight: bold;
            }
            .benefits-list {
                list-style-type: none; /* Remove default bullet points */
                margin-left: 0; /* Remove indentation for bullet points */
                padding-left: 30px; /* Add space to the left of bullet points */
                color: #FF0000; /* Dark gray text color for the benefits list */
            }

            .benefits-list li:before {
                content: "➜ "; /* Unicode arrow character as bullet point */
                font-weight: bold; /* Make the arrow bold */
                font-size: 18px; /* Adjust the size of the arrow as needed */
                padding-right: 5px; /* Add some space between the arrow and text */
            }
        </style>
    </head>
    <body>
        <div class="home-content">
            <p>Welcome to the <span class="highlight">Customer Churn EDA Dashboard</span>!</p>
            <p>Explore insights and data visualizations to uncover patterns and trends in customer churn.</p>
            <p>This interactive visualizations are powered by:</p>
            <ul class="benefits-list">
                <li><span class="highlight">Pandas:</span> for data manipulation and analysis</li>
                <li><span class="highlight">Numpy:</span> for numerical operations</li>
                <li><span class="highlight">Plotly:</span> for creating interactive visualizations</li>
                <li><span class="highlight">Streamlit:</span> for building an interactive EDA dashboard</li>
            </ul>
            <p>Discover valuable insights and make informed decisions to reduce churn rates and improve customer retention.</p>
            <p>Use the navigation menu to explore different sections of the application, including Data, EDA Visualizations, and About Me.</p>
            <p>Project Repository: <a href="https://github.com/Abirgit44/Customer_Churn_EDA_Analysis"><img src="https://img.shields.io/badge/GitHub-Repository-blue?logo=github" alt="GitHub Badge"></a></p>
            <p>Dataset Source: <a href="https://www.kaggle.com/datasets/moe5998/telecom-customer-churn"><img src="https://img.shields.io/badge/Kaggle-Dataset-blue?logo=kaggle" alt="Kaggle Dataset Badge"></a></p>
        </div>
    </body>
    </html>
    """
    st.markdown(content,unsafe_allow_html=True)


# Data Page
elif page == "📊 Data":
    # Custom CSS styles
    css = """
        <style>
            h2 {
                color: #B5FFFA;  /* Dark Purple */
            }

            p {
                margin-bottom: 10px;
            }

            .header {
                color: #FF5733;  /* Red */
                font-size: 42px;
            }

            span.colored-text {
                font-weight: bold;
            }

            span.CustomerID {
                color: #CEEE28;  /* Light Green */
            }

            span.Gender {
                color: #33FFB8;  /* Cyan */
            }

            span.SeniorCitizen {
                color: #9B33FF;  /* Purple */
            }

            span.Partner {
                color: #33FF33;  /* Green */
            }

            span.Dependents {
                color: #FF33E3;  /* Pink */
            }

            span.Tenure {
                color: #33FFFF;  /* Light Blue */
            }

            span.PhoneService {
                color: #FFC300;  /* Yellow */
            }

            span.MultipleLines {
                color: #FF33A6;  /* Magenta */
            }

            span.InternetService {
                color: #33A6FF;  /* Blue */
            }

            span.OnlineSecurity {
                color: #33FF33;  /* Green */
            }

            span.OnlineBackup {
                color: #FF5733;  /* Red */
            }

            span.DeviceProtection {
                color: #33FFB8;  /* Cyan */
            }

            span.TechSupport {
                color: #9B33FF;  /* Purple */
            }

            span.StreamingTV {
                color: #33FF33;  /* Green */
            }

            span.StreamingMovies {
                color: #FF33E3;  /* Pink */
            }

            span.Contract {
                color: #33FFFF;  /* Light Blue */
            }

            span.PaperlessBilling {
                color: #FFC300;  /* Yellow */
            }

            span.PaymentMethod {
                color: #FF33A6;  /* Magenta */
            }

            span.MonthlyCharges {
                color: #33A6FF;  /* Blue */
            }

            span.TotalCharges {
                color: #33FF33;  /* Green */
            }

            span.Churn {
                color: #FF5733;  /* Red */
            }
        </style>
        """
    st.markdown(css, unsafe_allow_html=True)
    st.markdown("<h1 class='header'>About the Data</h1>", unsafe_allow_html=True)
    # Dataset description in HTML format with different text colors for each column name
    dataset_description = f"""
    <!DOCTYPE html>
    <html>
    <body>
        <h2>Telecom Customer Churn Dataset Description</h2>
        <p><span class="colored-text CustomerID">CustomerID</span>: <b><em>A unique identifier for each customer.</em></b></p>
        <p><span class="colored-text Gender">Gender</span>: <b><em>The gender of the customer (Male or Female).</em></b></p>
        <p><span class="colored-text SeniorCitizen">SeniorCitizen</span>: <b><em>Indicates whether the customer is a senior citizen (1 for Yes, 0 for No).</em></b></p>
        <p><span class="colored-text Partner">Partner</span>: <b><em>Whether the customer has a partner (Yes or No).</em></b></p>
        <p><span class="colored-text Dependents">Dependents</span>: <b><em>Whether the customer has dependents (Yes or No).</em></b></p>
        <p><span class="colored-text Tenure">Tenure</span>: <b><em>The number of months the customer has stayed with the company.</em></b></p>
        <p><span class="colored-text PhoneService">PhoneService</span>: <b><em>Whether the customer has phone service (Yes or No).</em></b></p>
        <p><span class="colored-text MultipleLines">MultipleLines</span>: <b><em>Whether the customer has multiple phone lines (Yes, No, or No phone service).</em></b></p>
        <p><span class="colored-text InternetService">InternetService</span>: <b><em>The type of internet service (DSL, Fiber optic, or No).</em></b></p>
        <p><span class="colored-text OnlineSecurity">OnlineSecurity</span>: <b><em>Whether the customer has online security (Yes, No, or No internet service).</em></b></p>
        <p><span class="colored-text OnlineBackup">OnlineBackup</span>: <b><em>Whether the customer has online backup (Yes, No, or No internet service).</em></b></p>
        <p><span class="colored-text DeviceProtection">DeviceProtection</span>: <b><em>Whether the customer has device protection (Yes, No, or No internet service).</em></b></p>
        <p><span class="colored-text TechSupport">TechSupport</span>: <b><em>Whether the customer has tech support (Yes, No, or No internet service).</em></b></p>
        <p><span class="colored-text StreamingTV">StreamingTV</span>: <b><em>Whether the customer has streaming TV (Yes, No, or No internet service).</em></b></p>
        <p><span class="colored-text StreamingMovies">StreamingMovies</span>: <b><em>Whether the customer has streaming movies (Yes, No, or No internet service).</em></b></p>
        <p><span class="colored-text Contract">Contract</span>: <b><em>The type of contract (Month-to-month, One year, or Two year).</em></b></p>
        <p><span class="colored-text PaperlessBilling">PaperlessBilling</span>: <b><em>Whether the customer uses paperless billing (Yes or No).</em></b></p>
        <p><span class="colored-text PaymentMethod">PaymentMethod</span>: <b><em>The payment method (Electronic check, Mailed check, Bank transfer (automatic), or Credit card (automatic)).</em></b></p>
        <p><span class="colored-text MonthlyCharges">MonthlyCharges</span>: <b><em>The monthly charges for the customer's service.</em></b></p>
        <p><span class="colored-text TotalCharges">TotalCharges</span>: <b><em>The total charges paid by the customer.</em></b></p>
        <p><span class="colored-text Churn">Churn</span>: <b><em>Whether the customer churned (Yes or No).</em></b></p>

    </body>
    </html>
    """
    # Display the dataset description in the Home page with different text colors using HTML
    st.markdown(dataset_description, unsafe_allow_html=True)

    st.subheader("View the Data")

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

    custom_css = """
    <style>
    .rainbow-text-container {
        background-color: rgba(0, 0, 0, 1); /* Light blue background color */
        background-size: cover;
        border-radius: 20px; /* Rounded corners */
        padding: 20px;
    }
    </style>
    """

    # Display the HTML element with custom CSS styles
    st.markdown(custom_css, unsafe_allow_html=True)
    st.write("""<div class="rainbow-text-container">
              <p style="background-image: linear-gradient(to right, violet, indigo, blue, green, yellow, orange, red);
                      -webkit-background-clip: text;
                      color: transparent;
                      display: inline-block;
                      font-size: 24px;"><strong>To see the visualizations created based on the dataset, please go to the EDA page from the sidebar selectbox.</strong></p>""",unsafe_allow_html=True)




# EDA Page
elif page == "📈 EDA":
    st.header("Exploratory Data Analysis")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Remove the "CustomerID" column from the dataset
    df['SeniorCitizen'] = df['SeniorCitizen'].replace({0: 'No', 1: 'Yes'})
    df.drop(columns=['customerID'], inplace=True)

    # Univariate Analysis
    st.subheader("Univariate Analysis")

    # Gender distribution
    st.markdown("<p style='text-align:center;'>This chart displays the distribution of customers by gender.</p>", unsafe_allow_html=True)
    gender_counts = df['gender'].value_counts()
    fig_gender = px.bar(gender_counts, x=gender_counts.index, y=gender_counts.values, labels={'x': 'Gender', 'y': 'Count'}, title='Gender Distribution')
    st.plotly_chart(fig_gender)


    # Senior Citizen distribution
    st.markdown("&nbsp;&nbsp;&nbsp;"
    "<p style='text-align:center;'>This chart shows the distribution of senior citizens among customers.</p>", unsafe_allow_html=True)
    senior_counts = df['SeniorCitizen'].value_counts()
    fig_senior = px.bar(senior_counts, x=senior_counts.index, y=senior_counts.values, labels={'x': 'Senior Citizen', 'y': 'Count'}, title='Senior Citizen Distribution')
    st.plotly_chart(fig_senior)

    # Internet Service distribution
    st.markdown("&nbsp;&nbsp;&nbsp;"
    "<p style='text-align:center;'>This visualization represents the distribution of customers by internet service type.</p>", unsafe_allow_html=True)
    internet_counts = df['InternetService'].value_counts()
    fig_internet = px.bar(internet_counts, x=internet_counts.index, y=internet_counts.values, labels={'x': 'Internet Service', 'y': 'Count'}, title='Internet Service Distribution')
    st.plotly_chart(fig_internet)

    # Monthly Charges distribution
    st.markdown("&nbsp;&nbsp;&nbsp;"
    "<p style='text-align:center;'>This histogram illustrates the distribution of monthly charges incurred by customers.</p>", unsafe_allow_html=True)
    fig_monthly_charges = px.histogram(df, x='MonthlyCharges', title='Monthly Charges Distribution', labels={'x': 'Monthly Charges'})
    st.plotly_chart(fig_monthly_charges)

    # Total Charges distribution
    st.markdown("&nbsp;&nbsp;&nbsp;"
    "<p style='text-align:center;'>This histogram displays the distribution of total charges across all customers.</p>", unsafe_allow_html=True)
    fig_total_charges = px.histogram(df, x='TotalCharges', title='Total Charges Distribution', labels={'x': 'Total Charges'})
    st.plotly_chart(fig_total_charges)

    # Tenure distribution using
    st.markdown("&nbsp;&nbsp;&nbsp;"
    "<p style='text-align:center;'>This chart visualizes the distribution of customer tenure (duration of service).</p>", unsafe_allow_html=True)
    fig_tenure = px.histogram(df, x='tenure', title='Tenure Distribution', labels={'x': 'Tenure'})
    st.plotly_chart(fig_tenure)

    # Bivariate Analysis
    st.subheader("Bivariate Analysis")

    # Custom widgets for selecting X and Y variables
    x_variable = st.selectbox('Select X-axis variable:', df.columns[1:], key='x_variable')  # Unique key for X variable
    y_variable = st.selectbox('Select Y-axis variable:', df.columns[1:], key='y_variable')  # Unique key for Y variable

    # Create bivariate analysis plots based on user selection
    if x_variable != y_variable:
        if df[x_variable].dtype == 'object' and df[y_variable].dtype == 'object':
            # Create a grouped bar plot for categorical variables
            fig_bivariate = px.bar(df, x=x_variable, color=y_variable, title=f'{x_variable} by {y_variable}', labels={x_variable: x_variable, y_variable: y_variable})
        else:
            # Create a scatter plot for numeric variables
            fig_bivariate = px.scatter(df, x=x_variable, y=y_variable, color='Churn', title=f'{x_variable} vs. {y_variable} (Churn)', labels={x_variable: x_variable, y_variable: y_variable})

        # Add description including variable names
        if df[x_variable].dtype == 'object' and df[y_variable].dtype == 'object':
            description = f"This grouped bar plot shows the distribution of {x_variable} by {y_variable}."
        else:
            description = f"This scatter plot illustrates the relationship between {x_variable} and {y_variable} while considering churn status (Churn)."

        st.markdown(description)
        st.plotly_chart(fig_bivariate)
    else:
        st.warning("Please choose different X and Y variables for bivariate analysis.")





    # Interactive histogram for Monthly Charges by Churn
    st.markdown("### Monthly Charges Distribution by Churn")
    st.markdown("This interactive histogram displays the distribution of monthly charges for customers, grouped by churn status (Churn).")
    fig1 = px.histogram(df, x='MonthlyCharges', color='Churn', title='Monthly Charges Distribution by Churn',
                        labels={'MonthlyCharges': 'Monthly Charges'}, marginal='box')
    st.plotly_chart(fig1)

    # Interactive bar plot for Contract vs. Churn
    st.markdown("### Contract vs. Churn")
    st.markdown("This interactive bar plot shows the distribution of customer contracts, categorized by churn status (Churn).")
    contract_churn = df.groupby(['Contract', 'Churn']).size().reset_index(name='Count')
    fig2 = px.bar(contract_churn, x='Contract', y='Count', color='Churn',
                  title='Contract vs. Churn', labels={'Count': 'Count'})
    st.plotly_chart(fig2)

    # Interactive box plot for Tenure by Payment Method and Churn
    st.markdown("### Tenure by Payment Method and Churn")
    st.markdown("This interactive box plot represents the tenure (duration of service) of customers based on their payment methods, with consideration of churn status (Churn).")
    fig3 = px.box(df, x='PaymentMethod', y='tenure', color='Churn',
                  title='Tenure by Payment Method and Churn',
                  labels={'tenure': 'Tenure', 'PaymentMethod': 'Payment Method'})
    st.plotly_chart(fig3)


    # Interactive scatter matrix for Tenure, Monthly Charges, and Total Charges
    st.subheader('Interactive Scatter Matrix')
    st.markdown("This interactive scatter matrix provides insights into the relationships between tenure, monthly charges, and total charges. Each point represents a customer, color-coded by churn status (Churn).")
    fig4 = px.scatter_matrix(df, dimensions=['tenure', 'MonthlyCharges', 'TotalCharges'], color='Churn',
                              labels={'tenure': 'Tenure',
                                      'MonthlyCharges': 'Monthly Charges',
                                      'TotalCharges': 'Total Charges'})
    st.plotly_chart(fig4)

# About Me Page
elif page == "🧑‍💻 About Me":
    st.header("About Me 🧑‍💻")

    # Description
    st.write("I am a passionate data analyst currently pursuing my B.Tech degree in Computer Science with a specialization in Data Science. With a strong foundation in programming languages such as Python, R, Java, and Linux, I have honed my skills in data analysis and machine learning.")

    # Skills
    st.subheader("🔥 Skills")
    st.write("- **Programming Languages and Libraries:** Proficient in Python with expertise in Pandas, NumPy, Seaborn, Matplotlib, Plotly, Scikit-Learn, and TensorFlow. Additionally, I have experience with SQL, including PostgreSQL and Oracle SQL.")
    st.write("- **Data Analytics Tools:** I am well-versed in Tableau, which allows me to create compelling visualizations and gain insights from data. I am also proficient in Microsoft Excel.")

    # Interests
    st.subheader("💭 Interests")
    st.write("Outside the world of data, I have a variety of interests. I find solace in listening to music, which often serves as my creative inspiration. Additionally, I am an avid reader with a keen interest in geopolitics and history. These hobbies provide me with a well-rounded perspective and inspire my analytical thinking.")

    st.write("I am deeply committed to the field of data science and constantly seek opportunities to apply my skills to real-world problems. With a solid foundation and a passion for learning, I look forward to contributing to the data science community and making a positive impact.")

    # GitHub link # LinkedIn link # Tableau link
    st.subheader("Follow me here:")
    st.markdown(
    "<a href='https://bit.ly/Abirgit44'><img src='https://www.vectorlogo.zone/logos/github/github-icon.svg' width='32'></a>"
    "&nbsp;&nbsp;&nbsp;"
    "<a href='https://bit.ly/linkAbir'><img src='https://www.linkedin.com/favicon.ico' width='32'></a>"
    "&nbsp;&nbsp;&nbsp;"
    "<a href='https://bit.ly/abir-tableau'><img src='https://www.tableau.com/favicon.ico' width='32'></a>",
    unsafe_allow_html=True
    )



    # Contact information
    st.subheader("Send your feedbacks here:")
    st.markdown(
    "<a href='mailto:abirmaiti56@gmail.com'><img src='https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico' width='32'></a>",
    unsafe_allow_html=True
    )
