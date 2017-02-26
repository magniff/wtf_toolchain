import pytest
from lib import parse


CASES = (
    ('>>>>+-', ('>>>>+-', {})),
    ('++[-->]+', ('++[-->]+', {2: 7, 6: 2})),
)


@pytest.mark.parametrize('code,parsed', CASES)
def test_parser(code, parsed):
    assert parse(code) == parsed

