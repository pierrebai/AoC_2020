# AoC_2020
Advent of Code 2020

I chose to write solutions in Python because:

  1. Python is one of the most popular language after Javascript, so most people will immediately understand the code.
  2. For those who don't know Python, Python is generally recognized as being one of the most grokable language.
  3. Python tend to produce short code and has a lot of text parsing functions built-in.

Ironically, when I wrote these solutions, I wilfully aimed at succintness instead of clarity.
I did not go completely overboard on it though, sometimes writing helper functions where I could
have easily added more level of inlined lambdas.

... but I did use a lot of lambdas, map-function and filter-functions. This kind of code is cute
but I think that embedding multiple level of lambda, map and filter obscures the goal of the code.
Even a single map-function is more obtuse than the equivalent for-loop. The reason is simple:
a map-function has its salient relevant code in the middle of gobbledydock, while a for loop puts
the salient code in its own separate line.

Compare these two equivalent forms:

   ```
   data = list(...)
   foo = map(lambda x: salient-core-logic, data)
   ```
   
   ```
   data = list(...)
   result = list()
   for d in data:
      salient-core-logic
   ```
   
In the first case, the eye must scan a complex line to find the words salient-core-logic. In the loop form,
it is isolated on its own line, at the of a block of code. In both forms, over time, the brain rapidly
learns to ignore the irrelevant parts. But in the function-style, the core is always embedded in the middle.
The for-loop style always isolates the salient parts. I think this generalizes to most constructs of functional
languages vs imperative languages. I think it's a major reason why people have negative reactions to functional
languages. They tend to put the salient bits "in the middle", instead of "in the end".

I think this explains the resistance to adopting functional-style code in almost all languages. They all have
taken the style from the original truly functional languages without questioning the form. At the origin, the
form was dictated by the syntax of the functional languages.

For Python, imagine that map, filter, etc were built-in syntax. Then the object being operated on could be given
first and the salient-code on its own. For example, it could look like:

   ```
   data = list(...)
   result = map data as x:
      salient-core-logic
   ```
 
 The interesting thing to note is that Python list comprehension made the same mistake of adopting a syntax that
 force putting the salient-core-logic in the middle of line noise. They could have put the programmer-provided
 code in the end, but they chose to put it in the middle. Look at LISP popularity. LISP had it wrong. Readable
 code, which is governed by the core syntax of a language is important. Python imperative-style bits got it right.
 I think readability was Python not-so-hidden super-power. Unfortunately, recent Python additions have got
 it all wrong.
 
