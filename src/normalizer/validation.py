def is_normalizer_type_exist(normalizer_type: str, supported_normalizer_type: list) -> None:
    """

    :param normalizer_type:
    :param supported_normalizer_type:
    :return:
    """
    if normalizer_type not in supported_normalizer_type:
        raise Exception(f"Normalizer type is not supported.\n"
                        f"supported normalizer type : {supported_normalizer_type}")
