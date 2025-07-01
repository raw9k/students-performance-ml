✏️ Student Performance Predictor
A machine learning web application that predicts a student’s Math score based on demographic and academic attributes like gender, parental education, and performance in other subjects.

📌 Features
🎯 Predicts Math Score based on:

Gender

Race/Ethnicity

Parental level of education

Lunch type

Test preparation course

Reading and Writing scores

🛠️ ML pipeline using scikit-learn

⚙️ Flask web app for interactive input

📦 Model & preprocessing artifacts managed in artifacts/

🚀 Live Demo
(If hosted, add a link here)

🧠 ML Workflow
Data Collection: Student performance dataset

Preprocessing: Encoding categorical features, scaling numeric features

Model Training: Various regressors (Random Forest, XGBoost, CatBoost, etc.)

Hyperparameter Tuning: RandomizedSearchCV on each model

Model Selection: Best model saved as model.pkl

Prediction Pipeline: Flask handles real-time prediction using saved artifacts

📊 Technologies Used
Layer	Tech Stack
Frontend	HTML5, CSS3, Bootstrap 5
Backend	Python, Flask
ML Libraries	scikit-learn, pandas, numpy, matplotlib
Deployment	(e.g., Docker, Heroku – optional to include)

🖥️ Screenshots
<details> <summary>Form UI</summary>
![form UI screenshot here]

</details> <details> <summary>Prediction Result</summary>
![prediction result screenshot here]

</details>
📁 Directory Structure
arduino
Copy
Edit
├── app.py
├── templates/
│   ├── index.html
│   └── home.html
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── utils.py
│   ├── logger.py
│   └── exception.py
├── artifacts/
│   ├── model.pkl
│   └── preprocessor.pkl
├── static/
├── README.md
├── requirements.txt
└── venv/
⚙️ How to Run Locally
bash
Copy
Edit
git clone https://github.com/your-username/student-performance-predictor.git
cd student-performance-predictor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # for Linux/macOS
venv\Scripts\activate     # for Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
Visit http://localhost:5001 to open the app in your browser.

✅ Future Improvements
Deploy on Heroku or AWS

Add prediction history tracking

Improve model interpretability with SHAP or LIME

🙋‍♂️ Author
Rounak Gupta
📫 Connect on LinkedIn
🚀 Joint President, Data Science Society