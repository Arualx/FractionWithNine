# FractionWithNine
Turn any recurring decimal number into a fraction containing the number nine.
#
Depending on the appearance of the inputted number a fraction will be automatically made with this code.
In this document, the word recurring number will be shortened into {r} so it's more readable.
#
The fraction is made out of a numerator and denominator.
#
In the numerator part {n}, the whole number (of {r}) - we'll call this variable {a}, will be subtracted by, the whole number (of {r}) without the numbers that are repeated - we'll call this variable {b}.

For example: 

The number 1.233333333... will be turned into 2 new numbers {a}, 123, and {b}, 12.
Those 2 variables will be subtracted and will give a result {n}, 111.
That will be put in the numerator part of the fraction.
#
The denominator part {d} is a bit tricky.

The number of digits in the repeated part (of {r}) - we'll call this variable {c}, will give an output of that same amount of digits but with the number 9.

And the number of digits in the part behind the decimal that is non-repeated (of {r}) - we'll call this variable {e}, will give an output of the same amount of digits but with the number 0. 

{c} and {e} will be added together and they will make the {d} of the fraction.

For example:

Still with the same number (1.233333333...).
It will give 2 new results {c}, 1, and {e}, 1.
Those two variables will turn into that many digits of those numbers so now, {c} is 9 and {e} is 0.
They will be added together and give a result {d}, 90.
That will be put in the denominator part of the fraction.
#
And that's how this code made that fraction.



