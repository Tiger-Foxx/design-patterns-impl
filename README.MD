# design-patterns-impl

**Implémentations pédagogiques (en Python)** des patrons de conception abordés dans la *Leçon 5 — Structural Patterns* (exemple : **Menu de restaurant**).
Ce dépôt contient les sources, diagrammes et tests permettant de répondre aux exercices demandés et de générer un rapport LaTeX prêt pour Overleaf / impression.

**Étudiant :** Donfack Pascal — **Classe :** M2-GI
**Encadreur :** Pr Kouamou — **Établissement :** École Nationale Supérieure Polytechnique de Yaoundé

---

## Objectifs / Exercices traités

1. **Reproduire en Python le code de l'arbre du menu (Composite pattern)** et, **à la fin**, implémenter dans la classe « serveur » (ici `Waitress`) une méthode `print_specific_menu(name)` qui permet d'afficher un menu spécifique (sous-arbre) ou un item précis.

   * Réponse : `src/menu_composite/` contient l'implémentation complète (Menu, MenuItem, composite iterator, waitress, demo).

2. **Faire le schéma du patron Iterator** (participants, mapping général) puis **appliquer ce schéma à l'exemple du menu**.

   * Réponse : implémentation d'un `CompositeIterator` (itérateur DFS) + diagrammes (images PNG dans `docs/diagrams/`) qui illustrent le schéma général et le mapping.

3. **Chercher ce qu'est le “Head First Design Patterns”** — produire un schéma et un code exemple (ici le pattern **Decorator**, style Head First — Starbuzz Coffee).

   * Réponse : `src/headfirst_decorator/` contient l'exemple `beverage.py`, `condiments.py`, `starbuzz_demo.py` et le schéma associé (images).

---

## Arborescence du dépôt (actuelle)

```
C:.
├───docs
│   ├───diagrams
│   │       menu_example.png
│   │       Schema-genral-iterator-2.png
│   │       Schema-genral-iterator.png
│   └───report
├───src
│   ├───headfirst_decorator
│   │       beverage.py
│   │       condiments.py
│   │       starbuzz_demo.py
│   │       __init__.py
│   └───menu_composite
│           composite_iterator.py
│           demo.py
│           menu.py
│           menu_component.py
│           menu_item.py
│           waitress.py
│           __init__.py
└───tests
        test_menu.py
```

---

## But de chaque répertoire / fichier

### `src/menu_composite/`

* `menu_component.py` — interface abstraite `MenuComponent` (API commune pour `Menu` et `MenuItem`).
  **Répond à :** exercice 1 (Composite).
* `menu_item.py` — feuille (`MenuItem`) : nom, description, prix, végétarien.
  **Répond à :** exercice 1.
* `menu.py` — composite (`Menu`) : conteneur d'enfants, `create_iterator()`, print, to_dict.
  **Répond à :** exercice 1.
