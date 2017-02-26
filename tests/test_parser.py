import pytest
from lib.compiler import build_token_generator, ProgramNode, p_program


CASES = [
    '+++++++++++',
    '+++--......-[...--[><>>,,<<-]]++',
]


@pytest.mark.parametrize('code', CASES)
def test_parser(code):
    assert p_program.parse(tuple(build_token_generator(code))).to_bf_code() == code

