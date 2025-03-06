# Documentation des Routes Marines

Cette API permet de gérer les marines dans le système. Vous pouvez ajouter, afficher, et supprimer des marines.

## 1. Afficher tous les marines

**Route** : `/marines`  
**Méthode HTTP** : `GET`  
**Description** : Cette route retourne la liste de tous les marines enregistrés dans la base de données.

### Réponse :

- **Code 200** : La liste des marines.
- **Exemple de réponse** :

```json
[
  [
    1,
    "Sakazuki (Akainu)",
    55,
    306,
    "N/A",
    "Magu Magu no Mi",
    null,
    "Fleet Admiral"
  ],
  [2, "Borsalino (Kizaru)", 58, 302, "N/A", "Pika Pika no Mi", null, "Admiral"],
  [3, "Issho (Fujitora)", 54, 270, "N/A", "Zushi Zushi no Mi", null, "Admiral"],
  [4, "Monkey D. Garp", 78, 287, "N/A", "Haki", null, "Vice Admiral"],
  [
    5,
    "Sengoku",
    79,
    278,
    "N/A",
    "Hito Hito no Mi, Model: Daibutsu",
    null,
    "Former Fleet Admiral"
  ],
  [6, "Smoker", 36, 209, "N/A", "Moku Moku no Mi", null, "Vice Admiral"],
  [7, "Tashigi", 26, 170, "N/A", "Sword", null, "Captain"],
  [8, "Coby", 18, 167, "N/A", "Haki", null, "Captain"],
  [9, "Helmeppo", 19, 174, "N/A", "Sword", null, "Lieutenant Commander"],
  [10, "Aramaki", 47, 298, null, "Nature Manipulation", null, "Admiral"]
]
```

## 2. Afficher un marine par son ID

**Route** : `/marine/<int:id>`  
**Méthode HTTP** : `GET`  
**Description** : Cette route retourne les informations détaillées d'un marine basé sur son ID unique.

### Paramètres :

- `id` (int) : L'ID du marine.

### Réponse :

- **Code 200** : Détails du marine.
- **Code 404** : Marine non trouvé.

### Exemple de réponse (Code 200) :

```json
{
  "id": 8,
  "name": "Coby",
  "age": 18,
  "height": 167,
  "weapon": "N/A",
  "devilFruit": "Haki",
  "cgbounty": null,
  "rank": "Captain"
}
```

## 3. Ajouter un marine

**Route** : `/marine/add`  
**Méthode HTTP** : `POST`  
**Description** : Cette route permet d'ajouter un nouveau marine à la base de données.

### Corps de la requête (JSON) :

- `name` (string) : Nom du marine.
- `age` (int) : Âge du marine.
- `height` (int) : Taille du marine en cm.
- `weapon` (string) : Arme du marine.
- `devilFruit_id` (int, optionnel) : L'ID du fruit du démon du marine (s'il en a un).
- `cgbounty` (int, optionnel) : Prime du marine (s'il en a une).
- `rank` (string) : Rang du marine.

### Réponse :

- **Code 201** : Le marine a été ajouté avec succès.
- **Code 400** : Un champ requis est manquant dans la requête.
- **Code 500** : Une erreur interne est survenue lors de l'ajout du marine.

### Exemple de corps de la requête (JSON) :

```json
{
  "name": "Coby",
  "age": 18,
  "height": 167,
  "weapon": "N/A",
  "devilFruit_id": null,
  "cgbounty": null,
  "rank": "Captain"
}
```

## 4. Supprimer un marine par son ID

**Route** : `/marine/<int:id>/delete`  
**Méthode HTTP** : `DELETE`  
**Description** : Cette route permet de supprimer un marine par son ID unique.

### Paramètres :

- `id` (int) : L'ID du marine à supprimer.

### Réponse :

- **Code 204** : Marine supprimé avec succès.
- **Code 404** : Marine non trouvé.
- **Code 400** : Format de la requête invalide.
- **Code 500** : Erreur interne lors de la suppression du marine.

### Exemple de réponse (Code 204) :

- Aucune réponse ne sera retournée.

### Exemple de réponse (Code 404) :

```json
{
  "error": "Marine not found"
}
```
