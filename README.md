# Djot-py

A Python wrapper for the [djot.lua](https://github.com/jgm/djot.lua) library.

`Djot-py` provides a convenient Pythonic interface to parse and render Djot-formatted text, leveraging the speed and efficiency of the original Lua implementation via `lupa`.

## Features

-   Convert Djot to HTML.
-   Parse Djot text into Abstract Syntax Trees (AST).
-   Render ASTs in human-readable or JSON formats.
-   Iterate over parsing events.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Djot-py.git
    cd Djot-py
    ```

2.  **Install LuaRocks and `djot.lua`:**
    Ensure you have [LuaRocks](https://luarocks.org/) installed. Then, install `djot.lua` locally:
    ```bash
    luarocks install --local djot
    ```

3.  **Set up Python environment:**
    It's recommended to use a virtual environment. This project uses `uv` for dependency management.
    ```bash
    uv venv .venv
    source .venv/bin/activate
    uv pip install -e . pytest
    ```

## Quick Start

```python
from djot_py.wrapper import Djot

djot_wrapper = Djot()
markdown_text = "*Hello*, **Djot**!"

html_output = djot_wrapper.to_html(markdown_text)
print(html_output)
# Output: <p><strong>Hello</strong>, <strong><strong>Djot</strong></strong>!</p>\n
# You can also parse to AST, render as JSON, or iterate events:
# ast_json = djot_wrapper.render_ast_json(markdown_text)
# print(ast_json)
```

## Documentation

-   [Detailed Wrapper Information](docs/wrapper_details.md)
-   [API Reference](docs/API.md)
-   [Usage Examples](docs/usage.md)

## Contributing

Contributions are welcome! Please see the [contributing guidelines](CONTRIBUTING.md) (if available).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.