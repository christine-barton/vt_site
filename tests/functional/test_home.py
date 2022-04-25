import time

def test_index_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b"Welcome to VTM!" in res.data
        

def test_about_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/about' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200
        assert b"About Vertical Tank Maintenance" in res.data 

def test_estimate_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/estimate' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 200

def test_estimate_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the 'Calculate' button is selected (POST)
    THEN check that the correct price estimate is returned to the user
    """
    with app.test_client() as test_client:
        estimate = {"Tank radius":"180","Tank height":"360"}
        res = test_client.get('/estimate', data= estimate)
        assert res.status_code == 200
