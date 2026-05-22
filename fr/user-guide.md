# NVH Source Locator — Guide de l'utilisateur

NVH Source Locator est un outil de mesure pour localiser les sources de bruit et de vibration en utilisant le TDOA (Time Difference of Arrival) à partir des signaux d'accéléromètres capturés sur un oscilloscope ou un système de mesure.

Ce guide couvre toutes les fonctionnalités. Pour un rappel rapide, consultez **Référence Rapide**.

---

## Table des matières

1. [Comment ça fonctionne](#how-it-works)
2. [Avant de commencer](#before-you-start)
3. [Les onglets principaux](#the-main-tabs)
4. [Mode 2-Sensor](#2-sensor-mode)
5. [Mode 3-Sensor](#3-sensor-mode)
6. [Modes Pro+ (3-Sen+, 4-Sensor, 4-Sen+, 3D, 3D+)](#pro-modes)
7. [L'onglet Materials](#the-materials-tab)
8. [Compensation de température](#temperature-compensation)
9. [Annotation de photo](#photo-annotation)
10. [Rapports](#reports)
11. [Sauvegarde et restauration](#backup-and-restore)
12. [Paramètres](#settings)
13. [Fonctionnalités Pro](#pro-features)
14. [Onglet Help et tutoriels](#help-tab-and-tutorials)
15. [Dépannage](#troubleshooting)

---

## Comment ça fonctionne {#how-it-works}

Lorsqu'une source de bruit émet un son ou une vibration, l'onde se propage à travers le matériau à une vitesse connue. Si vous placez deux ou plusieurs accéléromètres sur le matériau et mesurez le moment où l'onde arrive à chacun, la différence de temps vous indique où se trouve la source.

NVH Source Locator prend :

- **Calibration** : la distance entre les capteurs et le temps qu'il faut à une onde pour parcourir cette distance (utilisé pour calculer la vitesse du son du matériau)
- **Événement** : la différence de temps entre les capteurs détectant l'événement de bruit/vibration

Puis il calcule où se trouve la source dans la structure.

Plus vous utilisez de capteurs, plus précisément vous pouvez localiser la source :

- **2 capteurs** → distance le long d'une ligne
- **3 capteurs** → position sur une surface 2D (X, Y)
- **4 capteurs** → position dans l'espace 3D (X, Y, Z)

---

## Avant de commencer {#before-you-start}

Vous aurez besoin de :

- **Un oscilloscope ou système de mesure** qui peut vous montrer la différence de temps entre les canaux d'accéléromètre en microsecondes (µs)
- **Au moins 2 accéléromètres** physiquement attachés à la structure (plus de capteurs = plus de précision)
- **Un moyen de mesurer la distance** entre les capteurs (mètre, pieds à coulisse)
- **Un moyen de déclencher une onde** à un endroit connu pour la calibration (impact de marteau calibré, frappe de tournevis ou autre signal connu)

![Écran d'accueil avec onglet 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Les onglets principaux {#the-main-tabs}

L'application a des onglets en haut :

![Barre d'onglets](../screenshots/02-tab-bar.png)

| Onglet | Ce qu'il fait | Quand l'utiliser |
|---|---|---|
| **2-Sensor** | Localisation de source 1D le long d'une ligne entre 2 capteurs | Vérifications rapides, structures de type poutre. **Entièrement gratuit.** |
| **3-Sensor** | Localisation de source 2D à l'aide de 3 capteurs dans un triangle | Utilisation la plus générale, panneaux et surfaces |
| **3-Sen+** | 3-Sensor avec solveur des moindres carrés surdéterminé | Mesures plus exigeantes, robuste au bruit |
| **4-Sensor** | Localisation 2D à l'aide de deux paires (A-B + C-D) | Disposition rectangulaire des capteurs, vérification croisée |
| **4-Sen+** | Mode 2D avancé, 4 capteurs à n'importe quelle position | Géométries non rectangulaires, LSQ complet |
| **3D** | Localisation de source 3D à l'aide de 4 capteurs avec coordonnées XYZ | Structures complexes dans l'espace 3D |
| **3D+** | 3D avec jusqu'à 6 capteurs, LSQ surdéterminé | Géométries très complexes, précision maximale |
| **Materials** | Bibliothèque de vitesse du son + matériaux personnalisés | Choisir une fois par session de mesure |
| **Help** | Tutoriels intégrés et référence | Quand vous avez besoin d'un rappel rapide |

> **Gratuit vs Pro** : L'onglet 2-Sensor est entièrement gratuit. Les autres onglets sont accessibles mais ont des champs de saisie spécifiques verrouillés pour les utilisateurs Pro (marqués d'un badge cadenas doré). Toucher un champ verrouillé affiche la paywall Pro.

Les paramètres sont accessibles via l'icône d'engrenage ⚙ dans le coin supérieur droit (pas un onglet).

---

## Mode 2-Sensor {#2-sensor-mode}

La mesure la plus simple : localisation de source le long d'une ligne entre deux accéléromètres.

![Onglet 2-Sensor](../screenshots/01-home-2sensor.png)

### Étape 1 : Appliquer un matériau

Touchez l'onglet Materials. Choisissez le matériau dont est composée votre structure (par exemple, « Aluminium », « Acier, Mild (1020) »). L'application utilise la vitesse du son connue du matériau pour remplir automatiquement le champ de temps de calibration.

Si le matériau de votre structure n'est pas dans la liste, vous pouvez choisir « Air » temporairement et remplacer le temps de calibration manuellement à l'étape 2.

### Étape 2 : Saisir les données de calibration

Sur l'onglet 2-Sensor, vous verrez deux sections de paires : **Paire A–B** et **Paire A–C** (seul A–B est requis si vous n'avez que 2 capteurs).

Pour chaque paire, vous remplissez :

- **Espacement des capteurs** (`d`) : distance physique entre les capteurs, en cm ou pouces (défini dans les Paramètres)
- **Délai de temps de calibration** (`tCal`) : temps pour qu'une onde voyage entre les capteurs à la vitesse du son du matériau — rempli automatiquement quand vous choisissez un matériau, mais vous pouvez le remplacer

### Étape 3 : Saisir le temps de l'événement

- **Délai de temps de l'événement** (`tEvent`) : différence de temps entre les capteurs détectant l'événement de bruit, en microsecondes
- **Premier capteur** : quel capteur a entendu l'événement en premier (A ou B)

### Étape 4 : Lire le résultat

L'application affiche la position de la source comme une distance depuis le capteur A :
- Résultat = 0 : la source est au capteur A
- Résultat = distance : la source est au capteur B
- Résultat intermédiaire : la source est entre eux
- Résultat à l'extérieur : la source est au-delà d'un des capteurs (le toast avertira)

La carte de résultats affiche les deux distances (depuis A, depuis B) et indique quel capteur est plus proche.

### Étape 5 (optionnelle) : Annoter une photo

Touchez **📷 Annoter une photo** pour prendre une photo de votre configuration. L'application superpose des marqueurs pour les capteurs A, B et la source. Utile pour les rapports.

---

## Mode 3-Sensor {#3-sensor-mode}

Localise une source sur un plan 2D à l'aide de trois capteurs disposés en triangle.

![Onglet 3-Sensor](../screenshots/03-3sensor-tab.png)

### Configuration

Placez trois capteurs sur votre structure formant un triangle. Équilatéral, rectangle ou scalène — l'application gère toutes les géométries.

### Saisir les données

Dans la section **Longueurs des côtés du triangle**, saisissez la distance physique pour les trois côtés (A–B, A–C, B–C).

Pour chaque paire (A–B et A–C), saisissez :
- **tCal** : temps de calibration (rempli automatiquement depuis le matériau)
- **tEvent** : différence de temps mesurée pour l'événement de bruit
- **Premier capteur** : lequel l'a entendu en premier

### Lire le résultat

L'application affiche la position de la source comme coordonnées X, Y relatives au capteur A (capteur A à l'origine, capteur B sur l'axe X). La visualisation montre les trois capteurs et l'emplacement de la source.

![Résultat triangle](../screenshots/04-triangle-result.png)

---

## Modes Pro+ {#pro-modes}

Plusieurs onglets avancés offrent des solveurs surdéterminés et une dimensionnalité supérieure :

### 3-Sen+ (Pro)

Même configuration triangulaire que 3-Sensor, mais calibrez ET mesurez les trois paires (A–B, A–C, B–C). Le solveur utilise les 3 TDOAs dans un ajustement par moindres carrés — plus robuste au bruit de mesure et aux matériaux anisotropes. Les résidus par paire sont rapportés pour que vous puissiez repérer les mesures incohérentes.

### 4-Sensor

Placez quatre capteurs autour de la zone :
- **A–B** = paire horizontale (côtés gauche/droite)
- **C–D** = paire verticale (côtés haut/bas)

Exécutez d'abord la paire A–B (horizontale), puis la paire C–D (verticale). La carte 2D montre l'intersection. Chaque paire est calibrée séparément — utile lorsque le matériau varie à travers la structure.

### 4-Sen+ (2D avancé)

Quatre capteurs à n'importe quelle position (pas forcés rectangulaires). Appariez A avec chacun de B, C, D et calibrez séparément. Le solveur des moindres carrés surdéterminé moyenne le bruit de mesure par paire et rapporte les résidus par paire.

### 3D

Mesure 3D complète avec 4 capteurs placés dans l'espace 3D. Saisissez les coordonnées (X, Y, Z) de chaque capteur, plus les temps de calibration et d'événement pour chaque paire (A–B, A–C, A–D).

### 3D+ (Pro)

Comme 3D mais prend en charge jusqu'à **6 capteurs** (A à F) avec LSQ surdéterminé. Précision maximale pour les géométries 3D complexes.

---

## L'onglet Materials {#the-materials-tab}

Bibliothèque de matériaux d'ingénierie courants avec vitesse du son connue à 20 °C.

![Onglet Materials](../screenshots/05-materials-tab.png)

### Liste des matériaux

La liste comprend l'air, les fluides, les caoutchoucs, les polymères, les bois, les verres et les métaux. Les vitesses vont de ~340 m/s (air) à ~13 000 m/s (certains métaux à température ambiante).

### Matériaux intégrés avec compensation de température

14 métaux couramment utilisés incluent des données de coefficient de température. Lorsque la Température de référence dans les Paramètres diffère de 20 °C, l'application ajuste automatiquement les vitesses de ces matériaux :

- Aluminium
- Acier, Mild (1020)
- Acier Inoxydable (304)
- Fer (fonte)
- Fer
- Cuivre
- Laiton
- Bronze
- Titane
- Magnésium
- Plomb
- Zinc
- Nickel
- Tungstène

Les matériaux avec compensation affichent deux valeurs dans le sélecteur : la **vitesse compensée** (grande, importante) et la **vitesse de référence à 20 °C** (petite, grise en dessous).

Les matériaux sans compensation affichent **« ref only »** en italique — leur vitesse listée est utilisée telle quelle indépendamment de la température.

### Matériaux personnalisés

Si vous mesurez une calibration sur l'onglet 2-Sensor, vous pouvez enregistrer le résultat en tant que matériau personnalisé. Après une mesure 2-sensor réussie, recherchez l'option d'enregistrer la vitesse dérivée sous un nom de votre choix.

Les matériaux personnalisés stockent la vitesse mesurée in-situ ; ils n'appliquent jamais de compensation de température (la vitesse a déjà été mesurée à la température de test).

### Favoris

Touchez l'étoile à côté de tout matériau pour le marquer comme favori. Les favoris apparaissent en haut de la liste pour un accès rapide.

### Recherche

Utilisez la barre de recherche en haut pour filtrer les matériaux par nom. La recherche correspond à la fois aux noms canoniques anglais et aux noms d'affichage traduits.

---

## Compensation de température {#temperature-compensation}

La vitesse du son dans les matériaux change avec la température. Dans les tests NVH automobiles, cela compte : un compartiment moteur à 80 °C, une cabine refroidie à -10 °C ou une zone du collecteur d'échappement à 200 °C se comportent tous différemment des conditions de laboratoire à température ambiante.

### Réglage de la température

Ouvrez Paramètres (icône ⚙) → Température de référence. Saisissez la température de votre environnement de test en °C (plage -40 à +200).

![Panneau Paramètres](../screenshots/06-settings.png)

### Que se passe-t-il lorsque la température ≠ 20 °C

- Les champs de temps de calibration se remplissent automatiquement avec la vitesse ajustée à la température
- Le sélecteur de Materials affiche la vitesse ajustée de manière importante
- Un toast confirme : *« Aluminium appliqué (6 284 m/s @ 60 °C) — N paire(s) mise(s) à jour »*
- L'indice « Matériau le plus proche » compare avec les vitesses ajustées à la température
- Les entrées d'historique enregistrées enregistrent la température active
- Les rapports incluent une ligne de pied de page : *« Température de référence : 60 °C, compensation appliquée »*

### Réinitialisation au lancement de l'application

La Température de référence **se réinitialise toujours à 20 °C** quand vous lancez l'application. Cela empêche les paramètres obsolètes d'une session de mesure passée d'affecter silencieusement le travail d'aujourd'hui. Une petite note en italique dans les Paramètres vous rappelle ce comportement.

Si vous voulez rejouer une mesure historique à sa température d'origine, touchez simplement l'entrée — la température est restaurée automatiquement.

### Matériaux sans compensation

La plupart des matériaux non métalliques n'ont pas de coefficients de température publiés fiables. L'application affiche un badge **« ref only »** pour ceux-ci — leur vitesse listée est utilisée indépendamment du réglage de la température. Si vous avez besoin de mesures précises à des températures non ambiantes pour ces matériaux, effectuez une calibration in-situ et enregistrez le résultat en tant que matériau personnalisé.

---

## Annotation de photo {#photo-annotation}

Après un calcul réussi, touchez le bouton **📷 Annoter une photo** pour superposer des marqueurs de capteur et de source sur une photo de votre configuration.

![Annotation de photo](../screenshots/08-photo-annotation.png)

### Flux

1. Touchez **Annoter une photo** — la caméra système s'ouvre
2. Prenez une photo de votre placement de capteur
3. L'application charge la photo dans la superposition d'annotation
4. Les marqueurs de capteur (A, B, C, D, E, F selon le cas — jusqu'à 6 capteurs) et le marqueur de source se placent automatiquement en fonction de votre calcul
5. Faites glisser tout marqueur pour affiner la position. Au fur et à mesure que vous ajustez, la position de la source est recalculée à partir des positions de capteur corrigées
6. Touchez **Enregistrer** pour conserver, ou **Reprendre** pour réessayer

La photo annotée est incluse automatiquement dans les rapports PDF.

---

## Rapports {#reports}

Touchez le bouton **Imprimer le résultat** sur n'importe quel écran de résultats pour générer un rapport formaté.

![Rapport PDF](../screenshots/09-pdf-report.png)

### Contenu du rapport

- En-tête (personnalisable dans Paramètres → En-tête de rapport)
- Titre de la mesure et horodatage
- Toutes les valeurs d'entrée dans un tableau propre
- Résultat du calcul
- Texte de conclusion
- Visualisation (graphique de géométrie)
- Photo annotée (si vous en avez pris une)
- Ligne de pied de page de température (si la compensation était active)
- Numéro de page et ligne de crédit

### Format de sortie

- **Android** : génération PDF native, enregistrer sur votre téléphone ou partager
- **iOS** : boîte de dialogue d'impression système → enregistrer en PDF, AirPrint ou partager

### Personnalisation de l'en-tête

Paramètres → En-tête de rapport. Saisissez votre nom d'entreprise, nom de laboratoire, informations sur le projet ou ce que vous voulez en haut de chaque rapport.

---

## Sauvegarde et restauration {#backup-and-restore}

Enregistrez tous vos matériaux personnalisés, favoris, paramètres et historique dans un seul fichier. Transférer entre appareils.

### Sauvegarde

Paramètres → **Sauvegarde** → touchez « Enregistrer le fichier de sauvegarde ». L'application génère un fichier JSON et ouvre la feuille de partage de votre téléphone. Enregistrez-le dans votre lecteur cloud (Google Drive, iCloud, OneDrive), envoyez-le par e-mail à vous-même ou transférez-le de la manière que vous souhaitez.

### Restauration

Paramètres → **Restauration** → choisissez le fichier de sauvegarde dans le stockage de votre téléphone. L'application importe les matériaux personnalisés, les favoris, l'historique et les paramètres.

⚠️ **La restauration remplace vos données actuelles.** Si vous avez des mesures importantes sur l'appareil actuel, sauvegardez-les d'abord avant de restaurer depuis une autre sauvegarde.

---

## Paramètres {#settings}

Accès via l'icône d'engrenage ⚙ dans le coin supérieur droit. Les paramètres sont une fenêtre modale, pas un onglet.

![Paramètres](../screenshots/06-settings.png)

| Paramètre | Ce qu'il contrôle |
|---|---|
| **Passer à Pro** | Acheter ou en savoir plus sur les fonctionnalités Pro (19,99 $) |
| **Langue** | Langue d'affichage de l'application (30 prises en charge) |
| **Thème** | Clair, Sombre ou Auto (suivre le système) |
| **Unité de distance** | cm ou pouces |
| **Température de référence** | Température active pour la compensation, -40 à +200 °C |
| **En-tête de rapport** | Texte personnalisé en haut des rapports générés |
| **Sauvegarde** | Exporter toutes les données vers un fichier |
| **Restauration** | Importer des données depuis un fichier de sauvegarde |
| **Restaurer l'achat** | Ré-acquérir Pro sur un nouvel appareil |

---

## Fonctionnalités Pro {#pro-features}

NVH Source Locator utilise un **modèle freemium avec verrouillage par fonctionnalité** :

- **Gratuit** : L'onglet 2-Sensor est entièrement fonctionnel sans limites
- **Pro** : Tous les autres onglets ont des champs de saisie spécifiques verrouillés. La paywall apparaît quand un utilisateur gratuit touche un champ verrouillé

### Ce qui est verrouillé

Les champs requérant Pro sont répartis sur :
- 3-Sensor, 3-Sen+, 4-Sensor, 4-Sen+
- Modes 3D et 3D+
- Sauvegarde et Restauration
- Rapports PDF
- Matériaux personnalisés
- Annotation de photo

Un utilisateur gratuit peut OUVRIR n'importe quel onglet et VOIR l'interface. Il ne peut simplement pas saisir de valeurs dans les champs de saisie verrouillés par Pro.

![Champ verrouillé par Pro](../screenshots/11-pro-locked-field.png)

### La paywall

![Paywall](../screenshots/07-paywall.png)

Quand un utilisateur gratuit touche un champ verrouillé, la paywall glisse en montrant :
- Icône de l'application avec badge PRO
- Liste de fonctionnalités
- Bouton de déverrouillage avec prix (19,99 $ par défaut ; peut varier selon la région)
- Échange de code promotionnel (Android uniquement — iOS utilise le flux d'Offer Code séparé d'Apple)
- Lien promotionnel optionnel vers les canaux communautaires

### Acheter Pro

Touchez n'importe quel champ verrouillé, ou touchez **Passer à Pro** dans les Paramètres. Utilise le système de paiement officiel de votre plateforme (Google Play sur Android, Apple App Store sur iOS).

### Restaurer Pro sur un nouvel appareil

Si vous avez acheté sur un appareil et voulez Pro sur un autre (même compte) :

1. Connectez-vous au **même** compte Google (Android) ou Apple ID (iOS) que vous avez utilisé pour acheter
2. Ouvrez NVH Source Locator sur le nouvel appareil
3. Allez à Paramètres → **Restaurer l'achat**
4. L'application vérifie avec les enregistrements d'achat de la plateforme et déverrouille Pro

### Auto-restauration au lancement

Si vous échangez un code promotionnel dans le Google Play Store ou l'App Store pendant que NVH Source Locator s'exécute en arrière-plan, le retour à l'application détecte automatiquement le nouvel achat et déverrouille Pro — pas besoin de Restauration manuelle.

### Échange de code promotionnel

**Android** : un bouton « Avez-vous un code promotionnel Google Play ? » dans la paywall ouvre le flux d'échange de Google Play avec votre code pré-rempli.

**iOS** : La politique de l'App Store 3.1.1 exige l'échange via le flux officiel « Échanger un code » d'Apple. Le bouton Google Play est masqué sur iOS. Cherchez « Échanger un code App Store » dans les Paramètres à la place.

---

## Onglet Help et tutoriels {#help-tab-and-tutorials}

L'onglet **Help** inclut des tutoriels intégrés, des guides de meilleures pratiques et des informations de référence.

![Onglet Help](../screenshots/10-help-tab.png)

Sujets couverts :
- Quel équipement vous avez besoin
- Comment placer les capteurs pour la meilleure précision
- Conseils de calibration
- Scénarios de mesure courants
- Conseils pour la triangulation et les placements 3D
- Cheminement des câbles et qualité du signal

---

## Dépannage {#troubleshooting}

### Le résultat du calcul est faux ou n'a aucun sens

1. Vérifiez votre calibration. Le `tCal` rempli automatiquement suppose la vitesse publiée du matériau — les matériaux réels varient. La calibration la plus précise est in-situ : touchez un emplacement connu et laissez l'application dériver la vitesse réelle.
2. Vérifiez le paramètre **Premier capteur** — quel capteur a entendu l'événement en premier compte pour les mathématiques.
3. Vérifiez vos mesures de distance. Les erreurs de quelques mm se propagent.

### Le toast dit « Résultat hors plage »

Les mathématiques disent que la source n'est pas entre vos capteurs. Causes possibles :
- La source est en fait à l'extérieur de la ligne/du plan du capteur
- L'une de vos entrées est fausse
- La vitesse de calibration est trop éloignée de la réalité

### L'indice de vitesse de calcul affiche une couleur d'avertissement

La vitesse du son implicite de vos entrées est loin de tout matériau commun (moins de 50 m/s ou plus de 20 000 m/s). Vérifiez vos entrées — probablement une faute de frappe dans tCal ou distance.

### Le sélecteur Materials affiche des vitesses différentes de celles attendues

Vérifiez la Température de référence dans les Paramètres. Si non-20 °C, les vitesses affichées reflètent la compensation de température. L'application affiche « ref X @ 20°C » sous les vitesses compensées pour que vous puissiez vérifier.

### L'entrée d'historique se rejoue avec un résultat différent

Les anciennes entrées d'historique créées avant la version 1.75 de l'application peuvent ne pas avoir stocké la température. Si vous avez pris la mesure à une température non-20 °C, la relecture utilisera le paramètre actuel. Définissez manuellement la température dans les Paramètres avant de rejouer, OU re-mesurez.

### Les marqueurs d'annotation de photo ne sont pas où je m'y attends

Les marqueurs se placent automatiquement en fonction de la géométrie d'entrée. Faites-les glisser pour ajuster. Ajuster les marqueurs met à jour la position de la source dans la superposition photo — mais NE change PAS le résultat de calcul sous-jacent.

### La sauvegarde/restauration échoue

Assurez-vous d'utiliser un fichier de sauvegarde généré par la même version ou une version plus récente de l'application. Les fichiers de sauvegarde plus anciens peuvent manquer des champs de données actuels.

### Restaurer l'achat dit « aucun achat trouvé »

1. Vérifiez que vous êtes connecté au même compte de boutique que vous avez utilisé pour acheter
2. Vérifiez que l'achat n'a pas été remboursé ou n'a pas expiré
3. Essayez de désinstaller et réinstaller l'application (l'achat est lié à votre compte de boutique, pas à l'installation de l'application)
4. Contactez support@evdiag.net si cela persiste

### L'entrée numérique se réinitialise à 0 de manière inattendue

Par conception : quand vous quittez un champ numérique (touchez ailleurs), s'il est vide, négatif ou contient du texte non numérique, il se réinitialise à 0. Empêche les calculs silencieusement cassés à partir d'entrées accidentellement effacées. L'entrée de température est exemptée (elle se limite à -40/+200 à la place).

### Besoin de plus d'aide

Contactez `support@evdiag.net` avec :
- Le modèle et la version OS de votre appareil
- La version de l'application (Paramètres → bas de page)
- Description de ce que vous avez essayé
- Captures d'écran si possible

---

*NVH Source Locator est développé par EVDiag. Visitez https://evdiag.net pour les mises à jour et les ressources.*
