**TASK:**
Turn the content into valid json like on the schema.
Remember to put values of arguments in correct lists.
Tool called `apply_math_function` expects `categorical_arguments` to be filled with one of accepted string values and `numerical_arguments` to be empty! Same goes for `normalizer` etc. Look at TOOLS section for accepted values.

**TOOLS:**
- `standard_scaler(column_name:)`
- `min_max_scaler(column_name:)`
- `max_abs_scaler(column_name:)`
- `quantile_transformer(column_name:, n_quantiles:, output_distribution:['uniform', 'normal'])`
- `power_transformer(column_name:, method:['yeo-johnson', 'box-cox'])`
- `apply_math_function(column_name:, function:['log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round'])`
- `normalizer(column_name:, norm:['l1', 'l2', 'max'])`
- `binarizer(column_name:, threshold:)`
- `polynomial_features(column_name:, degree:)`
- `k_bins_discretizer(column_name:, n_bins:, encode:['ordinal'], strategy:['uniform', 'quantile', 'kmeans'])`
- `ordinal_encoder(column_name:)`
- `one_hot_encoder(column_name:)`
- `linear_combination(column_name_1:, column_name_2:, weight_1:, weight_2:)`
- `create_interaction(column_name_1:, column_name_2:)`
- `subtract_columns(column_name_1:, column_name_2:)`
- `reduce_dimentionality(columns:, method:['PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis'])`

**SCHEMA:**
{'type': 'object', 'properties': {'transformations': {'type': 'array', 'items': {'type': 'object', 'properties': {'function': {'type': 'string', 'enum': ['standard_scaler', 'min_max_scaler', 'max_abs_scaler', 'quantile_transformer', 'power_transformer', 'apply_math_function', 'normalizer', 'binarizer', 'polynomial_features', 'k_bins_discretizer', 'ordinal_encoder', 'one_hot_encoder', 'linear_combination', 'create_interaction', 'subtract_columns', 'reduce_dimentionality']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['petal_length', 'petal_width', 'sepal_length', 'sepal_width', 'species']}}, 'numerical_arguments': {'type': 'array', 'items': {'type': 'number'}}, 'categorical_arguments': {'type': 'array', 'items': {'type': 'string', 'enum': ['uniform', 'normal', 'yeo-johnson', 'box-cox', 'max', 'ordinal', 'quantile', 'kmeans', 'log', 'sqrt', 'exp', 'square', 'cube', 'inverse', 'log2', 'log10', 'abs', 'ceil', 'floor', 'round', 'l1', 'l2', 'PCA', 'TruncatedSVD', 'FastICA', 'FactorAnalysis']}}}, 'required': ['function', 'columns', 'numerical_arguments', 'categorical_arguments']}}}, 'required': ['transformations']}

**CONTENT**:
 Based on the current dataset and the information provided, here are ten possible column-tool combinations for feature engineering that could potentially improve the performance of the Gaussian Naive Bayes Classifier model:

1. **One-hot encoder for 'workclass'**: This categorical feature has missing values, so it would be beneficial to encode it as one-hot vectors, which will convert each unique category into a binary column.

   ```python
   one_hot_encoder('workclass')
   ```

2. **Polynomial features for 'education'**: Adding polynomial features can capture non-linear relationships between the input variables and the target label. The degree of interaction between the features can be specified as an argument.

   ```python
   polynomial_features('education', degree=2)
   ```

3. **Subtract 'capitalgain' from 'fnlwgt'**: The difference between these two columns might have a strong correlation with the target label, providing additional information for the model to use.

   ```python
   subtract_columns('capitalgain', 'fnlwgt')
   ```

4. **Binarizer for 'marital-status'**: Transform categorical features like marital status into binary columns using a threshold value, which is set based on the distinct values in the column.

   ```python
   binarizer('marital-status', threshold='Divorced')
   binarizer('marital-status', threshold='Married-AF-Spouse')
   binarizer('marital-status', threshold='Married-Civ-Spouse')
   binarizer('marital-status', threshold='Married-Spouse-Absent')
   binarizer('marital-status', threshold='Never-Married')
   binarizer('marital-status', threshold='Separated')
   binarizer('marital-status', threshold='Widowed')
   ```

5. **Create interaction between 'age' and 'education-num'**: The interaction between these two features might be important in understanding the relationship with the target variable, as they are both relevant factors.

   ```python
   create_interaction('age', 'education-num')
   ```

6. **Quantile transformer for 'fnlwgt'**: Transform 'fnlwgt' into quantiles to make the distribution more Gaussian, which is expected by the Naive Bayes Classifier algorithm.

   ```python
   quantile_transformer('fnlwgt', n_quantiles=10, output_distribution='uniform')
   ```

7. **Ordinal encoder for 'marital-status'**: Encode marital status as ordinal numbers instead of one-hot vectors to preserve the inherent ordering of the categories.

   ```python
   ordinal_encoder('marital-status')
   ```

8. **Normalizer for 'age'**: Normalize the age feature by applying a normalization method like L1 or L2 norm, which will reshape the distribution to have zero mean and unit variance.

   ```python
   normalizer('age', norm='l2')
   ```

9. **Power transformer for 'capitalgain'**: Apply a power transformation to 'capitalgain' using methods like Yeo-Johnson or Box-Cox to make the distribution more Gaussian and better suited for the Naive Bayes Classifier model.

   ```python
   power_transformer('capitalgain', method='box-cox')
   ```

10. **Linear combination of 'hoursperweek' and 'capitalloss'**: Create a new feature by combining these two columns using a linear combination, which might provide additional insights into the relationship with the target variable.

    ```python
    linear_combination('hoursperweek', 'capitalloss', weight_1=-0.5, weight_2=0.5)
    ```

**JSON:**
