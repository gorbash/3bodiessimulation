from setup import s
import time

delta = 0.00001

start = time.time()
while (s.totalTime < 30):
    s.step(delta)
end = time.time()

# 3M steps in ~60s
print("%d steps in %f s" % (s.steps, end - start))

