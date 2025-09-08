## Example Usage

### Using the top-level `djot_to_html` function

For simple conversions, you can use the `djot_to_html` function directly:

```python
from djot_py import djot_to_html

html_output = djot_to_html("*Hello*, **Djot**!")
print(html_output)
# Output: <p><strong>Hello</strong>, <strong><strong>Djot</strong></strong>!</p>\n
```

### Using the `Djot` class

For more advanced usage, including AST rendering and event parsing, you can instantiate the `Djot` class:

```python
from djot_py.wrapper import Djot

djot_wrapper = Djot()
markdown_text = "*Hello*, **Djot**!\n\n- Item 1\n- Item 2"

# Convert to HTML
html_output = djot_wrapper.to_html(markdown_text)
print("--- HTML Output ---")
print(html_output)

# Render Pretty AST
pretty_ast_output = djot_wrapper.render_ast_pretty(markdown_text)
print("\n--- Pretty AST Output ---")
print(pretty_ast_output)

# Render JSON AST
json_ast_output = djot_wrapper.render_ast_json(markdown_text)
print("\n--- JSON AST Output ---")
print(json_ast_output)

# Parse Events
print("\n--- Events Output ---")
for startpos, endpos, annotation in djot_wrapper.parse_events(markdown_text):
    print(f"Start: {startpos}, End: {endpos}, Annotation: {annotation}")
```
