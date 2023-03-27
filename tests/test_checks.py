from checks import check_site


def test_check_site():
    url = "https://www.example.com"
    response_time, status_code, match = check_site(url)
    assert isinstance(response_time, float)
    assert isinstance(status_code, int)
    assert isinstance(match, bool)
    assert response_time > 0
    assert status_code == 200
    assert match is True or match is False
