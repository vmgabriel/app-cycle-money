# Develop: vmgabriel

"""Module that define convertion data"""

from typing import Any, List
from django import template

register = template.Library()


def minus(data: int):
    """Minus data 1"""
    return data - 1


def more(data: int):
    """more data 1"""
    return data + 1


def join_array(data: List[Any]):
    """convert split to comma"""
    return ','.join(data)


def add_comma_end(data: List[Any]):
    """add to str a comma"""
    return data + ',' if len(data) > 0 else ''


def negative(data: str):
    """convert negative data if this not have"""
    return '-' + data if data[0] != '-' else data[1:]


def delete_last(data: str):
    """delete last data"""
    return data[:-1]


def add_anpersand_search(data: str):
    """Add Data Anpersand data"""
    return '&search={}'.format(data) if len(data) > 0 else ''


def to_boolean_know(data: bool):
    """Convert to boolean know"""
    return 'Yes' if data else 'No'


register.filter('minus', minus)
register.filter('more', more)
register.filter('join_array', join_array)
register.filter('negative', negative)
register.filter('delete_tast', delete_last)
register.filter('add_comma_end', add_comma_end)
register.filter('add_anpersand_search', add_anpersand_search)
register.filter('to_boolean_know', to_boolean_know)
