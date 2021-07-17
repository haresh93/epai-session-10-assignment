# Polygon Class

## Constructor - __init__

Initializes a Polygon object and defines its properties.
- Number of EDGES (to be passed in args)
- Number of Vertices
- Circum-radius (to be passed in args)
- interior_angle 
- edge_length 
- apothem 
- area 
- perimeter 

Raises the ValueError if invalid params are passed into the constructor:
- Num Of edges should be greater than or equal to 3
- Circumradius should be greater than 0

## Equality method - __eq__
Checks for the Equality of two Polygon objects based on the Circum-radius and Number of vertices.
Raises a TypeError if operation performed on any other object other than Polygon object

## Comparison method - __gt__
Checks for the Comparison of two Polygon objects based on the Number of vertices.

If the Number of vertices of the Polygon is greater than the number of vertices of the other Polygon then it returns True 
else returns False

Raises a TypeError if operation performed on any other type other than Polygon Object.

## Representation method - __repr__

Returns the representation of the Polygon class Object with the following properties:
- Number of EDGES
- Number of Vertices
- Circum-radius
- interior_angle 
- edge_length 
- apothem 
- area 
- perimeter 

# Polygon Sequence Class

This is a custom sequence type which contains the sequence of polygons.

## Constructor - __init__

Initializes a PolygonSequence object which takes the max_num_of_vertices in the sequence and 
common circumradius for all the polygons as parameters.

It creates the sequence of polygons from num of vertices of 3 to the max_num_of_vertices and circum radius 
which is passed.

It raises a ValueError when invalid params are passed to it:
- Max Num Of vertices should be greater than or equal to 3
- Circumradius should be greater than 0

## Length - __len__

Returns the length of the Polygon Sequence which is the max_num_of_vertices - 2 as 
there can't be any polygon constructed with 1 or 2 sides.

## Item at a particular index - __getitem__

Returns the Polygon object at the specified index or slice Raises Index Error if we try to access the item less than 0 or greater than self.max_num_of_vertices - 2

## Representation of the PolygonSequence - __repr__

Returns the representation of the Polygon sequence with the properties of the Polygon Sequence
max_num_of_vertices
circum_radius
max_efficience_polygon

## Maximum Efficiency Polygon - max_efficiency_polygon

This method returns the num of sides of the max_efficiency_polygon in the polygon sequence
which means the polygon with the maximum area to perimeter ratio.