# kuma_auto_asset_add

_English version below_

# О программе

Данный скрипт и набор ресурсов позволяют автоматически на основании информации из событий (ip-адреса, доменные имена) создавать активы в KUMA

# Требования

python 3.6+
- urllib
- argparse
- json
- requests
- os

KUMA 3.0.2

---

# Быстрый старт

## Подготовка скрипта

1. Поместите файлы `asset-import.py`, `kumaPublicApiV1.py`, `params.json` на сервер коррелятора в папку scripts: /opt/kaspersky/kuma/correlator/`id`/scripts

`id` коррелятора можно получить из веб-интерфейса KUMA: Ресурсы -> Активные сервисы -> Выбрать галочкой коррелятор и в верхнем меню `Копировать идентификатор сервиса`. Идентификатор будет скопирован в буфер обмена.

2. Внесите изменения в файл `params.json`:

- kumaAddress - укажите ip-адрес сервера ядра KUMA
- kumaAPIPort - укажите API-порт ядра KUMA (значение по умолчанию `7223`, если сомневаетесь - оставьте без изменений)
- kumaToken - токен для работы с API с правами `POST /assets/import`

3. Измените владельца файлов на kuma:
```commandline
chown kuma:kuma asset-import.py kumaPublicApiV1.py params.json
```

4. Разрешите запуск файла `asset-import.py`:
```commandline
chmod +x asset-import.py
```

## Подготовка KUMA

1. Импортируйте все ресурсы из файла `auto_asset_add` (Пароль импорта: Qwerty123!)

2. Если нужно, внесите изменения в фильтры `org address filter` и `org hostname filter`, указав домены и подсети вашей организации, по ним отбираются активы из событий для импорта.

3. Привяжите все правила корреляции `Auto import asset info (src/dst/dvc)` к коррелятору

4. Привяжите правило реагирования `Auto asset import`

5. Обновите параметры сервиса коррелятора

## Результат

В результате проделанных манипуляций в KUMA будут создаваться активы на основании информации, получаемой из событий.

---

# About

This script and resources automatically import host info (ip-addresses and fqdns) from events to Assets in KUMA

# Requirements

python 3.6+
- urllib
- argparse
- json
- requests
- os

KUMA 3.0.2

---

# Quick start

## Script preparation

1. Move `asset-import.py`, `kumaPublicApiV1.py`, `params.json` to scripts correlator folder: /opt/kaspersky/kuma/correlator/`id`/scripts

`id` of correlator can be found in KUMA Web UI: Resources -> Active Services -> Select correlator checkbox and choose `Copy service ID`

2. Edit `params.json` file:

- kumaAddress - IP address (or FQDN) of KUMA Core server
- kumaAPIPort - KUMA Core API port (by default `7223`)
- kumaToken - API Token with `POST /assets/import` API rights

3. Change owner of files to kuma:
```commandline
chown kuma:kuma asset-import.py kumaPublicApiV1.py params.json
```

4. Make file `asset-import.py` executable:
```commandline
chmod +x asset-import.py
```

## KUMA preparation

1. Import all resources from file `auto_asset_add` (Passphrase: Qwerty123!)

2. If needed edit filters `org address filter` and `org hostname filter` with your org parameters (domain, subnets)

3. Link correlation rules `Auto import asset info (src/dst/dvc)` to correlator

4. Link response rule `Auto asset import`

5. Reload correlator

