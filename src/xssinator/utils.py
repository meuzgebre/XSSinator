import logging
import re

def read_file(file_path):
    """
    Read the contents of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        list: The contents of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If there was an error reading the file.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        return [line.strip() for line in lines]
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    except IOError:
        raise IOError(f"Error reading the file '{file_path}'.")


def write_payloads_to_file(payloads: list, output_file: str):
    """
    Writes the generated XSS payloads to a file.

    Args:
        payloads (List[str]): The list of XSS payloads to write.
        output_file (str): The file path to save the payloads.

    Raises:
        ValueError: If the output_file is not a valid file path.

    Returns:
        None
    """

    # Todo: try/catch block
    with open(output_file, "a") as file:
        for payload in payloads:
            file.write(payload + "\n")

    return {
        "num_of_lines_written": len(payloads),
        "output_location": output_file,
        "complete_status": True
    }


def is_valid_url(url):
    """
    Check if a URL is valid.

    Args:
        url (str): The URL to validate.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """

    pattern = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https://
        # domain
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
        r"localhost|"  # localhost
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # or IP
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$", re.IGNORECASE)

    return bool(re.match(pattern, url))


def log_message(message, level="info"):
    """
    Logs a message with the specified logging level.

    Args:
        message (str): The message to be logged.
        level (str): The logging level to use. Defaults to 'info'.

    Returns:
        None
    """

    # Configure the logging level using a dictionary mapping
    # logging levels to their corresponding functions:

    log_functions = {
        'info': logging.info,
        'warning': logging.warning,
        'error': logging.error,
        'critical': logging.critical
    }

    if level in log_functions:
        log_functions[level](message)
    else:
        raise ValueError(f"Invalid logging level: {level}")
