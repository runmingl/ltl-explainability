#!/usr/bin/perl

# Qformula.pl
#
# Input: n = the number of variables arranged in the output formula
# 
# Output: an LTL formula of the form 
#           Q(n) = & _{i=1} ^{n} ((F (p{i})) || (G (p{i+1})))
#
# Usage: Qformula.pl n
#

# System Description
#
# - n variables: p1 .. pn

# Purpose: to create scaleable formulas as described in "Larger Automata and Less Work for LTL Model Checking" by Geldenhuys and Hansen



#################### Argument Setup ####################

#Check for correct number and type of command line arguments
if ($ARGV[0] =~ /^-v?/) {
    $verbose = 1;
    shift(@ARGV);
} #end if
else {
    $verbose = 0;
} #end else

if (@ARGV != 1) {
    die "Usage: Qformula.pl n\n\tproduces an n-part formula of the form Q(n) = & _{i=1} ^{n} ((F (p{i})) || (G (p{i+1})))\n\tUse flag -v for verbose, human-readable output.\n";
} #end if

$n = $ARGV[0];

#Check that we have an integer
if (($n !~ /^\d+?/) || ($n < 2)) {
    die "Error: Expecting a positive integer (at least 2) as input; Got $n\n";
} #end if


#################### Generation of the Formula ####################
$pattern = "((F (p1)) || (G (p2)))"; #initialize the pattern

for ($i = 2; $i < $n; $i++) {
    $iplus1 = $i + 1;
    $pattern = "($pattern && ((F (p${i})) || (G (p${iplus1}))))";
} #end for

if ($verbose == 1) {
    print "\nComputer readable: ";
} #end if
print "$pattern\n";
