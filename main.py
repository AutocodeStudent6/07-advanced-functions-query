from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    modifiers = [selector, *filters]
    for modifier in modifiers:
        data = modifier(data)
    return list(data)


def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""
    def modifier(data: DataType) -> DataType:
        for row in data:
            yield {col: row[col] for col in columns}
    return modifier


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""
    def modifier(data: DataType) -> DataType:
        for row in data:
            if row[column] in values:
                yield row
    return modifier
