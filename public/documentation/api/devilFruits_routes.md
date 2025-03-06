
# Documentation des Routes : Fruits du Démon

Cette section décrit les différentes routes de l'API pour gérer les **Fruits du Démon** dans le monde de **One Piece**.

## 1. Liste des Devil Fruits

### Route :
```
GET /devilFruits
```

### Description :
Cette route récupère tous les fruits du démon présents dans la base de données.

### Exemple de réponse :
```json
[
  {
    "id": 1,
    "name": "Gomu Gomu no Mi",
    "typeFruit": "Paramecia",
    "description": "Un fruit du démon de type Paramecia qui permet à son utilisateur d'étirer son corps comme du caoutchouc.",
    "ability": "Elasticité",
    "rarity": "Common",
    "is_eaten": true
  },
  {
    "id": 2,
    "name": "Mera Mera no Mi",
    "typeFruit": "Logia",
    "description": "Un fruit du démon de type Logia qui permet à son utilisateur de contrôler, créer et se transformer en feu.",
    "ability": "Pyrokinésie",
    "rarity": "Rare",
    "is_eaten": false
  }
]
```

---

## 2. Détails d'un Devil Fruit

### Route :
```
GET /devilFruit/<int:id>
```

### Description :
Cette route récupère les détails d'un fruit du démon spécifique en fonction de son identifiant unique.

### Paramètre :
- `id` : L'identifiant unique du fruit du démon.

### Exemple de réponse :
```json
{
  "id": 1,
  "name": "Gomu Gomu no Mi",
  "typeFruit": "Paramecia",
  "description": "Un fruit du démon de type Paramecia qui permet à son utilisateur d'étirer son corps comme du caoutchouc.",
  "ability": "Elasticité",
  "rarity": "Common",
  "is_eaten": true
}
```

---

## 3. Ajouter un Devil Fruit

### Route :
```
POST /devilFruit/add
```

### Description :
Cette route permet d'ajouter un nouveau fruit du démon à la base de données. Les informations nécessaires incluent le nom, le type, la description, l'abilité, la rareté, et si le fruit a été mangé ou non.

### Corps de la requête :
L'utilisateur doit fournir un objet JSON contenant les informations suivantes :
- **name** (string) : Le nom du fruit du démon.
- **type** (string) : Le type du fruit (ex. : "Paramecia", "Logia").
- **description** (string) : La description du fruit.
- **ability** (string) : L'abilité conférée par le fruit.
- **rarity** (string) : La rareté du fruit (ex. : "Common", "Rare").
- **is_eaten** (bool) : Indique si le fruit a été mangé.

### Exemple de corps de la requête :
```json
{
  "name": "Gomu Gomu no Mi",
  "type": "Paramecia",
  "description": "Un fruit du démon de type Paramecia qui permet à son utilisateur d'étirer son corps comme du caoutchouc.",
  "ability": "Elasticité",
  "rarity": "Common",
  "is_eaten": true
}
```

### Réponses possibles :

- **Code 201** : Le fruit du démon a été ajouté avec succès.
  - Exemple de réponse :
  ```json
  {
    "message": "✅ Devil Fruit added successfully!"
  }
  ```

- **Code 400** : Un champ requis est manquant ou une erreur de formatage dans les données.
  - Exemple de réponse :
  ```json
  {
    "error": "The field 'name' is missing."
  }
  ```

- **Code 500** : Une erreur interne s'est produite lors de l'ajout du fruit.
  - Exemple de réponse :
  ```json
  {
    "error": "Error adding devil fruit: <détails de l'erreur>"
  }
  ```

---

## 4. Supprimer un Devil Fruit

### Route :
```
DELETE /devilFruit/<int:id>/delete
```

### Description :
Cette route permet de supprimer un fruit du démon spécifique de la base de données en utilisant son identifiant unique.

### Paramètre :
- `id` : L'identifiant unique du fruit du démon à supprimer.

### Exemple de réponse :
- **Code 204** : Le fruit du démon a été supprimé avec succès.
- **Code 404** : Le fruit du démon avec l'identifiant spécifié n'a pas été trouvé.
  - Exemple de réponse en cas d'erreur :
  ```json
  {
    "error": "Devil Fruit not found"
  }
  ```

### Réponses possibles :

- **Code 204** : Succès de la suppression.
  - Pas de corps de réponse.

- **Code 400** : Erreur de formatage de l'ID.
  - Exemple de réponse :
  ```json
  {
    "error": "Format error: <détails de l'erreur>"
  }
  ```

- **Code 500** : Une erreur interne s'est produite lors de la suppression du fruit.
  - Exemple de réponse :
  ```json
  {
    "error": "Error deleting devil fruit: <détails de l'erreur>"
  }
  ```

---
