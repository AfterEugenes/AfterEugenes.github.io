---
layout: privacy-doc
title: Proton
description: Proton caca
excerpt: Proton caca
date: 2026-09-08T23:36
platform: privacy
permalink: /privacy/mails/proton/
category: Mails
tags:
- Privacy
- Mails
---

{% raw %}

### Proton mail
[Betraying the users](https://factually.co/fact-checks/technology/does-protonmail-log-ip-addresses-session-information-c42f3c)
[Video about proton selling the data from users and abusing their non profit image](https://www.youtube.com/watch?v=xFKSKjyBVDU)

Mails:

Proton mail, en théorie, ne conserve aucune donnée excepté celles nécessaires pour les mails. C'est, à une exception près, vrai. Ils ne conservent que les données nécessaires pour envoyer ou recevoir les mails. Il faut bien prendre en compte cependant que si un mail vous identifie clairement, il est alors possible de lier le mail à votre compte.

Proton encrypte tous les mails. Le corps du mail est encrypté en End to End (E2EE), le sujet, le destinataire et l'expéditeur sont encryptés (avec quelle encryption?) mais pas end-to-end. Enfin, le tout est stocké en zero-access, ce qui signifie que le tout est seulement accessible sur notre appareil et que personne ne peut le lire à moins de posséder notre clé privée.

Mais: (et il est gros)
- Déchiffrer la ligne du sujet, bien que difficile, n'est pas impossible.
- D'autres services de mail comme gmail n'utilise pas E2EE, ce qui signifie que les serveurs de proton reçoivent le mail et peuvent le lire avant de vous l'envoyer. Cela demande de leur faire confiance.
- Les mails sont zero-encrypted mais seulement en local, il est toujours nécessaire que proton lise les mails pour vous les envoyer.
- Enfin la partie problématique: proton assure garder l'IP de la personne se connectant dans le cas de l'activation d'une option désactivée par défaut. En revanche, il se trouve que dans certains cas des preuves sont disponibles montrant que Proton a bel et bien traqué l'IP d'une personne sans son accord. Proton prétend avoir obéit au gouvernement dans ce cas, il n'empêche qu'ils ont enregistré son IP sans qu'il le sache et l'ont donné au gouvernement. (cas de l'activiste français)

En bref, on ne peut pas faire confiance à Proton mais certaines parties demande de leur faire confiance, c'est un peu contradictoire.
{% endraw %}
