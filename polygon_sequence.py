from polygon import Polygon

class PolygonSequence(object):
    def __init__(
        self,
        max_num_of_vertices: "Number of Vertices for the largest Polygon",
        circum_radius: "Common Circumradius for all the polygons"
    ):
        """
            Initializes a PolygonSequence object which takes the max_num_of_vertices in the sequence and 
            common circumradius for all the polygons as parameters
        """

        if max_num_of_vertices < 3 or circum_radius < 0:
            raise ValueError("Polygon Sequence cannot be formed with max_num_of_vertices less than 3 or circum_radius less than 0")

        self.max_num_of_vertices = max_num_of_vertices
        self.circum_radius = circum_radius
    
    def max_efficiency_polygon(self) -> int:
        """
            This method returns the num of sides of the max_efficiency_polygon in the polygon sequence
            which means the polygon with the maximum area to perimeter ratio
        """
        max_ratio = 0
        max_ratio_sides = 0
        for num_of_vertices in range(3, self.max_num_of_vertices + 1):
            polygon = Polygon(num_of_vertices, self.circum_radius)
            ratio = polygon.area/polygon.perimeter
            if max_ratio <= ratio:
                max_ratio = ratio
                max_ratio_sides = num_of_vertices
        
        return max_ratio_sides
    
    def __len__(self):
        """
            Returns the length of the Polygon Sequence which is the max_num_of_vertices - 2 as 
            there can't be any polygon constructed with 1 or 2 sides.
        """
        return self.max_num_of_vertices - 2
    
    def __getitem__(self, s: "index or slice") -> "Polygon or list(Polygon)":
        """
            Returns the Polygon object at the specified index or slice
            Raises Index Error if we try to access the item less than 0 or 
            greater than self.max_num_of_vertices - 2
        """
        if isinstance(s, int):
            if s < 0 or s >= self.max_num_of_vertices - 2:
                raise IndexError
            else:
                return Polygon(s + 3, self.circum_radius)
        else:
            start, stop, step = s.indices(self.max_num_of_vertices - 2)
            rng = range(start, stop, step)
            return [Polygon(i + 3, self.circum_radius) for i in rng]

    def __repr__(self):
        """
            Returns the representation of the Polygon sequence with the properties of the Polygon Sequence
            max_num_of_vertices
            circum_radius
            max_efficience_polygon
        """
        return f"""
            A Polygon sequence Object with the following properties
                length_of_the_sequence - {self.__len__()} 
                max_num_of_vertices    - {self.max_num_of_vertices}
                circum_radius          - {self.circum_radius}
                max_efficiency_polygon - {self.max_efficiency_polygon()}
        """ 
    