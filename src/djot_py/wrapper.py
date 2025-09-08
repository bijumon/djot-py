import lupa
import os
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DjotError(Exception):
    """Base exception for Djot-py wrapper errors."""
    pass

class DjotLuaError(DjotError):
    """Exception raised for errors originating from the Lua runtime."""
    pass

class DjotInputError(DjotError):
    """Exception raised for invalid input to Djot methods."""
    pass

class Djot:
    def __init__(self):
        try:
            self.lua = lupa.LuaRuntime()
            
            # Get the directory of the current file (wrapper.py)
            current_dir = os.path.dirname(os.path.abspath(__file__))
            
            # Construct the path to the lua_modules directory
            lua_modules_path = os.path.join(current_dir, 'lua_modules')
            
            # Add the lua_modules path to Lua's package.path
            self.lua.execute(f"package.path = package.path .. ';{lua_modules_path}/?.lua;{lua_modules_path}/?/init.lua'")
            
            self.djot_module = self.lua.require('djot')[0]
            logger.info("djot.lua module loaded successfully.")
        except lupa.lua54.LuaError as e:
            logger.error(f"Failed to initialize Djot wrapper due to Lua error: {e}", exc_info=True)
            raise DjotLuaError(f"Failed to load djot.lua module: {e}") from e
        except Exception as e:
            logger.error(f"An unexpected error occurred during Djot wrapper initialization: {e}", exc_info=True)
            raise DjotError(f"Unexpected error during initialization: {e}") from e

    def parse(self, djot_text: str):
        """Parses djot text and returns the Abstract Syntax Tree (AST)."""
        if not isinstance(djot_text, str):
            raise DjotInputError("Input 'djot_text' must be a string.")
        try:
            return self.djot_module.parse(djot_text)
        except lupa.lua54.LuaError as e:
            logger.error(f"Lua error during parse operation: {e}", exc_info=True)
            raise DjotLuaError(f"Error parsing Djot text: {e}") from e

    def to_html(self, djot_text: str) -> str:
        """Converts djot text to HTML."""
        if not isinstance(djot_text, str):
            raise DjotInputError("Input 'djot_text' must be a string.")
        try:
            doc = self.parse(djot_text)
            return self.djot_module.render_html(doc)
        except lupa.lua54.LuaError as e:
            logger.error(f"Lua error during to_html operation: {e}", exc_info=True)
            raise DjotLuaError(f"Error converting Djot text to HTML: {e}") from e

    def render_ast_pretty(self, djot_text: str) -> str:
        """Renders the AST of djot text in a human-readable form."""
        if not isinstance(djot_text, str):
            raise DjotInputError("Input 'djot_text' must be a string.")
        try:
            doc = self.parse(djot_text)
            return self.djot_module.render_ast_pretty(doc)
        except lupa.lua54.LuaError as e:
            logger.error(f"Lua error during render_ast_pretty operation: {e}", exc_info=True)
            raise DjotLuaError(f"Error rendering pretty AST: {e}") from e

    def render_ast_json(self, djot_text: str) -> str:
        """Renders the AST of djot text as JSON."""
        if not isinstance(djot_text, str):
            raise DjotInputError("Input 'djot_text' must be a string.")
        try:
            doc = self.parse(djot_text)
            return self.djot_module.render_ast_json(doc)
        except lupa.lua54.LuaError as e:
            logger.error(f"Lua error during render_ast_json operation: {e}", exc_info=True)
            raise DjotLuaError(f"Error rendering JSON AST: {e}") from e

    def parse_events(self, djot_text: str):
        """Parses djot text and returns an iterator over events.
        Each event is a tuple: (startpos, endpos, annotation).
        """
        if not isinstance(djot_text, str):
            raise DjotInputError("Input 'djot_text' must be a string.")
        try:
            lua_iterator_func = self.djot_module.parse_events(djot_text)
            while True:
                result = lua_iterator_func()
                if result is None:
                    break
                yield result
        except lupa.lua54.LuaError as e:
            logger.error(f"Lua error during parse_events operation: {e}", exc_info=True)
            raise DjotLuaError(f"Error parsing Djot events: {e}") from e

    # Example usage (for testing purposes)
if __name__ == "__main__":
    try:
        djot_wrapper = Djot()
        markdown_text = "*Hello*, **Djot**!\n\n- Item 1\n- Item 2"
        invalid_input = 123 # Example of invalid input
        
        print("--- HTML Output ---")
        html_output = djot_wrapper.to_html(markdown_text)
        print(html_output)

        print("\n--- Pretty AST Output ---")
        pretty_ast_output = djot_wrapper.render_ast_pretty(markdown_text)
        print(pretty_ast_output)

        print("\n--- JSON AST Output ---")
        json_ast_output = djot_wrapper.render_ast_json(markdown_text)
        print(json_ast_output)

        print("\n--- Events Output ---")
        for startpos, endpos, annotation in djot_wrapper.parse_events(markdown_text):
            print(f"Start: {startpos}, End: {endpos}, Annotation: {annotation}")

        print("\n--- Testing InputError (expected) ---")
        djot_wrapper.to_html(invalid_input)

    except DjotInputError as e:
        print(f"Caught expected DjotInputError: {e}")
    except DjotLuaError as e:
        print(f"Caught DjotLuaError: {e}")
    except DjotError as e:
        print(f"Caught general DjotError: {e}")
    except Exception as e:
        print(f"Caught unexpected Exception: {e}")
