[[Culture Informatique]]

Le composant principal est la **carte mère** sur laquelle on va brancher un certains nombres de périphériques, et des composants comme le processeur.

Le cœur de la machine est le processeur, connectée à la RAM (Random Access Memory) qui est dynamique (on doit rafraichir constamment sa charge électrique).
La ROM (Read-Only Memory) est statique, située sur la carte mère.
Les périphériques de stockage de données sont connectés a la PIO (périphérique d'entrée / sortie).

![[Architecture carte-mère.png]]

Deux grands fournisseurs de **processeurs** a l'heure actuelle:
- **Intel** (i3, i5, i7, i9, Xeon)
- **AMD**  (Ryzen 3, 5, 7, Threadripper)
On place le processeur sur la carte mère par l'intermédiaire d'un socket:
- PGA (Pin Grid Array)
- LGA (Land Grid Array)

On peut brancher des périphériques via les ports PCI (ou PCI express pour la carte graphique).

La **mémoire vive** utilisé est de la DDR (Double Data Rate), et avec la DDR5, la gestion de la tension électrique se fait maintenant directement sur la barrette mémoire.
Il y'a maintenant aussi un code de correction d'erreur directement sur la barrette (ECC) comme on l'as connu sur les serveurs.
On met généralement les barrettes par deux pour pouvoir profiter du Dual-channel (le processeur peut envoyer des informations en alternance entre les deux canaux).
L'équivalent de la DDR pour les portables est la SO-DIMM DDR.

Pour les **disques durs**, on a deux technologies:
- HDD (Hard Disk Drive)
- SSD (Solid State Drive)
Ils sont connectés à la carte mère via les ports SATA (en série) qui a remplacé l'IDE (parallèle).
On a maintenant aussi une connectique M2 (format NVMe) qui se branche directement sur la carte mère et qui est beaucoup plus rapide.. C'est une version spécifique du PCIExpress améliorée, avec 3 différents standards de socket (B key, M, key, B+M key).

Virtualisation de stockage
On utilise différents modes [[RAID]] pour gérer plusieurs disque durs. On retrouve ça dans les NAS (Network-Attached Storage) par exemple. On peut avoir des raids physiques ou virtuels.








