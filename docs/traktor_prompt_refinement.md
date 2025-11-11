# Traktor Audio-Migration Prompt Refinements

This document captures refined prompt variants tailored for orchestrating a network-wide Traktor audio library migration via macOS. Each variant offers a distinct tone and workflow emphasis while preserving clear instructions for ChatGPT.

## Variante A – Technisch fokussiert und prozessorientiert
```
Du agierst als erfahrener macOS-Terminal- und Netzwerkadministrator. Ziel: Erstelle einen belastbaren Workflow, um sämtliche Audiodateien in meinem Heim-/Firmennetzwerk auf eine externe Festplatte zu verschieben, ohne meine Traktor-Playlisten zu beschädigen. Bitte berücksichtige:

1. Umgebung  
   - macOS Terminal mit Zugriff auf Netzwerkfreigaben und die externe Festplatte (gemountet unter `/Volumes/ExterneMusik`).  
   - Traktor-Software mit bestehender Sammlung und Playlisten.

2. Aufgabenabfolge  
   a) Finde alle Audiodateien (inkl. Unterordner) im Netzwerk und schreibe alle Pfade gesammelt in die Datei `aalleaudio.txt` als verbindliche Ausgangsbasis.  
   b) Verschiebe sie in einen Zielordner `Traktor_Migration` auf der externen Festplatte.  
   c) Führe eine Duplikat-Prüfung durch (z. B. nach Dateiname, Hash oder Metadaten) und filtere redundante Dateien heraus.  
   d) Mische und bereinige Tags/Metadaten so, dass nur qualitativ hochwertige Einträge verbleiben.  
   e) Sorge dafür, dass Traktor-Playlisten weiterhin funktionieren (Pfadaktualisierung, Relinks).  
   f) Dokumentiere, wie Apple Music die Bibliothek anschließend wieder korrekt einliest.

3. Ausgabeformat  
   - Liefere nummerierte Schritte mit konkreten Terminalbefehlen, Erklärungen und möglichen Alternativen (z. B. `rsync`, `find`, `ffprobe`, Skripte).  
   - Weisen auf Vorsichtsmaßnahmen hin (Backups, Testlauf, Rechteverwaltung).  
   - Markiere Stellen, an denen manuelle Prüfungen sinnvoll sind.

Gehe Schritt für Schritt vor und begründe deine Empfehlungen kurz, damit ich sie direkt nachvollziehen und anwenden kann.
```

## Variante B – Strategisch, mit Fokus auf Datenintegrität
```
Ich benötige einen strukturierten Plan, um alle Audiodateien aus meinem Netzwerkbestand (macOS-Umgebung) auf eine externe Festplatte zu übertragen und gleichzeitig Traktor-Playlisten sowie Apple-Music-Integration zu erhalten. Bitte liefere:

- Eine Übersicht der notwendigen Vorbereitungen (Backups, Überprüfung der Netzwerkmounts, Festplattenformat).
- Einen detailreichen Ablauf in logisch nummerierten Schritten:
  1. Audiodateien im Netzwerk lokalisieren und sämtliche gefundenen Pfade in `aalleaudio.txt` sichern (diese Datei dient als verbindliches Arbeitsverzeichnis).  
  2. Kopieren/Verschieben auf die externe Festplatte (`/Volumes/ExterneMusik/Traktor_Migration`).  
  3. Duplikate erkennen und eliminieren; definieren, wann eine Datei als Duplikat gilt (z. B. Hash, BPM, Länge).  
  4. Tags/Metadaten konsolidieren; Konflikte dokumentieren.  
  5. Traktor-Bibliothek aktualisieren (Pfad-Anpassungen, Collection.nml prüfen, ggf. Relocate).  
  6. Hinweise, wie Apple Music anschließend die Bibliothek reimportiert oder referenziert.

- Für jeden Schritt die passenden Tools oder Befehle (z. B. `find`, `mdfind`, `rsync`, Skripte, Dritttools) samt kurzer Erläuterung. 
- Einen Abschnitt „Qualitätssicherung & Tests“ mit empfohlenen Prüfungen, um Datenverlust und Playlistenfehler zu vermeiden.

Bitte liefere die Antwort in gut gegliederten Abschnitten mit Überschriften, sodass ich direkt danach arbeiten kann.
```

