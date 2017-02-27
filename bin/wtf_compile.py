import sys
import datetime

import click

from lib.compiler import generator, tokenizer, parser, optimizer


@click.command(
    context_settings=dict(help_option_names=['-h', '--help']),
    help=('Pretty straight forward demultiplexing algorithm.')
)
@click.option(
    '-i', '--input', required=True,
    help='Path to bf source to compile.', type=click.File()
)
@click.option(
    '-o', '--output', required=True,
    help='Path to file containing result.', type=click.File('wb')
)
def main(input, output):
    ast = parser.p_program.parse(
        tuple(tokenizer.build_token_generator(input.read()))
    )
    opt_ast = optimizer.optimize(ast)
    result = bytes(generator.visit(opt_ast))
    output.write(bytes(generator.visit(opt_ast)))

