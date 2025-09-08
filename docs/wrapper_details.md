# Djot-py Wrapper Details

This document provides a detailed description of the `Djot-py` Python wrapper for `djot.lua`.

## Purpose

The `Djot-py` wrapper allows Python applications to leverage the `djot.lua` library for parsing and rendering Djot-formatted text. It provides a convenient Pythonic interface to the core functionalities of `djot.lua`, enabling tasks such as converting Djot to HTML, generating Abstract Syntax Trees (ASTs), and analyzing parsing events.

## How it Works

The wrapper utilizes the `lupa` library to create a bridge between Python and a Lua runtime. It dynamically loads the `djot.lua` library and its dependencies from a local `lua_modules` directory within the Python package. This approach ensures that the Python wrapper can interact directly with the Lua code, executing `djot.lua` functions and receiving their results.

### Key Components:

-   **`lupa`**: A Python library that provides a bridge to the Lua interpreter. It allows Python code to execute Lua code, call Lua functions, and access Lua data structures.
-   **`djot.lua`**: The core Lua library for Djot parsing and rendering.
-   **`src/djot_py/lua_modules/`**: A directory within the Python package that contains the `djot.lua` source files and its sub-modules. This ensures that the Lua runtime can find and load the necessary `djot.lua` components.

## `Djot` Class API

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

## Example Usage

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

## Prerequisites

To use the `Djot-py` wrapper, you need:

-   **Python 3.x**
-   **`lupa`**: Installable via `pip install lupa`.
-   **`djot.lua`**: The `djot.lua` source files are expected to be present in the `src/djot_py/lua_modules/` directory. These files are typically obtained by installing `djot` via `luarocks` and then copying the relevant files.

## Updating `djot.lua`

To update the `djot.lua` library used by the `Djot-py` wrapper, follow these steps:

1.  **Update `djot` via LuaRocks:**
    First, update your local `djot` installation using LuaRocks. It's recommended to use the `--local` flag to avoid permission issues:
    ```bash
    luarocks install --local djot
    ```

2.  **Copy Updated Files to `lua_modules`:**
    After updating, copy the new `djot.lua` and its sub-modules from your LuaRocks installation to the `src/djot_py/lua_modules/` directory. You'll need to replace the existing files.
    
    Assuming `djot.lua` is installed in `/home/bj/.luarocks/share/lua/5.4/`:
    ```bash
    cp /home/bj/.luarocks/share/lua/5.4/djot.lua src/djot_py/lua_modules/djot.lua
    cp -r /home/bj/.luarocks/share/lua/5.4/djot src/djot_py/lua_modules/djot
    ```
    **Note:** The exact paths might vary slightly depending on your LuaRocks installation.

3.  **Verify the Update:**
    After copying the files, run the unit tests to ensure that the wrapper still functions correctly with the updated `djot.lua` version:
    ```bash
    pytest
    ```
    If all tests pass, your `Djot-py` wrapper is successfully updated to use the new `djot.lua` version.
