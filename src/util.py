from ltl_regex import *
from typing import Set


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

                # r1(r2r3) = (r1r2)r3
                case (r1_new, Concat(r2_new, r3_new)):
                    return Concat(Concat(r1_new, r2_new), r3_new)
            return r_new
        case Union(r1, r2):
            r_new = Union(regex_simplifier(r1), regex_simplifier(r2))
            match (r_new.left, r_new.right):
                # r1 + r1r2* = r1r2*
                case (r1_new, Concat(r1_neww, Star(r2_new))):
                    if r1_new == r1_neww:
                        return Concat(r1_new, Star(r2_new))
                    match (r_new.left, r_new.right):
                        # r1 + r1 = r1
                        case (r1_new, r1_neww):
                            if r1_new == r1_neww:
                                return r1_new

                # r1 + r2*r1 = r2*r1
                case (r1_new, Concat(Star(r2_new), r1_neww)):
                    if r1_new == r1_neww:
                        return Concat(Star(r2_new), r1_new)
                    match (r_new.left, r_new.right):
                        # r1 + r1 = r1
                        case (r1_new, r1_neww):
                            if r1_new == r1_neww:
                                return r1_new

                # r1 + (r2 + r3) = (r1 + r2) + r3
                case (r1_new, Union(r2_new, r3_new)):
                    return Union(Union(r1_new, r2_new), r3_new)

                # r1 + r1 = r1
                case (r1_new, r1_neww):
                    if r1_new == r1_neww:
                        return r1_new
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
        case _:
            raise TypeError(f'Unsupported regex type: {type(r)}')


def omega_regex_simplifier(r: OmegaRegex) -> OmegaRegex:
    match r:
        case Repeat(rp):
            r_new = Repeat(regex_simplifier(rp))
            match r_new.regex:
                # (r*)w = rw
                case Star(r_neww):
                    return Repeat(r_neww)
            return r_new
        case ConcatOmega(r1, r2):
            r_new = ConcatOmega(regex_simplifier(
                r1), omega_regex_simplifier(r2))
            match (r_new.left, r_new.right):
                # (r1r2*)r2w = r1r2w
                case (Concat(r1_new, Star(r2_new)), Repeat(r2_neww)):
                    if r2_new == r2_neww:
                        return ConcatOmega(r1_new, Repeat(r2_new))
                # r1*r1w = r1w
                case (Star(r1_new), Repeat(r1_neww)):
                    if r1_new == r1_neww:
                        return Repeat(r1_new)
                # (r1r2)r2w = r1r2w
                case (Concat(r1_new, r2_new), Repeat(r2_neww)):
                    if r2_new == r2_neww:
                        return ConcatOmega(r1_new, Repeat(r2_new))
                    match (r_new.left, r_new.right):
                        case (r1_new, Repeat(r1_neww)):
                            if r1_new == r1_neww:
                                return Repeat(r1_new)
                # r1r1w = r1w
                case (r1_new, Repeat(r1_neww)):
                    if r1_new == r1_neww:
                        return Repeat(r1_new)
            return r_new
        case UnionOmega(r1, r2):
            r_new = UnionOmega(omega_regex_simplifier(r1), omega_regex_simplifier(r2))

            # a semi hard-code optimization (TODO: generalize)
            match (r_new.left, r_new.right):
                case (ConcatOmega(Union(r1, Concat(r11, r12)), Repeat(Concat(r21, r22))),
                      ConcatOmega(Union(r3, Concat(r31, r32)), Repeat(Concat(r41, r42)))):
                    if r1 == r12 and r1 == r22 and r11 == r21 \
                        and r3 == r32 and r3 == r42 and r31 == r41 \
                        and r1 == r31 and r3 == r11:
                        return r_new.left
            return r_new

def simplify(func):
    def inner(*args, **kwargs):
        r = func(*args, **kwargs)
        if r is None:
            return None
        return omega_regex_simplifier(r)
    return inner


def regex_size(r: Regex) -> int:
    match r:
        case Epsilon():
            return 1
        case Empty():
            return 1
        case Symbol(_):
            return 1
        case Concat(r1, r2):
            return 1 + regex_size(r1) + regex_size(r2)
        case Union(r1, r2):
            return 1 + regex_size(r1) + regex_size(r2)
        case Star(r):
            return 1 + regex_size(r)
        case _:
            raise TypeError(f'Unsupported regex type: {type(r)}')


def omega_regex_size(r: OmegaRegex) -> int:
    match r:
        case Repeat(rp):
            return 1 + regex_size(rp)
        case ConcatOmega(r1, r2):
            return 1 + omega_regex_size(r1) + omega_regex_size(r2)
        case UnionOmega(r1, r2):
            return 1 + omega_regex_size(r1) + omega_regex_size(r2)
        case _:
            raise TypeError(f'Unsupported regex type: {type(r)}')


