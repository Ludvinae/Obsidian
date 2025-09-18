[[Linux]] 

Tout système peut fonctionner grâce aux lignes de commande. Une commande est un programme qui permet de faire certaines actions. Après le prompt (généralement un #), on tape le nom de la commande, suivi d'un espace et d'options (qui commencent toujours avec un tiret). On peut aussi entrer éventuellement des paramètres après les options.

```
# nom_commande [-options] [paramètres]
```


### 📂 Navigation dans les fichiers et dossiers 

pwd          # Affiche le chemin du dossier courant 
ls           # Liste les fichiers 
ls -l        # Liste détaillée (droits, taille, date)
ls -a        # Affiche aussi les fichiers cachés 
cd /chemin   # Aller dans un dossier 
cd ..        # Remonter d’un niveau 
cd ~         # Aller dans le home de ton utilisateur  

### 📄 Manipulation de fichiers et dossiers 

touch fichier.txt        # Crée un fichier vide 
mkdir mon_dossier        # Crée un dossier 
cp fichier.txt copie.txt # Copier un fichier 
mv fichier.txt dossier/  # Déplacer un fichier 
mv ancien.txt nouveau.txt # Renommer un fichier 
rm fichier.txt           # Supprimer un fichier 
rm -r dossier/           # Supprimer un dossier et son contenu  

### 🔍 Recherche et affichage 

cat fichier.txt          # Affiche le contenu 
less fichier.txt         # Affiche page par page 
head fichier.txt         # Affiche les 10 premières lignes 
tail fichier.txt         # Affiche les 10 dernières lignes 
tail -f log.txt          # Suivre un fichier en temps réel (logs) 
find / -name fichier.txt # Recherche un fichier 
grep "mot" fichier.txt   # Recherche un mot dans un fichier  

### 👤 Gestion des utilisateurs et droits 

whoami                   # Affiche ton utilisateur 
id                       # Infos sur ton utilisateur et groupes 
sudo commande            # Exécuter une commande en administrateur 
chmod 755 fichier.sh     # Modifier les droits (rwxr-xr-x) 
chown user:group fichier   # Changer le propriétaire  

### ⚙️ Gestion des processus 

ps aux                   # Liste tous les processus 
top                      # Affiche les processus en temps réel 
htop                     # (si installé) version améliorée de top 
kill 1234                # Tuer un processus par son PID 
kill -9 1234             # Forcer l’arrêt d’un processus  

### 🌐 Réseau 

ip a                     # Affiche les adresses IP 
ping google.com          # Test de connexion 
curl [http://site.com](http://site.com/)     # Test requête HTTP 
wget [http://site.com](http://site.com/)     # Télécharger un fichier 
ss -tulnp                # Voir les ports ouverts  

### 📦 Gestion des paquets (Debian/Ubuntu) 

sudo apt update          # Met à jour la liste des paquets 
sudo apt upgrade         # Installe les mises à jour 
sudo apt install paquet  # Installe un paquet 
sudo apt remove paquet   # Désinstalle un paquet 
dpkg -l                  # Liste des paquets installés  

### 📑 Navigation et édition de fichiers 

nano fichier.txt         # Éditeur simple en ligne de commande 
vim fichier.txt          # Éditeur avancé (plus difficile à prendre en main) 

```ad-note
La commande sudo (SuperUser do) permet d’exécuter une ligne de commande en tant que SuperUser sans être connecté sur le profil root.
```