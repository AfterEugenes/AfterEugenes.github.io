---
title: Browsers
description:
tags:
-
date: 2026-09-08T16:34
category:
  - privacy
---

### Tor
[Can law enforcement track Tor users - comprehensive analysis article](https://factually.co/fact-checks/technology/can-law-enforcement-track-tor-users-onion-sites-6898a6)
[The reality of timing correlation attacks on Tor. - comprehensive article](https://factually.co/fact-checks/technology/timing-correlation-attacks-tor-circuits-defenses-b39c41)
[Recommendations for tor over vpn - factually again](https://factually.co/fact-checks/technology/should-tor-users-run-vpn-with-tor-reduce-deanonymization-risk-ffdbd3)

[Arma's message on deauthentication attacks (the one in germany) - forum](https://forum.torproject.org/t/tor-relays-important-update-on-an-upcoming-german-broadcasting-story-about-tor-onion-services/14656/3)

[Traffic analysis to identify Tor users (and their traffic) - research paper](https://www.freehaven.net/anonbib/cache/murdoch-pet2007.pdf)
[Arrests of Tor users, cases study - research paper](https://dl.gi.de/server/api/core/bitstreams/60051049-690c-4dd3-bd17-a4e9f7c490f9/content)
[Comprehensive study of Tor deanonymization attacks - research paper](https://www.atlantis-press.com/article/126025317.pdf)
[Congestion attacks on Tor - research paper](https://www.freehaven.net/anonbib/papers/congestion-longpaths.pdf)
[Untraceable electronic emails and mixnet - David L. Chaum research paper](https://dl.acm.org/doi/pdf/10.1145/358549.358563?download=true)

VPN:

Tor est sensible majoritairement dans le cas où une personne contrôle deux nœuds: celui d'entrée et celui de sortie. De cette façon la personne peut corréler les connexions entrantes et sortantes et associer une adresse IP à des recherches ou connexions. Cette attaque est appelée "timing correlation attack", elle rentre dans la catégorie des "deanonymization attack". Une fois les noeuds contrôllés il s'agit en fait de faire une étude probabiliste pour remonter à la source.

De la même façon il est possible de prendre le contrôle de l'ISP plutôt que du noeud d'entrée, ce qui est clairement plus déterministe.

Les limitations de cette attaque sont:
- Obtenir d'une connexion d'avoir le contrôle des deux noeuds est improbable.
- Comme il suffit d'avoir une seule fois la connexion pour incriminer quelqu'un, Tor a mis en place les "guard nodes" (rotation plus lente, garantit plus longtemps l'anonymat).
- Elle nécessite des moyens immense en réalité et pas toujours très légaux et beaucoup de temps, n'ayant ainsi pris place que 2 fois connues en réalité.

D'autres attaques sont possibles mais visent généralement à désanonymiser un seul nœud ou identifier si un utilisateur utilise un nœud en particulier mais ces attaques utilisent généralement des ressources absurdes pour ne pas vraiment désanonymiser l'utilisateur.

Browser:

Le browser met en place plusieurs mesures pour que tous les utilisateurs se ressemblent. Les principales sont la tailles de l'écran, la résolution, la gestion de certaines images, etc. Récemment les data aggregator et autres vautours ont commencé à développer l'identification par IA, qui donne des résultats bien plus intéressants que ce qui pouvait être déduit d'un browser jusqu'ici. Cela se base notamment sur les données envoyées (timing, taille, etc). Les développeurs de Tor sont justement en train de développer des méthodes de plus en plus efficaces pour s'en protéger.

### Mullvad
[No log policy review](https://factually.co/fact-checks/technology/is-mullvad-vpn-really-no-logs-2025-92189c)
[Police raid on mullvad VPN leaves empty-handed](https://www.techradar.com/news/mullvads-no-log-policy-proven-after-police-raid)
[Theory on DAITA - research paper](https://dl.acm.org/doi/pdf/10.1145/3603216.3624953?download=true)

VPN:

Mullvad VPN met en avant l'absence totale de stockage de données. Les seules données stockées sont les associations entre les numéros de compte et le temps restant, ils regardent aussi combien d'appareils sont connectés simultanément. Au-delà de ça, rien n'est stocké, rien ne reste, en théorie. Comme il est impossible de vérifier si en effet les données ne passent que par la ram, le problème est la confiance.

Comme pour tout autre VPN, la faille majeure est la possibilité que l'état (ou autre) accède aux données du VPN, par des moyens légaux (ou non).

Dans le cas de mullvad, on ne pourra jamais être sûr que tout passe bien par la ram mais:
- Mullvad VPN a fait à plusieurs reprises des expertises par des entreprises indépendantes, chaque fois aucun problème n'a été trouvé.
- La police (suédoise?) a eu pour ordre une fois d'aller dans les locaux de mullvad pour récupérer les données mais est repartie sans même toucher aux serveurs après que Mullvad VPN les ait assuré que rien n'était dans les données et donc qu'ils n'avaient le droit de rien saisir.
- Mullvad VPN nous rappelle régulièrement, notamment via des communications officielles, leurs valeurs et ce qu'ils mettent en place pour s'y tenir.

Il serait aussi techniquement possible de désanonymiser l'utilisateur en ayant le contrôle de l'ISP et de l'ISP du site cible mais cela requiert encore une fois des moyens absurdes, plus que pour Tor.

Il est possible d'acheter des cartes cadeau pour mullvad VPN via amazon, ce qui permet l'anonymat, plus rapidement qu'avec des cryptomonnaies, en revanche cela vient avec le coût de dire à amazon qu'on achète une carte cadeau mullvad VPN.

Browser:

Le browser en lui-même a été développé en collaboration avec Tor Project pour proposer un browser sécurisé. Bien que manquant certaines des fonctionnalités qui rendent Tor presque invulnérable, Mullvad browser propose nombre de fonctionnalités proches et très efficaces, le rendant sensiblement aussi robuste.

Dans la lutte contre l'ia, Mullvad Browser propose DAITA, qui, de la même façon qu'avec Tor, modifie les paquets pour les rendre impossible à tracer.
