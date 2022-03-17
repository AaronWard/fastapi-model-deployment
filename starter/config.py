TEST_SPLIT_SIZE = 0.2
TARGET = "salary"
DATA_PATH = "./starter/data/census_cleaned.csv"
MODEL_PATH = "./starter/model/classifier.pkl"
METRICS_OUTPUT_PATH = "./starter/model/metrics_by_slice.csv"

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]