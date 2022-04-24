def test_index_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client as test_client:
        res = test_client/get('/')
        assert res.status_code == 200
        assert b"Vertical Tank Maintenance" in res.data 
        assert b"Welcome to VTM!" in res.data
        assert b"image source" in res.data
        assert b"Lorem ipsum dolor sit amet" in res.data
        

def test_about_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/about' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client as test_client:
        res = test_client/get('/about')
        assert res.status_code == 200
        assert b"About VTM" in res.data
        assert b"About Vertical Tank Maintenance" in res.data 
        assert b"Lorem ipsum dolor sit amet" in res.data
        assert b"Eu tincidunt tortor aliquam nulla facilisi cras fermentum odio." in res.data
        assert b"Sed vulputate mi sit amet." in res.data

def test_estimate_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/estimate' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client as test_client:
        res = test_client/get('/estimate')
        assert res.status_code == 302
        assert b"VTM Estimator" in res.data 
        assert b"Tank radius" in res.data
        assert b"Tank height" in res.data
        assert b"Submit" in res.data

def test_estimate_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the 'Submit' button is selected (POST)
    THEN check that the correct price estimate is returned to the user
    """
    print("-- /estimate 'price_estimate' POST test")
    with app.test_client as test_client:
        estimate = {"height":"360", "radius":"180", "price_estimate":"x"}
        assert res.status_code == 200
        assert b"$141,300.00" in res.data
