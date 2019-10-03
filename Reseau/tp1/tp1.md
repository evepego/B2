# TP1 : Back to basics

# I. Gather informations

* 🌞 récupérer une **liste des cartes réseau** avec leur nom, leur IP et leur adresse MAC
```bash
[centos8@localhost ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:53:5f:73 brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic noprefixroute enp0s3
       valid_lft 85647sec preferred_lft 85647sec
    inet6 fe80::4ad6:a897:e477:132f/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:1c:84:f6 brd ff:ff:ff:ff:ff:ff
    inet 192.168.63.6/24 brd 192.168.63.255 scope global dynamic noprefixroute enp0s8
       valid_lft 1046sec preferred_lft 1046sec
    inet6 fe80::6aeb:993b:6184:6827/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
[centos8@localhost ~]$
```

* 🌞 déterminer si les cartes réseaux ont récupéré une **IP en DHCP** ou non
```bash
[centos8@localhost ~]$ sudo nmcli -f DHCP4 con show enp0s3
DHCP4.OPTION[1]:                        domain_name = auvence.co
DHCP4.OPTION[2]:                        domain_name_servers = 10.33.10.20 10.33>
DHCP4.OPTION[3]:                        expiry = 1569589165
DHCP4.OPTION[4]:                        ip_address = 10.0.2.15
DHCP4.OPTION[5]:                        requested_broadcast_address = 1
DHCP4.OPTION[6]:                        requested_dhcp_server_identifier = 1
DHCP4.OPTION[7]:                        requested_domain_name = 1
DHCP4.OPTION[8]:                        requested_domain_name_servers = 1
DHCP4.OPTION[9]:                        requested_domain_search = 1
DHCP4.OPTION[10]:                       requested_host_name = 1
DHCP4.OPTION[11]:                       requested_interface_mtu = 1
DHCP4.OPTION[12]:                       requested_ms_classless_static_routes = 1
DHCP4.OPTION[13]:                       requested_nis_domain = 1
DHCP4.OPTION[14]:                       requested_nis_servers = 1
DHCP4.OPTION[15]:                       requested_ntp_servers = 1
DHCP4.OPTION[16]:                       requested_rfc3442_classless_static_rout>
DHCP4.OPTION[17]:                       requested_routers = 1
DHCP4.OPTION[18]:                       requested_static_routes = 1
DHCP4.OPTION[19]:                       requested_subnet_mask = 1
DHCP4.OPTION[20]:                       requested_time_offset = 1
DHCP4.OPTION[21]:                       requested_wpad = 1
DHCP4.OPTION[22]:                       routers = 10.0.2.2
DHCP4.OPTION[23]:                       subnet_mask = 255.255.255.0

[centos8@localhost ~]$ sudo nmcli -f DHCP4 con show Wired\ connection\ 1
DHCP4.OPTION[1]:                        expiry = 1569506968
DHCP4.OPTION[2]:                        ip_address = 192.168.63.6
DHCP4.OPTION[3]:                        requested_broadcast_address = 1
DHCP4.OPTION[4]:                        requested_dhcp_server_identifier = 1
DHCP4.OPTION[5]:                        requested_domain_name = 1
DHCP4.OPTION[6]:                        requested_domain_name_servers = 1
DHCP4.OPTION[7]:                        requested_domain_search = 1
DHCP4.OPTION[8]:                        requested_host_name = 1
DHCP4.OPTION[9]:                        requested_interface_mtu = 1
DHCP4.OPTION[10]:                       requested_ms_classless_static_routes = 1
DHCP4.OPTION[11]:                       requested_nis_domain = 1
DHCP4.OPTION[12]:                       requested_nis_servers = 1
DHCP4.OPTION[13]:                       requested_ntp_servers = 1
DHCP4.OPTION[14]:                       requested_rfc3442_classless_static_rout>
DHCP4.OPTION[15]:                       requested_routers = 1
DHCP4.OPTION[16]:                       requested_static_routes = 1
DHCP4.OPTION[17]:                       requested_subnet_mask = 1
DHCP4.OPTION[18]:                       requested_time_offset = 1
DHCP4.OPTION[19]:                       requested_wpad = 1
DHCP4.OPTION[20]:                       subnet_mask = 255.255.255.0
```


