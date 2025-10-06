
# Steam-Profiles-Ban-Checker (JSON/XLSX)
# Steam maFile → Bans Reporter (JSON/XLSX)
*UA/EN Цей README двомовний (Ukrainian & English).**

---

## 🇺🇦 Опис

**Для чого цей інструмент**
- Сканує всі `*.maFile` у теці (типово `./maFile`) і витягує `SteamID` + логін (назва файлу).
- Пакетами звертається до Steam Web API `ISteamUser/GetPlayerBans` з контрольованою частотою (типово **10–15 запитів/хв**).
- Зберігає результати:
  - `steam_ids64.txt` — список SteamID,
  - `data.json` — сирі відповіді API,
  - `data_ban.json` — відфільтровані записи з банами,
  - `report.xlsx` — Excel-звіт (**Login, SteamID, Ігрові блокування, Ком'юніті бан, VAC бан**).

**Вимоги**
- Python **3.8+**
- Пакети: `requests`, `openpyxl`  
  Встановлення:
  ```bash
  pip install -r requirements.txt
  # або
  pip install requests openpyxl


**Налаштування**

1. Створіть `.env` у корені проєкту:

   ```dotenv
   STEAM_API_KEY=YOUR_STEAM_WEB_API_KEY
   # (необов’язково) Ліміти запитів:
   # RPM_MIN=10
   # RPM_MAX=15
   ```
2. Покладіть ваші `*.maFile` у теку `maFile/`.

**Запуск (просто)**

> Нічого додатково вказувати в команді **не потрібно** — всі параметри вже підібрані за замовчуванням для стабільної роботи.

```bash
python main.py
```

**Запуск (просунуті параметри — лише для тих, хто розуміє, що робить)**

```bash
python main.py --dir maFile --chunk 50 --days 10 --out-json data.json --out-ban data_ban.json --out-xlsx report.xlsx --rpm-min 10 --rpm-max 15
```

> Якщо ви не впевнені — **не змінюйте параметри**. Дефолти оптимальні: безпечна швидкість запитів, здоровий розмір батчів, зручні імена файлів.

**Поради з безпеки**

* Не комітьте `.env` та `.maFile` у публічні репозиторії.
* Дотримуйтесь **Steam Subscriber Agreement** і політик **Steam Web API**.

**Зворотний зв’язок / Новий функціонал**

* Маєте ідеї або потрібні нові можливості? **Створіть Issue** у репозиторії або надішліть PR. Буду радий запитам на фічі!

---

## EN Description

**What it does**

* Scans `*.maFile` in a folder (default `./maFile`) and extracts `SteamID` + login (file base name).
* Calls Steam Web API `ISteamUser/GetPlayerBans` in batches with a controlled rate (default **10–15 req/min**).
* Saves:

  * `steam_ids64.txt` — SteamID list,
  * `data.json` — raw API responses,
  * `data_ban.json` — filtered entries with bans,
  * `report.xlsx` — Excel report (**Login, SteamID, Ігрові блокування, Ком'юніті бан, VAC бан**).

**Requirements**

* Python **3.8+**
* Packages: `requests`, `openpyxl`

  ```bash
  pip install -r requirements.txt
  # or
  pip install requests openpyxl
  ```

**Setup**

1. Create `.env` in project root:

   ```dotenv
   STEAM_API_KEY=YOUR_STEAM_WEB_API_KEY
   # (optional) request-rate bounds:
   # RPM_MIN=10
   # RPM_MAX=15
   ```
2. Put your `*.maFile` into `maFile/`.

**Run (the simple way)**

> You **don’t need to pass any CLI parameters** — sensible defaults are chosen for reliable operation.

```bash
python main.py
```

**Run (advanced — only if you know what you’re doing)**

```bash
python main.py --dir maFile --chunk 50 --days 10 --out-json data.json --out-ban data_ban.json --out-xlsx report.xlsx --rpm-min 10 --rpm-max 15
```

> If unsure, **do not change the defaults**. They balance API safety, batch size, and output naming.

**Security notes**

* Don’t commit `.env` or `.maFile` to public repos.
* Respect the **Steam Subscriber Agreement** and **Steam Web API** policies.

**Feature requests**

* Want extra functionality? **Open an Issue** or send a PR — feature requests are welcome!

---

## Структура / Structure

```
.
├─ main.py
├─ maFile/                 # your *.maFile go here
├─ data.json               # raw API responses (generated)
├─ data_ban.json           # filtered bans (generated)
├─ steam_ids64.txt         # SteamID list (generated)
├─ report.xlsx             # Excel report (generated)
├─ .env                    # STEAM_API_KEY (+ optional RPM bounds)
├─ requirements.txt
└─ README.md
```

## Ліцензія / License

Цей проєкт ліцензовано за **MIT License** — див. розділ нижче.
This project is licensed under the **MIT License** — see below.

---

### MIT License

Copyright (c) 2025 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

```
```
