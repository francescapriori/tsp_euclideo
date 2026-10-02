import itertools

class EuclideanTSPSolver:

    def minimum_cycle_euclidean_tsp(self, points):
        n = len(points)
        C = {((0,), 0): 0} #C(S={p1},p1)=0
        prev = {}
        
        for s in range(2, n+1):
            for other_points in itertools.combinations(range(1, n), s-1): 
                subset = (0,) + other_points # S in P : |S|=s & p1 in S
                for pf in other_points: # pf in S : pf != p1
                    subset_without_pf = tuple(p for p in subset if p != pf)
                    C[(subset, pf)] = float('inf')
                    for pk in subset_without_pf:
                        if pk == 0 and len(other_points) > 1: # p_k != p_1 oppure S\{p_f}={p_1}
                            continue
                        dist_kf = points[pk].distance_to(points[pf])
                        q = C[(subset_without_pf, pk)] + dist_kf
                        if q < C[(subset, pf)]:
                            C[(subset, pf)] = q
                            prev[(subset, pf)] = pk
        optimal_cost = float('inf')
        for pf in range(1, n): # pf in P\{p1}
            v = C[(tuple(range(n)), pf)] + points[pf].distance_to(points[0])
            if v < optimal_cost:
                optimal_cost = v
                last = pf
        return optimal_cost, C, prev, last

    def minimum_chain_euclidean_tsp(self, S, prev, last):
        if last == 0: # last == p1
            return [0]
        else:
            pk = prev[(S, last)]
            subset_without_last = tuple(p for p in S if p != last)
            path = self.minimum_chain_euclidean_tsp(subset_without_last, prev, pk)
            path.append(last)
        
        return path