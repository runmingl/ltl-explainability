#!/usr/bin/perl

# U2formula.pl
#
# Input: n = the number of variables arranged in the output formula of the form
#            "(p1 U (p2 U ( ... p{n-1} U pn)...)"
# 
# Output: an LTL formula of the form U2(n) = (p1 U (p2 U ( ... p{n-1} U pn)...)
#
# Note: These formulas should provide data similar to that from E formulas. 
#
# Usage: U2formula.pl n
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
    die "Usage: U2formula.pl n\n\tproduces an n-part formula of the form U2(n) = (p1 U (p2 U ( ... p{n-1} U pn)...)\n\tUse flag -v for verbose, human-readable output.\n";
} #end if

$n = $ARGV[0];

#Check that we have an integer
if (($n !~ /^\d+?/) || ($n < 2)) {
    die "Error: Expecting a positive integer (at least 2) as input; Got $n\n";
} #end if


#################### Generation of the Formula ####################
$nminus1 = $n - 1;
$pattern = "(p${nminus1} U p${n})"; #initialize the pattern
$nminus1--;

for ($i = $nminus1; $i >= 1; $i--) {
    $pattern = "(p${i} U $pattern)";
} #end for

if ($verbose == 1) {
    print "\nComputer readable: ";
} #end if
print "$pattern\n";
