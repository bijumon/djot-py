import lupa
import os

class Djot:
    def __init__(self):
        self.lua = lupa.LuaRuntime()
        
        # Get the directory of the current file (wrapper.py)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the path to the lua_modules directory
        lua_modules_path = os.path.join(current_dir, 'lua_modules')
        
        # Add the lua_modules path to Lua's package.path
        self.lua.execute(f"package.path = package.path .. ';{lua_modules_path}/?.lua;{lua_modules_path}/?/init.lua'")
        
        # Load the djot module
        self.djot_module = self.lua.require('djot')[0] # Access the Lua table

    def parse(self, djot_text: str):
        """Parses djot text and returns the Abstract Syntax Tree (AST)."""
        return self.djot_module.parse(djot_text)

    def to_html(self, djot_text: str) -> str:
        """Converts djot text to HTML."""
        doc = self.parse(djot_text)
        return self.djot_module.render_html(doc)

    def render_ast_pretty(self, djot_text: str) -> str:
        """Renders the AST of djot text in a human-readable form."""
        doc = self.parse(djot_text)
        return self.djot_module.render_ast_pretty(doc)

    def render_ast_json(self, djot_text: str) -> str:
        """Renders the AST of djot text as JSON."""
        doc = self.parse(djot_text)
        return self.djot_module.render_ast_json(doc)

    def parse_events(self, djot_text: str):
        """Parses djot text and returns an iterator over events.
        Each event is a tuple: (startpos, endpos, annotation).
        """
        lua_iterator_func = self.djot_module.parse_events(djot_text)
        while True:
            result = lua_iterator_func()
            if result is None:
                break
            yield result

# Example usage (for testing purposes)
if __name__ == "__main__":
    djot_wrapper = Djot()
    markdown_text = "*Hello*, **Djot**!\n\n- Item 1\n- Item 2"
    
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
