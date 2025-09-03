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
    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('andrii_savinov_repo_pont_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_with_cingle_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

#INDIVIDUAL TESTS

# Test1: Is the emoji "adult" included in the list?
@pytest.mark.api
def test_emojis(github_api):
    r = github_api.emojis()
    
    assert 'adult' in r
    #print(r)

# Test2: Is the unexist emoji "adult10"?
@pytest.mark.api
def test_unexist_emojis(github_api):
    r = github_api.emojis()
    
    assert 'adult10' not in r

# Test3: Is the status_code emoji 200?
@pytest.mark.api
def test_status_code(github_api):
    r = github_api.emojis_response()
    
    assert r.status_code == 200


#Test4: Is exist commit response 200?
@pytest.mark.api
def test_status_code_commit(github_api):
    r = github_api.commit_responce('Astaarro', 'AndriiQA25')
    
    assert r.status_code == 200

#Test5: Is not exist commit response 404?
@pytest.mark.api
def test_status_code_unexist_commit(github_api):
    r = github_api.commit_responce('Astaarro1111', 'AndriiQA25')
   
    assert r.status_code == 404

#Test6: Is user name Astaarro?
@pytest.mark.api
def test_user_name_in_commit(github_api):
    commits = github_api.commit('Astaarro', 'AndriiQA25')
    first_commit = commits[0]  
    
    assert first_commit["author"]["login"] == "Astaarro"


#Test7: How many request for API remaining
@pytest.mark.api
def test_rate_limit(github_api):
    r = github_api.rate_limit()
    remaining = r["resources"]["core"]["remaining"]
    #print(r)
    print(f"\nRequests remaining: {remaining}")

    assert remaining >= 0


#Test8: Is code write in Python language?
@pytest.mark.api
def test_repo_language(github_api):
    r = github_api.repo_language("Astaarro", "AndriiQA25")
    #print(r)
    assert "Python" in r
   