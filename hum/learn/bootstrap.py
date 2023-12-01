import time
from types import GeneratorType


def bootstrap_without_decorator(to, stack=[]):
  while True:
    if type(to) is GeneratorType:
      stack.append(to)
      to = next(to)
    else:
      stack.pop()
      if not stack:
        break
      to = stack[-1].send(to)
  return to


def fun(n):
  if n == 0:
    yield
  yield fun(n - 1)
  yield


t1 = time.time()
for i in range(500):
  bootstrap_without_decorator(fun(4000))
print(time.time() - t1)


def bootstrap_with_returns(f, stack=[]):
  def wrappedfunc(*args, **kwargs):
    if stack:
      return f(*args, **kwargs)
    else:
      to = stack.append(f(*args, **kwargs))
      while True:
        try:
          to = stack.append(stack[-1].send(to))
        except StopIteration as e:
          stack.pop()
          to = e.value
          if not stack:
            break
      return to

  return wrappedfunc


@bootstrap_with_returns
def fun(n):
  if n <= 0:
    return 1
  return (yield fun(n - 1)) + 1


t1 = time.time()
for i in range(500):
  fun(4000)
print(time.time() - t1)
