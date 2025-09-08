## Top-Level Functions

### `djot_to_html(text: str) -> str`

Converts Djot text to HTML using the `Djot-py` wrapper. This is a convenience function for simple conversions, internally utilizing the `Djot` class.

-   **`text`**: The Djot formatted string to convert.
-   **Returns**: The HTML representation of the input Djot text.

## Djot Class API

The `Djot` class is the primary interface for interacting with `djot.lua`. It provides the following methods:

### `__init__(self)`

Initializes the `Djot` wrapper. This involves setting up the Lua runtime, configuring the Lua `package.path` to include the `lua_modules` directory, and loading the `djot.lua` module.

### `parse(self, djot_text: str)`

Parses Djot-formatted text and returns its Abstract Syntax Tree (AST).

-   **`djot_text`**: The input string containing Djot-formatted text.
-   **Returns**: A Lua table representing the AST of the input text.

### `to_html(self, djot_text: str) -> str`

Converts Djot-formatted text to HTML.

-   **`djot_text`**: The input string containing Djot-formatted text.
-   **Returns**: A string containing the HTML representation of the input Djot text.

### `render_ast_pretty(self, djot_text: str) -> str`

Renders the AST of Djot-formatted text in a human-readable, pretty-printed format.

-   **`djot_text`**: The input string containing Djot-formatted text.
-   **Returns**: A string containing the pretty-printed AST.

### `render_ast_json(self, djot_text: str) -> str`

Renders the AST of Djot-formatted text as a JSON string.

-   **`djot_text`**: The input string containing Djot-formatted text.
-   **Returns**: A string containing the JSON representation of the AST.

### `parse_events(self, djot_text: str)`

Parses Djot-formatted text and returns an iterator over parsing events. Each event is typically a tuple containing `(startpos, endpos, annotation)`.

-   **`djot_text`**: The input string containing Djot-formatted text.
-   **Returns**: A Python iterator that yields tuples representing parsing events.
