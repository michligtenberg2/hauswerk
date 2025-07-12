# ✅ Commit Guide for Hauswerk

Gebruik deze prefixen bij je commit messages om automatisch nette changelogs te krijgen en toekomstige versiebeheer te ondersteunen.

## 📦 Structuur
Elke commitmessage begint met een type en optioneel een korte uitleg:

```
<type>: beschrijving
```

## 🏷️ Types

| Type       | Betekenis                                      |
|------------|-------------------------------------------------|
| feat       | ✨ Nieuwe functionaliteit                        |
| fix        | 🐛 Bugfix of probleem opgelost                  |
| chore      | 🔧 Niet-functionele wijziging (bv. deps)        |
| docs       | 📚 Documentatie toegevoegd of aangepast         |
| style      | 💅 Alleen opmaak, geen codewijziging            |
| refactor   | ♻️ Codeverbetering zonder nieuwe functionaliteit|
| test       | 🧪 Testcode toegevoegd of aangepast              |
| perf       | 🚀 Prestatieverbetering                         |
| build      | 🏗️ Buildsystem of dependencymanagement         |
| ci         | 🤖 Continuous Integration scripts of config     |

## 🧾 Voorbeelden

```
feat: voeg plugin preview toe aan builder
fix: corrigeer fade-effect in collage export
chore: upgrade PyQt6 naar nieuwste versie
docs: verbeter README met installatiehandleiding
```

> 📌 Tip: Gebruik Engelse commitmessages voor maximale compatibiliteit met changelog tools zoals `git-cliff`.

