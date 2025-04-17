from utils.constants import PAGE_MAP

def load_file(file_path):
    """
    Load a file and return its contents as a string.

    Args:
        file_path: The path of the file.

    Returns:
        str: Contents of the file as a string.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def remove_placeholders(text):
    """
    Remove all known placeholder tokens from a text string.

    Args:
        text: The string containing placeholders to be removed.

    Returns:
        str: The cleaned string with placeholders removed.
    """

    for placeholder in PAGE_MAP:
        text = text.replace(placeholder, "")
    return text