* `composite_iterator.py` — **Iterator** récursif (pile d'itérateurs) pour parcourir l'arbre en profondeur (DFS).
  **Répond à :** exercice 2 (Iterator appliqué).
* `waitress.py` — **Serveur (Waitress)** : méthodes `print_menu()`, `print_vegetarian()`, `find_menu_by_name()` et **`print_specific_menu(name)`** (méthode demandée par l'exercice).
  **Répond à :** exercice 1.
* `demo.py` — script de démonstration : construit un menu d'exemple, exécute affichage complet, végétariens, menu spécifique.
  **Usage / test manuel**.

### `src/headfirst_decorator/`

* `beverage.py`, `condiments.py` — exemple **Decorator** (Head First style — Starbuzz Coffee) avec diagramme associé.
  **Répond à :** exercice 3 (Head First Design Patterns).

### `docs/diagrams/`

* `menu_example.png` — schéma illustrant l'arbre du menu (Composite).
* `Schema-genral-iterator.png`, `Schema-genral-iterator-2.png` — schéma général du pattern Iterator et mapping pour le menu.
  **Répondent à :** exercice 2.

### `docs/report/`

* Emplacement prévu pour le rapport LaTeX (`rapport.tex`, `title.tex`, `references.bib`) — le `.tex` final sera généré ici ou à la racine selon ta préférence.
  **Contenu du futur PDF :** explications détaillées, diagrammes inclus, listings de code (`\lstinputlisting`), justification conceptuelle (Nom / Problème / Solution / Conséquences), résultats d’exécution, et références (cours Leçon 5, GoF, Head First).

### `tests/`

* `test_menu.py` — tests `pytest` qui vérifient la recherche et l'affichage d'un menu spécifique.
  **Permet de vérifier** la conformité du comportement demandé.

---

## Que contiendra le PDF (rapport LaTeX final) — résumé

Le rapport (long et académique) contiendra :

1. Page de titre (Donfack Pascal, M2-GI, Pr Kouamou, ENSP Yaoundé).
2. Résumé / objectifs / énoncé des exercices.
3. Rappel théorique : patrons structurels (Composite, Iterator), rôle des auteurs GoF (Gamma, Helm, Johnson, Vlissides) et approche Head First.
4. **Détail chirurgical** de l’exemple Menu :

   * Modèle conceptuel, arbre du menu, exigences (traversée globale vs. traversée ciblée).
   * UML (schéma Composite) + diagrammes Iterator (général et appliqué).
5. **Code** : extraits commentés et **inclusion automatique des fichiers `.py`** (annexes) via `\lstinputlisting{src/menu_composite/menu.py}` etc.
6. **Explications pas-à-pas** : pourquoi ce design, alternatives, complexité, conséquences.
7. **Résultats d’exécution** (captures / sorties du `demo.py`).
8. **Tests** (ex. `pytest`) et instructions d’exécution.
9. **Références** : leçon 5 (fichier PDF fourni), GoF (Design Patterns), Head First Design Patterns.
10. Annexes : code complet, diagrammes en haute résolution, notes.

> Remarque : dans le `.tex` je relierai chaque section d’explication à l’exercice précis (ex. « Section 4.2 : Réponse à l’exercice 1 — `print_specific_menu` ») pour faciliter la lecture par le professeur.

---

## Installation et exécution (rapide)

Prérequis : **Python 3.8+**, `pip`.

Installer dépendances :

```bash
python -m pip install --upgrade pip
pip install pytest
```

Exécuter le demo (depuis la racine du repo) :

```bash
# Option A : exécuter le module
python -m src.menu_composite.demo

# Option B : exécuter directement le fichier
python src/menu_composite/demo.py
```

Exécuter les tests :

```bash
pytest -q
```

---

## Commandes Git utiles (si tu veux pousser sur GitHub puis importer sur Overleaf)

```bash
# depuis le dossier racine
git init
git add .
git commit -m "Initial commit — Composite + Iterator + HeadFirst examples"
git branch -M main
git remote add origin https://github.com/<ton-compte>/design-patterns-impl.git
git push -u origin main
```

Sur **Overleaf**, tu peux ensuite :

* Lier directement le dépôt GitHub (si tu as un projet Overleaf payant avec import Git) ou
* **Importer le repo** (Upload ZIP), ou
* Créer un projet Overleaf et `git push` dessus si tu as configuré l'accès Git Overleaf.

---

## Inclusion automatique du code dans LaTeX

Le rapport `.tex` utilisera `listings` pour inclure les fichiers Python et conserver la coloration / mise en forme :

```tex
\usepackage{listings}
\lstset{language=Python, breaklines=true, basicstyle=\ttfamily\small}

% Exemple d'inclusion dans le document
\lstinputlisting[caption={menu.py — Composite}, label={lst:menu}]{src/menu_composite/menu.py}
```

Ainsi le PDF contiendra les portions de code **exactes** (pas de copier/coller manuel), ce qui garantit la cohérence entre le rapport et le dépôt.

---

## Références (préliminaires) — à citer dans `references.bib`

* Leçon 5 — *Structural Patterns* (cours fourni).
* Gamma, E., Helm, R., Johnson, R., Vlissides, J. (1995). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
* Freeman, E., & Robson, E. (Head First Design Patterns) — *O’Reilly Media*.
  (Je remplirai `references.bib` avec les entrées BibTeX complètes dans le rapport final.)

