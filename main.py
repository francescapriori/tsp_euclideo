from point import Point
from euclidean_tsp_solver import EuclideanTSPSolver


p1 = Point(0, 0)
p2 = Point(3, 4)
#print(p1.distance_to(p2))

solver = EuclideanTSPSolver()
points = [p1, p2]
cost, C, prev, last = solver.minimum_cycle_euclidean_tsp(points)
print(f"Optimal cost: {cost}")
path = solver.minimum_chain_euclidean_tsp(tuple(range(len(points))), prev, last)
print(f"Optimal path: {[f'p{i}' for i in path]}")

