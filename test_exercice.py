#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest

import exercice


class TestExercice(unittest.TestCase):
    def test_check_brackets(self):
        brackets = ("(", ")", "{", "}")
        values = [
            "(yeet){yeet}",
            "({yeet})",
            "({yeet)}",
            "(yeet",
            "yeet}",
        ]
        expected = [
            True,
            True,
            False,
            False,
            False,
        ]

        output = [exercice.check_brackets(v, brackets) for v in values]
        self.assertListEqual(
            output,
            expected,
            "Mauvaise vérification des parenthèses et accolades"
        )

    def test_remove_comments1(self):
        comment = ("/*", "*/")
        values = [
            "Hello, /* OOGAH BOOGAH */world!",
            "Hello, /* OOGAH BOOGAH world!",
            "Hello, OOGAH BOOGAH*/ world!",
            "Hello, /*/ OOGAH BOOGAH world!",
            "Hello, */ OOGAH BOOGAH /*world!",
            "Hello, /**/world!",
        ]
        expected = [
            "Hello, world!",
            None,
            None,
            None,
            None,
            "Hello, world!",
        ]

        output = [exercice.remove_comments(v, comment[0], comment[1]) for v in values]
        self.assertListEqual(
            output,
            expected,
            "Mauvais retrait des commentaires"
        )


if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
    print(open('logs/tests_results.txt', 'r').read())
