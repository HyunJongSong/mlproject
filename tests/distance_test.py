from mlproject.distance import haversine

def test_type_of_distance():
    assert type(haversine(48.865, 2.380, 48.235, 2.393)) == float

def test_valid_distance():
    assert haversine(48.865, 2.380, 48.235, 2.393) > 0