* 🌞 afficher la **table de routage** de la machine et sa **table ARP**
#### Table de routage :
```bash
[centos8@localhost ~]$ ip route
default via 10.0.2.2 dev enp0s3 proto dhcp metric 100
10.0.2.0/24 dev enp0s3 proto kernel scope link src 10.0.2.15 metric 100
192.168.63.0/24 dev enp0s8 proto kernel scope link src 192.168.63.6 metric 101
```
ligne 1 : cette route est vers le réseau XXX (nom + adresse réseau), elle est utilisée pour une connexion (locale|externe), la passerelle de cette route est à l'IP XXX et cette IP est portée par XXX  
ligne 2 : cette route est vers le réseau XXX (nom + adresse réseau), elle est utilisée pour une connexion (locale|externe), la passerelle de cette route est à l'IP XXX et cette IP est portée par XXX  
ligne 3 :cette route est vers le réseau XXX (nom + adresse réseau), elle est utilisée pour une connexion (locale|externe), la passerelle de cette route est à l'IP XXX et cette IP est portée par XXX
#### Table ARP :
```bash
[centos8@localhost ~]$ arp -an
? (10.0.2.2) at 52:54:00:12:35:02 [ether] on enp0s3
? (192.168.63.1) at 0a:00:27:00:00:07 [ether] on enp0s8
? (192.168.63.2) at 08:00:27:96:8c:82 [ether] on enp0s8
```
ligne 1 : cette route est vers le réseau XXX (nom + adresse réseau), elle est utilisée pour une connexion (locale|externe), la passerelle de cette route est à l'IP XXX et cette IP est portée par XXX  
ligne 2 : cette route est vers le réseau XXX (nom + adresse réseau), elle est utilisée pour une connexion (locale|externe), la passerelle de cette route est à l'IP XXX et cette IP est portée par XXX  
ligne 3 :cette route est vers le réseau XXX (nom + adresse réseau), elle est utilisée pour une connexion (locale|externe), la passerelle de cette route est à l'IP XXX et cette IP est portée par XXX


* 🌞 récupérer **la liste des ports en écoute** (*listening*) sur la machine (TCP et UDP)
```bash
[centos8@localhost ~]$ netstat -atu
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN
tcp        0     64 localhost.localdoma:ssh 192.168.63.1:51255      ESTABLISHED
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN
```

* 🌞 récupérer **la liste des DNS utilisés par la machine**
```bash
[centos8@localhost ~]$ command nmcli device show enp0s3
IP4.DNS[1]:                             10.33.10.20
IP4.DNS[2]:                             10.33.10.2
IP4.DNS[3]:                             8.8.8.8
IP4.DNS[4]:                             8.8.4.4
```
  * effectuez une requête DNS afin de récupérer l'adresse IP associée au domaine `www.reddit.com` ~~(parce que c'est important d'avoir les bonnes adresses)~~
  * dans le retour de cette requête DNS, vérifier que vous utilisez bien les bons DNS renseignés sur votre machine

* 🌞 afficher **l'état actuel du firewall**
```bash
[centos8@localhost ~]$ systemctl status firewalld
● firewalld.service - firewalld - dynamic firewall daemon
   Loaded: loaded (/usr/lib/systemd/system/firewalld.service; enabled; vendor p>
   Active: active (running) since Thu 2019-09-26 08:59:22 EDT; 2h 20min ago
     Docs: man:firewalld(1)
 Main PID: 790 (firewalld)
    Tasks: 2 (limit: 17712)
   Memory: 29.4M
   CGroup: /system.slice/firewalld.service
           └─790 /usr/libexec/platform-python -s /usr/sbin/firewalld --nofork ->

Sep 26 08:59:20 localhost.localdomain systemd[1]: Starting firewalld - dynamic >
Sep 26 08:59:22 localhost.localdomain systemd[1]: Started firewalld - dynamic f>
```
OU
```bash
[centos8@localhost ~]$ sudo firewall-cmd --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s3 enp0s8
  sources:
  services: cockpit dhcpv6-client ssh
  ports:
  protocols:
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:

```
* Quelles interfaces sont filtrées ?  
enp0s3 et enp0s8
* Quel port TCP/UDP sont autorisés/filtrés ?   
cockpit, dhcpv6 et ssh qui est le port 22tcp

## II. Edit configuration

### 1. Configuration cartes réseau 
---

