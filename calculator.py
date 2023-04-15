def cal(a,b,op):
  if op == '+':
    return a+b
  elif op == '-':
    return a-b
  elif op == '*':
    return a*b
  elif == '/':
     if b==0:
        return "unable to divide by zero"
     else:
        return a/b
  else:
    return "invalid operator"
