---
layout: privacy-doc
title: RVNT
description: ''
excerpt: ''
date: 2026-09-08T16:34
platform: privacy
permalink: /privacy/messaging/rvnt/
category: Messaging
tags:
- Privacy
- Messaging
---

{% raw %}

# RVNT
## TL;DR
RVNT a pour but de créer une messagerie privée, sécurisée, p2p. Ils insistent fort sur la vie privée et la sécurité et promettent d'utiliser certains protocoles très, très intéressants, qui en feraient peut-être la messagerie la plus sécurisée. L'application elle-même n'ayant pas encore de release open-source auditée ou d'avis extérieur, on ne peut vérifier leurs promesses.

## Analyse
RVNT se pose comme un service de messagerie p2p dont le but n'est pas de remplacer signal mais putôt une alternative qui ne vous demanderait jamais de faire confiance à quiconque, à l'image de Tor. C'est une alternative d'autant plus utile dans des pays en guerre ou dans lesquels il est dangereux d'être reconnu.[^rvntofflinemesh]

Le service paraît phénoménal. Tout d'abord le plus évident, l'encryption. A travers l'utilisation de **double ratchet**, **tor**, **mixnet**, **sealed enveloppes**, **signing**, il semble impossible de lire quoi que ce soit, c'est à se demander comment ça peut même trouver son destinataire.[^rvntratchet][^rvntprotection] Le double hatchet protège en plus des attaquants, si un attaquant prend le contrôle d'une clé et arrive à lire un message, il ne pourra pas lire le suivant, ce qui rend toute attaque vraiment difficile si elle ne cible pas l'utilisateur directement. Grâce au **mixnet**, aux tailles de paquets et aux paquets aléatoires, même si quelqu'un analyse le réseau, il lui sera impossible de savoir ce qu'il se passe vraiment. [^rvntmixnet] Il en est de même pour la vie privée: rien ne transparaît. De l'expéditeur au contenu du message en comprenant toutes les métadonnées, il semble que les seules infos qui persistent sont les *timestamp* de connexion ainsi que les clés publiques associées aux noms d'utilisateurs. Un point bonus là-dedans est que, selon **RVNT** directement, même si un parti tiers parvenait à prendre le contrôle d'un relais, il ne pourrait absolument rien lire (ce qui est logique puisque tout est basé sur Tor).[^rvntprotection][^rvnttor]

Le réseau en lui-même a l'avantage d'être p2p, il est donc insensible aux lois gouvernementales, locales, etc. Il ne peut subir d'obligation légale, ne peut donner de secrets puisqu'il ne possède rien.[^rvntsealedsender] Comparé à un serveur fédéré ou centralisé, il est presque invincible. Ca a quand même l'inconvénient de ne pas permettre d'envoyer des messages lorsque l'un des deux est hors ligne, ce qui est corrigé par un système assez pratique: un *buffering* des messages. A voir ce que cela donne à l'avenir.[^rvntcomparison]

Entre le site web qui a l'air exhaustif sur tout ce qu'ils font et ne font pas, qui s'empresse de se comparer (honnêtement, qui plus est) aux autres services et le *warrant canary*, ils ont l'air de tenir la transparence à coeur, ce qui est d'autant plus louable.[^rvtncanary][^rvntsignal] Ils sont parfois peut-être un peu TROP exhaustifs, en plus d'un simple service de messagerie, ils ont l'air de vouloir proposer un service de payement utilisant la même méthode de contact ainsi que des méthodes pour envoyer des fichiers de toute taille! (source à vérifier, j'avais trouvé 50Go mais je ne trouve plus la phrase dans laquelle ils affirmaient ça)[^rvntfiletransfer][^rvntpayment]

En regardant les promesses seules ce service a l'air phénoménal, à voir si le développement suit.

[^rvntratchet]: [RVNT Double ratchet encryption](https://rvntos.io/docs/double-ratchet/)
[^rvntprotection]: [RVNT Network protection & zero logging policy](https://rvntos.io/docs/server/ (official documentation))
[^rvntsealedsender]: [RVNT Sealed sender](https://rvntos.io/glossary/sealed-sender/)
[^rvntmixnet]: [RVNT mixnet](https://rvntos.io/docs/mixnet/)
[^rvnttor]: [RVNT Tor integration](https://rvntos.io/docs/tor-integration/)
[^rvntcanary]:[RVNT Warrant canary](https://rvntos.io/glossary/warrant-canary/)
[^rvntsignal]:[RVNT vs Signal](https://rvntos.io/compare/rvnt-vs-signal/)
[^rvntofflinemesh]:[RVNT Offline mesh](https://rvntos.io/docs/offline-mesh/)
[^rvntfiletransfer]: [RVNT file transfer](https://rvntos.io/docs/file-transfer/)
[^rvntpayment]: [RVNT payment system](https://rvntos.io/docs/payments/)

[^rvntcomparison]: [RVNT comparison between federated, P2P and centralised](https://rvntos.io/blog/p2p-vs-federated-vs-centralized-messaging/)
{% endraw %}
