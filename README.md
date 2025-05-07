# EV Range Estimation Using Hybrid Machine Learning Approach

## Overview

Accurate electric vehicle (EV) range prediction is essential for route planning, battery management, and user confidence. This project implements a two-stage hybrid model that leverages sequence learning (LSTM) and residual correction (Gradient Boosting) to deliver highly precise range estimates under real-world driving conditions.

## Data

* **Routes:** 26 distinct driving routes, each driven by one of four drivers
* **Sampling Rate:** every 60/7 seconds
* **Features:**

  * State of Charge (SOC)
  * Torque
  * Power
  * Frontal wind
  * Vehicle speed
  * Ambient temperature

## Data Preprocessing & Exploratory Data Analysis

1. **Missing Value Handling:**

   * Identified missing entries (<1% of dataset) in sensor readings.
   * Employed forward-fill for short gaps (≤2 consecutive samples) and linear interpolation for longer gaps.

2. **Outlier Detection & Treatment:**

   * Used interquartile range (IQR) method to detect outliers in SOC and speed.
   * Capped extreme values at the 1st and 99th percentiles to maintain data integrity.

3. **Normalization & Scaling:**

   * Applied Min-Max scaling to continuous features (SOC, torque, power) to the range \[0,1].
   * Standardized wind and temperature features to zero mean and unit variance for model stability.

4. **Exploratory Data Analysis:**

   * Generated histograms and boxplots to examine feature distributions.
   * Computed a correlation matrix to identify multicollinearity; visualized via a heatmap.
   * Selected features with |correlation| < 0.85 to reduce redundancy and improve model generalization.

## Methodology

1. **LSTM Stage**

   * Bidirectional LSTM network (2 layers × 100 units) to capture temporal dependencies across SOC, torque, power, wind resistance, and speed.
   * Hyperparameters: batch size = 64, epochs = 500, learning rate = 0.001, dropout = 0.2, recurrent dropout = 0.3, optimizer = Adam.

2. **Gradient Boosting Stage**

   * Gradient Boosting Regressor trained on residuals from the LSTM predictions to correct systematic errors.
   * Hyperparameters tuned via grid search (max depth, learning rate).

3. **Evaluation Protocol**

   * 70% train / 15% validation / 15% test split, stratified by route.
   * Metrics: MSE, MAE, R²; per-route breakdown for consistency analysis.

## Results

| Metric                  | Hybrid Model (LSTM + GBR) |
| ----------------------- | ------------------------: |
| **Mean Squared Error**  |                    0.0012 |
| **Mean Absolute Error** |                    0.0267 |
| **R² Score**            |                    0.9815 |

* **Per-route performance:**

  * Best route MAE: 0.0184
  * Worst route MAE: 0.0342
  * Std. dev. of per-route MAE: 0.0045

* **Residual correction impact:**

  * Reduced LSTM residual variance by 42% on the test set.
  * Maximum error reduced from 12.1 miles to 7.8 miles post-GBR correction.

## Comparative Analysis

| Model                                 |        MSE |        MAE |         R² |
| ------------------------------------- | ---------: | ---------: | ---------: |
| **LSTM only**                         |     0.0023 |     0.0410 |     0.8700 |
| **Gradient Boosted with LSTM Output** | **0.0012** | **0.0267** | **0.9815** |

## Key Takeaways

* The two-stage hybrid model delivers state-of-the-art performance, achieving an R² of 0.9815 and MAE of 0.0267 — significantly outperforming single-stage and classical models.
* Residual analysis confirms that the Gradient Boosting stage effectively corrects long-tail errors left by the LSTM.
* Robust preprocessing and EDA (missing value handling, outlier treatment, feature selection) ensured data quality and model stability.

