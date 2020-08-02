import stdio
import random

# simulate a coin flip by writing 'heads' or 'tails' to standard
# output.

if random.randrange(0, 2) == 0:
    stdio.writeln('Heads')
else:
    stdio.writeln('Tails')
