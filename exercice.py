#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def check_brackets(text, brackets):
    opening = dict(zip(brackets[0::2], brackets[1::2]))
    closing = dict(zip(brackets[1::2], brackets[0::2]))

    bracket_stack = deque()

    for t in text:
        if t in opening:
            bracket_stack.append(opening[t])
        elif t in closing:
            if bracket_stack and bracket_stack[-1] == t:
                bracket_stack.pop()
            else:
                return False

    return not bracket_stack


def remove_comments(full_text, comment_start, comment_end):
    text = ""
    comment = False

    i = 0
    while i < len(full_text):
        if full_text[i:i + len(comment_start)] == comment_start and not comment:
            comment = True
            i += len(comment_start) - 1
        elif full_text[i:i + len(comment_end)] == comment_end:
            if comment:
                comment = False
                i += len(comment_end) - 1
            else:
                return None
        elif not comment:
            text += full_text[i]
        i += 1

    if comment:
        return None
    return text


def get_tag_prefix(text, opening_tags, closing_tags):
    return (None, None)


def check_tags(full_text, tag_names, comment_tags):
    return False


if __name__ == "__main__":
    brackets = ("(", ")", "{", "}")
    yeet = "(yeet){yeet}"
    yeeet = "({yeet})"
    yeeeet = "({yeet)}"
    yeeeeet = "(yeet"
    print(check_brackets(yeet, brackets))
    print(check_brackets(yeeet, brackets))
    print(check_brackets(yeeeet, brackets))
    print(check_brackets(yeeeeet, brackets))
    print()

    spam = "Hello, /* OOGAH BOOGAH */world!"
    eggs = "Hello, /* OOGAH BOOGAH world!"
    parrot = "Hello, OOGAH BOOGAH*/ world!"
    print(remove_comments(spam, "/*", "*/"))
    print(remove_comments(eggs, "/*", "*/"))
    print(remove_comments(parrot, "/*", "*/"))
    print()

    otags = ("<head>", "<body>", "<h1>")
    ctags = ("</head>", "</body>", "</h1>")
    print(get_tag_prefix("<body><h1>Hello!</h1></body>", otags, ctags))
    print(get_tag_prefix("<h1>Hello!</h1></body>", otags, ctags))
    print(get_tag_prefix("Hello!</h1></body>", otags, ctags))
    print(get_tag_prefix("</h1></body>", otags, ctags))
    print(get_tag_prefix("</body>", otags, ctags))
    print()

    spam = (
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
        "</html>"
    )
    eggs = (
        "<html>"
        "  <head>"
        "    <title>"
        "      <!-- Ici j'ai écrit qqch -->"
        "      Example"
        "    <!-- Il manque un end tag"
        "    </title>-->"
        "  </head>"
        "</html>"
    )
    parrot = (
        "<html>"
        "  <head>"
        "    <title>"
        "      Commentaire mal formé -->"
        "      Example"
        "    </title>"
        "  </head>"
        "</html>"
    )
    tags = ("html", "head", "title", "body", "h1")
    comment_tags = ("<!--", "-->")
    print(check_tags(spam, tags, comment_tags))
    print(check_tags(eggs, tags, comment_tags))
    print(check_tags(parrot, tags, comment_tags))
    print()
