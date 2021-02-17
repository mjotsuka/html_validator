#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by
    checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    if len(html) == 0:
        return True
    if "</" not in html:
        return False
    if type(html) == list:
        html = "".join(html)
    lis = _extract_tags(html)
    stack = []
    if len(lis) == 1:
        return False
    if "</" in lis[0]:
        return False
    for i in range(len(lis)):
        if "</" not in lis[i]:
            stack.append(lis[i])
        elif "</" in lis[i]:
            n = list(stack[-1])
            n.insert(1, "/")
            if n == list(lis[i]):
                stack.pop()
            else:
                return False
    return len(stack) == 0

    # HINT:
    # use the _extract_tags function below to generate a list of
    # html tags without any extra text;
    # then process these html tags using the balanced parentheses
    # algorithm from the class/book
    # the main difference between your code and the code from
    # class will be that you will have to keep track of not just
    # the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant
    to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained
    in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    lis = []
    if len(html) == 0:
        return lis
    elif "<" not in html:
        return lis
    else:
        for i in range(len(html)):
            if html[i] == "<":
                n = i
            if html[i] == ">":
                m = i
                lis.append(html[n:m + 1])
        return [j for j in lis if j.count("<") == 1]