def star_height_regex(r: Regex) -> int:
    match r:
        case Epsilon():
            return 0
        case Empty():
            return 0
        case Symbol(_):
            return 0
        case Concat(r1, r2):
            return max(star_height_regex(r1), star_height_regex(r2))
        case Union(r1, r2):
            return max(star_height_regex(r1), star_height_regex(r2))
        case Star(r):
            return 1 + star_height_regex(r)
        case _:
            raise TypeError(f'Unsupported regex type: {type(r)}')


def star_height_omega_regex(r: OmegaRegex) -> int:
    match r:
        case Repeat(r):
            return star_height_regex(r)
        case ConcatOmega(r1, r2):
            return max(star_height_omega_regex(r1), star_height_omega_regex(r2))
        case UnionOmega(r1, r2):
            return max(star_height_omega_regex(r1), star_height_omega_regex(r2))
        case _:
            raise TypeError(f'Unsupported regex type: {type(r)}')


# def forward_chaining(r: OmegaRegex, set: Set[OmegaRegex]) -> Set[OmegaRegex]:
#     match r:
#         case Repeat(rp):
#             match rp:
#                 case Concat(r1, r2):
#                     newr = ConcatOmega(r1, Repeat(Concat(r2, r1)))
#                     if newr not in set:
#                         set.add(newr)
#                         set = set | forward_chaining(newr, set)
#         case ConcatOmega(r1, r2):
#             match r1:
#                 case Union(r11, r12):
#                     newr = UnionOmega(ConcatOmega(r11, r2), ConcatOmega(r12, r2))
#                     if newr not in set:
#                         set.add(newr)
#                         set = set | forward_chaining(newr, set)
#                     newr = ConcatOmega(Union(r12, r11), r2)
#                     if newr not in set:
#                         set.add(newr)
#                         set = set | forward_chaining(newr, set)
#             match r2:
#                 case Repeat(Concat(r21, r22)):
#                     newr = ConcatOmega(r1, ConcatOmega(r21, Repeat(Concat(r22, r21))))
#                     if newr not in set:
#                         set.add(newr)
#                         set = set | forward_chaining(newr, set)
#         case UnionOmega(r1, r2):
#             newr1 = r1
#             newr2 = r2
#             match (r1, r2):
#                 case (ConcatOmega(r11, Repeat(r12)), ConcatOmega(r21, Repeat(r22))):
#                     if r11 == r11:
#                         newr1 = Repeat(r11)
#                     if r21 == r22:
#                         newr2 = Repeat(r21)
#                     newr = UnionOmega(newr1, newr2)
#                     if newr not in set:
#                         set.add(newr)
#                         set = set | forward_chaining(newr, set)
#                     if r12 == r22:
#                         newr = ConcatOmega(Union(r1, r21), Repeat(r12))
#                         if newr not in set:
#                             set.add(newr)
#                             set = set | forward_chaining(newr, set)
#                 case (ConcatOmega(r11, Repeat(r12)), Repeat(r22)):
#                     if r11 == r11:
#                         newr1 = Repeat(r11)
#                     newr = UnionOmega(newr1, newr2)
#                     if newr not in set:
#                         set.add(newr)
#                         set = set | forward_chaining(newr, set)
#                     if r12 == r22:
#                         newr = ConcatOmega(Union(r1, Epsilon()), Repeat(r12))
#                         if newr not in set:
#                             set.add(newr)
#                             set = set | forward_chaining(newr, set)
#                 case (Repeat(r12), ConcatOmega(r21, Repeat(r22))):
#                     if r21 == r22:
#                         newr2 = Repeat(r21)
#                     newr = UnionOmega(newr1, newr2)
#                     if newr not in set:
#                         set.add(newr)
#                         set = set | forward_chaining(newr, set)
#                     if r12 == r22:
#                         newr = ConcatOmega(Union(Epsilon(), r2), Repeat(r12))
#                         if newr not in set:
#                             set.add(newr)
#                             set = set | forward_chaining(newr, set)
#                 case (Repeat(r12), Repeat(r22)):
#                     if r12 == r22:
#                         newr = Repeat(r12)
#                         if newr not in set:
#                             set.add(newr)
#                             set = set | forward_chaining(newr, set)
#             match r1:
#                 case ConcatOmega(Concat(r11, r12), ConcatOmega(r13, Repeat(r14))):
#                     newrp = Concat(r12, r13)
#                     if newrp == r14:
#                         newr = UnionOmega(ConcatOmega(r11, Repeat(r14)), r2)
#                         if newr not in set:
#                             set.add(newr)
#                             set = set | forward_chaining(newr, set)
#             match r2:
#                 case ConcatOmega(Concat(r21, r22), ConcatOmega(r23, Repeat(r24))):
#                     newrp = Concat(r22, r23)
#                     if newrp == r24:
#                         newr = UnionOmega(r1, ConcatOmega(r21, Repeat(r24)))
#                         if newr not in set:
#                             set.add(newr)
#                             set = set | forward_chaining(newr, set)
#         case _:
#             raise TypeError(f'Unsupported regex type: {type(r)}')

#     return set
