import time

import matplotlib.pyplot as plt
import numpy as np
from heap_sort import heap_sort
from merge_sort import merge_sort
from quick_sort import quick_sort


# Đo thời gian chạy (ms)
def time_it(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return (end - start) * 1000


# Đọc file từ dataset
def read_one_file(path):
    with open(path, "r", encoding="utf-8") as f:
        tokens = f.read().split()

    if not tokens:
        return np.array([], dtype=np.float64)

    n = int(tokens[0])
    vals = [float(x) for x in tokens[1 : 1 + n]]
    return np.array(vals, dtype=np.float64)


# Đọc dataset
def read_datasets():
    labels = [f'{i}' for i in range(1, 11)]

    sets = []
    for i in range(1, 11):
        path = f"datasets/test{i}.txt"
        arr = read_one_file(path)
        sets.append((labels[i - 1], arr))

    return sets


# Benchmark
def benchmark():
    sets = read_datasets()

    header = (
        "dataset".ljust(14)
        + "merge_sort(ms)".rjust(14)
        + "quick_sort(ms)".rjust(14)
        + "heap_sort(ms)".rjust(12)
        + "numpy_sort(ms)".rjust(14)
    )
    print(header)
    print("-" * len(header))

    results = {
        "dataset": [],
        "merge_sort": [],
        "quick_sort": [],
        "heap_sort": [],
        "numpy_sort": [],
    }

    for name, data in sets:
        results["dataset"].append(name)
        arr = data.tolist()
        row = name.ljust(14)

        t = time_it(merge_sort, arr.copy())
        results["merge_sort"].append(t)
        row += f"{t:>14.2f}"

        t = time_it(quick_sort, arr.copy())
        results["quick_sort"].append(t)
        row += f"{t:>14.2f}"

        t = time_it(heap_sort, arr.copy())
        results["heap_sort"].append(t)
        row += f"{t:>12.2f}"

        t = time_it(np.sort, data)
        results["numpy_sort"].append(t)
        row += f"{t:>14.2f}"

        print(row)

    return results


# Vẽ biểu đồ
def plot_results(results):
    labels = results["dataset"]
    x = np.arange(len(labels))
    w = 0.2

    plt.figure(figsize=(12, 6))
    plt.bar(x - 1.5 * w, results["merge_sort"], width=w, label="merge_sort")
    plt.bar(x - 0.5 * w, results["quick_sort"], width=w, label="quick_sort")
    plt.bar(x + 0.5 * w, results["heap_sort"], width=w, label="heap_sort")
    plt.bar(x + 1.5 * w, results["numpy_sort"], width=w, label="numpy_sort")

    plt.xticks(x, labels, rotation=30, ha="right")
    plt.xlabel("Bộ dữ liệu")
    plt.ylabel("Thời gian thực hiện (ms)")
    plt.title("Kết quả thử nghiệm trên bộ dữ liệu")
    plt.grid(True, axis="y", linestyle="--", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    results = benchmark()
    plot_results(results)


if __name__ == "__main__":
    main()
