# import json
#
# import pytest
#
#
# @pytest.mark.usefixtures("client")
# def test_rsi_getter(client):
#     response = client.get('/ta/rsi/crypto/ETHUSDT/1m/0000', follow_redirects=False)
#     data = json.loads(response.data)
#     assert response.status_code == 200
#     assert len(data) > 0
#
# @pytest.mark.usefixtures("client")
# def test_roc_getter(client):
#     response = client.get('/ta/roc/crypto/ETHUSDT/1m/0000', follow_redirects=False)
#     data = json.loads(response.data)
#     assert response.status_code == 200
#     assert len(data) > 0
#
# @pytest.mark.usefixtures("client")
# def test_obv_getter(client):
#     response = client.get('/ta/obv/crypto/ETHUSDT/1m/0000', follow_redirects=False)
#     data = json.loads(response.data)
#     assert response.status_code == 200
#     assert len(data) > 0
#
# @pytest.mark.usefixtures("client")
# def test_ema_getter(client):
#     response = client.get('/ta/ema/crypto/ETHUSDT/1m/0000', follow_redirects=False)
#     data = json.loads(response.data)
#     assert response.status_code == 200
#     assert len(data) > 0
#
# @pytest.mark.usefixtures("client")
# def test_ma_getter(client):
#     response = client.get('/ta/ma/crypto/ETHUSDT/1m/0000', follow_redirects=False)
#     data = json.loads(response.data)
#     assert response.status_code == 200
#     assert len(data) > 0
#
# @pytest.mark.usefixtures("client")
# def test_sma_getter(client):
#     response = client.get('/ta/sma/crypto/ETHUSDT/1m/0000', follow_redirects=False)
#     data = json.loads(response.data)
#     assert response.status_code == 200
#     assert len(data) > 0
#
# @pytest.mark.usefixtures("client")
# def test_wma_getter(client):
#     response = client.get('/ta/wma/crypto/ETHUSDT/1m/0000', follow_redirects=False)
#     data = json.loads(response.data)
#     assert response.status_code == 200
#     assert len(data) > 0
#
# @pytest.mark.usefixtures("client")
# def test_stoch_getter(client):
#     response = client.get('/ta/stoch/crypto/ETHUSDT/1m/0000', follow_redirects=False)
#     data = json.loads(response.data)
#     assert response.status_code == 200
#     assert len(data) > 0
#
# @pytest.mark.usefixtures("client")
# def test_bbands_getter(client):
#     response = client.get('/ta/bbands/crypto/ETHUSDT/1m/0000', follow_redirects=False)
#     data = json.loads(response.data)
#     assert response.status_code == 200
#     assert len(data) > 0
#
# @pytest.mark.usefixtures("client")
# def test_macd_getter(client):
#     response = client.get('/ta/macd/crypto/ETHUSDT/1m/0000', follow_redirects=False)
#     data = json.loads(response.data)
#     assert response.status_code == 200
#     assert len(data) > 0