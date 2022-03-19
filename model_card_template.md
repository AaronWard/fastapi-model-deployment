# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
- Model consists of a Random Forest classifier which predicts whether someones salary is above $50,000. For this use case a binary classification approach was taken, whereby a sample showing a probability of 1.0 being positive and 0.0 being negative case.

## Intended Use
- This model isn't inteded to be used in a production setting. Just for this udacity projects :)

## Training Data
- The data utilized for training this model came from the Census Beurau, and consists of salary information - More information here: https://archive.ics.uci.edu/ml/datasets/census+income

## Evaluation Data
- Evaluation data comes from the same dataset, but it's from a 20% split of the samples not used during training.

## Metrics

```python
Precision: 0.7137404580152672
Recall: 0.6051779935275081
F1: 0.6549912434325744
```

## Ethical Considerations
- Some bias may be embedded within the data, particularly around race and ethnicity. This should be checked before depending on a model using demographic data as it's inputs.

## Caveats and Recommendations
- Recommendations include further data preprocessing and feature engineering to improve results.
- With respect to the above ethical considerations, it is required further investigation into the demographic data be performed to look for bias and fairness within the data.