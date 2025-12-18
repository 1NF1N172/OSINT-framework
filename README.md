# OSINT Framework - Web Application Vulnerability Scanner

A comprehensive Python-based framework for web application vulnerability scanning. Developed in 2021.

## Overview

This framework integrates three powerful security scanning tools:
- **OWASP ZAP** - Web application security testing
- **Wfuzz** - Web application fuzzer
- **Nmap** - Network scanning and service detection

## Features

### OWASP ZAP Integration
- **Spider Scan**: Automatic discovery of new resources (URLs) on a specific site
- **Active Scan**: Active search for potential vulnerabilities using known methods
- Automatic HTML and XML report generation

### Wfuzz Integration
- **Directory Scan**: Directory brute-forcing to discover hidden files and directories
- **POST Parameter Fuzzing**: Fuzzing POST parameters with support for known/unknown user credentials

### Nmap Integration
- **Service Version Detection**: Detect service versions on target hosts
- **Top Ports Scan**: Scan top ports with service version detection

## Installation

### Prerequisites

1. **Python 3.7+** installed on your system
2. **OWASP ZAP** installed (for ZAP functionality)
   - Linux: Usually at `/usr/share/zaproxy/zap.sh`
   - Windows: Download from [OWASP ZAP website](https://www.zaproxy.org/download/)
3. **Nmap** installed (for Nmap functionality)
   - Download from [Nmap website](https://nmap.org/download.html)

### Python Dependencies

Install required Python packages:

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install python-owasp-zap-v2.4
pip install wfuzz
pip install nmap3
```

## Usage

Run the main script:

```bash
python main.py
```

or

```bash
py main.py
```

## Project Structure

```
OSINT framework/
├── main.py           # Main menu and application entry point
├── zap.py            # OWASP ZAP integration module
├── wfuzz.py          # Wfuzz integration module
├── nmap.py           # Nmap integration module
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## Workflow Diagrams

### Main Menu Flow

```
┌─────────────────┐
│  MAIN MENU      │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────┐
│  SELECT SCAN OPTION         │
└────────┬────────────────────┘
         │
         ▼
    ┌──────────┐
    │ SPIDER   │
    │ SCAN?    │
    └────┬─────┘
         │
    ┌────┴────┐
    │         │
   YES       NO
    │         │
    ▼         ▼
┌─────────┐ ┌──────────┐
│ START   │ │ ACTIVE   │
│ SPIDER  │ │ SCAN?    │
│ SCAN    │ └────┬─────┘
└─────────┘      │
            ┌────┴────┐
            │         │
           YES       NO
            │         │
            ▼         ▼
      ┌─────────┐ ┌──────────┐
      │ START    │ │ MAIN     │
      │ ACTIVE   │ │ MENU?    │
      │ SCAN     │ └────┬─────┘
      └─────────┘       │
                       │
                       ▼
              ┌─────────────────┐
              │  MAIN MENU       │◄────┐
              └──────────────────┘     │
                                       │
                                   (Loop back)
```

### OWASP ZAP Scanning Process

```
┌─────────────────────────────────────┐
│ USER ENTERS TARGET IP/URL           │
└──────────────┬───────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ OWASP ZAP OPENS URL                 │
└──────────────┬───────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ SCANNING STARTS                      │
└──────────────┬───────────────────────┘
               │
               ▼
         ┌──────────┐
         │ SCANNING │◄────┐
         └────┬─────┘     │
              │           │
              ▼           │
      ┌──────────────┐   │
      │ PROGRESS =   │   │
      │ 100%?        │   │
      └──────┬───────┘   │
             │           │
        ┌────┴────┐      │
        │         │      │
       NO        YES     │
        │         │      │
        └─────────┘      │
                         │
                         │
               ┌─────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ RESULT                               │
│ (Reports generated)                  │
└─────────────────────────────────────┘
```

### POST Fuzzing Process

```
┌─────────────────────┐
│ POST FUZZING START  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────────────┐
│ USER ADDS WEB URL                    │
└──────────┬───────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│ USER ADDS WORDLIST DIRECTORY         │
└──────────┬───────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│ ADD FIRST PARAMETER                   │
└──────────┬───────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│ ADD SECOND PARAMETER                 │
└──────────┬───────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│ CHECK FOR MISSING PARAMETERS?        │
└──────────┬───────────────────────────┘
           │
      ┌────┴────┐
      │         │
    MISSING   NONE
      │         │
      ▼         │
┌─────────────────────────────────────┐
│ SAVE PARAMETERS IN VARIABLE          │
└──────────┬───────────────────────────┘
           │
           └──────────┐
                      │
                      ▼
┌─────────────────────────────────────┐
│ SAVE ADDED INFORMATION               │
└──────────┬───────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│ DOES USER KNOW ANY USERNAMES?        │
└──────────┬───────────────────────────┘
           │
      ┌────┴────┐
      │         │
     YES       NO
      │         │
      ▼         │
┌─────────────────────────────────────┐│
│ USER ADDS NECESSARY DATA            ││
└──────────┬───────────────────────────┘│
           │                           │
           └───────────┬───────────────┘
                       │
                       ▼
┌─────────────────────────────────────┐
│ "FUZZING" STARTS                     │
└──────────┬───────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│ RESULTS                              │
└──────────┬───────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│ EXIT                                 │
└─────────────────────────────────────┘
```

## Configuration

### OWASP ZAP Configuration

The ZAP daemon is configured with API key `hello` by default. To change this:

1. Edit `zap.py`
2. Update the API key in the `start_zap()` function and scan functions
3. On Windows, update the ZAP path in `start_zap()` function

### Windows Configuration

For Windows users, update the ZAP path in `zap.py`:

```python
# Change this line in start_zap() function:
subprocess.Popen(['C:\\Path\\To\\ZAP\\zap.bat', '-daemon', '-config', 'api.key=hello'], ...)
```

## Output

### OWASP ZAP Reports
- `report.html` - HTML formatted scan report
- `report.xml` - XML formatted scan report

Reports are automatically generated after each scan completes.

## Notes

- All scans require proper network connectivity
- Some scans may take significant time depending on target size
- Ensure you have proper authorization before scanning any target

## Author

1NF1N172

## License

Please use responsibly and only on systems you own or have explicit permission to test.

## Disclaimer

This tool is for educational and authorized security testing purposes only. Unauthorized access to computer systems is illegal. The authors are not responsible for any misuse of this software.


