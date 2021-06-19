import pandas

from normalizer import is_normalizer_type_exist
from utils import SUPPORTED_NORMALIZER_TYPE, NORMALIZER_TYPE_2_NORMALIZER_METHOD


def normalizer(data: pandas.DataFrame, normalizer_type: str) -> pandas.DataFrame:
    """

    :param data:
    :param normalizer_type:
    :return:
    """
    is_normalizer_type_exist(normalizer_type, SUPPORTED_NORMALIZER_TYPE)
    normalizer_method = NORMALIZER_TYPE_2_NORMALIZER_METHOD[normalizer_type]
    data.iloc[:, 0:-1] = normalizer_method.fit_transform(data.iloc[:, 0:-1].to_numpy())
    return data


if __name__ == '__main__':
    import os
    from configuration import BaseConfig
    from data_loader import load_excel
    args = BaseConfig().get_config()
    path = os.path.join(args.data_dir, args.data_file)
    headers = ["VO", "DVO",	"IL", "DIL", "E", "DE",	"U=Target"]
    df = load_excel(path, headers)
    print(df.head())
    data_scaled = normalizer(df, args.normalizer_type)
    data_scaled.to_excel("tt.xlsx", index=False)

