from unittest import TestCase


def stringClean(s: str) -> str:
    """
    Given a string, return recursively a "cleaned" string where adjacent chars that are the same have been reduced to a
    single char. So "yyzzza" yields "yza".
    
    Examples:
    stringClean("yyzzza") → "yza"
    stringClean("abbbcdd") → "abcd"
    stringClean("Hello") → "Helo"
    """
    pass


class Test(TestCase):
    def test1(self):
        self.assertEqual("yza", stringClean("yyzzza"))

    def test2(self):
        self.assertEqual("abcd", stringClean("abbbcdd"))

    def test3(self):
        self.assertEqual("Helo", stringClean("Hello"))

    def test4(self):
        self.assertEqual("XabcY", stringClean("XXabcYY"))

    def test5(self):
        self.assertEqual("12ab45", stringClean("112ab445"))
