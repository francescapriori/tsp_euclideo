import csv
import random
import time
import tracemalloc

from euclidean_tsp_solver import EuclideanTSPSolver
from point import Point


def generate_instance_of_points(n, seed):
    random.seed(seed)
    return [Point(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]


def time_of_execution(fn, repeats=1):
    t0 = time.perf_counter()
    for _ in range(repeats):
        result = fn()
    return (time.perf_counter() - t0) / repeats, result


def memory_occupation_of_execution(fn):
    tracemalloc.start()
    fn()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak


def cycle_length(points, path):
    total = 0.0
    for i in range(len(path)):
        total += points[path[i]].distance_to(points[path[(i + 1) % len(path)]])
    return total


def main():
    solver = EuclideanTSPSolver()
    with open("results.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["algorithm", "n", "seed", "time_s", "memory_byte", "cost"])
        for n in range(2, 21): # da 2 a 20 punti
            time_results = []
            for seed in range(10):
                points = generate_instance_of_points(n, seed)

                cycle = lambda: solver.minimum_cycle_euclidean_tsp(points)
                t1, (cost, C, prev, last) = time_of_execution(cycle)
                mem1 = memory_occupation_of_execution(cycle)
                w.writerow(["minimum_cycle", n, seed, t1, mem1, cost])

                S = tuple(range(n))
                chain = lambda: solver.minimum_chain_euclidean_tsp(S, prev, last)
                t2, path = time_of_execution(chain, repeats=1000)
                mem2 = memory_occupation_of_execution(chain)
                w.writerow(["minimum_chain", n, seed, t2, mem2,
                            cycle_length(points, path)])

                f.flush()
                time_results.append(t1)
            if max(time_results) > 60:
                break


if __name__ == "__main__":
    main()