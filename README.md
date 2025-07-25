Rainfall Prediction Model Overview
This project builds a machine learning model to predict monthly rainfall amounts for different Indian subdivisions (states/cities) based on historical rainfall data from 1901 to 2015.

Key Features:
Input Variables:
State/Subdivision: The geographic region within India.
Month: The specific month for which rainfall is predicted.
Year: The year of interest.

Data Preparation:
1.The original wide-format dataset, with one column per month, is reshaped (melted) into a long-format table where each row corresponds to a unique (Subdivision, Year, Month) triplet with rainfall value.
2.Categorical variables Subdivision and Month are transformed using one-hot encoding, allowing the model to learn distinct rainfall patterns per region and month.
3.The final feature set includes one-hot encoded subdivision and month columns plus the numeric year value.

Model:
-A Linear Regression model is trained on this feature set to predict monthly rainfall amounts.
-The model learns to capture temporal (year), seasonal (month), and spatial (subdivision) variations in rainfall.

Prediction:
-Users supply a combination of subdivision, month, and year.
-The model outputs the predicted rainfall (in millimeters) for that specific combination.
-Input features are created by setting the corresponding one-hot encoded subdivision and month flags to 1 and including the year.

Benefits and Use Cases:
   1.Helps forecast rainfall trends at a fine spatial and temporal resolution.
   2.Supports agricultural planning, water resource management, and climate analysis.
   3.Easily extendable and deployable as an interactive web app using Streamlit for user-friendly predictions.

Output Screenshot:
<img width="1917" height="871" alt="Screenshot 2025-07-25 214304" src="https://github.com/user-attachments/assets/45b216c2-38ad-465d-8576-b4029a48e738" />