## Variante C – Kreativ-pragmatisch, mit Automatisierungsvorschlägen
```
Du bist mein technischer Assistent für macOS mit Fokus auf Audio-Workflows. Hilf mir, alle Audiodateien aus meinem Netzwerk auf eine externe Festplatte zu migrieren und dabei Traktor- und Apple-Music-Kompatibilität sicherzustellen. Struktur der Antwort:

1. Kurzüberblick  
   - Projektziel und potenzielle Stolperfallen (z. B. verlorene Playlisten, widersprüchliche Tags, Duplikate).

2. Skript-/Automatisierungsentwurf  
   - Schlage ein Bash- oder Python-Skript vor, das folgende Aufgaben automatisiert:  
     • Suche alle Audioformate, schreibe jede gefundene Datei zunächst nach `aalleaudio.txt` (als verbindliches Inventar) und kopiere/move sie anschließend.  
     • Duplikat-Check (mit Hash oder `ffprobe` + Metadatenabgleich).  
     • Konsolidierung von Tags; Prioritäten bei Konflikten nennen.  
     • Protokollierung (Logdatei) der verschobenen, übersprungenen und zusammengeführten Dateien.  

3. Integration in Traktor und Apple Music  
   - Beschreibe, wie das Skript bzw. der Prozess sicherstellt, dass Traktor-Playlisten unverändert funktionieren (z. B. relative Pfade, `Collection.nml`-Pfadupdate).  
   - Erläutere, wie Apple Music nach der Migration die Bibliothek wiederfindet (Reimport, Watch-Folder, Duplikatschutz).

4. Ergebnispräsentation  
   - Gib den finalen Befehl oder das Skript (ggf. als Codeblock) plus eine kurze Anleitung zum Ausführen.  
   - Ergänze Checkliste für Nachkontrollen und Backups.

Bitte antworte in einem lebendigen, motivierenden Ton, damit der Prozess trotz Komplexität gut nachvollziehbar bleibt.
```

## Anwendung und Möglichkeiten
- **Einsatz**: Wähle die Variante, die am besten zu deinem Stil passt (technisch, strategisch oder kreativ). Kopiere den jeweiligen Markdown-Block direkt in ChatGPT, um eine maßgeschneiderte Antwort zu erhalten und nutze `aalleaudio.txt` als zentrale Referenz für alle folgenden Schritte.
- **Anpassung**: Ergänze bei Bedarf konkrete Pfade, Dateiformate oder Tool-Präferenzen (inkl. Speicherort von `aalleaudio.txt`), damit ChatGPT noch präzisere Anweisungen liefert.
- **Variationen**: Wechsle zwischen den Varianten, um alternative Lösungsansätze (z. B. stärker skriptbasiert vs. prozessorientiert) zu explorieren. Du kannst die Varianten auch kombinieren, indem du Abschnitte zusammenführst.
- **Validierung**: Bitte ChatGPT nach Ausführung des Workflows um eine Zusammenfassung der Schritte oder um zusätzliche Tests (z. B. Stichproben in Traktor), um die Ergebnisse zu überprüfen.
- **Erweiterung**: Falls du mehrere Systeme oder zusätzliche DJ-Software einbeziehst, erweitere die Prompts um entsprechende Hinweise, damit alle relevanten Tools berücksichtigt werden.

## Praxis: Audio-Inventar erzeugen
Um die Prompts unmittelbar anwenden zu können, steht dir jetzt das ausführbare Hilfsskript `scripts/collect_audio_paths.py` zur Verfügung. Es durchsucht beliebige Verzeichnisse nach gängigen Audioformaten und erstellt daraus die Datei `aalleaudio.txt`, die in jeder Variante als Ausgangsbasis dient.

### Beispielaufrufe

```bash
# Alle Netzwerk-Freigaben scannen und absolute Pfade erfassen
python scripts/collect_audio_paths.py /Volumes/NetzwerkMusik ~/Music/Traktor

# Pfade relativ zur externen Festplatte schreiben und Symlinks folgen
python scripts/collect_audio_paths.py /Volumes/NetzwerkMusik \
    --relative-to /Volumes/ExterneMusik \
    --follow-symlinks \
    --output /Volumes/ExterneMusik/Traktor_Migration/aalleaudio.txt

# Nur spezifische Formate aufnehmen und zuerst testen, ohne eine Datei anzulegen
python scripts/collect_audio_paths.py /Volumes/NetzwerkMusik \
    --extensions mp3,flac,wav \
    --dry-run
```

Das Skript meldet, wie viele Dateien gefunden wurden, und überschreibt standardmäßig bestehende Inventar-Dateien. Sichere vorhandene Versionen also zuvor oder nutze unterschiedliche Ausgabepfade, wenn du mehrere Varianten vergleichen möchtest.
