def check_is_numeric(value):
  if not isinstance(value, (int, float)):
    raise ValueError("Wartość musi być numeryczna!")
  return True


def rectangle(a, b):
  if check_is_numeric(a) and check_is_numeric(b):
    return a * b


def triangle(a, h):
  if check_is_numeric(a) and check_is_numeric(h):
    return 0.5 * a * h

def trapezoid(a, b, h):
  if check_is_numeric(a) and check_is_numeric(b) and check_is_numeric(h):
    return (a + b) * h * 0.5

