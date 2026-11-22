# Lumières de la Parole

Un jeu calme pour téléphone et ordinateur : de nuit, des lumières montent au-dessus d'un jardin,
et chacune porte une parole d'amour de la Bible. On peut aussi y lire la Bible entière.

## Télécharger le jeu

Page des téléchargements : **[dernière version](https://github.com/HaelyosStudio/lumieres-de-la-parole/releases/latest)**

- **Windows** : télécharger `LumieresDeLaParole.exe` et le lancer (un seul fichier, rien à installer).
  Windows peut afficher « Windows a protégé votre ordinateur » car le jeu n'est pas signé :
  cliquer sur « Informations complémentaires » puis « Exécuter quand même ».
- **Android** : télécharger `LumieresDeLaParole.apk` sur le téléphone et l'ouvrir.
  Android demande d'autoriser l'installation d'applications provenant de cette source (navigateur ou gestionnaire de fichiers).

## Ce qu'on y fait

- **Le jardin** : toucher une lumière pour recevoir un verset ; le garder fait pousser une fleur.
  Les lumières dorées sont rares et donnent une fleur dorée.
- **Lire la Bible** : les 66 livres, chapitre par chapitre. Toucher un verset pour le garder dans son jardin.
- **L'Arbre de vie** raconte la lecture : une branche par livre commencé, une feuille par chapitre lu ;
  il grandit à chaque livre entièrement lu, et chaque livre terminé allume aussi une étoile dans le ciel.
- **Le verset du jour**, **Reconstituer un verset** (les mots sont mélangés), **Mon carnet**.
- **Une fleur = un verset gardé** : 36 variétés à collectionner, réelles ou inventées ; toucher une fleur rouvre son verset.
- **Merveilles du jardin** : 13 merveilles à débloquer (lucioles, colombe, fontaine, arc de l'alliance…).
- **8 décors** pour le jardin (Nuit étoilée, Lac de Galilée, Nuit d'hiver, Désert de Judée, Aurore boréale, Jardin d'Éden…).

Le jeu fonctionne sans Internet. Avec Internet, il reçoit automatiquement les nouveaux versets des lumières
et signale quand une nouvelle version est disponible.

## Textes

Louis Segond 1910, domaine public (texte d'[eBible.org](https://ebible.org/find/details.php?id=fraLSG)).

## Contenu de ce dépôt

Ce dépôt contient uniquement ce qui sert aux joueurs : les fichiers du jeu sont dans les
[versions (Releases)](https://github.com/HaelyosStudio/lumieres-de-la-parole/releases), et les fichiers ci-dessous
servent aux mises à jour automatiques.

```
data/versets.json    Les versets des lumières, lus par le jeu au démarrage
manifest.json        Manifeste : dernière version du jeu + empreinte des versets (recalculé automatiquement)
VERSION              Numéro de la dernière version du jeu
tools/manifeste.py   Vérification des versets et calcul du manifeste (lancé par l'action GitHub)
```

Modifier `data/versets.json` ici (même depuis le site GitHub) : l'action *Manifeste des mises à jour*
vérifie le fichier et met à jour le manifeste ; les jeux reçoivent les nouveaux versets à leur prochain démarrage.
Un fichier invalide est refusé et n'atteint pas les joueurs.

Le code source du jeu (projet Godot) est privé.
