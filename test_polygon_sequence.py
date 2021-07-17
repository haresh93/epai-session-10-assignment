import pytest
from polygon import Polygon
from polygon_sequence import PolygonSequence


def test_create_polygon_sequence_with_invalid_max_number_of_vertices():

    with pytest.raises(ValueError) as execinfo:
        p = PolygonSequence(-2, 10)
    
    with pytest.raises(ValueError) as execinfo:
        p = PolygonSequence(0, 10)
    
    with pytest.raises(ValueError) as execinfo:
        p = PolygonSequence(2, 10)

def test_create_polygon_sequence_with_with_invalid_circum_radius():

    with pytest.raises(ValueError) as execinfo:
        p = PolygonSequence(10, -10)
    
    with pytest.raises(ValueError) as execinfo:
        p = Polygon(5, 0)
    

def test_create_polygon_sequence_with_valid_params():
    p = PolygonSequence(5, 10)
    assert p.max_num_of_vertices == 5, "Polygon Sequence object is created incorrectly the max_num_of_vertices is not equal to the value passed"

    assert p.circum_radius == 10, "Polygon Sequence object is created incorrectly the circum_radius is not equal to the circum_radius passed"

    assert isinstance(p[0], Polygon), "Items in the sequence are of type Polygon"

    assert p[0].num_of_edges == 3, "First item in "

def test_polygon_sequence_length():
    p1_seq = PolygonSequence(5, 10)
    p2_seq = PolygonSequence(8, 10)
    assert len(p1_seq) == 3, "Length of the Polygon Sequence is not working as expected"
    assert len(p2_seq) == 6, "Length of the Polygon Sequence is not working as expected"

def test_polygon_sequence_repr():
    p_seq = PolygonSequence(5,10)

    p_repr = p_seq.__repr__()

    assert "length_of_the_sequence" in p_repr , "The representation of the polygon sequence object does not contain the Length of the sequence"
    assert "max_num_of_vertices" in p_repr , "The representation of the polygon sequence object does not contain the max_num_of_vertices"
    assert "circum_radius" in p_repr , "The representation of the polygon sequence object does not contain the circum_radius"
    assert "max_efficiency_polygon" in p_repr , "The representation of the polygon sequence object does not contain the max_efficiency_polygon"
    
def test_polygon_sequence_list():
    p1 = PolygonSequence(8, 10)

    assert type(list(p1)) == list, "List could not be created from the Polygon Sequence"

    assert p1[2].num_of_vertices == 5, "Polygon object in the sequence does not have the expected num_of_vertices"
    
def test_polygon_sequence_max_efficiency_polygon():
    p1 = PolygonSequence(3, 10)

    p2 = PolygonSequence(5, 10)

    assert p1.max_efficiency_polygon() == 3, "Polygon Sequence max efficiency Polygon is not working as expected"

    assert p2.max_efficiency_polygon() == 5, "Polygon Sequence max efficiency Polygon is not working as expected"

def test_polygon_sequence_max():

    p1 = PolygonSequence(7, 10)

    assert max(p1).num_of_vertices == 7, "Max operation on the Polygon sequence in not working as expected"


def test_polygon_sequence_min():

    p1 = PolygonSequence(7, 10)

    assert min(p1).num_of_vertices == 3, "Min operation on the Polygon sequence in not working as expected"