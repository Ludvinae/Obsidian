[[Remote/Réseau/Réseau|Réseau]]

Permet de multiplier les disques durs pour les faire fonctionner de concert.
(Redundant Array of Independant Disks)

Types de raid:
- **mirroring** (raid 1): haute disponibilité, permet de contrer les incidents, si un disque lâche, on a encore les données sur le second. 
- **striping** (raid 0): place une partie des données sur chaque disque afin de gagner en vitesse de lecture. Si un des disques ne fonctionne plus, toutes les données sont perdues.
- **striping & parité distribuée** (raid 5): comme le raid 0, mais on ajoute un bit de parité pour pouvoir corriger des données manquantes, ce qui permet de parer à une panne d'un des disques. Requiers au moins 3 disques durs.
- Avec le RAID 6, on peut se permettre de perdre deux disques.
- **Striping + Mirroring** (Raid 1-0) combine les deux types de Raids, avec une tolérance à l'erreur et un gain de vitesse.

Les raid 4 et supérieurs se servent de la **parité** pour assurer une correction d'erreur.
On fixe la parité a *pair* ou *impair*, et on code le 8ème bit de chaque octet de données pour avoir un total de 1 dans l'octet a la parité choisie.
Exemple:
	0000000 -> nombre de 1 : 0 -> en parité pair le 8ème bit sera 0
	1111111 -> nombre de 1 : 7 -> en parité pair, le 8eme bit sera 1
	0000111 -> nombre de 1 : 3 -> en parité impaire, le 8eme bit sera 0
	

![[RAID.jpg]]