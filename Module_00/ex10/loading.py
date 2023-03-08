import time


def ft_progress(listy):
    for i in range(len(listy)):
        percent = i / len(listy) * 100
        print(f"\rETA: {int((len(listy) - i) * 0.01)}s [{int(percent)}%] [{'=' * int(percent / 5)}{'>' if percent % 5 != 0 else ''}{' ' * (20 - int(percent / 5))}] {i}/{len(listy)} | elapsed time {int(i * 0.01)}s", end="")
        yield listy[i]


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)