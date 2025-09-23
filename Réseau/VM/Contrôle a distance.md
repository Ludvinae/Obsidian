[[Virtual machine]]
[[Linux]]

On peut exécuter **`apt intall openssh-server`** sur notre VM pour installer un outil pour prendre le contrôle de notre VM à distance de façon sécurisée.

Pour cela, on lance la commande  suivante depuis le terminal (ou l'invite de commande):
```ad-important
\# **ssh user@ip**
ex: `ssh root@127.0.0.1`
```

Toutefois, on a besoin de configurer la *redirection de ports* sur VirtualBox, afin de pouvoir communiquer avec la VM malgré le mode de réseau NAT:
Dans la configuration de la VM, partie réseau, on click sur "Redirection de port", puis on rentre les valeurs suivantes:
- Nom : SSH (ou autre chose, c'est purement indicatif)
- Protocole: TCP
- IP Hôte : 127.0.0.1 (correspond au localhost)
- Port Hôte: 22 (le port de communication du protocole SSH)
- IP invité: 10.0.2.15 (de base, peut varier en réseau NAT)
- Port invité : 22

Lorsque l'on installe openSSH, la contrôle du SuperUser est par défaut désactivée. Il faut donc rajouter une option dans le fichier de configuration afin de permettre de se connecter en root.
```ad-info
\# **nano /etc/ssh/sshd_config**
On rajoute la ligne suivante sous "Authentication":
PermitRootLogin yes
```
