# Audio Filename Cleaning Plan (Variant A Response)

## Zielsetzung
- Audio-Dateinamen automatisiert bereinigen, damit ausschließlich der Kern „Interpret – Titel“ (oder nur der Titel) übrig bleibt.
- Entferne systematisch Tonarten, Track-IDs, laufende Nummerierungen, Mix-/Remix-Zusätze, Datumsstempel und kryptische Artefakte.

## Beispielhafte Transformationen
| Ursprünglicher Dateiname | Erwartetes Ergebnis |
| --- | --- |
| `01_TrackID123-ArtistName_-_SongTitle_(Key_C#m).mp3` | `ArtistName – Song Title` |
| `Artist - Song Name [Live 2019] #45.flac` | `Artist – Song Name` |
| `AnotherArtist__Track99__Key-Gm (Extended Mix).wav` | `AnotherArtist – Track` |
| `05 RandomChars123 ArtistName - Hit_Title (Original Mix).wav` | `ArtistName – Hit Title` |

## Schritt-für-Schritt-Vorgehen
1. **Vorverarbeitung**
   - Entferne die Dateiendung (`.[^.]+$`).
   - Normalisiere Trennzeichen: ersetze Sequenzen aus `_`, `__`, `-` und mehreren Leerzeichen durch ein Leerzeichen.
   - Kürze führende/abschließende Trennzeichen (Leerzeichen, Bindestriche, Unterstriche).

2. **Segmentierung**
   - Teile den String an Bindestrichen, Unterstrichen oder Klammern, um potenzielle Metadatenfragmente gezielt zu entfernen.
   - Halte die ursprüngliche Reihenfolge fest, damit relevante Teile bei der Rekonstruktion wieder korrekt angeordnet werden können.

3. **Entfernung unerwünschter Muster**
   - Track-Nummern & IDs: `^\s*\d{1,3}\b`, `\bTrack(ID)?\s*\d+\b`, `#[0-9]+`.
   - Tonarten: `\bKey[:\s-]*[A-G](#|b)?m?\b`, `\((Key|Tonart)[:\s-]*[A-G](#|b)?m?\)`.
   - Mix-/Remix-Zusätze: `(?i)(Original|Extended|Club|Radio|Live|Festival|Demo)\s*(Mix|Edit|Version)`, `(?i)(Remix|Rework|Bootleg)`.
   - Datumsangaben: `\b(19|20)\d{2}\b`, `\b\d{1,2}[./-]\d{1,2}[./-](19|20)\d{2}\b`.
   - Kryptische Artefakte: Sequenzen aus Unterstrichen, zufällige alphanumerische Blöcke (`[A-Za-z]*\d{2,}[A-Za-z]*`).

4. **Nachbereitung & Formatierung**
   - Entferne übrig gebliebene Klammern oder Sonderzeichen.
   - Fasse Segmente wieder zu einem String zusammen, reduziere doppelte Leerzeichen.
   - Ersetze einfache Bindestriche zwischen Interpret und Titel durch einen Gedankenstrich „ – “.

5. **Heuristiken zur Interpreten-/Titel-Erkennung**
   - Wenn ein Bindestrich vorhanden ist, behandle das linke Segment als Interpret, das rechte als Titel (nach Trimmen).
   - Enthalten Segmente Keywords wie `feat.` oder `vs.`, bleiben sie Teil des Interpretsegments.
   - Für Single-Word-Künstler (z. B. „Prince“) kann eine Whitelist helfen, Fehlklassifikationen zu verhindern.
   - Liegt kein Interpretenhinweis vor, gib nur den bereinigten Titel zurück.

## Regex- und Operationstabellen
| Schritt | Regex / Operation | Zweck |
| --- | --- | --- |
| Dateiendung | `re.compile(r"\.[^.]+$")` | Entfernt Dateiendung. |
| Unterstriche | `re.compile(r"[_]+")` | Ersetzt Unterstriche durch Leerzeichen. |
| Track-ID | `re.compile(r"\bTrack(ID)?\s*\d+\b", re.I)` | Entfernt Track-IDs. |
| Führende Nummer | `re.compile(r"^\s*\d{1,3}\s*-?")` | Entfernt Tracknummern am Beginn. |
| Tonart | `re.compile(r"\bKey[:\s-]*[A-G](#|b)?m?\b", re.I)` | Entfernt Tonartangaben. |
| Mix-/Remix-Klammern | `re.compile(r"\(([^)]*(Mix|Edit|Version|Remix)[^)]*)\)", re.I)` | Entfernt Mixinformationen in Klammern. |
| Jahreszahl | `re.compile(r"\b(19|20)\d{2}\b")` | Entfernt Datumsangaben. |
| Hashtag-Zählung | `re.compile(r"#[0-9]+")` | Entfernt Trackzählungen. |

## Pseudocode (Python)
```python
import re

CLEAN_STEPS = [
    (re.compile(r"\.[^.]+$"), ""),
    (re.compile(r"[_]+"), " "),
    (re.compile(r"\s{2,}"), " "),
    (re.compile(r"^\s*\d{1,3}\s*-?"), ""),
    (re.compile(r"\bTrack(ID)?\s*\d+\b", re.I), ""),
    (re.compile(r"#[0-9]+"), ""),
    (re.compile(r"\bKey[:\s-]*[A-G](#|b)?m?\b", re.I), ""),
    (re.compile(r"\(([^)]*(Mix|Edit|Version|Remix|Bootleg)[^)]*)\)", re.I), ""),
    (re.compile(r"\b(19|20)\d{2}\b"), ""),
]

TRIM_EDGES = re.compile(r"^[\s\-_]+|[\s\-_]+$")


def clean_filename(name: str) -> str:
    base = name.strip()
    for pattern, replacement in CLEAN_STEPS:
        base = pattern.sub(replacement, base)
    base = re.sub(r"\s{2,}", " ", base)
    base = TRIM_EDGES.sub("", base)

    if " - " in base:
        artist, title = [segment.strip() for segment in base.split(" - ", 1)]
        if not artist:
            return title
        return f"{artist} – {title}"

    return base
```

## Validierung & Tests
- Erstelle Unit-Tests oder Assertions mit repräsentativen Beispielen (siehe Tabelle oben).
- Ergänze Negativtests (z. B. bereits saubere Titel, Songs ohne Interpret), um Überbereinigung zu vermeiden.
- Prüfe, dass keine doppelten Leerzeichen, führende/trailende Trennzeichen oder nicht entfernte Metadaten verbleiben.

## Erweiterungsmöglichkeiten
- Aufbau einer Liste bekannter Interpreten zur besseren Segmentierung.
- Optionaler Sprachfilter für zusätzliche Begriffe (z. B. „Live“, „Acoustic“, „Remastered“).
- Integration in ein Skript, das Dateisystem-Operationen (Umbenennen) sicher durchführt, inklusive Dry-Run-Modus.
