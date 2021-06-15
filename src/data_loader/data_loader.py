import pandas


def load_excel(path: str, headers: list) -> pandas.DataFrame:
    """

    :param path:
    :param headers:
    :return:
    """
    return pandas.read_excel(path, usecols=headers)
