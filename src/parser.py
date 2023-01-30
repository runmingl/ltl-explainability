import sys
sys.path.append('./pylogics')

from pylogics.parsers import parse_pl
from pylogics.syntax.base import Not, And, Or, TrueFormula
from pylogics.syntax.pl import Atomic

def to_latex(f) -> str:
    match f:
        case Atomic():
            return f"\\text{{{f.name}}}"
        case Not():
            return f"\\neg {to_latex(f.argument)}"
        case And():
            output = f"{to_latex(f.operands[0])}"
            for operand in f.operands[1:]:
                output += f" \\land {to_latex(operand)}"
            return output
        case Or():
            output = f"{to_latex(f.operands[0])}"
            for operand in f.operands[1:]:
                output += f" \\lor {to_latex(operand)}"
            return output
        case TrueFormula():
            return "\\top"

def parse(formula: str):
    return to_latex(parse_pl(formula))
