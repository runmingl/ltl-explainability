from ltl_regex import *

def regex_simplifier(r: Regex) -> Regex:
    match r:
        case Epsilon():
            return Epsilon()
        case Symbol(s):
            return Symbol(s)
        case Concat(r1, r2):
            r_new = Concat(regex_simplifier(r1), regex_simplifier(r2))
            match (r_new.left, r_new.right):
                # εr = rε = r
                case (Epsilon(), r2_new):
                    return r2_new
                case (r1_new, Epsilon()):
                    return r1_new

                # (ε+r)r* = r*(ε+r) = r*
                case (Union(Epsilon(), r1_new), Star(r2_new)):
                    if r1_new == r2_new:
                        return Star(r2_new)
                case (Star(r1_new), Union(Epsilon(), r2_new)):
                    if r1_new == r2_new:
                        return Star(r1_new)

                # (r1+r2)r2* = r1r2*
                case (Union(r1_new, r2_neww), Star(r2_new)):
                    if r2_neww == r2_new:
                        return Concat(r1_new, Star(r2_new))

                # r1(r2r3) = (r1r2)r3
                case (r1_new, Concat(r2_new, r3_new)):
                    return Concat(Concat(r1_new, r2_new), r3_new)
            return r_new
        case Union(r1, r2):
            r_new = Union(regex_simplifier(r1), regex_simplifier(r2))
            match (r_new.left, r_new.right):
                # r1 + (r1r2)* = r1r2*
                case (r1_new, Star(Concat(r1_neww, r2_new))):
                    if r1_new == r1_neww:
                        return Concat(r1_new, Star(r2_new))

                # r1 + (r2r1)* = r2r1*
                case (r1_new, Star(Concat(r2_new, r1_neww))):
                    if r1_new == r1_neww:
                        return Concat(r2_new, Star(r1_new))

                # r1 + r1 = r1
                case (r1_new, r1_neww):
                    if r1_new == r1_neww:
                        return r1_new

                # r1 + (r2 + r3) = (r1 + r2) + r3
                case (r1_new, Union(r2_new, r3_new)):
                    return Union(Union(r1_new, r2_new), r3_new)
            return r_new
        case Star(r):
            r_new = Star(regex_simplifier(r))
            match r_new.regex:
                # (ε + r)* = (r + ε) = r*
                case Union(Epsilon(), r2_new):
                    return Star(r2_new)
                case Union(r2_new, Epsilon()):
                    return Star(r2_new)
            return r_new

def omega_regex_simplifier(r: OmegaRegex) -> OmegaRegex:
    match r:
        case Repeat(r):
            return Repeat(regex_simplifier(r))
        case ConcatOmega(r1, r2):
            r_new = ConcatOmega(regex_simplifier(r1), omega_regex_simplifier(r2))
            match (r_new.left, r_new.right):
                # (r1r2*)r2w = r1r2w
                case (Concat(r1_new, Star(r2_new)), Repeat(r2_neww)):
                    if r2_new == r2_neww:
                        return ConcatOmega(r1_new, Repeat(r2_new))

                # r1r1w = r1w
                case (r1_new, Repeat(r1_neww)):
                    if r1_new == r1_neww:
                        return Repeat(r1_new)
            return r_new
        case UnionOmega(r1, r2):
            return UnionOmega(omega_regex_simplifier(r1), omega_regex_simplifier(r2))

def simplify(func):
    def inner(*args, **kwargs):
        r = func(*args, **kwargs)
        if r is None:
            return None
        return omega_regex_simplifier(r)
    return inner
