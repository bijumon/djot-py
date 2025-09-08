import click
import sys
from .wrapper import Djot, DjotError, DjotInputError, DjotLuaError

@click.group()
def cli():
    """A Python wrapper for djot.lua."""
    pass

@cli.command()
@click.argument('input_file', type=click.File('r'), default=sys.stdin)
def to_html(input_file):
    """Converts Djot text to HTML.

    Reads from INPUT_FILE or stdin.
    """
    djot_text = input_file.read()
    try:
        djot_wrapper = Djot()
        html_output = djot_wrapper.to_html(djot_text)
        click.echo(html_output)
    except (DjotError, DjotInputError, DjotLuaError) as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)

@cli.command()
@click.argument('input_file', type=click.File('r'), default=sys.stdin)
def render_ast_pretty(input_file):
    """Renders the AST of Djot text in a human-readable form.

    Reads from INPUT_FILE or stdin.
    """
    djot_text = input_file.read()
    try:
        djot_wrapper = Djot()
        pretty_ast_output = djot_wrapper.render_ast_pretty(djot_text)
        click.echo(pretty_ast_output)
    except (DjotError, DjotInputError, DjotLuaError) as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)

@cli.command()
@click.argument('input_file', type=click.File('r'), default=sys.stdin)
def render_ast_json(input_file):
    """Renders the AST of Djot text as JSON.

    Reads from INPUT_FILE or stdin.
    """
    djot_text = input_file.read()
    try:
        djot_wrapper = Djot()
        json_ast_output = djot_wrapper.render_ast_json(djot_text)
        click.echo(json_ast_output)
    except (DjotError, DjotInputError, DjotLuaError) as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)

@cli.command()
@click.argument('input_file', type=click.File('r'), default=sys.stdin)
def parse_events(input_file):
    """Parses Djot text and prints parsing events.

    Reads from INPUT_FILE or stdin.
    """
    djot_text = input_file.read()
    try:
        djot_wrapper = Djot()
        for startpos, endpos, annotation in djot_wrapper.parse_events(djot_text):
            click.echo(f"Start: {startpos}, End: {endpos}, Annotation: {annotation}")
    except (DjotError, DjotInputError, DjotLuaError) as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)

if __name__ == '__main__':
    cli()
