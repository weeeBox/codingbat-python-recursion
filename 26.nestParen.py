from unittest import TestCase


def nestParen(s: str) -> bool:
    """
    Given a string, return true if it is a nesting of zero or more pairs of parenthesis, like "(())" or "((()))".
    Suggestion: check the first and last chars, and then recur on what's inside them.
    nestParen("(())") → true
    nestParen("((()))") → true
    nestParen("(((x))") → false
    """
    pass


class Test(TestCase):
    pass
