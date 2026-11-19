# Steam Profiles Ban Checker

Check VAC, community and game bans for many Steam accounts at once and get a clean Excel report.

The tool reads your `.maFile` exports, extracts each SteamID, queries the official Steam Web API in rate-limited batches, and writes the results to JSON and XLSX.

## Features

- Scans a folder of `*.maFile` files and extracts the SteamID and login (file name).
- Calls `ISteamUser/GetPlayerBans` in batches at a controlled rate (10–15 requests per minute by default).
- Writes four outputs:

| File | Content |
|---|---|
| `steam_ids64.txt` | List of extracted SteamIDs |
| `data.json` | Raw API responses |
| `data_ban.json` | Only the entries that have bans |
| `report.xlsx` | Excel report: login, SteamID, game bans, community ban, VAC ban |

## Requirements

- Python 3.8+
- A Steam Web API key
- Packages: `requests`, `openpyxl`

```bash
pip install requests openpyxl
```

## Setup

1. Create a `.env` file in the project root:

   ```dotenv
   STEAM_API_KEY=YOUR_STEAM_WEB_API_KEY
   # optional request-rate bounds
   # RPM_MIN=10
   # RPM_MAX=15
   ```

2. Put your `*.maFile` files into the `maFile/` folder.

## Usage

```bash
python main.py
```

The defaults are tuned for stable, API-safe operation. Advanced options:

```bash
python main.py --dir maFile --chunk 50 --days 10 --out-json data.json --out-ban data_ban.json --out-xlsx report.xlsx --rpm-min 10 --rpm-max 15
```

| Option | Meaning |
|---|---|
| `--dir` | Folder with `.maFile` files |
| `--chunk` | Accounts per API request |
| `--days` | Report window for recent bans |
| `--out-json`, `--out-ban`, `--out-xlsx` | Output file names |
| `--rpm-min`, `--rpm-max` | Request-rate bounds (per minute) |

## Security

- Never commit a real `.env` or any `.maFile` to a public repository.
- Follow the Steam Subscriber Agreement and Steam Web API terms.

## Project structure

```
.
├─ main.py
├─ maFile/            # your *.maFile files
├─ .env               # STEAM_API_KEY and optional rate bounds
├─ requirements.txt
└─ README.md
```

## License

MIT. See the license text below.

<details>
<summary>MIT License</summary>

Copyright (c) 2025 AndraX

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

</details>
