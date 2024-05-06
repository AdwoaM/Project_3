![Nutritional-value-of-wine](https://github.com/AdwoaM/Project_3_Wine-Quality-Prediction/blob/main/Images/Nutritional-value-of-wine.jpg)


# Wine Quality Prediction with Machine Learning and Streamlit
This project predicts the quality of wines based on physicochemical features using machine learning techniques and provides interactive visualization and analysis through a Streamlit web application.

## Motivation for Quality Prediction:
The motivation for quality prediction in various industries such as manufacturing, healthcare, and retail stems from the need to improve efficiency, reduce costs, and enhance customer satisfaction. Predicting the quality of products or services allows companies to identify potential issues early, optimize processes, and deliver high-quality outcomes consistently.

## Overview
The goal of this project is to develop a predictive model that can accurately assess the quality of wines based on various physicochemical properties. The model is deployed using Streamlit to create an intuitive and interactive interface for users to input wine characteristics and visualize predictions and analysis.

## Dataset
The dataset used for training and evaluation is the Wine Quality dataset, which contains samples of red and white wines. Each sample is described by 11 input variables, including fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, and alcohol. The target variable, quality, is a rating between 3 and 8.
The dataset can be found at [link to dataset].

**fixed acidity**: Wines mostly contain tartaric, malic, citric, and succinic fixed acids. Grapes grown in cool climates provide wines with high acidity and a sour flavor. You can take steps to lessen the acidity of these highly acidic wines..

**volatile acidity**:It refers to the acidic elements of a wine that are gaseous, rather than liquid, and therefore can be sensed as a smell The main acid connected to the flavor and aroma of vinegar is acetic acid.

**citric acid**: A supplement of acid added during fermentation to help winemakers increase the acidity of their wine, particularly from grapes produced in warmer climates.

**residual sugar**: Natural sugars from grapes that remain in wine after alcoholic fermentation is complete.

**chlorides**: The saltiness in wine is influenced by this.

**free sulfur dioxide**: Quantity of SO2 that is unbound from other molecules. Throughout the whole winemaking process, sulfur dioxide is utilized to stop oxidation and microbiological growth.

**total sulfur dioxide**: The amount of SO2 in the wine that is free as well as the amount that is attached to other substances like sugars, aldehydes, or pigments.

**density**: The concentration of alcohol, sugar, glycerol, and other dissolved substances in wine determines its density mainly..

**pH**: Technique for calculating ripeness in relation to acidity.

**sulphates**: A common food preservative used in winemaking to preserve the freshness and flavor.

**alcohol**: The amount of alcohol the wine contains.

**quality**: How the wine is rated. In this dataset the lowest quality is 3 while the highest is 8.

## Reason for Data Selection:
The Wine Quality dataset was selected because it provides a diverse range of features that can potentially influence the quality of wine. Additionally, the dataset is publicly available, well-documented, and widely used in machine learning research, making it suitable for experimentation and comparison of different predictive models.


## Methodology
**Data Preprocessing**: The dataset is cleaned and preprocessed to handle missing values, outliers, and categorical variables. Feature scaling and encoding are applied as necessary.

**Exploratory Data Analysis (EDA)**: We conduct EDA to understand the distribution of features, identify correlations, and gain insights into the relationships between input variables and wine quality.

**Model Building**: Various machine learning models such as Random Forest, Support Vector Machine, and Gradient Boosting are trained on the preprocessed data to predict wine quality. Hyperparameter tuning and cross-validation are used to optimize model performance.

**Model Evaluation**: The trained models are evaluated using appropriate metrics such as accuracy, precision, recall, and F1-score. Visualization techniques such as confusion matrices and ROC curves are used to assess model performance.

**Streamlit Deployment**: The best-performing model is deployed using Streamlit, allowing users to input wine characteristics and receive quality predictions in real-time. Interactive visualizations such as scatter plots, bar charts, and heatmaps are provided to enhance user experience and interpretability.

# Data Analysis
## EDA-Whitewine
 In wine production, achieving the right balance of acidity and density is crucial for producing wines with complexity and depth of flavor. High fixed acidity can contribute to tartness and crispness, while density can affect the body and texture of the wine. 

 Wines with higher residual sugar content tend to have higher densities due to the added mass from dissolved sugars.

 Chlorides are a measure of salt content in wine, and their presence can affect the density of the liquid.
High chloride levels may slightly increase the density of wine, but the effect is usually minimal compared to other components like sugars and alcohol.

Sulfur dioxide is often added to wine as a preservative, and its concentration is typically low relative to other components.
While SO2 may contribute to the overall density of wine to some extent, its effect is usually overshadowed by other factors such as sugars, alcohol, and dissolved solids.

![EDA-whitewine](https://github.com/AdwoaM/Project_3_Wine-Quality-Prediction/blob/main/Images/EDA-whitewine.png)

## Box-plot-whitewine
 This provides insights into the relative importance of different wine characteristics in predicting quality, with acidity-related features appearing to have a more significant impact. The numerical values suggest that acidity-related features are relatively more important in predicting wine quality compared to other features like density, pH, or sulphates.

![box-plot-whitewine](https://github.com/AdwoaM/Project_3_Wine-Quality-Prediction/blob/main/Images/box-plot-whitewine.png)

## Heatmap-whitewine

![Heatmap-whitewine](https://github.com/AdwoaM/Project_3_Wine-Quality-Prediction/blob/main/Images/Heatmap-whitewine.png)

**Positive Correlation:** Values close to 1 indicate a strong positive correlation between the corresponding features. For example, a correlation coefficient of 0.85 between citric acid and residual sugar suggests a strong positive correlation between these two features.

**Negative Correlation:** Values close to -1 indicate a strong negative correlation between the corresponding features. For example, a correlation coefficient of -0.8 between quality and alcohol suggests a strong negative correlation between these two features.

**No Correlation:** Values close to 0 indicate no correlation between the corresponding features. For example, a correlation coefficient of -0.017 between pH and density suggests no significant correlation between these two features.

## LR-Classification report-whitewine

![LR-classification report-whitewine](https://github.com/AdwoaM/Project_3_Wine-Quality-Prediction/blob/main/Images/LR-classification%20report-whitewine.png)
Based on the classification report for a logistic regression model, we observe an overall accuracy of 58%.

* Precision class indicate that when the model predict an excellent or very bad quality, it is correct 0.63, 0.56, 0.61 times. 
  
* Recall means the model correctly identifies  52% 76% 23% of the actual instances of excellent or very bad quality

## WhiteWine_modelDF
![WhiteWine_modelDF](https://github.com/AdwoaM/Project_3_Wine-Quality-Prediction/blob/main/Images/WhiteWine_modelDF.png)

**Numerical Values (e.g., 0.8, 0.7, etc.):** These values likely represent performance metrics such as accuracy, precision, recall, F1-score, or any other evaluation metric for each respective model.

**Machine Learning Models (e.g., Logistic Regression, KNN, etc.):** These are the names of the machine learning algorithms or models being evaluated.

**Interpretation:** The numerical values indicate the performance of each model according to the specified metric(s). For example, if the values represent accuracy, then a value of 0.8 for Logistic Regression indicates an accuracy of 80% for that model.

**Comparison:** You can compare the performance of different models based on the numerical values provided. Higher values typically indicate better performance, but it depends on the specific metric being used and the context of the problem.

**Selection of Best Model:** Based on these values, you can identify which model performs best according to the chosen metric(s). For example, if accuracy is the metric of interest, the model with the highest accuracy value would be considered the best performing model.

**Consideration of Multiple Metrics:** It's important to consider multiple metrics and not rely solely on one metric to evaluate model performance. Different metrics provide different insights into a model's performance, and it's essential to understand the trade-offs between them.

## RandomF-featureImportance-white
 These values represent the importance or contribution of each feature to the model's predictive performance. Higher importance values indicate that the corresponding feature has a greater influence on the model's predictions.

You can compare the importance of different features to understand their relative importance in the model. Features with higher importance are considered more influential in making predictions, while features with lower importance have less impact.

![RandomF-featureImportance-whiteF](https://github.com/AdwoaM/Project_3_Wine-Quality-Prediction/blob/main/Images/RandomF-featureImportances-white.png)

## Streamlit wineapp-screenshot
This outlines the functionality and purpose of the wine quality prediction app, providing users with the necessary information to input their wine characteristics and interpret the prediction results effectively.

![Streamlit wineapp-screenshot](https://github.com/AdwoaM/Project_3_Wine-Quality-Prediction/blob/main/Images/Streamlit%20wineapp-screenshot.png)

**User Input Parameters:** These are the specific characteristics or attributes of the wine that the user can input into the app for quality prediction. The parameters include fixed acidity, volatile acidity, citric acid, residual sugar, and chlorides, each with its range of possible values.

**Description of Features:** Each feature is accompanied by a brief description explaining its significance in wine and its acceptable range of values. This helps users understand the meaning and relevance of each parameter when assessing wine quality.

**Wine Quality Prediction App:** This is the name of the app or tool that users can utilize to predict the quality of wine based on the input parameters provided.

**Prediction Guidelines:** The app provides guidelines for interpreting the quality prediction results. If the predicted quality is less than 7, it indicates poor quality wine, whereas a prediction of 7 or higher suggests excellent quality wine.

**Options for Wine Type:** The app offers users the choice between predicting the quality of white wine or red wine. This allows users to specify the type of wine they are evaluating, as different types may have distinct characteristics and quality criteria.

## Features
**Prediction Input**: Users can input wine characteristics such as acidity, sugar content, and alcohol level to receive quality predictions.

**Interactive Visualizations**: Various plots and charts are generated to visualize the distribution of features, feature importance, and model performance metrics.

**Model Analysis**: Users can explore model predictions, examine feature importance, and gain insights into the factors affecting wine quality.

## Usage
Install the required dependencies listed in `requirements.txt`.
Run the Streamlit application using the command `streamlit run app.py`.
Access the application via the provided URL and interact with the interface to input wine characteristics and explore predictions and analysis.

## Challenges and Successes:
One challenge in quality prediction is handling imbalanced datasets, where certain quality ratings may be underrepresented. Successes include achieving accurate predictions and identifying key factors that influence quality.

## Future Improvements
Incorporate additional features or data sources such as wine origin or production process to improve prediction accuracy.
Experiment with advanced machine learning algorithms or ensemble techniques to further enhance model performance.
Enhance the user interface and visualization capabilities of the Streamlit application based on user feedback.

## Streamlit Video Snippet

[streamlit-wineapp-2024-05-05-21-05-83.webm](https://github.com/AdwoaM/Project_3_Wine-Quality-Prediction/assets/149966206/5899d82d-56de-4f9d-a7e4-f9ef7e230e3b)

## Contributors
[Adwoa & Owura]

## License
This project is licensed under the [License Name] License - see the [LICENSE.md](LICENSE.md) file for details.
---
Feel free to customize this template according to your specific project details and requirements!














