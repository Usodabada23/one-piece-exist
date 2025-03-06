# Documentation des Routes Iles 

Cette API permet de gérer les îles dans le système. Vous pouvez ajouter, afficher, et supprimer des îles.

## 1. Afficher toutes les îles

**Route** : `/islands`  
**Méthode HTTP** : `GET`  
**Description** : Cette route retourne la liste de toutes les îles enregistrés dans la base de données.

**Réponse** :

- **Code 200** : La liste des îles.
- **Exemple de réponse** :
  ```json
  [
    [
        1,
        "Logue Town",
        "East Blue",
        "World Government",
        "N/A"
    ],
    [
        2,
        "Drum Island",
        "Grand Line",
        "Kingdom of Drum",
        "N/A"
    ],
    [
        3,
        "Alabasta",
        "Grand Line",
        "Kingdom of Alabasta",
        "N/A"
    ],
    [
        4,
        "Skypiea",
        "Sky Islands",
        "Tribal Council",
        "Shandia"
    ],
    [
        5,
        "Water 7",
        "Grand Line",
        "Mayor",
        "Galley-La Company"
    ],
    ...
    [
        15,
        "Elbaf",
        "Grand Line",
        "Giant Kingdom",
        null
    ]
  ]
  ```

## 2. Afficher une île par son ID

**Route** : `/island/<int:id>`  
**Méthode HTTP** : `GET`  
**Description** : Cette route retourne les informations détaillées d'une île basé sur son ID unique.

### Paramètres :

- `id` (int) : L'ID de l'île.

### Réponse :

- **Code 200** : Détails de l'île.
- **Code 404** : île non trouvé.

### Exemple de réponse (Code 200) :

```json
[
    "id" : 15,
    "name": "Elbaf",
    "location": "Grand Line",
    "government": "Giant Kingdom",
    "affiliated_group": null


]
```
## 3. Ajouter une île

**Route** : `/island/add`  
**Méthode HTTP** : `POST`  
**Description** : Cette route permet d'ajouter une nouvelle île à la base de données. L'utilisateur doit fournir les informations essentielles concernant l'île, telles que son nom, sa localisation, son gouvernement, et éventuellement un groupe affilié. 

### Paramètres de la requête :
La requête doit être envoyée avec un corps au format JSON contenant les champs suivants :

- `name` (string) : Nom de l'île. **Requis**.
- `location` (string) : Localisation de l'île (par exemple, "Grand Line", "East Blue"). **Requis**.
- `government` (string) : Type de gouvernement qui régit l'île (par exemple, "World Government", "Tribal Council"). **Requis**.
- `affiliated_group` (string, optionnel) : Groupe ou faction auquel l'île est associée (par exemple, "Marine", "Pirates", etc.). Ce champ est **optionnel** et peut être laissé à `null` si l'île n'est pas affiliée à un groupe spécifique.

### Exemple de corps de la requête (JSON) :

```json
{
  "name": "Elbaf",
  "location": "Grand Line",
  "government": "Giant Kingdom",
  "affiliated_group": null
}
```

## 4. Supprimer une île par son ID

**Route** : `/island/<int:id>/delete`  
**Méthode HTTP** : `DELETE`  
**Description** : Cette route permet de supprimer une île de la base de données en spécifiant son ID unique. L'ID est un identifiant unique pour chaque île dans la base de données. Si l'île existe, elle sera supprimée, et un message de confirmation sera retourné.

### Paramètres de la route :

- `id` (int) : L'ID unique de l'île à supprimer. **Requis**.

### Exemple d'URL pour supprimer une île avec l'ID 15 :

-> `/island/15/delete`

### Réponse :

La réponse dépendra de l'existence de l'île dans la base de données et du succès de la suppression.

- **Code 204 (No Content)** : Si l'île a été supprimée avec succès, la réponse sera vide avec un code HTTP 204, indiquant que l'action a été réalisée sans contenu supplémentaire à retourner.
  
  **Exemple de réponse (Code 204)** :
  Aucun contenu ne sera renvoyé. Une réponse vide avec le code 204 signifiera que la suppression a réussi.

- **Code 404 (Not Found)** : Si l'île avec l'ID spécifié n'existe pas, une erreur sera renvoyée avec un message indiquant que l'île n'a pas été trouvée dans la base de données.
  
  **Exemple de réponse (Code 404)** :
  ```json
  {
    "error": "Island not found"
  }

