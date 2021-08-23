from typing import List, Dict, Any


def select(*field_names: str) -> List:
    """Returns a list of sorted field names to display in query result"""
    return sorted(list(field_names))


def field_filter(field_name: str, *values) -> List:
    """Returns filter as list"""
    filter = [field_name]
    filter.extend(values)
    return filter


def query(data: List[Dict[str, Any]], selection, *filters: callable) -> List[Dict[str, Any]]:
    """Returns query result"""
    if filters:
        new_data = []
        count = len(filters)
        for i in range(len(data)):
            for j in filters:
                if data[i][j[0]] in j[:]:
                    count -= 1
                    if count == 0:
                        new_data.append(data[i])
                else:
                    break

        query_rez = []
        for i in range(len(new_data)):
            rez_item = {}
            for j in selection:
                rez_item[j] = new_data[i][j]
            query_rez.append(rez_item)
        return query_rez
    return data
