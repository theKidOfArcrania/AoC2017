import sys

ind  = 0
tape = {}
state = 'A'
for i in range(12317297):
    if state == 'A':
      if (not ind in tape) or tape[ind] == 0:
        tape[ind] = 1
        ind += 1
        state = 'B'
      else:
        tape[ind] = 0
        ind -= 1
        state = 'D'

    elif state == 'B':
      if (not ind in tape) or tape[ind] == 0:
        tape[ind] = 1
        ind += 1
        state = 'C'
      else:
        tape[ind] = 0
        ind += 1
        state = 'F'

    elif state == 'C':
      if (not ind in tape) or tape[ind] == 0:
        tape[ind] = 1
        ind -= 1
        state = 'C'
      else:
        tape[ind] = 1
        ind -= 1
        state = 'A'

    elif state == 'D':
      if (not ind in tape) or tape[ind] == 0:
        tape[ind] = 0
        ind -= 1
        state = 'E'
      else:
        tape[ind] = 1
        ind += 1
        state = 'A'

    elif state == 'E':
      if (not ind in tape) or tape[ind] == 0:
        tape[ind] = 1
        ind -= 1
        state = 'A'
      else:
        tape[ind] = 0
        ind += 1
        state = 'B'

    elif state == 'F':
      if (not ind in tape) or tape[ind] == 0:
        tape[ind] = 0
        ind += 1
        state = 'C'
      else:
        tape[ind] = 0
        ind += 1
        state = 'E'
count = 0
for x in tape:
    if tape[x] == 1:
        count += 1
print(count)
