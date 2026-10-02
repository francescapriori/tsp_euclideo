from point import Point
from euclidean_tsp_solver import EuclideanTSPSolver
from point_parser import PointParser


points = PointParser().parse_points_from_json("points.json")
print(f"Parsed points:", [(p.x, p.y) for p in points])
#print(type(points),points)

solver = EuclideanTSPSolver()
cost, C, prev, last = solver.minimum_cycle_euclidean_tsp(points)
print(f"Optimal cost: {cost}")
path = solver.minimum_chain_euclidean_tsp(tuple(range(len(points))), prev, last)
print(f"Optimal path: {[(points[i].x, points[i].y) for i in path]}")

