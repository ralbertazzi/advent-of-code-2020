from functools import reduce
from typing import Union, cast

from pyparsing import Forward, Group, ParserElement, Suppress, Word, ZeroOrMore, nums, oneOf


def grammar() -> ParserElement:
    # https://stackoverflow.com/questions/23879784/parse-mathematical-expressions-with-pyparsing
    lpar, rpar = map(Suppress, "()")
    operand = Word(nums)
    expr = Forward()
    factor = operand | Group(lpar + expr + rpar)
    expr <<= factor + ZeroOrMore(oneOf("+ *") + factor)
    return expr


# v = "3 * (2 + (9 * 2 * 2 + 8) * (7 * 6 * 7 * 3) * (3 * 9 * 7) * (6 * 6)) * 9 * 8 + 6"
# expr = grammar()
# ret = expr.parseString(v)
# print(ret)


with open("data.txt") as f:
    expressions: list[str] = [line.strip() for line in f.readlines()]


def solve_1(expr: list) -> int:
    def solve_operand(operand: Union[str, list]) -> int:
        return int(operand) if isinstance(operand, str) else solve_1(operand)

    result = solve_operand(expr[0])
    for i in range(1, len(expr), 2):
        operator = expr[i]
        operand = solve_operand(expr[i + 1])
        result = (result + operand) if operator == "+" else (result * operand)

    return result


def solve_2(expr: list) -> int:
    def solve_operand(operand: Union[str, list]) -> int:
        return int(operand) if isinstance(operand, str) else solve_2(operand)

    expr = [op if i % 2 == 1 else solve_operand(op) for i, op in enumerate(expr)]

    try:
        while i := expr.index("+"):
            partial = expr[i - 1] + expr[i + 1]
            expr = expr[: i - 1] + [partial] + expr[i + 2 :]
    except ValueError:
        pass

    return reduce(lambda x, y: x * y, filter(lambda x: x != "*", expr), 1)


for solve_fn in (solve_1, solve_2):
    results: list[int] = []
    gram = grammar()

    for expression in expressions:
        results.append(solve_fn(cast(list, gram.parseString(expression))))

    print(sum(results))
