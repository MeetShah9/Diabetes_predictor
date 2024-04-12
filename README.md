# Diabetic Predictor Web App

## Overview
This web application utilizes the power of machine learning to predict the likelihood of an individual having diabetes based on certain health indicators. The model is trained on the well-known Pima Indians Diabetes dataset, and employs Support Vector Machine (SVM) classification, implemented using the SVC (Support Vector Classification) algorithm from scikit-learn. 

[demo](https://github.com/MeetShah9/Diabetes_predictor/assets/148629466/5e8f0776-d848-4faa-8933-3a67f295d6ef)
## Technologies Used
- **Streamlit:** The user interface is built using Streamlit, a popular Python library for creating interactive web applications.
- **NumPy:** For efficient array manipulation, NumPy is utilized.
- **Pandas:** Pandas is employed for data manipulation and handling, enabling seamless integration with the Pima Indians Diabetes dataset.
- **scikit-learn:** The scikit-learn library is leveraged for various tasks including data standardization and implementing the SVM classifier.
- **SVM (Support Vector Machine):** Specifically, the SVC implementation from scikit-learn is utilized for training the predictive model.

## Features
- **Diabetes Prediction:** Users can input their health parameters such as glucose level, blood pressure, skin thickness, etc., and the model will predict the likelihood of them having diabetes.
- **Model Accuracy:** The model has been trained with a high degree of accuracy, achieving an impressive 79% accuracy on the validation dataset.

## How to Run
To run the application locally, follow these steps:
1. Clone the repository containing the code.
2. Install the necessary dependencies specified in the `requirements.txt` file.
3. Run the Streamlit app using the command `streamlit run app.py`.
4. Access the web app through the provided URL in the terminal.

## Conclusion
This Streamlit-based web app provides a convenient and accessible platform for individuals to assess their risk of diabetes based on their health parameters. With its intuitive interface and robust predictive model, it serves as a valuable tool for both individuals and healthcare professionals.
