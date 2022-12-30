import pytest
from src import code_exception

def test_user_name_validation():
    with pytest.raises(ValueError) as e:
        code_exception.user_name_validation(None)
    assert str(e.value) == 'name is not set'