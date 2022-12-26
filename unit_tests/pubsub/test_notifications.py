from app.pubsub.notifications import historical_nots


def test_historical_nots():
    response = historical_nots()
    size = len(response["last 5 days notifications"])
    assert size == 20
