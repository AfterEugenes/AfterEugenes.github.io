---
layout: privacy-doc
title: Matrix
description: ''
excerpt: ''
date: 2026-09-08T16:33
platform: privacy
permalink: /privacy/messaging/matrix/
category: Messaging
tags:
- Privacy
- Messaging
---

{% raw %}

# Matrix
## TL;DR
Le but est d'avoir une messagerie fédérée pour échanger des messages dans des communautés. La cryptographie en elle-même est correcte mais pas exceptionnelle, l'ego des développeurs les empêche apparemment d'avancer et corriger leurs erreurs et certaines options sont à revoir pour avoir quelque chose de privé ou agréable à utiliser.

## Analyse
Matrix se présente comme un service orienté vers les communautés, qui permet de joindre des communautés de toutes origines (skype, discord, signal, etc) en une seule application via des réseaux *fédérés*.

Le protocole et l'idée, en eux-même, n'ont pas l'air trop mal du tout. Ils ont l'air d'attacher une certaine importance à l'idée de vie privée et notamment de la développer avec cette idée de messagerie fédérée. En plus de ça leur application est centrée autour de leurs *bridges* qui permettent de connecter une room matrix à beaucoup d'autres types d'applications. Un autre point intéressant est l'absence d'information importante lors de l'inscription, matrix n'a besoin ni d'email ni de numéro de téléphone, rien du tout.

Le problème est que c'est un service trop dispersé, à vouloir tout faire il ne fait pas grand chose de bien. De plus, ils se démarquent un peu des derniers en corrigeant certains bugs mais n'ont pas pour autant réinventé la roue. Du côté de la protection, elle est suffisante dans beaucoup de cas mais a quand même des lacunes.

Déjà, les messages sont envoyés de bout en bout par TLS, c'est la seule sécurité qui existe par défaut. Certes cela permet de cacher certaines parties du message mais pas tout. Un tiers qui écoute sur le réseau obtient ainsi des métadonnées. En plus de ça, l'encryption E2EE est disponible, mais optionnelle, ce qui est sensiblement embêtant, ça fait notamment que, par défaut, les serveurs impliqués peuvent tout à fait lire les messages, ce qui est notamment embêtant quand matrix.org est hôte pour plus de 30% des utilisateurs. 

Le plus gros problème de cette application est les métadonnées. Entre celles collectées pour l'amélioration des services, celles collectées pour transmettre les messages ou celles collectées lors de l'inscription d'un utilisateur, tout est log. Alors certains pourraient vous dire que si l'on a rien à se reprocher, on a rien à craindre, auquel cas j'aimerais vous rappeler que oui c'est vrai en un sens mais aussi que "big brother is watching you", eux aussi n'avaient rien à cacher... Cela va jusqu'à leur obtenir le surnom d'"éponge à métadonnées" par un utilisateur reddit, surnom largement mérité en mon opinion. Pour couronner le tout un bon 30% des connexions se font sur les serveurs principaux de matrix ou sur leur application principale qui, si je comprends bien, force les utilisateurs à s'inscrire sur le réseau principal, recentralisant donc le service.

En plus de ça la mentalité des développeurs est problématique. Ils sont lents, n'arrivent pas vraiment à faire décoller leur application, qui a pourtant maintenant 6 ans, choisissent de développer le côté pratique plutôt que la sécurité et, plutôt que d'accepter leurs problèmes de leur application, ont l'air de tout tenter pour blâmer les autres et les enfoncer, tout en ayant une idée glorifiée de leur travail. Il faudrait leur donner encore du temps pour leur permettre de développer un meilleur protocole, pour leur donner le temps de s'atteler à une meilleure sécurité mais a-t-on vraiment besoin de tant d'années pour se jeter des lauriers pas mérités?
{% endraw %}
