# outreachy-task-2
# URL Status Checker

Reads URLs from a CSV file and prints the HTTP status code for each.

## Requirements

- Python 3
- No external dependencies (uses standard library only)

## Usage

1. Place `Task 2 - Intern.csv` in the same directory as the script
2. Run:
```bash
   python3 check_url_status.py
```

## Output
```
(200) https://www.nytimes.com/...
(404) http://www.saadec.com.br/...
(ERR) http://jogandocomelas.com.br/...
```
<img width="912" height="438" alt="Screenshot 2026-03-23 at 13 01 51" src="https://github.com/user-attachments/assets/de3c302c-0ebb-4916-93f8-a669a12553ef" />


- `2xx` — page is live
- `3xx` — redirect
- `4xx` — page not found or access denied
- `5xx` — server error
- `ERR` — could not connect (timeout, DNS failure, SSL error, etc.)
