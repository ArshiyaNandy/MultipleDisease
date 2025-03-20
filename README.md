The **Multiple Disease Prediction System** is a machine learning-based web application that predicts the likelihood of three critical diseases:  
✅ **Heart Disease**  
✅ **Diabetes**  
✅ **Parkinson's Disease**  

Users can input relevant medical data such as age, blood pressure, glucose level, and other symptoms. The system analyzes this information and predicts the probability of the respective diseases, helping users make informed decisions about their health.

---

💡 **Problem Statement**  
In today’s fast-paced world, early diagnosis of chronic diseases like Heart Disease, Diabetes, and Parkinson’s is essential to prevent severe health complications. However:  
- Manual screening processes can be time-consuming and prone to human error.  
- Many individuals delay medical consultations due to busy schedules or lack of awareness.  
- Access to medical professionals may be limited, especially in remote areas.

---

🛠️ **Solution Statement**  
The **Multiple Disease Prediction System** solves these challenges by:  
✅ Providing a **fast and reliable** way to assess disease risk based on user input.  
✅ Enabling **early detection** by offering instant predictions using pre-trained machine learning models.  
✅ Offering a **user-friendly interface** that allows anyone to use the system, regardless of technical expertise.  
✅ Increasing **accessibility** by making the system available online, allowing users to check their health status anytime.

---

⚙️ **Technologies Used**  
- **Python**: Backend development and machine learning model implementation.  
- **Streamlit**: Interactive web application interface.  
- **Scikit-learn**: Machine learning model development and training.  
- **Pandas & NumPy**: Data processing and handling.  
- **Matplotlib & Seaborn**: Visualizing prediction results and performance.

---

🔍 **Key Features**  
✨ **Disease Prediction** – Provides accurate predictions based on trained machine learning models.  
✨ **User-Friendly Interface** – Clean and easy-to-use interface built with Streamlit.  
✨ **Multiple Model Integration** – Uses individual models for Heart Disease, Diabetes, and Parkinson's Prediction.  
✨ **Instant Results** – Predictions are generated in real-time based on user input.  
✨ **Secure and Reliable** – Ensures that user data is processed securely with no external leakage.

---

📚 **How It Works**  
1. **Input Medical Data** – Users enter details like age, BMI, glucose level, and other health parameters.  
2. **Select Disease Type** – Choose the disease to predict from the available options.  
3. **Model Prediction** – The system processes the data through the relevant machine learning model.  
4. **Get Results** – The predicted result is displayed instantly with a probability score.

---

🚀 **Installation and Setup**  
1. **Clone the Repository**  
```
git clone https://github.com/ArshiyaNandy/Multiple-Disease-Prediction.git
cd Multiple-Disease-Prediction
```
2. **Create and Activate Virtual Environment**  
```
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```
3. **Install Required Dependencies**  
```
pip install -r requirements.txt
```
4. **Run the Streamlit App**  
```
streamlit run multiple_disease.py
```

---

🧠 **Machine Learning Models Used**  
- **Logistic Regression** – For predicting Heart Disease.  
- **Decision Tree Classifier** – For Diabetes Prediction.  
- **SVM Classifier** – For Parkinson’s Disease.  

Each model is trained on high-quality datasets, ensuring reliable and accurate predictions.

---

📊 **Performance and Accuracy**  
The models have been evaluated on multiple datasets to ensure high accuracy. The average performance scores for each model are:  
- Heart Disease Prediction: **~89% Accuracy**  
- Diabetes Prediction: **~92% Accuracy**  
- Parkinson's Prediction: **~95% Accuracy**  

---

🎨 **UI Preview**  
The application features an interactive, colorful interface, making it easy for users to enter their data and get results seamlessly.

---

📝 **Future Enhancements**  
🚩 **Adding More Diseases** – Expand the system to predict additional diseases.  
🚩 **Enhance Model Accuracy** – Continuous improvement of models with better datasets.  
🚩 **Mobile Version** – Develop a mobile-friendly version for better accessibility.

---

🤝 **Contributing**  
Contributions are always welcome!  
- Fork the repository.  
- Create a new branch.  
- Make improvements and submit a pull request.  

---

📬 **Contact and Support**  
If you encounter any issues or have suggestions for improvement, feel free to reach out.  

📧 **Email:** [arshiyanandy1731@gmail.com]  
🔗 **GitHub Repository:** [https://github.com/ArshiyaNandy/Multiple-Disease-Prediction](https://github.com/ArshiyaNandy/Multiple-Disease-Prediction)  