* 🌞 modifier la configuration de la carte réseau privée
```bash
[centos8@localhost ~]$ nmtui
[centos8@localhost ~]$ ip a
...
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:1c:84:f6 brd ff:ff:ff:ff:ff:ff
    inet 192.168.63.4/24 brd 192.168.63.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::6aeb:993b:6184:6827/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
```
* ajouter une nouvelle carte réseau dans un DEUXIEME réseau privé UNIQUEMENT privé
```bash
[root@localhost ~]# nmtui
[root@localhost ~]# ip a
...
4: enp0s9: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:49:32:42 brd ff:ff:ff:ff:ff:ff
    inet 192.168.10.2/24 brd 192.168.10.255 scope global noprefixroute enp0s9
       valid_lft forever preferred_lft forever
    inet6 fe80::8666:a3a7:5737:64bb/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
```
* vérifier vos changements
```bash
[root@localhost ~]# ip route
default via 10.0.2.2 dev enp0s3 proto dhcp metric 100
10.0.2.0/24 dev enp0s3 proto kernel scope link src 10.0.2.15 metric 100
192.168.10.0/24 dev enp0s9 proto kernel scope link src 192.168.10.2 metric 102
192.168.63.0/24 dev enp0s8 proto kernel scope link src 192.168.63.4 metric 101
[root@localhost ~]# arp -an
? (10.0.2.2) at 52:54:00:12:35:02 [ether] on enp0s3
? (192.168.63.1) at 0a:00:27:00:00:08 [ether] on enp0s8
```
* 🐙 mettre en place un NIC *teaming* (ou *bonding*)
  * il vous faut deux cartes dans le même réseau puisque vous allez les agréger (vous pouvez en créer de nouvelles)
  * le *teaming* ou *bonding* consiste à agréger deux cartes réseau pour augmenter les performances/la bande passante
  * je vous laisse free sur la configuration (active/passive, loadbalancing, round-robin, autres)
  * prouver que le NIC *teaming* est en place

---

### 2. Serveur SSH

* 🌞 modifier la configuration du système pour que le serveur SSH tourne sur le port 2222
  * adapter la configuration du firewall (fermer l'ancien port, ouvrir le nouveau)
* pour l'étape suivante, il faudra un hôte qui ne s'est jamais connecté à la VM afin d'observer les échanges ARP (vous pouvez aussi juste vider la table ARP du client). Je vous conseille de faire une deuxième VM dans le même réseau, mais vous pouvez utiliser votre PC hôte.
* 🌞 analyser les trames de connexion au serveur SSH
  * intercepter avec Wireshark et/ou `tcpdump` le trafic entre le client SSH et le serveur SSH
  * détailler l'établissement de la connexion
    * doivent figurer au moins : échanges ARP, 3-way handshake TCP
    * 🐙 configurer une connexion par échange de clés, analyser les échanges réseau réalisés par le protocole SSH au moment de la connexion
  * une fois la connexion établie, choisir une trame du trafic SSH et détailler son contenu

# III. Routage simple

Dans cette partie, vous allez remettre en place un routage statique simple. Vous êtes libres du choix de la techno (CentOS8, Cisco, autres. Vous pouvez utiliser GNS3). 

Vous devez reproduire la mini-archi suivante : 
```
                   +-------+
                   |Outside|
                   | world |
                   +---+---+
                       |
                       |
+-------+         +----+---+         +-------+
|       |   net1  |        |   net2  |       |
|  VM1  +---------+ Router +---------+  VM2  |
|       |         |        |         |       |
+-------+         +--------+         +-------+
```

* **Description**
  * Le routeur a trois interfaces, dont une qui permet de joindre l'extérieur (internet)
  * La `VM1` a une interface dans le réseau `net1`
  * La `VM2` a une interface dans le réseau `net2`
  * Les deux VMs peuvent joindre Internet en passant par le `Router`
* 🌞 **To Do** 
  * Tableau récapitulatif des IPs
  * Configuration (bref) de VM1 et VM2
  * Configuration routeur
  * Preuve que VM1 passe par le routeur pour joindre internet
  * Une (ou deux ? ;) ) capture(s) réseau ainsi que des explications qui mettent en évidence le routage effectué par le routeur

# IV. Autres applications et métrologie

Dans cette partie, on va jouer un peu avec de nouvelles commandes qui peuvent être utiles pour diagnostiquer un peu ce qu'il se passe niveau réseau.

---

## 1. Commandes

* jouer avec `iftop`
  * expliquer son utilisation et imaginer un cas où `iftop` peut être utile

---

## 2. Cockpit

* 🌞 mettre en place cockpit sur la VM1
  * c'est quoi ? C'est un service web. Pour quoi faire ? Vous allez vite comprendre en le voyant.
  * `sudo dnf install -y cockpit`
  * `sudo systemctl start cockpit`
  * trouver (à l'aide d'une commande shell) sur quel port (TCP ou UDP) écoute Cockpit 
  * vérifier que le port est ouvert dans le firewall
* 🌞 explorer Cockpit, plus spécifiquement ce qui est en rapport avec le réseau

---

## 3. Netdata

Netdata est un outil utilisé pour récolter des métriques et envoyer des alertes. Il peut aussi être utilisé afin de visionner ces métriques, à court terme. Nous allons ici l'utiliser pour observer les métriques réseau et mettre en place un service web supplémentaire.

* 🌞 mettre en place Netdata sur la VM1 et la VM2
  * se référer à la documentation officielle
  * repérer et ouvrir le port dédié à l'interface web de Netdata
* 🌞 explorer les métriques liées au réseau que récolte Netdata