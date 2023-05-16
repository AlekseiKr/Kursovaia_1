class TestMain:

    def test_root_status(self, test_client):
        response = test_client.get('/',follow_redirects = True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"

