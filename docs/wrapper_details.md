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

## API Reference

For a detailed API reference of the `Djot` class, please refer to [API.md](API.md).

## Usage

For examples on how to use the `Djot-py` wrapper, please refer to [usage.md](usage.md).

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

## TODO

Here are some potential improvements and future work for the `Djot-py` wrapper:

-   **More Comprehensive Testing:** Expand unit tests with more edge cases, and add integration tests for the CLI.
-   **Performance Benchmarking:** Add benchmarks to measure the performance of the wrapper for various input sizes.
-   **Expose `djot.lua` Options/Extensions:** Investigate how to expose `djot.lua`'s options (e.g., for HTML rendering, parsing behavior, custom filters) through the Python API.
-   **Asynchronous API:** Consider adding asynchronous versions of the methods if `lupa` supports it and there's a performance benefit.
-   **Type Hinting:** Ensure all methods have comprehensive type hints for better code clarity and static analysis.
-   **Packaging and Distribution:** Finalize metadata in `pyproject.toml` and prepare for PyPI distribution.
-   **CI/CD Pipeline:** Set up automated testing and building using a platform like GitHub Actions.
-   **CLI Enhancements:** Add more features to the CLI, such as options for output files, custom configurations, and more detailed error reporting.
-   **Error Handling Refinement:** Map specific Lua errors to more granular Python exceptions for better error handling by consumers of the library.
