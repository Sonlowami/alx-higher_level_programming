#!/usr/bin/python3
"""Contain NyInt class"""


class MyInt(int):
    """Create a rebel class MyInt"""

    def __eq__(self, number):
        """Create an rebel equality check"""
        return self.real != number

    def __ne__(self, number):
        """Create a rebel non-equality check"""
        return self.real == number
