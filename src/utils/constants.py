from sklearn import preprocessing

SUPPORTED_NORMALIZER_TYPE = ["StandardScaler", "MinMaxScaler"]

NORMALIZER_TYPE_2_NORMALIZER_METHOD = {
    "StandardScaler": preprocessing.StandardScaler(),
    "MinMaxScaler": preprocessing.MinMaxScaler(),
}
