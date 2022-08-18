#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cons(v1, v2) -> list:
    return [v1, v2]


def car(v: list):
    return v[0]


def cdr(v: list):
    return v[1]


def cadr(v: list):
    return car(cdr(v))


def caddr(v: list):
    return car(cdr(cdr(v)))


def is_pair(x) -> bool:
    return isinstance(x, list) and len(x) == 2


def list_(*args) -> list:
    if args:
        return cons(args[0], list_(*args[1:]))
    else:
        return []


def is_variable(e) -> bool:
    return isinstance(e, str)


def is_same_variable(v1, v2) -> bool:
    if isinstance(v1, str) and isinstance(v2, str) and v1 == v2:
        return True
    else:
        return False


def is_number(e) -> bool:
    return isinstance(e, int)


def is_sum(x) -> bool:
    return is_pair(x) and car(x) == '+'


def addend(s):
    return cadr(s)


def augend(s):
    return caddr(s)


def make_sum(a1, a2) -> list:
    if is_number(a1) and a1 == 0:
        return a2
    elif is_number(a2) and a2 == 0:
        return a1
    else:
        return list_('+', a1, a2)


def is_product(x) -> bool:
    return is_pair(x) and car(x) == '*'


def multiplier(p):
    return cadr(p)


def multiplicand(p):
    return caddr(p)


def make_product(m1, m2):
    if (is_number(m1) and m1 == 0) or (is_number(m2) and m2 == 0):
        return 0
    elif is_number(m1) and m1 == 1:
        return m2
    elif is_number(m2) and m2 == 1:
        return m1
    elif is_number(m1) and is_number(m2):
        return m1 * m2
    else:
        return list_('*', m1, m2)


def deriv(exp, var):
    if is_number(exp):
        return 0
    elif is_variable(exp):
        if is_same_variable(exp, var):
            return 1
        else:
            return 0
    elif is_sum(exp):
        return make_sum(deriv(addend(exp), var), deriv(augend(exp), var))
    elif is_product(exp):
        return make_sum(
            make_product(
                multiplier(exp), deriv(multiplicand(exp), var)
            ),
            make_product(
                deriv(multiplier(exp), var), multiplicand(exp)
            ),
        )
    else:
        raise Exception("unknow expression type -- %r" % exp)


def print_(p):
    if is_sum(p) or is_product(p):
        print("( %s" % car(p), end=' ')
        print_(cdr(p))
        print(")", end='')
    elif is_pair(p) and p != []:
        print_(car(p))
        print_(cdr(p))
    elif is_number(p) or is_variable(p):
        print(p, end=' ')


if __name__ == '__main__':
    r = deriv(
        list_(
            '*', list_('*', 'x', 'y'), list_('+', 'x', 3)
        ),
        'x'
    )
    print_(r)
