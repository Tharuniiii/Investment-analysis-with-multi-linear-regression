📊 Investment Profit Prediction using Multiple Linear Regression

This project predicts company profit based on investment in R&D, Administration, and Marketing, using a Multiple Linear Regression (MLR) model. The trained model is saved as a Pickle file and deployed via a Streamlit web application for real-time predictions.

🚀 Features

Data preprocessing & encoding categorical variables.

Model training with scikit-learn’s Linear Regression.

Evaluation using R² Score and MSE (Mean Squared Error).

Exported trained model as .pkl file for deployment.

Streamlit frontend for interactive user input and prediction.

🛠️ Tech Stack

Python (NumPy, Pandas, Scikit-learn, Matplotlib)

Streamlit (Frontend UI)

Pickle (Model serialization)

📂 Project Structure
📦 investment-profit-prediction
 ┣ 📜 investment_MLR.py        # Model training script
 ┣ 📜 multilinear_regression_model.pkl # Saved model
 ┣ 📜 app.py                   # Streamlit app for prediction
 ┣ 📜 requirements.txt         # Dependencies
 ┣ 📜 README.md                # Project documentation
 ┗ 📂 data
    ┗ 📜 Investment.csv        # Dataset used
⚙️ Installation & Setup
git clone https://github.com/your-username/investment-profit-prediction.git
cd investment-profit-prediction
Run the Streamlit app:
streamlit run app.py

📊 Model Performance

R² Score: ~0.93 (varies depending on dataset split)
MSE: Reported after testing
