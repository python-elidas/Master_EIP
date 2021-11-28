'''
Author: Oscar Gutierrez
Email:  o.guty66@gmail.com
Date:   2021-06-21
Python Version: 3.6.9
code version: 0.0.1
'''
# __LIBRARIES__ #
import pytest
from actividad_2 import CSV


# __MAIN CODE__ #
def test_spend():
    file = CSV('finanzas2020.csv')
    assert file.get_month_spend()[0] < 0
    for key in file.get_month_spend()[1]:
        assert file.get_month_spend()[1][key] < 0
    assert len(file.get_month_spend()[1]) == 12


def test_income():
    file = CSV('finanzas2020.csv')
    assert file.get_month_income()[0] > 0
    for key in file.get_month_income()[1]:
        assert file.get_month_income()[1][key] > 0
    assert len(file.get_month_income()[1]) == 12


def test_save():
    file = CSV('finanzas2020.csv')
    assert len(file.get_month_save()) == 12


# __NOTES__ #
'''

'''
# __BIBLIOGRAPHY__ #
'''

'''
