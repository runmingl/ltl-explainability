from ltl_regex import *
from ltl2aut import ltl_to_aut, aut_to_graph
from aut2regex import aut_to_regex

def test(formula: str):
    print(aut_to_regex(aut_to_graph(ltl_to_aut(formula))))

test('G(a & b)')
test('G(a & b) & F(c & d)')
test('GFa -> GFb')
test('G(p xor Xp)')
test('0')
test('0 R p1')
test('F(XG(F!p1 M Fp1) W (p1 R p0))')
test('F(p0 R !p2)')
test('G(p0 | Fp1) W (FGp1 R !p1)')
test('X!(Xp0 U !p2)')
test('Fp2 | !(X(p2 xor Gp2) R (p1 W !Fp2))')
test('XXG((Xp1 R (p0 W p2)) -> (p2 R GXp0))')
test('X(0)')
test('XXF(p0 R p1)')