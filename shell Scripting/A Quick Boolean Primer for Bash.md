### A Quick Boolean Primer for Bash

The <code>if</code> statement takes a command as an argument (as do &&, ||, etc.). The integer result code of the command is interpreted as a boolean (0/null=true, 1/else=false).
The test statement takes operators and operands as arguments and returns a result code in the same format as if. An alias of the test statement is [, which is often used with if to perform more complex comparisons.

The true and false statements do nothing and return a result code (0 and 1, respectively). So they can be used as boolean literals in Bash. But if you put the statements in a place where they're interpreted as strings, you'll run into issues. In your case:

    if [ foo ]; then ... # "if the string 'foo' is non-empty, return true"
    if foo; then ...     # "if the command foo succeeds, return true"

So:

    if [ true  ] ; then echo "This text will always appear." ; fi;
    if [ false ] ; then echo "This text will always appear." ; fi;
    if true      ; then echo "This text will always appear." ; fi;
    if false     ; then echo "This text will never appear."  ; fi;
This is similar to doing something like echo '$foo' vs. echo "$foo".

When using the test statement, the result depends on the operators used.

    if [ "$foo" = "$bar" ]   # true if the string values of $foo and $bar are equal
    if [ "$foo" -eq "$bar" ] # true if the integer values of $foo and $bar are equal
    if [ -f "$foo" ]         # true if $foo is a file that exists (by path)
    if [ "$foo" ]            # true if $foo evaluates to a non-empty string
    if foo                   # true if foo, as a command/subroutine,
                             # evaluates to true/success (returns 0 or null)

In short, if you just want to test something as pass/fail (aka "true"/"false"), then pass a command to your if or && etc. statement, without brackets. For complex comparisons, use brackets with the proper operators.


Source : [stackoverflow](link=https://stackoverflow.com/a/47876317/2120239)
