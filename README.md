# mullafacation
Implementation of the mullafacation operator in python

# Short explanation
Mullafacation is a mathematical operation I created a long time ago. The rules are:

If the second number is 1 you add the first number plus the first number. Example: 11 Ⓜ︎ 1 = 22

If the second number is 2 you subtract the first number minus the first number. Example: 11 Ⓜ︎ 2 = 0

If the second number is 3 you multiply the first number by the first number. Example: 11 Ⓜ︎ 3 = 121

If the second number is 4 you divide the first number by the first number. Example: 11 Ⓜ︎ 4 = 0

If the second number is 5 or higher you round the first number to the the second number. Example: 11 Ⓜ︎ 5 = 10

Source: https://mullafacation.com/operation.html (ASCII-only; uses M instead of the original Ⓜ︎)

---

# More details
This background section was written on 15:03, 20 July 2021. First published on GitHub on 7 April, 2025

## Etymology

_Mullafacation_ is derived from "Mullac" (_Callum_ backwards), and the suffix ["-ation"](https://en.wiktionary.org/wiki/-ation#English), denoting a noun. The original verb used was to "_mullac_" two numbers together, despite probably being the improper verb form of _Mullafacation_, but it is now only used to denote the original operation, while the term _mullify_ is used to refer to modern mullafacation.

## Bimullafacation
_Bimullafacation_ or "_mullacation_" (digitally represented by M⦂) are the terms hereby used to describe the original mullafacation. It could take two arguments, with the second argument being either 1 or 2. If the second argument was 1, the first argument would be added on to itself (doubled/multiplied by 2) and if it was 2 it would be subtracted from itself (made 0). The original rules were like this:

𝑥 Ⓜ︎ 1 = 𝑥 + 𝑥

𝑥 Ⓜ︎ 2 = 𝑥 - 𝑥

It did not do exception handling for any larger second parameters. (i.e. 𝑥 Ⓜ︎ n = NaN | n > 2)

The above can be simplified as:

𝑥 Ⓜ︎ 1 = 2𝑥

𝑥 Ⓜ︎ 2 = 0

This is hereby known as _compressed mullacation_. According to Callum, the only reasonable use for mullafacation is to demonstrate how to simplify functions like this because its definition is overly superfluous.

Because the operations that mullafacation employs are already very simple ways to achieve the same result including already having a relatively simple second parameter, mullafacation's only possible use is to demonstrate compressed functions.
Mullacation's notation changed to clarify that the second argument must be one of two inputs. This notation had two checkboxes at the side of the M so that bimullafacation could never output NaN, and was then represented as an M with two boxes above each other, one to be ticked. (hereby digitally represented as 𝑥 M⦂ 𝑦).


## Operation
Apart from any 𝑥 Ⓜ︎ n = NaN | n > 2, the modern version of mullafacation completely incorporates mullacation as well as multipication, division and rounding, despite Callum not learning division yet when this was introduced. This would mean the second arguments 3 and 4 would be division and subtraction respectively, and anything over 4 would return the nearest multiple of the second argument from the first argument (rounding). This means the compressed version would be:

𝑥 Ⓜ︎ 1 = 2𝑥

𝑥 Ⓜ︎ 2 = 0

𝑥 Ⓜ︎ 3 = 𝑥²

𝑥 Ⓜ︎ 4 = 0

𝑥 Ⓜ︎ 𝑦 = round 𝑦 to the nearest 𝑥, where 𝑦 > 4

# Additional note
Additions to mullafacation (besides the second parameter being 1–4) was mailed in [a letter](https://mullafacation.com/original.jpg) on 3 February, 2015
