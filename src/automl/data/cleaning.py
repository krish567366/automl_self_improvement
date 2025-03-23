# Outlier detection & label correction
# src/automl/data/cleaning.py  
from sklearn.ensemble import IsolationForest  
from transformers import pipeline  

class DataCleaner:  
    def __init__(self, contamination=0.05):  
        self.outlier_detector = IsolationForest(contamination=contamination)  
        self.llm_corrector = pipeline("text2text-generation", model="google/flan-t5-xl")  

    def detect_outliers(self, X):  
        return self.outlier_detector.fit_predict(X)  

    def correct_labels(self, text, expected_format):  
        prompt = f"Correct this label to match {expected_format}: {text}"  
        return self.llm_corrector(prompt, max_length=512)[0]['generated_text']  