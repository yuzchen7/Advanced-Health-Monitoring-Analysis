from typing import List

def filter_nondigits(data: list) -> list:
    """
    Function Name: filter_nondigits

    Return the data that is filter out all the non digits, and cover the STRING
    dat into INTEGER data type

    Args:
        data (List[str]): List of data in str type
    Returns:
        List[integer]: the result of all valid data in Integer from input List
    """
    data = data.split("\n")
    result: List[int] = []
    for line in data:
        if line.isdigit():
            result.append(int(line))
    return result
    # pass