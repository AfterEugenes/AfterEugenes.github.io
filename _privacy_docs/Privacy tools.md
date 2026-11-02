---
layout: privacy-hub
title: Privacy tools
description: ''
excerpt: ''
date: 2026-09-19T21:43
platform: privacy
permalink: /privacy/privacy-tools/
category: Privacy tools
tags:
- Privacy
- Privacy tools
---

{% raw %}
Legend:
- [ ] Work is left to do
- [x] Accepted as the better option
- [<] Accepted but there is a better option
- [-] Rejected as an option entirely
- [?] Still lacking information to decide
(in this case, time might allow for better results)
- [>] Information yields both positive and negative results
(in this case, time might allow for better results)
- [n] Marked for later: service is new and information is scarce, if any, but results are promising
- [.] Still need time to decide/ongoing rabbit hole/information is difficult and annoying to find

- [ ] 
- [x] 
- [-] 
- [?] 
- [!] 
- [>] 
- [<] 
- [/] 
- [*] 
- [.] 
- [$] 
- ["] 
- [+] 
- [i] 
- [w] 
- [r] 
- [t] 
- [u] 
- [p] 
- [d] 
- [f] 
- [k] 
- [l] 
- [m] 
- [c] 
- [b] 
- [n] 
- [T] 
- [U] 
- [I] 
- [P] 
- [S] 
- [D] 
- [F] 
- [L] 
- [M] 
- [W] 

# Préambule

- Meilleurs services
	- [x] Browsing
		- [x] <a class="obsidian-link" href="#tor">Tor</a>
		- [x] <a class="obsidian-link" href="#mullvad">Mullvad</a> Browser
	- [ ] VPN
		- [ ] Mullvad VPN
	- [ ] Mail
	- [ ] Messages (group and direct)
		- [ ] <a class="obsidian-link" href="#signal">Signal</a>
	- [x] Cryptocurrency
		- [x] <a class="obsidian-link" href="#monero">Monero</a>
		- [?] <a class="obsidian-link" href="#feather-wallet">Feather wallet</a>
		- [?] <a class="obsidian-link" href="#haveno">Haveno</a>
		- [?] <a class="obsidian-link" href="#retoswap">RetoSwap</a>
- Autres options
	- [ ] Browsing
	- [ ] VPN
	- [ ] <a class="obsidian-link" href="#secure-messaging">secure messaging</a>
		- [n] <a class="obsidian-link" href="#rvnt">RVNT</a>
	- [ ] <a class="obsidian-link" href="#cryptocurrencies">Cryptocurrencies</a>
		- [ ] Blockchains
		- [ ] <a class="obsidian-link" href="#monero-nodes">Monero nodes</a>
			- [ ] <a class="obsidian-link" href="#monerod">Monerod</a>
		- [ ] <a class="obsidian-link" href="#monero-wallets">Monero wallets</a>
			- [ ] <a class="obsidian-link" href="#monero-gui">Monero GUI</a>
			- [ ] <a class="obsidian-link" href="#cake-wallet">Cake wallet</a>
		- [ ] <a class="obsidian-link" href="#monero-funds">Monero funds</a>
			- [ ] <a class="obsidian-link" href="#monero-gift-cards">Monero gift cards</a>
	- [ ] <a class="obsidian-link" href="#vpn">VPN</a>
	- [ ] <a class="obsidian-link" href="#email">email</a>
		- [ ] <a class="obsidian-link" href="#throaway-email-long-lived">Throaway email (long-lived)</a>
		- [ ] <a class="obsidian-link" href="#throaway-email-short-lived">Throaway email (short-lived)</a>
	- [ ] <a class="obsidian-link" href="#phone-service">Phone service</a>
	- [ ] <a class="obsidian-link" href="#protecting-against-isp">Protecting against ISP</a>
	- [ ] <a class="obsidian-link" href="#os-security">OS security</a>
	- [ ] <a class="obsidian-link" href="#ansible-for-local-stack">Ansible for local-stack?</a>
	- [ ] <a class="obsidian-link" href="#sudos">Sudos</a>
- Autres catégories
	- [ ] Freetube/PipePipe

Avec le développement d'internet et sa conception actuelle, les achats et ventes de services ne sont plus suffisant pour faire tourner ces machines à sous, ces monstres à données. Géants du web, *data brokers*, agences gouvernementales, pour chacun d'entre eux vos données sont devenues le centre des opérations. Que ce soit pour vous faire acheter un produit, influencer les décisions de vote ou encore vous traquer, rien n'est sacré.

Bien que je pourrais rentrer dans les détails et continuer, cela me semble inutile quand Mullvad VPN a écrit un si bon article sur tout ce que ces entreprises sont prêtes à faire pour récupérer vos infos et pourquoi votre vie privée est importante.
[Total surveillance - Mullvad VPN](https://mullvad.net/pdfs/Total_surveillance.pdf)

La vie privée est, plus qu'une légende qu'un informaticien raconte à ses enfants avant qu'ils s'endorment, un droit. Pour certaines personnes comme les activistes, les *whistle blowers* et les personnes recherchées (svp ne traffiquez pas de drogue, c'est dangereux la drogue), la vie privée est encore plus, elle représente une sécurité, une assurance 

# Validated services

### Tor
- [x] Tor
	- [x] Logging *per documentation*
	- [x] Privacy *per documentation*
	- [x] Deanonymization
		- [x] Possible deanonymization attacks
		- [x] Legal cases of deanonymization attacks
		- [x] Details on Timing attacks
- [ ] Further readings

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
- [x] Mullvad
	- [x] Logging *per documentation*
	- [x] Privacy *per documentation*
	- [x] Deanonymization
		- [x] Legal cases against stored data
		- [x] Anonymization brought *per documentation*
		- [x] Deanonymization possibilities
- [ ] Further readings
	- [x] Better than Tor?
	- [x] Gift cards

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


### Signal
- [ ] Signal
	- [x] Logging *per documentation*
	- [x] Privacy *per documentation*
	- [ ] Deanonymization
		- [x] Legal cases
		- [ ] Tracebility
- [ ] Further readings

[Attaque sur Signal - official website](https://support.signal.org/hc/en-us/articles/4850133017242-Twilio-Incident-What-Signal-Users-Need-to-Know)
[Double ratchet algorithm - official website](https://signal.org/docs/specifications/doubleratchet/)
[Subpoenas aiming Signal - official website](https://signal.org/bigbrother/central-california-grand-jury/)
[Signal's principles (official website)](https://signal.org/blog/looking-back-as-the-world-moves-forward/)
[Signal's sealed sender - official website](https://signal.org/blog/sealed-sender/)
[Signal's private profiles - official website](https://signal.org/blog/signal-profiles-beta/)
[Signal protocols - official documentation](https://signal.org/blog/spqr/)
[Phone numbers privacy - official documentation](https://support.signal.org/hc/en-us/articles/6712070553754-Phone-Number-Privacy-and-Usernames)

[Legal orders on Signal - official website](https://signal.org/bigbrother/)
[List of third-party security audits - official website](https://community.signalusers.org/t/overview-of-third-party-security-audits/13243)
[Subpoena case on signal - official documentation](https://signal.org/bigbrother/cd-california-grand-jury/)

[Signal's code deep-dive - technical doc](https://deepwiki.com/signalapp/Signal-Server/4.1-message-controllers-and-routing)
[On signal's ability to know who is talking to who - article](https://sanesecurityguy.com/articles/signal-knows-who-youre-talking-to/)
[Security audit on Signal - independant audit](https://positive-intentions.com/docs/research/Security%20audit/signal-protocol-security-audit/)
[Analysis of signal protocol - research paper](https://eprint.iacr.org/2016/1013.pdf)
[Why is Signal so secure? - article](https://aboutsignal.com/signal-security-privacy-guide/)

Signal possède bien une license AGPLv3.0.

La théorie: Signal est une application largement tournée vers la vie privée. Tout ce qui est important (contacts, données personnelles, clés, messages, ...) est stocké sur l'appareil de l'utilisateur, nulle part ailleurs. Les seules informations stockées sur les serveurs sont le numéro de l'utilisateur, la date de création de son compte et la dernière date de connexion, tout le reste n'est que sur votre appareil, nulle part ailleurs. Certains articles mettent justement l'accent sur l'importance qu'ils accordent aux profils privés. En plus de ça Signal a développé le "**sealed sender**", qui permet normalement de cacher qui envoie un message (sauf pour le premier message.

La pratique: En pratique oui, Signal ne log rien du tout, certains cas d'intervention de la justice le prouvent d'ailleurs, ce qui renforce ce que signal dit de son système. En revanche cela ne signifie pas que tout est imperméable à l'identification. Chaque personne qui reçoit des messages doit toujours les faire transiter par les serveurs de signal. Utiliser Signal sans utiliser de VPN pourrait leur permettre de log les *IP*s, en théorie. De plus, Signal est *a fortiori* digne de confiance, prouvé par les nombreuses tentatives de la justice d'obtenir plus d'infos que ce qu'ils pouvaient donner.

Côté utilisateur aussi des problèmes surviennent. Le traffic n'étant pas infini, le nombre de messages reçus par une personne en particulier puis par une autre, potentiellement liée à cette première personne ou non, peuvent être corrélés. Il est rare que Alice reçoive 4 messages dans la journée, que Bob en reçoive 5 et que cela n'ait aucun lien. Tout cela se renforce encore lorsque l'on peut analyser les paquets qui partent vers signal ou encore les *timestamp* sur les paquets, car **Signal** n'utilise pas le **mixnet**.

En sommes, même sans que Signal faute, le gouvernement peut décider de tracer des utilisateurs. Dans l'idée, un utilisateur pourrait se protéger de corrélations en utilisant un **VPN**.

***Cela reste à prouver. En plus, potentiellement Signal peut associer l'IP utilisée depuis le départ pour envoyer au numéro (ou delivery token) auquel est renvoyé le message de réponse, ce qui leur permet de faire une association, et donc de vous identifier à un utilisateur de tor ou d'un vpn quelconque.***
{% endraw %}
