# FractionWithNine
Turn any recurring decimal number into a fraction containing number 9 in the denominator.
#
# Explanation
1. Identify the part with whole number (let's call it {a})
2. Identify the part without the repeating digits (let's call it {b})

- Subtract {b} from {a} to get the numerator {n}.

#
3. Identify the number of repeating digits in the decimal (let's call this {c})
4. Identify the number of digits before the repeating part starts (call this {e})

5. Create a denominator by combining {c} and {e}.

- For {c}, use a number with {c} nines (like 9 for 1 digit, 99 for 2 digits, etc.)
- For {e}, use a number with {e} zeros (like 0 for 1 digit, 00 for 2 digits, etc.)

- Combine them by adding {c} and {e} together to form the denominator {d}.
#
# Example
For the number 1.23333333...:

- {a} = 123 (whole number with repeating part)
- {b} = 12 (whole number without repeating part)
- {n} = {a} - {b} = 123 - 12 = 111

- {c} = 1 (1 repeating digit)
- {e} = 1 (1 non-repeating digit)
- {d} = 9 (from {c}) + 0 (from {e}) = 90

#
And that's how this code made that fraction.



