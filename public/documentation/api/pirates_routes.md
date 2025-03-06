# Documentation des Routes Pirates

Cette API permet de gérer les pirates dans le système. Vous pouvez ajouter, afficher, et supprimer des pirates.

## 1. Afficher tous les pirates

**Route** : `/pirates`  
**Méthode HTTP** : `GET`  
**Description** : Cette route retourne la liste de tous les pirates enregistrés dans la base de données.

**Réponse** :

- **Code 200** : La liste des pirates.
- **Exemple de réponse** :
  ```json
  [
    {
      "id": 1,
      "name": "Monkey D. Luffy",
      "age": 19,
      "height": 174,
      "birthDate": "2001-05-05",
      "bounty": 500000000,
      "weapon": "Gomu Gomu no Mi",
      "devilFruit_id": 1,
      "was_supernova": true
    },
    ...
  ]
  ```

## 1. Afficher tous les pirates

**Route** : `/pirates`  
**Méthode HTTP** : `GET`  
**Description** : Cette route retourne la liste de tous les pirates enregistrés dans la base de données.

**Réponse** :

- **Code 200** : La liste des pirates.
- **Exemple de réponse** :
  ```json
  [
    [
      1,
      "Monkey D. Luffy",
      19,
      174,
      "Wed, 05 May 1999 00:00:00 GMT",
      1500000000,
      "Gomu Gomu no Mi",
      null,
      true
    ],
    [
      2,
      "Roronoa Zoro",
      21,
      181,
      "Tue, 11 Nov 1997 00:00:00 GMT",
      320000000,
      "Swords",
      null,
      true
    ],
    [
      3,
      "Nami",
      20,
      170,
      "Fri, 03 Jul 1998 00:00:00 GMT",
      66000000,
      "Clima-Tact",
      null,
      false
    ],
    [
      4,
      "Usopp",
      19,
      176,
      "Thu, 01 Apr 1999 00:00:00 GMT",
      200000000,
      "Slingshot",
      null,
      false
    ],
    [
      5,
      "Sanji",
      21,
      180,
      "Sun, 02 Mar 1997 00:00:00 GMT",
      330000000,
      "Legs",
      null,
      true
    ],
    ...
  ]
  ```

## 2. Afficher un pirate par son ID

**Route** : `/pirate/<int:id>`  
**Méthode HTTP** : `GET`  
**Description** : Cette route retourne les informations détaillées d'un pirate basé sur son ID unique.

### Paramètres :

- `id` (int) : L'ID du pirate.

### Réponse :

- **Code 200** : Détails du pirate.
- **Code 404** : Pirate non trouvé.

### Exemple de réponse (Code 200) :

```json
{
  "id": 1,
  "name": "Monkey D. Luffy",
  "age": 19,
  "height": 174,
  "birthDate": "2001-05-05",
  "bounty": 500000000,
  "weapon": "Gomu Gomu no Mi",
  "devilFruit_id": 1,
  "was_supernova": true
}
```
## 3. Ajouter un pirate

**Route** : `/pirate/add`  
**Méthode HTTP** : `POST`  
**Description** : Cette route permet d'ajouter un nouveau pirate à la base de données.

### Corps de la requête (JSON) :
- `name` (string) : Nom du pirate.
- `age` (int) : Âge du pirate.
- `height` (int) : Taille du pirate en cm.
- `birthDate` (string) : Date de naissance du pirate (format : `YYYY-MM-DD`).
- `bounty` (int) : Prime du pirate.
- `weapon` (string) : Arme du pirate.
- `devilFruit_id` (int, optionnel) : L'ID du fruit du démon du pirate (s'il en a un).
- `was_supernova` (bool) : Indique si le pirate faisait partie des supernovae.

### Réponse :
- **Code 201** : Le pirate a été ajouté avec succès.
- **Code 400** : Un champ requis est manquant dans la requête.
- **Code 500** : Une erreur interne est survenue lors de l'ajout du pirate.

### Exemple de corps de la requête (JSON) :
```json
{
  "name": "Monkey D. Luffy",
  "age": 19,
  "height": 174,
  "birthDate": "2001-05-05",
  "bounty": 500000000,
  "weapon": "Gomu Gomu no Mi",
  "devilFruit_id": 1,
  "was_supernova": true
}

```
## 4. Supprimer un pirate par son ID

**Route** : `/pirate/<int:id>/delete`  
**Méthode HTTP** : `DELETE`  
**Description** : Cette route permet de supprimer un pirate par son ID unique.

### Paramètres :
- `id` (int) : L'ID du pirate à supprimer.

### Réponse :
- **Code 204** : Pirate supprimé avec succès.
- **Code 404** : Pirate non trouvé.
- **Code 400** : Format de la requête invalide.
- **Code 500** : Erreur interne lors de la suppression du pirate.

### Exemple de réponse (Code 204) :
  - Aucune réponse ne sera retournée.

### Exemple de réponse (Code 404) :
```json
{
  "error": "Pirate not found"
}
