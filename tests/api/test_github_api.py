import pytest

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('AndriiSavinov1')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 58
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('andrii_savinov_repo_pont_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_with_cingle_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0