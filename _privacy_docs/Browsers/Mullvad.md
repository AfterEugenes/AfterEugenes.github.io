---
layout: privacy-doc
title: Mullvad
description: Mullvad
excerpt: Mullvad
date: 2026-09-08T18:49
platform: privacy
permalink: /privacy/browsers/mullvad/
category: Browsers
tags:
- Privacy
- Browsers
---

{% raw %}


### Mullvad VPN
Mullvad VPN met en avant l'absence totale de stockage de données. Les seules données stockées sont les associations entre les numéros de compte et le temps restant, ils regardent aussi combien d'appareils sont connectés simultanément. Au-delà de ça, rien n'est stocké, rien ne reste, en théorie. Comme il est impossible de vérifier si en effet les données ne passent que par la ram, le problème est la confiance. [^mullvadnolog]

Comme pour tout autre VPN, la faille majeure est la possibilité que l'état (ou autre) accède aux données du VPN, par des moyens légaux (ou non).

Dans le cas de mullvad, on ne pourra jamais être sûr que tout passe bien par la ram mais:
- Mullvad VPN a fait à plusieurs reprises des expertises par des entreprises indépendantes, chaque fois aucun problème n'a été trouvé. [^mullvadpoliceraid]
- La police (suédoise?) a eu pour ordre une fois d'aller dans les locaux de mullvad pour récupérer les données mais est repartie sans même toucher aux serveurs après que Mullvad VPN les ait assuré que rien n'était dans les données et donc qu'ils n'avaient le droit de rien saisir.
- Mullvad VPN nous rappelle régulièrement, notamment via des communications officielles, leurs valeurs et ce qu'ils mettent en place pour s'y tenir.

Il serait aussi techniquement possible de désanonymiser l'utilisateur en ayant le contrôle de l'ISP et de l'ISP du site cible mais cela requiert encore une fois des moyens absurdes, plus que pour Tor.

Il est possible d'acheter des cartes cadeau pour mullvad VPN via amazon, ce qui permet l'anonymat, plus rapidement qu'avec des cryptomonnaies, en revanche cela vient avec le coût de dire à amazon qu'on achète une carte cadeau mullvad VPN.

Browser:

Le browser en lui-même a été développé en collaboration avec Tor Project pour proposer un browser sécurisé. Bien que manquant certaines des fonctionnalités qui rendent Tor presque invulnérable, Mullvad browser propose nombre de fonctionnalités proches et très efficaces, le rendant sensiblement aussi robuste.

Dans la lutte contre l'ia, Mullvad Browser propose DAITA, qui, de la même façon qu'avec Tor, modifie les paquets pour les rendre impossible à tracer. [^mullvaddaita]

[^mullvadnolog]: [No log policy review](https://factually.co/fact-checks/technology/is-mullvad-vpn-really-no-logs-2025-92189c)
[^mullvadpoliceraid]:[Police raid on mullvad VPN leaves empty-handed](https://www.techradar.com/news/mullvads-no-log-policy-proven-after-police-raid)
[^mullvaddaita]: [Theory on DAITA - research paper](https://dl.acm.org/doi/pdf/10.1145/3603216.3624953?download=true)
{% endraw %}
