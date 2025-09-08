from .wrapper import Djot

def djot_to_html(text: str) -> str:
    """
    Converts Djot text to HTML using the Djot-py wrapper.

    Args:
        text: The Djot formatted string to convert.

    Returns:
        The HTML representation of the input Djot text.
    """
    djot_wrapper = Djot()
    return djot_wrapper.to_html(text)
