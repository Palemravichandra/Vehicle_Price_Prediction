# Vehicle_Price_Prediction_Project
### Importing the required libraries
```python
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
```
### Data preprocessing
- checking for shape of data,columns data type
- converting the columns
- Creating dictionary with key value pairs by using carname column
### outlier tratement
- dropping the outliers which is faraway from other data points
### correlation and feature importance
- checking for correlation using heat map
- checking for most important features using extratreesRegreesor
### Model Building
- Splitting the model for Training and testing
- creating the model for using randomforest regressor
- make prediction on test data
- saving the model
### App creation
- Creating the app using streamlit application

