[[IP]]

A : numéro de réseau sur un octet ; premier octet entre 1 et 127, 3 octets pour le numéro d’hôte. 

Les IP commençant par 10.0.0.0 jusqu'à 10.255.255.255 sont réservés pour les réseaux locaux. 

B : numéro de réseau sur 2 octets ; premier octet entre 128 et 191, 2 octets pour le numéro d’hôte. 

Les IP commençant par 172.16.0.0. jusqu'à 172.31.255.255 sont réservés pour le local. 

C : numéro de réseau sur 3 octets ; premier octet entre 192 et 223, 1 octet pour le numéro d’hôte. 

Les IP commençant par 192.168.0.0 jusqu'à 192.168.255.255 sont réservés pour le local. 

Numéro de réseau 127 : réservé pour sa propre machine. 

D: De 224 jusqu'à 239
E: de 240 a 255


IP / 24 -> notation CIDR pour identifier le masque de sous-réseau

Calcul binaire:
192 en binaire : 1100 0000 car 128 + 64 (les deux premiers chiffres de l'octet)

VLSM : masque de sous réseau a longueur variable

![[bande_adresses_IP.png]]