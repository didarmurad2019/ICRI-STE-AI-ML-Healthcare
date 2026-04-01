# Project-I (Blood Sugar Risk)-Prototype
Medical Terminology Reference Guide: AI Blood Sugar Risk Simulator

Document ID:  ICRI-STE/DDS-001

Version: 1.0

Purpose: To provide clear, professional definitions for the clinical and technical terms used in the AI Clinical Decision Support System (DSS).

# 1. Glycemic Terms

1.1. Blood Glucose (Glycemia)
Definition: The concentration of sugar (glucose) present in the blood. Glucose is the primary energy source for the body's cells.

Clinical Significance: Maintaining stable blood glucose levels is critical for metabolic health. Significant deviations (hyperglycemia or hypoglycemia) indicate risk or disease.

Unit: Measured in mg/dL (milligrams per deciliter) in the US.

1.2. Fasting Glucose
Definition: Blood glucose level measured after the patient has not eaten for at least 8 hours.

Reference Range (Normal): 80–125 mg/dL

Risk Stratification:

≥126 mg/dL: Indicates potential diabetes.

≥250 mg/dL: Indicates dangerously high hyperglycemia.

1.3. Postprandial Glucose
Definition: Blood glucose levels measured after eating a meal.

2h Postprandial: Measured 2 hours after the start of a meal.

4h Postprandial: Measured 4 hours after a meal (indicates lingering elevation).

8h Postprandial: Often aligns with pre-meal or overnight basal levels.

Clinical Significance: Postprandial spikes are early indicators of insulin resistance and significant predictors of cardiovascular risk.

1.4. HbA1c (Hemoglobin A1c / Glycated Hemoglobin)
Definition: A measure of average blood glucose over the past 2–3 months. It represents the percentage of hemoglobin proteins in red blood cells that have glucose attached.

Interpretation:

< 5.7%: Normal

5.7% – 6.4%: Prediabetes

≥ 6.5%: Diabetes

> 9.0%: Poorly controlled diabetes; high risk of complications.

1.5. Hypoglycemia
Definition: Abnormally low blood glucose levels.

Threshold: Generally defined as < 70 mg/dL.

Risk: Dangerously Low (< 70 mg/dL) requires immediate intervention to prevent loss of consciousness or seizures.

1.6. Hyperglycemia
Definition: Abnormally high blood glucose levels.

Threshold: Generally defined as > 130 mg/dL fasting or > 180 mg/dL postprandial.

Risk: Dangerously High (e.g., fasting > 250 mg/dL) requires emergency medical intervention to prevent diabetic ketoacidosis (DKA).

# 2. Clinical and Patient Parameters

2.1. Body Mass Index (BMI)
Definition: A weight-for-height index calculated by dividing weight in kilograms by the square of height in meters (kg/m²).

Risk Stratification:

Normal: 18.5–24.9

Overweight: 25–29.9

Obese: ≥ 30

Impact on Glycemia: Higher BMI correlates with increased insulin resistance.

2.2. Blood Pressure (BP)
Components:

Systolic (SBP): Pressure in arteries when the heart beats.

Diastolic (DBP): Pressure in arteries when the heart rests between beats.

Risk Stratification: Hypertension (SBP > 140 mmHg or DBP > 90 mmHg) is a common comorbidity with diabetes, increasing cardiovascular risk.

2.3. Physical Activity
Definition: Frequency of structured exercise or physical movement (measured in days/week).

Impact: Acts as a metabolic modifier. Low activity (< 3 days/week) is a risk factor for poor glycemic control.

2.4. Stress Level
Definition: Perceived psychological stress (scale 1–10).

Impact: Chronic stress elevates cortisol, which antagonizes insulin, leading to increased blood glucose levels.

2.5. Medication Adherence
Definition: The degree to which a patient correctly follows medical advice regarding medication (e.g., insulin, oral hypoglycemics).

Stratification: Poor adherence (<50%) is a major modifiable risk factor for complications.

2.6. Family History
Definition: Presence of diabetes in first-degree relatives (parents, siblings, children).

Impact: A positive family history indicates a genetic predisposition to Type 2 Diabetes Mellitus (T2DM).

# 3. AI/ML Technical Terms

3.1. Ensemble Model
Definition: A machine learning technique that combines multiple algorithms (e.g., CatBoost, XGBoost) to improve predictive performance. The idea is that a "committee" of models is more accurate and robust than any single model.

3.2. CatBoost, XGBoost, LightGBM
Definition: Gradient Boosting algorithms. They are state-of-the-art machine learning models for structured/tabular data (like patient records). They build models in a stage-wise fashion and generalize well on decision trees.

3.3. Random Forest
Definition: An ensemble learning method that operates by constructing a multitude of decision trees at training time and outputting the class that is the mode of the classes (classification) of the individual trees.

3.4. SVM-RBF (Support Vector Machine with Radial Basis Function Kernel)
Definition: A supervised machine learning model used for classification. The RBF kernel allows the SVM to handle non-linear relationships between data points (e.g., complex interactions between glucose and lifestyle factors) by mapping them into a higher-dimensional space.

3.5. Logistic Regression
Definition: A statistical model that uses a logistic function to model a binary dependent variable. In this context, it serves as a baseline (explainable) model for risk probability.

3.6. AUC (Area Under the Curve)
Definition: A performance metric for classification models. It measures the model's ability to distinguish between classes (e.g., high risk vs. normal).

Interpretation: Ranges from 0.5 (random guess) to 1.0 (perfect classification). Values > 0.9 indicate excellent model performance.

# 4. System & Clinical Terms

4.1. AI Clinical DSS (Artificial Intelligence Clinical Decision Support System)
Definition: A software tool that analyzes patient data using AI/ML algorithms to assist clinicians in making evidence-based decisions. It provides risk assessments and recommendations but does not replace the clinician's judgment.

4.2. Risk Stratification
Definition: The process of classifying patients into distinct groups (e.g., Normal, High Risk, Dangerously High) based on their probability of adverse outcomes (e.g., complications, hospitalization). It enables targeted care management.

4.3. Reference Glycemic Atlas
Definition: A standardized table of reference values (thresholds) used to define risk categories based on clinical guidelines (e.g., ADA - American Diabetes Association). It serves as the ground truth for the AI's classification logic.

4.4. Confidence (AI Consensus)
Definition: A quantitative measure (0–100%) of the AI ensemble's certainty in its prediction. Higher confidence scores indicate that multiple models strongly agree on the risk category.

Note: This document is intended for educational and research use within the ICRI-STE Open Science AI/ML Lab. Clinical decisions should always be validated by a qualified healthcare professional. 

# 4. Laboratory work 

End-to-end Python development from scratch

# 5. Interactive demo 

See our youtube chanel presentation

