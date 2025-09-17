[[Obsidian]]

- Aller sur Github, et créer un nouveau **repository** (public ou privé, c'est vous qui voyez)
  ![[tuto1.jpg]]
- Créer un access token sur Github:
  -> Icone de votre acompte -> Settings
  -> Dans le menu de gauche, tout en bas -> **Developper settings**
  ![[tuto2.jpg]]
  -> Toujours dans le menu de gauche, Personnal access tokens, choisir **Tokens (classic)**
  ![[tuto3.jpg]]
  -> Generate new token (classic)
  -> mettre une description, choisir **No expiration**, et cliquer sur **repo**
  ![[tuto4.jpg]]
  -> Generate token, et dans la fenêtre suivante clique sur les deux carrés bleu pour copier le token dans le presse papier
  -> Vous pouvez enregistrer ce token dans un fichier texte si vous voulez
- Dans Obsidian, allez dans les options, **modules complémentaires** et cliquez sur parcourir a droite
- Tapez Git dans la barre de recherche et installer le plugin, puis activez le
  ![[tuto5.jpg]]
- Sortez des options, et créez un nouveau dossier dans la racine de votre vault (ne mettez rien dedans pour le moment)
- Appuyez sur Ctrl + P pour ouvrir la palette de commande
- Sélectionnez **Obsidian Git : Clone an existing repo**
  ![[tuto6.jpg]]
- Dans la barre, tapez sans les chevrons <>:
  ```
  https://<collez votre token ici>@github.com/<votre pseudo github>/<nom du repo>.git
  ```
  ![[tuto7.jpg]]
- Maintenant dans cette même barre vous devriez voir "Enter directory for clone". Tapez le nom du dossier que vous avez crée a la racine d'Obsidian
  - Dans "specify depth of clone", ne tapez rien, appuyez juste sur Entrée
  - Vous devriez avoir un message qui vous demande de redémarrer
  - Vous pouvez maintenant copier vos notes dans ce dossier pour qu'elles soient sauvegardées avec la commande **Git: Commit-and-sync** dans la palette de commande

Si vous voulez automatiser la synchronisation:
  - Retournez dans les options, tout en bas sélectionnez Git
  - Vous pouvez spécifier l'intervalle de temps a laquelle vous voulez synchroniser vos notes en choisissant une valeur autre que 0 dans **Auto commit-and-sync interval**
