# 🎓 Student Performance Predictor

An interactive machine learning web app that predicts a student's **Math Score** based on their reading & writing scores, demographics, and academic background.

---

## 📌 Key Features

- 🔢 Predicts **Math Score** using:
  - Gender
  - Race/Ethnicity
  - Parental Education Level
  - Lunch Type
  - Test Preparation Course
  - Reading Score
  - Writing Score

- ⚙️ Built with a robust ML pipeline
- 🧪 Trained with multiple regressors & hyperparameter tuning
- 💻 Web interface for easy predictions using Flask

---

## 🧠 Workflow Overview

```mermaid
graph TD
A[User Input] --> B[Data Preprocessing]
B --> C[Model Prediction]
C --> D[Result Display]
