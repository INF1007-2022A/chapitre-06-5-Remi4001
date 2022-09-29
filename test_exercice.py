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
            "Hello, /*/**/world!",
        ]
        expected = [
            "Hello, world!",
            None,
            None,
            None,
            None,
            "Hello, world!",
        ]

        output = [exercice.remove_comments(
            v, comment[0], comment[1]) for v in values]
        self.assertListEqual(
            output,
            expected,
            "Mauvais retrait des commentaires"
        )

    def test_remove_comments2(self):
        values = [
            ["Hello, 1 OOGAH BOOGAH 23456world!", "1", "23456"],
            ["Hello, world! ", "l", " "],
        ]
        expected = [
            "Hello, world!",
            "Hewor",
        ]

        output = [exercice.remove_comments(v[0], v[1], v[2]) for v in values]
        self.assertListEqual(
            output,
            expected,
            "Mauvais retrait des commentaires"
        )

    def test_get_tag_prefix(self):
        otags = ("<head>", "<body>", "<h1>", " ")
        ctags = ("</head>", "</body>", "</h1>", ".")
        values = [
            "<body><h1>Hello!</h1></body>",
            "<h1>Hello!</h1></body>",
            "Hello!</h1></body>",
            "</h1></body>",
            "</body>",
            " </body>",
            ".</body>",
        ]
        expected = [
            ("<body>", None),
            ("<h1>", None),
            (None, None),
            (None, "</h1>"),
            (None, "</body>"),
            (" ", None),
            (None, "."),
        ]

        output = [exercice.get_tag_prefix(v, otags, ctags) for v in values]
        self.assertListEqual(
            output,
            expected,
            "Mauvaise identification des balises au début d'un texte"
        )

    def test_check_tags(self):
        tags = ("html", "head", "title", "body", "h1")
        comment_tags = ("<!--", "-->")
        values = [
            "<html>"
            "  <head>"
            "    <title>"
            "      <!-- Ici j'ai écrit qqch -->"
            "      Example"
            "    </title>"
            "  </head>"
            "  <body>"
            "    <h1>Hello, world</h1>"
            "    <!-- Les tags vides sont ignorés -->"
            "    <br>"
            "    <h1/>"
            "  </body>"
            "</html>",
            "<html>"
            "  <head>"
            "    <title>"
            "      <!-- Ici j'ai écrit qqch -->"
            "      Example"
            "    <!-- Il manque un end tag"
            "    </title>-->"
            "  </head>"
            "</html>",
            "<html>"
            "  <head>"
            "    <title>"
            "      Commentaire mal formé -->"
            "      Example"
            "    </title>"
            "  </head>"
            "</html>",
        ]
        expected = [
            True,
            False,
            False,
        ]

        output = [exercice.check_tags(v, tags, comment_tags) for v in values]
        self.assertListEqual(
            output,
            expected,
            "Mauvaise vérification des balises HTML"
        )


if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
    print(open('logs/tests_results.txt', 'r').read())
