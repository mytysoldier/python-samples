from src import code_mock

def get_json_data_mock(id):
    return {'name':'test'}

def test_get_user_names(monkeypatch):
    monkeypatch.setattr(code_mock, 'get_json_data', get_json_data_mock)
    result = code_mock.get_user_names(['001', '002'])

    assert list(result.keys()) == ['001', '002']
    assert list(result.values()) == ['test', 'test']