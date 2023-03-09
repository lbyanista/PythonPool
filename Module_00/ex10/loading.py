import time


def ft_progress(listy):
    for i in range(len(listy)):
        percent = i / len(listy) * 100
        print(f"\rETA: {int((len(listy) - i) * 0.01)}s "           # Estimated time remaining in seconds
              # Percentage of completion
              f"[{int(percent)}%] "
              # Visual progress bar
              f"[{'=' * int(percent / 5)}{'>' if percent % 5 != 0 else ''}{' ' * (20 - int(percent / 5))}] "
              # Progress counter
              f"{i}/{len(listy)} | "
              f"elapsed time {int(i * 0.01)}s", end="")              # Time elapsed in seconds

        yield listy[i]


listy = range(8000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
