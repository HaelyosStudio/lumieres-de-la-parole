"""Recalcule manifest.json à partir de data/versets.json et project.godot.

Lancé automatiquement par l'action GitHub à chaque modification des versets
(et utilisable à la main : python tools/manifeste.py).
Refuse un fichier de versets invalide, pour ne jamais envoyer d'erreur aux joueurs.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
TAILLE_MAX = 1_000_000

brut = (RACINE / "data" / "versets.json").read_bytes()
erreurs = []
try:
    d = json.loads(brut.decode("utf-8"))
except (UnicodeDecodeError, json.JSONDecodeError) as e:
    sys.exit(f"versets.json n'est pas un JSON valide : {e}")

if len(brut) > TAILLE_MAX:
    erreurs.append(f"fichier trop gros ({len(brut)} octets, maximum {TAILLE_MAX})")
themes = {t.get("id") for t in d.get("themes", []) if isinstance(t, dict)}
versets = d.get("versets")
if not isinstance(versets, list) or not versets:
    erreurs.append("aucun verset")
    versets = []
vus = set()
for i, v in enumerate(versets, 1):
    if not isinstance(v, dict):
        erreurs.append(f"verset n°{i} : ce n'est pas un bloc {{ ... }}")
        continue
    for champ in ("ref", "theme", "texte"):
        if not isinstance(v.get(champ), str) or not v[champ].strip():
            erreurs.append(f"verset n°{i} : champ « {champ} » manquant ou vide")
    if v.get("theme") not in themes:
        erreurs.append(f"{v.get('ref')} : thème inconnu « {v.get('theme')} »")
    if v.get("ref") in vus:
        erreurs.append(f"{v.get('ref')} : présent deux fois")
    vus.add(v.get("ref"))
if erreurs:
    sys.exit("Fichier de versets refusé :\n- " + "\n- ".join(erreurs))

# Version du jeu : fichier VERSION (dépôt public) ou project.godot (dépôt du code).
version = "1.0.0"
if (RACINE / "VERSION").exists():
    version = (RACINE / "VERSION").read_text(encoding="utf-8").strip() or version
elif (RACINE / "project.godot").exists():
    m = re.search(r'^config/version="([^"]+)"', (RACINE / "project.godot").read_text(encoding="utf-8"), re.M)
    version = m.group(1) if m else version
manifeste = {
    "version_app": version,
    "versets_sha256": hashlib.sha256(brut).hexdigest(),
    "nombre_versets": len(versets),
    "traduction": d.get("traduction", ""),
}
# Fichiers de la dernière version (adresse, empreinte, taille), pour la mise à jour automatique du jeu.
# telechargements.json est écrit à chaque publication ; il n'est repris que s'il correspond à la version.
fichier_tl = RACINE / "telechargements.json"
if fichier_tl.exists():
    tl = json.loads(fichier_tl.read_text(encoding="utf-8"))
    if tl.get("version") == version:
        for plateforme in ("windows", "android"):
            e = tl.get(plateforme)
            if isinstance(e, dict) and str(e.get("url", "")).startswith("https://github.com/HaelyosStudio/lumieres-de-la-parole/releases/download/")                     and len(str(e.get("sha256", ""))) == 64 and int(e.get("taille", 0)) > 0:
                manifeste[plateforme] = {"url": e["url"], "sha256": str(e["sha256"]).lower(), "taille": int(e["taille"])}
(RACINE / "manifest.json").write_text(
    json.dumps(manifeste, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
)
print(f"manifest.json : version {manifeste['version_app']}, {len(versets)} versets, "
      f"empreinte {manifeste['versets_sha256'][:12]}…")
