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

XSSinator offers a flexible payload generation mechanism that allows you to customize templates, variations, and encoding styles. By default, XSSinator uses a set of predefined templates, but you can also create your own templates and save them for future use.

Generate XSS payloads with default settings:
```
xssinator generate --count 10
```

To learn more about payload generation and customization, refer to the Payload Generation Guide.

### Vulnerability Scanning

XSSinator includes a powerful vulnerability scanning module that automates the process of detecting and exploiting XSS vulnerabilities in web applications. It performs comprehensive testing using the generated payloads and provides detailed reports with vulnerability analysis.

Scan a web application for XSS vulnerabilities:
```
xssinator scan --url https://example.com
```
To learn more about vulnerability scanning and how to use it effectively, refer to the Vulnerability Scanning Guide.

For a complete list of available commands and options, refer to the CLI documentation.
