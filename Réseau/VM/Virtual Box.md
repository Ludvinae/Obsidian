[[Virtual machine]]

```ad-seealso
[**Tuto Virtual Box**](https://www.it-connect.fr/comprendre-les-differents-types-de-reseaux-virtualbox/)
```

On peut configurer sa VM avec plusieurs modes:
- **NAT**: la VM n'as pas d'adresse IP sur le réseau local mais une IP fixe (10.0.2.15), ce qui l'isole. Cela permet d'acceder a internet depuis la VM et de communiquer avec le réseau local de l'hôte physique. 
  Par contre, la VM est inaccessible par les autres VM installées sur l'hôte physique, ainsi que de l'exterieur du réseau local (à part avec du port-forwarding).
- **Réseau NAT**: le même principe que le NAT, mais on peut configurer les adresses IP des différentes VM pour qu'elles puissent communiquer entre elles.
  ![[virtualbox-schema-reseau-nat.png]]
- **Pont**: la VM fait partie du réseau local, comme si c'était une machine physique. Elle peut donc accéder a internet et être accéder depuis l'exterieur.
- **Hôte**: le réseau de la VM est isolé, il peut uniquement accéder a l'hôte physique.