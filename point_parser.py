import json
from point import Point

class PointParser:

    def parse_points_from_json(self, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)

            if len(data['points']) == 0:
                raise ValueError("The points list is empty. Please provide at least one point in the JSON file.")
            
        return [Point(point['x'], point['y']) for point in data['points']]