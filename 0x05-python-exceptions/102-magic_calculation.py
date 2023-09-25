#!/usr/bin/python3

def magic_calculation(a, b):
  """Code does a calculation on a and b

  Args:
     a: int
     b: int

  Returns:
      Result of the claculation.
  """

    res = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                res += a ** b / i
        except:
            res = b + a
            break
    return (res)
