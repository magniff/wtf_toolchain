import pytest
from lib.compiler import build_token_generator
import lib.compiler.tokenizer as t


CASES = (
    ('>>>>+-', (t.t_right(4), t.t_inc(1), t.t_dec(1))),
    ('--[+++]', (t.t_dec(2), t.t_loop_start(), t.t_inc(3), t.t_loop_end())),
    (
        '--[+[]++]', 
        (
            t.t_dec(2), t.t_loop_start(), t.t_inc(1),
            t.t_loop_start(), t.t_loop_end(), t.t_inc(2), t.t_loop_end(),
        )
    ),
)


@pytest.mark.parametrize('code,tokenized', CASES)
def test_tokenizer(code, tokenized):
    assert tuple(build_token_generator(code)) == tokenized

