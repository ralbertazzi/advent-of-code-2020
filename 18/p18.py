from pyparsing import ParserElement, Suppress, Forward, Group, ZeroOrMore, oneOf, Word, nums


def grammar() -> ParserElement:
    # https://stackoverflow.com/questions/23879784/parse-mathematical-expressions-with-pyparsing
    lpar, rpar = map(Suppress, '()')
    operand = Word(nums)
    expr = Forward()
    factor = operand | Group(lpar + expr + rpar)
    expr <<= factor + ZeroOrMore(oneOf('+ *') + factor)
    return expr


v = "3 * (2 + (9 * 2 * 2 + 8) * (7 * 6 * 7 * 3) * (3 * 9 * 7) * (6 * 6)) * 9 * 8 + 6"
expr = grammar()
ret = expr.parseString(v)
print(ret)
