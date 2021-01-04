(see below for English version) 
# Wie wir uns Geschwindigkeitsstatistiken a la fast.com als CSV besorgen

Dieses Repo beinhaltet ein Python-Skript, as zusammen mit selenium und cron csv-Dateien und Screenshots schreibt, um die Geschwindigkeit eines Internetzugangs zu monitoren. Das ganze ist eventuell nützlich, um dem eigenen ISP aufs Dach zu steigen, weil der nicht die Bandbreite liefert, die im Vertrag vereinbart wurde.

## Was wir brauchen

- Linux (vermutlich gehen auch Unix-artige Systeme und WSL, hab ich aber nicht probiert)
- python 3
- cron
- selenium / geckodriver

## Wie wir was bekommen

1. das Repo hier klonen.
2. mit `$ pip3 install selenium` Selenium besorgen
3. mit `$ brew install geckodriver` den Selenium-Treiber für den Firefox besorgen.
4. mit `$ which geckodriver` schauen, wo der hininstalliert wurde
5. gegebenenfalls den Pfad zum Script in fast-csv-helper.py als driver_path anpassen.
6. überlegen, wo die Screenshots und csv-Datei hinsollen, `csv_file`, `data_path` in fast-csv-helper.py anpassen und den Ordner anlegen
5. cronjob einrichten: `5-59/15 * * * * fast-csv-helper.py` in `crontab -e` vermerken
7. das gibt alle Viertelstunde, startend um 5 nach voll, einen Test, der dann in die CSV wandert.

> Wer andere Zeitsettings braucht, [https://crontab.guru/](https://crontab.guru/#5-59/15_*_*_*_*) hat euren Rücken.

## Noch was

Das hier ist analog zu: https://github.com/xenein/cloudflare-speed-csv - nur nicht mit irgendwelchen node-Modulen.

## Uffbasse!

- Messungen am besten (in der Netzwerktopologie) nahe am oder sogar im Router durchführen
- Messungen am besten mit einer Kabelverbindung (wie in LAN-Kabel) durchführen
- Messungen am besten mit einem Gerät durchführen, das mehr Bandbreite als der Internetzugang kann
- Der Spaß hier funktioniert für mich auf meinem macMini mit macOS 11. Andere Geräte habe ich nicht getestet
- Wenn ich mal Zeit und Lust hab, schaue ich, dass Fehlerbehandlung - sowas wie "hm grade gar kein Internet da" ordentlich behandelt wird

# How to: statistics on your internet connection speed. Automated. In CSV.

Let's use some python and selenium together with cron to create csv-data on broadband connection speed over time. May come in handy if you want to get into a fight with your ISP.

## What you need:

- macOS (most likely Unix, Linux or windows with WSL are fine - but untested)
- python 3
- cron
- selenium  + geckodriver

##  how do you turn this on

1. clone this repo
2. check in fast-csv-helper.py if `driver_path`, `data_path` and `csv_file` are correct for you.
3. check that `data_path` exists and is writable for you.
4. setup cronjob (I recommend absolute paths here.) : Add `5-59/15 * * * * fast-csv-helper.py` in `crontab -e`
5. Now you should get a new line in the csv every 15 minutes, starting at 5. (see [https://crontag.guru](https://crontab.guru/#5-59/15_*_*_*_*) for reference if you need something else)


## Here be dragons!

- Try measuring as near to the router/moden as possible
- Best results measuring with a wired connection
- Have enough bandwidth on the measuring device (e.g. don't expect good results measuering a 400 / 25 VDSL2 connection via Fast Ethernet)
- I put this together on macOS11. It may or may not work on other devices.
