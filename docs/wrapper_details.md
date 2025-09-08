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
