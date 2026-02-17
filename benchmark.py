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


def time_it_return(func, data):
    start = time.perf_counter()
    out = func(data)
    end = time.perf_counter()
    return (end - start) * 1000, out


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
        row = name.ljust(14)

        expected = np.sort(data)

        arr_merge = data.copy()
        t, out_merge = time_it_return(merge_sort, arr_merge)
        if not np.array_equal(out_merge, expected):
            raise AssertionError(f"Merge sort failed on dataset {name}")
        results["merge_sort"].append(t)
        row += f"{t:>14.2f}"

        arr_quick = data.copy()
        t = time_it(quick_sort, arr_quick)
        if not np.array_equal(arr_quick, expected):
            raise AssertionError(f"Quick sort failed on dataset {name}")
        results["quick_sort"].append(t)
        row += f"{t:>14.2f}"

        arr_heap = data.copy()
        t = time_it(heap_sort, arr_heap)
        if not np.array_equal(arr_heap, expected):
            raise AssertionError(f"Heap sort failed on dataset {name}")
        results["heap_sort"].append(t)
        row += f"{t:>12.2f}"

        arr_np = data.copy()
        t = time_it(lambda arr: arr.sort(), arr_np)
        if not np.array_equal(arr_np, expected):
            raise AssertionError(f"Numpy sort failed on dataset {name}")
        results["numpy_sort"].append(t)
        row += f"{t:>14.2f}"

        print(row)

    return results


# Vẽ biểu đồ
def plot_results(results):
    labels = results["dataset"]
    x = np.arange(len(labels))

    plt.figure(figsize=(12, 6))
    plt.plot(x, results["merge_sort"], marker="o", label="merge_sort")
    plt.plot(x, results["quick_sort"], marker="o", label="quick_sort")
    plt.plot(x, results["heap_sort"], marker="o", label="heap_sort")
    plt.plot(x, results["numpy_sort"], marker="o", label="numpy_sort")

    plt.xticks(x, labels, rotation=30, ha="right")
    plt.xlabel("Bộ dữ liệu")
    plt.ylabel("Thời gian thực hiện (ms)")
    plt.title("Kết quả thử nghiệm trên bộ dữ liệu")
    plt.grid(True, axis="y", linestyle="--", alpha=0.4)
    plt.legend(loc="center left", bbox_to_anchor=(1.02, 0.5))
    plt.tight_layout(rect=(0, 0, 0.82, 1))
    plt.show()


def main():
    results = benchmark()
    plot_results(results)


if __name__ == "__main__":
    main()
