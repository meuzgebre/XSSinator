# XSSinator

[![Build Status](https://img.shields.io/travis/meuzgebre/xssinator/master.svg?style=flat-square)](https://travis-ci.org/meuzgebre/xssinator)
[![License](https://img.shields.io/github/license/meuzgebre/xssinator.svg?style=flat-square)](LICENSE)

XSSinator is a powerful XSS payload generator and scanner designed to detect and exploit Cross-Site Scripting vulnerabilities in web applications. It provides a wide range of payload templates, variations, abstraction techniques, and evasion mechanisms to facilitate comprehensive testing and analysis.

## Features

- Automated generation of XSS payloads
- Customizable templates with variations and abstraction
- Evasion techniques to bypass filters and WAFs
- Multiple encoding styles for payload generation
- Scan web applications for XSS vulnerabilities
- Detailed reporting and vulnerability analysis


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Payload Generation](#payload-generation)
  - [Vulnerability Scanning](#vulnerability-scanning)
- [Contributing](#contributing)
- [License](#license)


## Installation

To install XSSinator, you need to have Python 3 and pip package manager installed. Run the following command to install the required dependencies:

#### From pip

```shell
pip install xssinator
```

#### From source

```
git clone https://github.com/meuzgebre/xssinator
cd xxsinator
pip install -r requirements.txt
```

## Usage

XSSinator provides a command-line interface (CLI) to generate XSS payloads and scan web applications. Here are some examples of how to use XSSinator:

### Payload Generation

Generate XSS payloads with default settings:
```
xssinator generate --count 10
```

### Vulnerability Scanning

Scan a web application for XSS vulnerabilities:
```
xssinator scan --url https://example.com
```

For a complete list of available commands and options, refer to the CLI documentation.
