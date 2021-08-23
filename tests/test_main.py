import pytest
from ..main import query, select, field_filter

friends = [
    {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
    {'name': 'Emily', 'gender': 'female', 'sport': 'Volleyball'},
    {'name': 'John', 'gender': 'male', 'sport': 'Golf'},
]


@pytest.mark.parametrize(
    'columns, filter1, filter2, result', [
        (('name', 'gender', 'sport'),
         ('sport', *('Basketball', 'Volleyball')),
         ('gender', *('male',)),
         [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}]),

        (('name', 'gender'),
         ('name', *('Emily', 'Sam')),
         ('gender', *('female',)),
         [{'gender': 'female', 'name': 'Emily'}]),

        (('name', 'gender', 'sport'),
         ('name', *('Emily', 'John')),
         ('sport', *('Basketball', 'Volleyball')),
         [{'gender': 'female', 'name': 'Emily', 'sport': 'Volleyball'}]),
    ]
)
def test_query_with_two_filters(columns, filter1, filter2, result):
    value = query(
        friends,
        select(*columns),
        field_filter(*filter1),
        field_filter(*filter2),
    )
    assert result == value
