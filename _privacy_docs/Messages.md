---
layout: privacy-doc
title: Messages
description: ''
excerpt: ''
date: 2026-09-19T21:43
platform: privacy
permalink: /privacy/messages/
category: General
tags:
- Privacy
---

{% raw %}
# Index
- [ ] Messaging apps
	- [x] [[#Signal]]
	- [>] [[#Matrix]]
	- [<] [[#session]]
	- [n] [[#RVNT]]
	- [ ] rocket.chat
	- [ ] briar
	- [ ] simplex
	- [ ] xmpp
	- [ ] Tox
	- [ ] Wickr

# Introduction

Les services de messagerie sont importants ils permettent de communiquer. La différence principale réside dans la différence entre centralisé, fédéré et p2p, c'est la différence la plus conséquente sur la vie privée. [^decentralizedcomparison]

[^decentralizedcomparison]: [P2P, federated et centralized comparaison - RVNT](https://rvntos.io/blog/p2p-vs-federated-vs-centralized-messaging/)

# Contenu

## Signal
- [ ] Signal
	- [x] Logging *per documentation*
	- [x] Privacy *per documentation*
	- [x] Deanonymization
		- [x] Legal cases
		- [x] Tracebility
- [ ] Further readings

### Footnotes
#### Documentation
[Attaque sur Signal - official website](https://support.signal.org/hc/en-us/articles/4850133017242-Twilio-Incident-What-Signal-Users-Need-to-Know)
[Signal Android - github](https://github.com/signalapp/Signal-Android)
[Signal's principles (official website)](https://signal.org/blog/looking-back-as-the-world-moves-forward/)
[Signal's private profiles - official website](https://signal.org/blog/signal-profiles-beta/)
[Signal's sealed sender - official website](https://signal.org/blog/sealed-sender/)
[Signal phone numbers privacy - official documentation](https://support.signal.org/hc/en-us/articles/6712070553754-Phone-Number-Privacy-and-Usernames)
[Legal orders on Signal - official website](https://signal.org/bigbrother/)
[Signal List of third-party security audits - official website](https://community.signalusers.org/t/overview-of-third-party-security-audits/13243)
[Subpoenas aiming Signal - official website](https://signal.org/bigbrother/central-california-grand-jury/)
[Double ratchet algorithm - official website](https://signal.org/docs/specifications/doubleratchet/)
[Signal protocols' security - official website](https://signal.org/blog/spqr/)
#### External reviews
[On signal's ability to know who is talking to who - article](https://sanesecurityguy.com/articles/signal-knows-who-youre-talking-to/)
[Signal's code deep-dive - technical doc](https://deepwiki.com/signalapp/Signal-Server/4.1-message-controllers-and-routing)
[Why is Signal so secure? - article](https://aboutsignal.com/signal-security-privacy-guide/)
#### Research papers
[Security audit on Signal - independant audit](https://positive-intentions.com/docs/research/Security%20audit/signal-protocol-security-audit/)
[Analysis of signal protocol - research paper](https://eprint.iacr.org/2016/1013.pdf)

### Analyse
Signal est une messagerie instantanée, centralisée, proposée comme un service de communication digne de confiance, tant pour la sécurité que pour la vie privée.[^signalattack][^signalprinciples][^signalphoneprivacy] Ils accordent clairement une forte importance à la transparence en effectuant des audits third-party[^signalaudits] et les instructions de la justice.[^signallegal][^signallsubpoena] Pour appuyer ça, ils ont aussi une license AGPLv3.0. [^signallicense]

La théorie: Signal est une application largement tournée vers la vie privée. Tout ce qui est important (contacts, données personnelles, clés, messages, ...) est stocké sur l'appareil de l'utilisateur, nulle part ailleurs.[^signalprivateprofiles] Les seules informations stockées sur les serveurs sont le numéro de l'utilisateur, la date de création de son compte et la dernière date de connexion, tout le reste n'est que sur votre appareil, nulle part ailleurs. Certains articles mettent justement l'accent sur l'importance qu'ils accordent aux profils privés. En plus de ça Signal a développé le "**sealed sender**", qui permet normalement de cacher qui envoie un message (sauf pour le premier message.[^signalsealedsender]

La pratique: En pratique oui, Signal ne log rien du tout, certains cas d'intervention de la justice le prouvent d'ailleurs, ce qui renforce ce que signal dit de son système.[^signallegal] En revanche cela ne signifie pas que tout est imperméable à l'identification. Pour ce qui est de l'encryption,  [^signalencryption]

En théorie il est possible de traquer un utilisateur: le traffic n'étant pas infini, le nombre de messages reçus par une personne en particulier puis par une autre, potentiellement liée à cette première personne ou non, peuvent être corrélés.[^signalsurveillance] Il est rare que Alice reçoive 4 messages dans la journée, que Bob en reçoive 5 et que cela n'ait aucun lien. Tout cela se renforce encore lorsque l'on peut analyser les paquets qui partent vers signal ou encore les *timestamp* sur les paquets, car **Signal** n'utilise pas le **mixnet**. Mais encore une fois Signal a prouvé qu'il était digne de confiance par le passé, a démontré à de multiples reprises qu'ils ne céderaient pas aux injonctions des forces de l'ordre et qu'ils tenaient particulièrement à ne garder aucune info.

En somme la conclusion est simple: tout comme un VPN, vous choisissez de faire confiance à une entité particulière et de garder un semblant de facilité d'utilisation plutôt que d'utiliser quelque chose d'intraçable. C'est, il me semble, un bon équilibre pour la vie de tous les jours.

[^signalattack]:[Attaque sur Signal - official website](https://support.signal.org/hc/en-us/articles/4850133017242-Twilio-Incident-What-Signal-Users-Need-to-Know)
[^signallsubpoena]:[Subpoenas aiming Signal - official website](https://signal.org/bigbrother/central-california-grand-jury/)
[^signallicense]:[Signal Android - github](https://github.com/signalapp/Signal-Android)
[^signalprinciples]:[Signal's principles (official website)](https://signal.org/blog/looking-back-as-the-world-moves-forward/)
[^signalprivateprofiles]:[Signal's private profiles - official website](https://signal.org/blog/signal-profiles-beta/)
[^signalsealedsender]:[Signal's sealed sender - official website](https://signal.org/blog/sealed-sender/)
[^signalphoneprivacy]:[Signal phone numbers privacy - official documentation](https://support.signal.org/hc/en-us/articles/6712070553754-Phone-Number-Privacy-and-Usernames)
[^signallegal]:[Legal orders on Signal - official website](https://signal.org/bigbrother/)
[^signalaudits]:[Signal List of third-party security audits - official website](https://community.signalusers.org/t/overview-of-third-party-security-audits/13243)
[^signaldoubleratchet]:[Double ratchet algorithm - official website](https://signal.org/docs/specifications/doubleratchet/)
[^signalprotocolsecurity]:[Signal protocols' security - official documentation](https://signal.org/blog/spqr/)

[^signalsurveillance]:[On signal's ability to know who is talking to who - article](https://sanesecurityguy.com/articles/signal-knows-who-youre-talking-to/)
[^signalcode]:[Signal's code deep-dive - technical doc](https://deepwiki.com/signalapp/Signal-Server/4.1-message-controllers-and-routing)
[^signalencryption]:[Why is Signal so secure? - article](https://aboutsignal.com/signal-security-privacy-guide/)

[^signalindependantaudit]:[Security audit on Signal - independant audit](https://positive-intentions.com/docs/research/Security%20audit/signal-protocol-security-audit/)
[^signalprotocolresearch]:[Analysis of signal protocol - research paper](https://eprint.iacr.org/2016/1013.pdf)

## Matrix

### Footnotes
#### Documentation
- [Matrix values - matrix's doc](https://matrix.org/foundation/about/)
- [Matrix on Signal and centralized messengers - matrix's forum](https://matrix.org/blog/2020/01/02/on-privacy-versus-freedom/)
- [Matrix logged informations - matrix's privacy policy](https://matrix.org/legal/privacy-notice/#2-2-1-1-account-and-profile-information)
- [Matrix privacy - matrixdocs](https://matrixdocs.github.io/docs/security/overview)
- [Matrix p2p goal - matrix forum post](https://matrix.org/blog/2020/06/02/introducing-p2p-matrix/)
- [Matrix p2p goal roadmap - forum post](http://arewep2pyet.com)
- [Matrix E2E](https://matrix.org/docs/matrix-concepts/end-to-end-encryption/)
#### External reviews
- [On matrix's privacy - Ycombinator](https://news.ycombinator.com/item?id=32780665)
- [Matrix's protocol - blog post](https://lwn.net/Articles/632572/)
#### Research papers
- [State of research and comprehensive study of research on matrix](https://link.springer.com/content/pdf/10.1186/s13677-025-00829-7.pdf?error=cookies_not_supported&code=3f7aab26-72e0-470e-b5f2-ae2b654a8f7e)
- [Cryptographic analysis of the matrix suite](https://arxiv.org/pdf/2408.12743)
- [Mapping of matrix]([https://dl.acm.org/doi/pdf/10.1145/3558482.3581773](https://link.springer.com/content/pdf/10.1186/s13677-025-00829-7.pdf))

### Analyse

Matrix se présente comme un service orienté vers les communautés, qui permet de joindre des communautés de toutes origines (skype, discord, signal, etc) en une seule application via des réseaux *fédérés*.

Le protocole et l'idée, en eux-même, n'ont pas l'air trop mal du tout. Ils ont l'air d'attacher une certaine importance à l'idée de vie privée et notamment de la développer avec cette idée de messagerie fédérée. En plus de ça leur application est centrée autour de leurs *bridges* qui permettent de connecter une room matrix à beaucoup d'autres types d'applications. Un autre point intéressant est l'absence d'information importante lors de l'inscription, matrix n'a besoin ni d'email ni de numéro de téléphone, rien du tout.

Le problème est que c'est un service trop dispersé, à vouloir tout faire il ne fait pas grand chose de bien. De plus, ils se démarquent un peu des derniers en corrigeant certains bugs mais n'ont pas pour autant réinventé la roue. Du côté de la protection, elle est suffisante dans beaucoup de cas mais a quand même des lacunes.

Déjà, les messages sont envoyés de bout en bout par TLS, c'est la seule sécurité qui existe par défaut. Certes cela permet de cacher certaines parties du message mais pas tout. Un tiers qui écoute sur le réseau obtient ainsi des métadonnées. En plus de ça, l'encryption E2EE est disponible, mais optionnelle, ce qui est sensiblement embêtant, ça fait notamment que, par défaut, les serveurs impliqués peuvent tout à fait lire les messages, ce qui est notamment embêtant quand matrix.org est hôte pour plus de 30% des utilisateurs. Le plus embêtant en plus de tout ça reste les métadonnées. Peu importe le niveau d'encryption, les protocoles ou le souhait des utilisateurs, les métadonnées sont toujours traquées par les serveurs, peu importe le cas.

Alors heureusement chacune de ces fonctionnalités peut être justifiée: l'encryption E2E optionnelle peut être activée par n'importe quel participant dans la room, les métadonnées ne servent qu'à faire fonctionner l'application et l'absence d'encryption est surtout là pour éviter que les utilisateurs aient une trop mauvaise expérience. De plus ils parlent encore de faire d'une partie de l'application une messagerie p2p, ce qui serait franchement une bonne idée.

Le problème dans tout ça est plutôt la mentalité des développeurs. Ils sont lents, n'arrivent pas vraiment à faire décoller leur application, qui a pourtant maintenant 6 ans, choisissent de développer le côté point commun plutôt que la sécurité et, plutôt que d'accepter leurs problèmes de leur application, ont l'air de tout tenter pour blâmer les autres et les enfoncer, tout en ayant une idée glorifiée de leur travail. Il faudrait leur donner encore du temps pour leur permettre de développer un meilleur protocole, pour leur donner le temps de s'atteler à une meilleure sécurité mais de combien d'années ont-ils vraiment besoin?

## Session

### Footnotes
#### Documentation
[Session's messenger's main page, technical details and privacy](https://docs.getsession.org/)
[Session litepaper](https://getsession.org/assets/papers/Litepaper_Session_private_messenger.pdf)
[Session financial problems](https://getsession.org/blog/the-future-of-session)
[Session main page](https://getsession.org/)
[Session's network](https://docs.getsession.org/session-network)
[Session's message routing in the onion network](https://docs.getsession.org/session-network/session-protocol/onion-requests-and-message-routing)
[Session requirement for account creation](https://docs.getsession.org/session-network/session-protocol/account-ids-and-self-managed-keys)
[session's staking incentive](https://docs.getsession.org/session-network/staking/staking-reward-pool)
[Session's second protocol version: post-quantum cryptography](https://getsession.org/blog/session-protocol-v2)
[Session protocol v1](https://getsession.org/blog/session-protocol-technical-information)
#### Outside sources, critics
[Value of session's SESH tokens](https://www.coingecko.com/en/coins/session-token?chart=type%3Dprice%26mode%3Dline%26timeframe%3Dmax)
[Session android's github page and AGPLv3 license](https://github.com/session-foundation/session-android)
[CyberInsider's shitty review of session](https://cyberinsider.com/secure-encrypted-messaging-apps/session/)
[reddit post, Session's removal of PFS](https://www.reddit.com/r/privacy/comments/13vanfj/session_messenger/)
[Session's onion protocol code (v4)](https://deepwiki.com/session-foundation/session-desktop/2.3-network-layer-and-onion-routing)
#### Research papers
[Quarkslab's independant audit of Session's app](https://blog.quarkslab.com/resources/2021-05-04_audit-of-session-secure-messaging-application/20-08-Oxen-REP-v1.4.pdf)
[Session's whitepaper](https://arxiv.org/pdf/2002.04609)
#### Other
[David Chaum's master thesis](https://cdn.nakamotoinstitute.org/docs/untraceable-electronic-mail.pdf)


La politique de Session est claire et honnête, le but est de proposer un service de messagerie sécurisé et anonyme. [^sessionmainpage] [^sessionlitepaper] [^sessionfinances] En plus d'insister sur l'importance de l'anonymat et les problèmes que représentent l'utilisation d'infos personnelles comme un numéro de téléphone ou un email, ils insistent sur l'absence d'info qui permettent d'identifier un utilisateur et la collecte minimale de métadonnées, ce qui présage de bonnes choses. [^sessionaccount][^sessionmessenger] Ils ont aussi la license AGPLv3 (j'aime cette license).
[^sessiongithub]
L'envoi de messages est basé sur l'utilisation d'un réseau de nœuds entretenus par des volontaires.[^sessionnetwork] Ce network est développé comme un onion router, ce qui lui permet de garantir en sortes la sécurité des utilisateurs et leurs données. Un des problèmes majeurs de ce système est qu'un noeud peut décider de stocker les messages jusqu'à les déchiffrer. Autrement, l'encryption a l'air solide, étant basé sur l'idée déjà théorisée des *onion routing*, le réseau propose un protocole solide.[^sessiononiontechnical][^sessionnetwork][^sessionmessage]

La motivation pour faire tourner des nœuds est plus qu'étrange: ils proposent de dédommager les utilisateurs avec des tokens SESH.[^sessionnetwork][^sessionstaking] Ils distribuent des parts de leur cryptomonnaie en fonction des contributions et des *staking*. C'est un système à double tranchant. L'avantage principal, au-delà de la motivation à faire tourner des nœuds, est de protéger contre les sybil attacks. Le problème majeur en revanche est probablement la valeur de ces tokens, qui ne fait que chuter depuis quelques temps, retirant ainsi probablement la motivation à maintenir un nœud. [^sessionseshvalue] Pour donner une idée à ceux qui auraient un doute sur le fait que le prix des noeuds puissent repousser certains utilisateurs, un noeud coûte, au moment de l'écriture de ce poste, environ 350€. Au lancement du service, faire tourner un noeud coûtait alors 3500€. Certes on peut partager le prix et ne payer que un quart, mais cela fait quand même quasiment 100€.[^sessionseshvalue][^sessionnetwork] Allez trouver les autres contributeurs en plus...

Au-delà du réseau, l'équipe de développement elle-même a l'air d'avoir des problèmes financiers: après ce qui semblait être la fin de la messagerie pour des raisons financières et une levée de fonds désespérée, les 3 développeurs qui restent sur le projet semblent sur le bord de mettre la clé sous la porte. C'est à se demander si le service et le réseau tiendront encore une année.[^sessionfinances]

Pour conclure, le protocole de session a l'air franchement bien, sa sécurité est assurée par plusieurs sources, par le papier de recherche sur lequel ils se basent, l'expérience de Signal (même s'ils ont décide de jeter certaines parties) et le test indépendant. Malheureusement il manque un peu de retour extérieurs, d'analyses ou de recherches third-party. Il serait également utile d'avoir certaines expériences légales comme pour Signal ou Mullvad. Le seul problème qui noircit l'horizon est la survivabilité du réseau dans un avenir proche comme lointain.

p.s. Attention à ne pas prendre pour argent comptant l'article de cyberinsider, ils mélangent tout. 
- "But Signal isn’t as strong on privacy as it is on security. It collects some metadata and doesn’t have a corporate sponsor like Facebook sucking up and monetizing that metadata." est aussi bien formulé que si l'on devait faire la promotion de la diarhée, les deux phrases sont contraires mais en fait pas du tout liées, rien ne prouve que Signal a des problèmes de collecte de métadata, absolument rien, on peut au contraire dire *a posteriori* qu'ils sont honnêtes. Pour ce qui est de la vie privée, la seule menace est le serveur centralisant les messages, ne prouvant pour le moment pas que la solution de vie privée qu'ils apportent est pire qu'une autre.
- "- Perfect Forward Secrecy removed" n'est plus d'actualité. Ils avaient apparemment décidé de se passer du PFS à la sortie mais l'ont repris lors de la v2 du protocole.[^sessionredditremovedsecrecy]
- "We consider the metadata issue to be the Achilles heel of many [secure messaging services](https://cyberinsider.com/secure-encrypted-messaging-apps/) and [secure email services](https://cyberinsider.com/email/secure/). Even the most popular secure email services, such as [ProtonMail](https://cyberinsider.com/email/reviews/protonmail/), do not have a good solution to the metadata problem." est en grande partie faux. Non seulement David Chaum a théorisé les emails anonymes il y a déjà plus de 40 ans[^davidchaummasterthesis], RVNT promet les messages complètement anonymisés, Signal a implémenté *sealed sender*, Proton a seulement décidé de traquer les utilisateurs sans les prévenir, c'est différent.[^signalsealedsender]

[^davidchaummasterthesis]:[David Chaum's master thesis](https://cdn.nakamotoinstitute.org/docs/untraceable-electronic-mail.pdf)

[^sessionmessenger]:[Session's messenger's main page, technical details and privacy](https://docs.getsession.org/)
[^sessionlitepaper]: [Session litepaper](https://getsession.org/assets/papers/Litepaper_Session_private_messenger.pdf)
[^sessionfinances]: [Session financial problems](https://getsession.org/blog/the-future-of-session)
[^sessionmainpage]:[Session main page](https://getsession.org/)
[^sessionnetwork]:[Session's network](https://docs.getsession.org/session-network)
[^sessionmessage]:[Session's message routing in the onion network](https://docs.getsession.org/session-network/session-protocol/onion-requests-and-message-routing)
[^sessionaccount]:[Session requirement for account creation](https://docs.getsession.org/session-network/session-protocol/account-ids-and-self-managed-keys)
[^sessionstaking]:[session's staking incentive](https://docs.getsession.org/session-network/staking/staking-reward-pool)
[^sessionpostquantum]:[Session's second protocol version: post-quantum cryptography](https://getsession.org/blog/session-protocol-v2)
[^sessionprotocol]:[Session protocol v1](https://getsession.org/blog/session-protocol-technical-information)

[^sessionseshvalue]:[Value of session's SESH tokens](https://www.coingecko.com/en/coins/session-token?chart=type%3Dprice%26mode%3Dline%26timeframe%3Dmax)
[^sessiongithub]:[Session android's github page and AGPLv3 license](https://github.com/session-foundation/session-android)
[^sessioncyberinsider]:[CyberInsider's shitty review of session](https://cyberinsider.com/secure-encrypted-messaging-apps/session/)
[^sessionredditremovedsecrecy]:[reddit post, Session's removal of PFS](https://www.reddit.com/r/privacy/comments/13vanfj/session_messenger/)
[^sessiononiontechnical]:[Session's onion protocol code (v4)](https://deepwiki.com/session-foundation/session-desktop/2.3-network-layer-and-onion-routing)

[^sessionaudit]:[Quarkslab's independant audit of Session's app](https://blog.quarkslab.com/resources/2021-05-04_audit-of-session-secure-messaging-application/20-08-Oxen-REP-v1.4.pdf)
[^sessionwhitepaper]:[Session's whitepaper](https://arxiv.org/pdf/2002.04609)

#### RVNT
- [n] RVNT
	- [x] Logging *per documentation*
	- [x] Privacy *per documentation*
	- [n] Deanonymization
		- [n] Traceability
- [ ] Further readings

Le service paraît phénoménal. Tout d'abord le plus évident, l'encryption. A travers l'utilisation de **double ratchet**, **tor**, **mixnet**, **sealed enveloppes**, **signing**, il semble impossible de lire quoi que ce soit, c'est à se demander comment ça peut même trouver son destinataire. Le double hatchet protège en plus des attaquants, si un attaquant prend le contrôle d'une clé et arrive à lire un message, il ne pourra pas lire le suivant, ce qui rend toute attaque vraiment difficile si elle ne cible pas l'utilisateur directement. Grâce au **mixnet**, aux tailles de paquets et aux paquets aléatoires, même si quelqu'un analyse le réseau, il lui sera impossible de savoir ce qu'il se passe vraiment.

Pour ce qui est de la vie privée on peut rester rassuré, rien ne transparaît. De l'expéditeur au contenu du message en comprenant toutes les métadonnées, il semble que les seules infos qui persistent sont les *timestamp* de connexion ainsi que les clés publiques associées aux noms d'utilisateurs. Un point bonus là-dedans est que, selon **RVNT** directement, même si un parti tiers parvenait à prendre le contrôle d'un relais, il ne pourrait absolument rien lire (ce qui est logique puisque tout est basé sur Tor).

Le réseau en lui-même a l'avantage d'être p2p, il est donc insensible aux lois gouvernementales, locales, etc. Il ne peut subir d'obligation légale, ne peut donner de secrets puisqu'il ne possède rien. Comparé à un serveur fédéré ou centralisé, il est presque invincible. Ca a quand même l'inconvénient de ne pas permettre d'envoyer des messages lorsque l'un des deux est hors ligne, ce qui est corrigé par un système assez pratique: un *buffering* des messages. A voir ce que cela donne à l'avenir.

Entre le site web qui a l'air exhaustif sur tout ce qu'ils font et ne font pas, qui s'empresse de se comparer (honnêtement, qui plus est) aux autres services et le *warrant canary*, ils ont l'air de tenir la transparence à coeur, ce qui est d'autant plus louable.

Clairement les attentes sont hautes, les promesses fortes, il faut voir ce que cela donne à l'avenir une fois que des audits indépendants auront été effectués, que des évaluations et des lectures du codes seront permises.

[Signal alternatives(official documentation)](https://rvntos.io/alternatives/signal/)
[Double ratchet encryption (official documentation)](https://rvntos.io/docs/double-ratchet/)
[RVNT vs Signal (official documentation)](https://rvntos.io/compare/rvnt-vs-signal/)
[Network protection (zero logging policy at the end)(official documentation)](https://rvntos.io/docs/server/ (official documentation))
[Sealed sender (official website)](https://rvntos.io/glossary/sealed-sender/)
[Warrant canary (official website)](https://rvntos.io/glossary/warrant-canary/)
[Offline mesh (official website)](https://rvntos.io/docs/offline-mesh/)
{% endraw %}
