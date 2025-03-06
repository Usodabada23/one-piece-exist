## 1. Afficher tous les Chevaliers Divins

**Route** : `/godsKnights`  
**Méthode HTTP** : `GET`  
**Description** : Cette route retourne la liste de tous les Chevaliers Divins enregistrés dans la base de données.

### Exemple de Réponse

**Code 200** : La liste des Chevaliers Divins est retournée avec succès. Voici un exemple de réponse :

```json
[
  [1, "Saint Figarland Garling", "Figarland", "Sword", null],
  [2, "Saint Ethanbaron V. Nusjuro", "Ethanbaron", "Unknown", null],
  [3, "Saint Topman Warcury", "Topman", "Unknown", null],
  [4, "Saint Shepherd Ju Peter", "Shepherd", "Unknown", null],
  [5, "Saint Marcus Mars", "Marcus", "Unknown", null],
  [6, "Saint Aurelius Sol", "Aurelius", "Spear of Light", null]
]
```

## 2. Afficher un Chevalier Divin par son ID

**Route** : `/godsKnight/<int:id>`  
**Méthode HTTP** : `GET`  
**Description** : Cette route retourne les informations détaillées d'un Chevalier Divin basé sur son ID unique.

### Paramètres :

- `id` (int) : L'ID du Chevalier Divin.

### Réponse :

- **Code 200** : Les détails du Chevalier Divin correspondant à l'ID fourni sont retournés avec succès. Exemple de réponse :

```json
{
  "id": 1,
  "name": "Saint Figarland Garling",
  "godFamily": "Figarland",
  "weapon": "Sword",
  "devilFruit_id": null
}
```

### Erreurs possibles

- **Code 404** : Chevalier Divin non trouvé.
- **Code 500** : Une erreur interne s'est produite lors de la récupération du Chevalier Divin.

## 3. Ajouter un Chevalier Divin

**Route** : `/godsKnight/add`  
**Méthode HTTP** : `POST`  
**Description** : Cette route permet d'ajouter un nouveau Chevalier Divin à la base de données.

### Corps de la requête (JSON) :

Les données suivantes doivent être envoyées dans le corps de la requête sous forme de JSON :

- `name` (string) : Nom du Chevalier Divin.
- `godFamily` (string) : Famille du Dieu du Chevalier Divin.
- `weapon` (string) : Arme principale du Chevalier Divin.
- `devilFruit_id` (int, optionnel) : L'ID du fruit du démon du Chevalier Divin (s'il en a un).

### Exemple de corps de la requête (JSON) :

```json
{
  "name": "Saint Figarland Garling",
  "godFamily": "Figarland",
  "weapon": "Sword",
  "devilFruit_id": null
}
```

### Réponse :

- **Code 201** : Le Chevalier Divin a été ajouté avec succès.
  ```json
  {
    "message": "✅ God knight added successfully!"
  }
  ```

-**Code 400** : Un champ requis est manquant dans la requête ou une erreur de formatage des données.

```json
{
  "error": "The field 'name' is missing."
}
```

-**Code 500** : Une erreur interne s'est produite lors de la récupération du Chevalier Divin.

```json
{
  "error": "Error fetching god knight with id: 1"
}
```

## 4. Supprimer un Chevalier Divin par son ID

**Route** : `/godsKnight/<int:id>/delete`  
**Méthode HTTP** : `DELETE`  
**Description** : Cette route permet de supprimer un Chevalier Divin par son ID unique.

### Paramètres :

- `id` (int) : L'ID du Chevalier Divin à supprimer.

### Réponse :

- **Code 204** : Chevalier Divin supprimé avec succès. Aucune réponse n'est retournée.

  - Exemple de réponse : (Aucune réponse ne sera retournée)

- **Code 404** : Chevalier Divin non trouvé.
  - Exemple de réponse :
  ```json
  {
    "error": "Gods Knight not found"
  }
  ```
- **Code 400** : Format de la requête invalide.

```json
{
  "error": "Format error: <détails de l'erreur>"
}
```

- **Code 500** : Erreur interne lors de la suppression du Chevalier Divin.

```json
{
  "error": "Error deleting gods knight: <détails de l'erreur>"
}
```
