import pytest
from djot_py.wrapper import Djot

@pytest.fixture(scope="module")
def djot_wrapper():
    return Djot()

def test_to_html(djot_wrapper):
    djot_text = "*Hello*, **Djot**!"
    expected_html = "<p><strong>Hello</strong>, <strong><strong>Djot</strong></strong>!</p>\n"
    assert djot_wrapper.to_html(djot_text) == expected_html

def test_render_ast_pretty(djot_wrapper):
    djot_text = "# Heading\n\n- Item 1"
    expected_pretty_ast = "doc\n  section id=\"Heading\"\n    heading level=\"1\"\n      str text=\"Heading\"\n    list style=\"-\" tight=\"true\"\n      list_item\n        para\n          str text=\"Item 1\"\nreferences\n  [\"Heading\"] =\n    reference destination=\"#Heading\"\n"
    assert djot_wrapper.render_ast_pretty(djot_text) == expected_pretty_ast

def test_render_ast_json(djot_wrapper):
    djot_text = "*Test*"
    expected_json = '{"tag":"doc","children":[{"tag":"para","children":[{"tag":"strong","children":[{"tag":"str","text":"Test"}]}]}],"references":[],"footnotes":[]}\n'
    assert djot_wrapper.render_ast_json(djot_text) == expected_json

def test_parse_events(djot_wrapper):
    djot_text = "*abc*"
    expected_events = [
        (1, 1, '+para'),
        (1, 1, '+strong'),
        (2, 4, 'str'),
        (5, 5, '-strong'),
        (6, 6, '-para'),
    ]
    actual_events = list(djot_wrapper.parse_events(djot_text))
    assert actual_events == expected_events
