# 🎓 Student Performance Predictor

An interactive machine learning web application that predicts a student's **Math Score** based on their academic profile and demographics. This project showcases an end-to-end ML pipeline, from raw data ingestion to a fully deployable prediction system with a responsive frontend.

---

## 📌 Key Features

- 🔢 Predicts a **student's math score** using:
  - Gender
  - Race/Ethnicity
  - Parental level of education
  - Lunch type
  - Test preparation course status
  - Reading score
  - Writing score

- 📁 Modular architecture:
  - Clean separation between data ingestion, transformation, modeling, and prediction
  - Easy scalability and maintenance

- 🧪 Multiple regression models used and compared:
  - Hyperparameter tuning with `RandomizedSearchCV`
  - Model selection based on R² score and other metrics

- 🧠 Saved model and preprocessor objects ensure consistent and fast predictions

- 🖥️ User-friendly web interface built using **Flask** and **Bootstrap 5**

---



## 🧪 Model Evaluation

- **Models Used**:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting
  - AdaBoost
  - XGBoost
  - CatBoost
  - K-Nearest Neighbors

- **Hyperparameter tuning** was performed using:

  ```python
  RandomizedSearchCV(estimator, param_distributions=params, cv=3, ...)

## 🧰 Tech Stack

| Layer       | Technologies                            |
|------------|------------------------------------------|
| Frontend   | HTML5, CSS3, Bootstrap 5                 |
| Backend    | Python, Flask                            |
| ML Framework | scikit-learn, pandas, numpy, xgboost   |
| Model Tools | RandomizedSearchCV, pickle/dill, CatBoost |

---

## 🧠 Workflow Overview

```mermaid
graph TD
    A["User visits Home Page"] --> B["User fills form: Gender, Ethnicity, Education, Lunch, Test Prep, Reading Score, Writing Score"]
    B --> C["Form submitted to /predictdata route"]
    C --> D["Flask receives request and creates CustomData instance"]
    D --> E["Convert data to DataFrame"]
    E --> F["Load saved Preprocessor and Model from artifacts"]
    F --> G["Preprocess input using saved ColumnTransformer"]
    G --> H["Predict math score using trained model"]
    H --> I["Render prediction result on home.html"]