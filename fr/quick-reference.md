# NVH Source Locator — Référence Rapide

Un rappel sur une page. Pour les détails complets, voir `user-guide.md`.

---

## Flux principal (2-Sensor, gratuit)

1. **Choisissez un matériau** — onglet Materials → touchez votre matériau
2. **Entrez la calibration** dans l'onglet 2-Sensor :
   - Espacement des capteurs (`d`)
   - Délai de temps de calibration (`tCal`) — automatiquement rempli depuis le matériau
3. **Entrez l'événement** — `tEvent` et Premier capteur (A ou B)
4. **Lisez le résultat** — distance depuis le capteur A

![Onglet 2-Sensor](../screenshots/01-home-2sensor.png)

---

## Tous les onglets

| Onglet | Sortie | Champs Pro ? |
|---|---|---|
| 2-Sensor | Distance le long d'une ligne | Non (entièrement gratuit) |
| 3-Sensor | X, Y sur une surface | Oui |
| 3-Sen+ | X, Y avec LSQ sur 3 paires | Oui |
| 4-Sensor | X, Y à partir de deux paires (A–B + C–D) | Oui |
| 4-Sen+ | X, Y à partir de 4 capteurs, position libre | Oui |
| 3D | X, Y, Z à partir de 4 capteurs | Oui |
| 3D+ | X, Y, Z à partir de jusqu'à 6 capteurs | Oui |
| Materials | Sélecteur de vitesse du son | Non |
| Help | Tutoriels | Non |

Les paramètres sont accessibles via l'icône ⚙ (en haut à droite), pas un onglet.

---

## Compensation de température

Paramètres → Température de référence, plage **-40 à +200 °C**.

- **14 métaux** ont une compensation intégrée (aluminium, aciers, cuivre, laiton, bronze, titane, magnésium, plomb, zinc, nickel, tungstène, fer, fonte)
- Les matériaux sans compensation affichent **« ref only »**
- **Réinitialisé à 20 °C à chaque lancement** (démarrage par défaut sécurisé)
- Rejouer une entrée d'historique restaure sa température d'origine

---

## Raccourcis

- **Toucher un matériau** → remplit automatiquement tous les champs `tCal` dans tous les onglets
- **Maintenir +/-** sur les champs numériques → incrémentation rapide
- **Glisser horizontalement** sur un champ numérique → faire défiler les valeurs
- **Entrée vide/négative/invalide** → se met à 0 à la perte de focus (le champ de température se limite à -40/200)
- **Marquer un matériau avec une étoile** → le déplace en haut du sélecteur

---

## Modèle Pro

**Freemium avec verrouillage par fonctionnalité** (19,99 $) :
- Gratuit : onglet 2-Sensor entièrement fonctionnel, sans limites
- Pro : Autres onglets accessibles mais avec des **champs verrouillés (cadenas doré)** qui affichent la paywall au toucher

Pro débloque : 3-Sensor jusqu'à 3D+, matériaux personnalisés, sauvegarde/restauration, rapports PDF, annotation de photos.

![Paywall](../screenshots/07-paywall.png)

---

## Rapports et sauvegarde

Bouton **Imprimer le résultat** sur n'importe quel écran de résultats → PDF avec en-tête, entrées, résultat, visualisation, photo (si prise) et pied de page de température (lorsque la compensation est active).

Personnalisez l'en-tête dans Paramètres → En-tête de rapport.

**Sauvegarde** : Paramètres → Sauvegarde → partager vers le cloud/courriel.  
**Restaurer** : Paramètres → Restaurer → sélectionnez le fichier de sauvegarde.

---

## Restaurer Pro sur un nouvel appareil

Même compte Google (Android) ou Apple ID (iOS) que celui utilisé pour l'achat → Paramètres → **Restaurer l'achat** → débloqué en quelques secondes.

La restauration automatique se produit silencieusement lorsque vous revenez à l'application après avoir échangé un code promo de manière externe.

---

## Dépannage rapide

- **Résultat hors plage ?** Vérifiez le signe de `tEvent` / Premier capteur / espacement des capteurs
- **Matériau le plus proche incorrect ?** La température de référence a probablement été définie accidentellement — vérifiez les paramètres
- **Échec de la restauration de l'achat ?** Vérifiez le même compte de magasin ; réinstallez si cela persiste
- **Champ mis à 0 ?** Les entrées vides/négatives se mettent automatiquement à 0 à la perte de focus — saisissez à nouveau la valeur
- **Boutons d'incrémentation manquants ?** Ils apparaissent à côté des champs avec `data-step` — redémarrez l'application s'ils manquent
- **Avertissement de température obsolète ?** Se réinitialise à 20 à chaque lancement — définissez à nouveau pour cette session

---

Contact `support@evdiag.net` — incluez le modèle de l'appareil, la version de l'application (Paramètres → bas) et une description de ce que vous avez essayé.
