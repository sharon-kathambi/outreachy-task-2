import csv
import urllib.request
import urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

csv_file = "Task 2 - Intern.csv"

with open(csv_file, newline='', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        url = row['urls'].strip()
        if not url:
            continue
        try:
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            with urllib.request.urlopen(req, timeout=10, context=ctx) as response:
                status = response.status
        except urllib.error.HTTPError as e:
            status = e.code
        except Exception:
            status = 'ERR'
        print(f"({status}) {url}")