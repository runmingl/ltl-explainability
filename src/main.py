import fire

from ltl_regex import *
from ltl2aut import ltl_to_aut, aut_to_graph
from aut2regex import aut_to_regex
from vis import make_graph


class Ltl2Regex(object):
    def ltl2regex(self, formula: str):
        return aut_to_regex(aut_to_graph(ltl_to_aut(formula)))

    def ltl2timeline(self, formula: str, filename: str = "ltl", output_format: str = "pdf"):
        g = make_graph(aut_to_regex(aut_to_graph(
            ltl_to_aut(formula))), filename, output_format)
        g.view()


if __name__ == '__main__':
    fire.Fire(Ltl2Regex)


# print(Ltl2Regex.ltl2regex('G(a & b)'))
# print(Ltl2Regex.ltl2regex('G(a & b) & F(c & d)'))
# print(Ltl2Regex.ltl2regex('GFa -> GFb'))
# print(Ltl2Regex.ltl2regex('G(p xor Xp)'))
# print(Ltl2Regex.ltl2regex('0'))
# print(Ltl2Regex.ltl2regex('0 R p1'))
# print(Ltl2Regex.ltl2regex('F(XG(F!p1 M Fp1) W (p1 R p0))'))
# print(Ltl2Regex.ltl2regex('F(p0 R !p2)'))
# print(Ltl2Regex.ltl2regex('G(p0 | Fp1) W (FGp1 R !p1)'))
# print(Ltl2Regex.ltl2regex('X!(Xp0 U !p2)'))
# print(Ltl2Regex.ltl2regex('Fp2 | !(X(p2 xor Gp2) R (p1 W !Fp2))'))
# print(Ltl2Regex.ltl2regex('XXG((Xp1 R (p0 W p2)) -> (p2 R GXp0))'))
# print(Ltl2Regex.ltl2regex('X(0)'))
# print(Ltl2Regex.ltl2regex('XXF(p0 R p1)'))
