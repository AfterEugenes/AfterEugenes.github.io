---
layout: privacy-hub
title: Messaging
description: ''
excerpt: ''
date: 2026-09-08T16:33
platform: privacy
permalink: /privacy/messaging/
category: Messaging
tags:
- Privacy
- Messaging
---

{% raw %}

# Index

Messaging apps
- Centralised
	- [x] Signal
- Federated
	- [x] SimpleX
	- [>] Matrix
	- [-] Rocket.chat
- P2P
	- [x] Briar
	- [>] Session
	- [t] RVNT
- [ ] xmpp
- [ ] Tox
- [ ] Wickr
- [ ] meshtastic/meshcore
- [ ] bitchat
- [ ] anonomi
- [ ] lora
- [ ] bridgeify
- [ ] telegram

# Introduction

Les services de messagerie sont importants ils permettent de communiquer. La différence principale réside dans la différence entre centralisé, fédéré et p2p, c'est la différence la plus conséquente sur la vie privée. [^decentralizedcomparison]

[^decentralizedcomparison]: [P2P, federated et centralized comparaison - RVNT](https://rvntos.io/blog/p2p-vs-federated-vs-centralized-messaging/)

# Contenu

<div class="note-embed">

<div class="note-embed-head"><a class="note-embed-title" href="/privacy/messaging/signal/">Signal</a><span class="note-embed-meta">Updated 2026-09-08</span>
</div>

<div class="note-embed-body">


### Signal
#### TL;DR
Très probablement la meilleure messagerie que vous pourrez installer pour une utilisation quotidienne et simple. La sécurité est sans appel. La messagerie est centralisée donc Signal pourrait décider d'enregistrer certaines métadonnées sur les communications mais le groupe a été est prouvé digne de confiance ***a posteriori*** et ***a priori***, un bel avantage.

#### Analyse
Signal est une messagerie instantanée, centralisée, proposée comme un service de communication digne de confiance, tant pour la sécurité que pour la vie privée.[^signalattack][^signalprinciples][^signalphoneprivacy] Ils accordent clairement une forte importance à la transparence en effectuant des audits third-party[^signalaudits] et les instructions de la justice.[^signallegal][^signallsubpoena] Pour appuyer ça, ils ont aussi une license AGPLv3.0 sur l'application ET le serveur. [^signallicense][^signalserverlicense] Si vous en doutez encore, vous pouvez opter pour l'option fédérée et faire tourner votre propre serveur.[^signallocalserver]

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
[^signalserverlicense]:[Signal server on github](https://github.com/signalapp/Signal-Server)

[^signalsurveillance]:[On signal's ability to know who is talking to who - article](https://sanesecurityguy.com/articles/signal-knows-who-youre-talking-to/)
[^signalcode]:[Signal's code deep-dive - technical doc](https://deepwiki.com/signalapp/Signal-Server/4.1-message-controllers-and-routing)
[^signalencryption]:[Why is Signal so secure? - article](https://aboutsignal.com/signal-security-privacy-guide/)
[^signallocalserver]:[Running a local server](https://www.reddit.com/r/signal/comments/7poh3f/is_it_possible_to_create_a_private_signal_server/)

[^signalindependantaudit]:[Security audit on Signal - independant audit](https://positive-intentions.com/docs/research/Security%20audit/signal-protocol-security-audit/)
[^signalprotocolresearch]:[Analysis of signal protocol - research paper](https://eprint.iacr.org/2016/1013.pdf)

</div>

<div class="note-embed-foot"><a href="/privacy/messaging/signal/">Open the full note →</a>
</div>

</div>

<div class="note-embed">

<div class="note-embed-head"><a class="note-embed-title" href="/privacy/messaging/briar/">Briar</a><span class="note-embed-meta">Updated 2026-09-08</span>
</div>

<div class="note-embed-body">


### Briar
#### TL;DR
Briar est destinée aux personnes dans des situations délicates qui ont besoin de pouvoir communiquer malgré tout (journalistes, utilisateurs en pays sous dictatures, etc) Il fait très bien le travail dans ce cas mais à un certain coût. La cryptographie en elle-même est robuste et les métadonnées sont bien protégées puisque les communications en ligne passent par Tor.

#### Analyse
Leur mission est claire: apporter des systèmes de messagerie à ceux pour qui ça peut être difficile de communiquer comme les utilisateurs dans des pays sous dictature, les journalistes, whistleblowers, etc. Il est donc clair dès le départ que l'emphase sera mise sur la sécurité et la vie privée et non sur la maniabilité.[^briarhomepage][^briarusermanual] C'est d'ailleurs très bien illustré par le modèle d'attaquant choisi, stipulé tout en bas de la page d'accueil.[^briarhomepage]

La sécurité elle-même est assurée par leur protocole p2p: Bramble Transport Protocol.[^briarbramble] Le protocole en lui-même est robuste, il a été audité, prouvé, il n'y a aucun doute sur sa capacité à résister.[^briarrelease][^briarcryptography][^briaraudit] En plus de toute cette encryption, Briar utilise Tor pour router ses messages quand ils sont envoyés en ligne, ce qui renforce la sécurité mais aussi le côté privé de l'application.[^briarhomepage][^briarcryptography]

La vie privée est clairement un des points importants pour briar, ils ont à coeur de développer quelque chose qui pourrait entièrement cacher les utilisateurs qui l'utilisent. Pour cela, dès que les messages sont envoyés par le réseau ils passent par Tor, dès qu'ils sont envoyés en local, ils ne sont reçus ou transmis que par les appareils concernés, clairement une mesure d'exception pour la vie privée.

Evidemment toutes ces mesures de sécurité ont un impact sur la facilité d'utilisation. Le plus important à mon avis est que Briar est loin d'être intuitif et certaines opérations ne sont pas du tout évidentes.[^briarreview][^briarreddit] En plus de ça les quelques fonctionnalités sur lesquelles les services se basent pour faciliter la vie aux utilisateurs sont retirées: contacts, ajout rapide, envoi hors ligne, etc etc. D'autant plus que Briar est inaccessible sur un produit Apple, une très bonne nouvelle à mon avis (disons le, n'importe quelle personne prétendant vouloir protéger ses données n'achètera pas un apple...). Malgré tout Briar a ajouté quelques fonctionnalités pour combler ce manque: une liste de contact qui correspond aux critères de Briar, une application mailbox pour pouvoir recevoir des messages hors ligne ou presque, etc.[^briermailbox]

Il faut aussi mentionner les groupes et communautés qui sont d'autant plus intéressantes en utilisant briar offline: du moment que deux personnes d'une communauté sont à portée l'une de l'autre, les messages sont transmis. Ca permet notamment qu'une personne qui voyage, se déplace, puisse transmettre les messages aux différentes parties de la communauté, vraiment sexy!

Enfin l'équipe de développement est plus qu'intéressante. Entre l'accent mis sur la vie privée, le but même de l'application et l'apparente absence de concession dans leur développement, même lorsqu'il s'agit de batterie, ils donnent plus que des raisons de leur faire confiance. En plus de ça le projet est open source et protégé par une license AGPLv3, un point positif à mon goût.[^briarmaintenance][^briargithub]

[^briarhomepage]:[Briar Homepage](https://briarproject.org/how-it-works/)
[^briarusermanual]:[Briar User manual](https://briarproject.org/manual/)
[^briarbrambre]:[Briar Bramble transport protocol v4](https://code.briarproject.org/briar/briar-spec/-/blob/master/protocols/BTP.md)
[^briarrelease]:[Briar Post about briar's release and audit](https://briarproject.org/news/2017-beta-released-security-audit/)
[^briarmailbox]:[Mailbox app](https://briarproject.org/download-briar-mailbox/)
[^briarmaintenance]:[Briar Development state & maintenance mode](https://briarproject.org/news/2026-maintenance-mode/)
[^briargithub]:[Briar on github](https://github.com/briar/briar?tab=License-1-ov-file)

[^briarreview]:[Briar Review by tech-oblivious people](https://www.pcmag.com/reviews/briar)
[^briarreddit]:[Briar User comparison with Signal](https://www.reddit.com/r/privacytoolsIO/comments/kpq3ri/comment/gisj73a/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
[^briaraudit]: [Briar Cure 53 security audit](https://briarproject.org/raw/BRP-01-report.pdf)

[^briarcryptography]: [Cryptography in the wild: Briar - Yuanming Song](https://ethz.ch/content/dam/ethz/special-interest/infk/inst-infsec/appliedcrypto/education/theses/report_YuanmingSong.pdf)

</div>

<div class="note-embed-foot"><a href="/privacy/messaging/briar/">Open the full note →</a>
</div>

</div>

<div class="note-embed">

<div class="note-embed-head"><a class="note-embed-title" href="/privacy/messaging/simplex/">SimpleX</a><span class="note-embed-meta">Updated 2026-09-08</span>
</div>

<div class="note-embed-body">


### SimpleX
#### TL;DR
SimpleX est une application fédérée en premier lieu. Au-delà du but initial de proposer un réseau de messagerie sécurisé et digne de confiance, ils ont développé, entre autres, les messages directs, le SimpleX network et les addresses anonymes, en faisant une des solutions à la fois les plus sûres et les plus polyvalentes. L'entreprise a en plus l'air d'avoir assuré et bonne base d'utilisateur et continue à se développer, sans promesse de s'éteindre bientôt.

#### Analyse
Pour commencer, comme d'habitude, le but de l'application. Ce service de messagerie fédéré est destiné aux utilisateurs professionnels (journalistes, whitleblowers, activistes, victimes de dictatures, anglais, ... Notre lot classique de personnes en milieu sensible.) mais aussi aux utilisateurs particuliers avec un simple but d'améliorer leur vie privée. Eh oui, n'importe qui peut facilement utiliser SimpleX. leur but est d'amener un service de messagerie qui s'adapte à chaque utilisateur. Même si je suis d'habitude assez opposé à utiliser un couteau-suisse, celui-ci est tellement bien pensé qu'il est difficile de l'éviter.[^simplexhomepage]

Déjà pour la partie importante, est-ce sécurisé? Oui. On retrouve le classique E2EE, double ratchet, et même de la post-quantum encryption. Et puis bien sûr le classique audit indépendant a permis de trouver quelques failles mais rien de majeur.[^simplexaudit]

Pour le reste je vais essayer de vous énumérer les fonctionnalités les plus importantes. Commençons par l'identification. Déjà vous ne donnez aucune information à la création d'un compte, vous entrez simplement un nom, un mot de passe et voilà. Le mieux là-dedans c'est que rien n'est stocké en ligne, le mot de passe vous sert à déchiffrer la base de données en local et rien d'autre. Alors il faut faire attention parce que cela signifie, comme pour briar, que vous ne pouvez avoir deux appareils sur le même compte et que si vous perdez votre compte, vous dites adieu à vos conversations.

C'est d'autant plus important que la façon d'ajouter un contact est, je dois le dire, un coup de génie. Chaque utilisateur peut avoir une addresse moyenne durée sur demande mais l'addresse de base, partagée à vos contact, change en fonction du contact.[^simplexaddresses] Cela signifie notamment que personne ne peut relier deux conversations avec deux personnes différentes à un seul utilisateur. Cela signifie aussi que c'est votre base de données locale qui gère ces connexions.

Une autre fonctionnalité importante, j'irais jusqu'à dire la plus séduisante, est le SimpleX network. SimpleX, après quelques changements, a décidé de développer son propre réseau s'apparentant à un onion routeur.[^simplexnetwork] Les différences sont qu'ils n'utilisent que deux noeuds pour router les connexions et que, plutôt que d'utiliser des noeuds aléatoires, ils ont décidé de n'utiliser que des noeuds choisis. L'expéditeur choisit le noeud de relais, premier noeud dans la suite, la destination choisit le noeud de destination, le second dans ce réseau. De cette façon aucun noeud ne peut avoir toutes les informations sur le réseau, il est impossible pour un organisme comme la NSA d'avoir un dixième des noeuds déployés sur le réseau. Alors ça a bien sûr ses inconvénients, notamment sur la difficulté pour une personne lambda d'avoir un serveur de confiance, mais ça a quand même le mérite de particulièrement bien fonctionner pour cacher les connexions, surtout que le protocole encrypte la destination (oui, la destination, non pas l'expéditeur) et la cache au noeud de relais, ce qui l'empêche de connaître tout le chemin et ne lui permet de connaître que l'expéditeur et le prochain noeud.[^simplexnetwork] Cette simple fonctionnalité de cacher la destination, combinée avec les serveurs et développeurs de confiance, font que je pense sincèrement que SimpleX peut tout à fait rivaliser avec Signal en terme de messagerie centralisée de confiance, alors qu'elle le fait largement en tant que messagerie fédérée.

La messagerie étant fédérée (j'aurais dû en parler dès le début mais vous voyez tout ce qu'il y a à dire) vous pouvez bien sûr faire tourner votre propre serveur localement sans grande difficulté. Si vous n'avez pas spécialement envie de le faire vous-même, certaines communautés et personnes proposent d'utiliser leurs serveurs et vous proposent des listes de tels serveurs, ce qui permet de multiplier les serveurs utilisés et est d'autant plus important de par la construction de SimpleX network.[^simplexcommunityservers]

Bien sûr cela peut poser problème pour les conversations où les deux utilisateurs se connectent aux serveurs d'une même entité, d'autant plus quand simplex est la connexion par défaut, mais encore une fois ils y ont pensé. Déjà ils ont ajouté la possibilité de se connecter aux serveurs de flux, un autre provider qui propose de se connecter par défaut à ses serveurs. Si l'option est activée, l'application se connecte d'ailleurs à l'un pour envoyer et l'autre pour recevoir, assurant qu'aucun n'aura d'infos sur le chemin complet.[^simplexflux] En plus SimpleX a (partiellement) prouvé être digne de confiance entre l'importance qu'ils accordent aux métadonnées et la façon dont ils ont répondu aux exigences de la loi et puis surtout la license AGPLv3.[^simplexprivacy][^simplextransparency][^simplexgithub]

En plus de tout ça on retrouve quelques fonctionnalités de sécurité telles que la connexion par tor, la messagerie incognito et les groupes secrets.[^simplexincognito][^simplexsecretgroups] Ces fonctionnalités combinées au développement de SimpleX font qu'aucune info ne peut vraiment transiter: SimpleX n'a jamais demandé votre identité, les quelques métadonnées qu'ils peuvent connecter sont en fait juste quel profil de conversation est associé à quel ip (puisqu'ils ne peuvent pas lier vos différentes addresses de vos différentes conversations ***a priori*** ils ne peuvent donc dire à qui vous parlez ou quand) lorsque ***et uniquement lorsque*** vous et votre interlocuteur utilisez tous deux leurs serveurs, auquel cas vous pouvez simplement décider d'utiliser Tor avant la connexion au noeud pour cacher votre IP, la seule info qu'ils avaient sur vous disparaît dans le vent.

Pour ce qui est de l'utilisation et des retours utilisateurs, ils sont étonnamment positifs. SimpleX a développé un paquet de fonctionnalités plutôt intéressantes. Certaines comme les communautés sont faites pour l'aisance d'utilisation alors que d'autre comme les live messages sont faites pour les utilisateurs sensibles, ce qui prouve d'autant plus l'importance qu'ils accordent à la sécurité de leur application et la possibilité de l'utiliser en contexte difficile.[^simplexfunctionnalities] En plus de ça les quelques reviews qui existent ont l'air de faire les louanges de SimpleX et de sa facilité d'utilisation, ce qui est d'autant plus rare que certaines de ces louanges viennent de reddit.[^simplexreview][^simplexreddit]

La messagerie elle-même est très bien développée. Entre la base d'utilisateurs massive et leurs idées pour développer l'application, c'est largement prometteur. Ils ont en effet prévu de financer la continuation du développement de l'application et la maintenance des serveurs en proposant aux serveurs des fonctionnalités payantes (nom de domaine personnalisé, serveurs, etc). Tout cela donne plus d'espoir sur le développement de SimpleX que sur celui de Session ou Briar. C'est d'autant plus intéressant que ces fonctionnalités sont utiles pour les communautés et qu'ils ne poussent pas leur modèle économique sur les utilisateurs comme rocket.chat. Ils annoncent même financer l'application entière en se basant entièrement sur les financements apportés par les serveurs.[^simplexfinancial]

SimpleX est même utilisé en ce moment même par la communauté principale de monero, vous permettant d'accéder à des ressources importantes ou de l'aide des développeurs.

En note additionnelle mais pas nécessairement utile, certaines sources s'amusent à critiquer ouvertement SimpleX et les associer à des communautés néo-nazies dans le but de promouvoir le chat control, ce qui prouve partiellement l'importance qu'a pu gagner SimpleX à travers les années.

En plus de ça, de par sa construction, SimpleX, ou plutôt les serveurs privés permettant de se connecter à SimpleX, sont immunisés normalement à chatcontrol et aux autres lois horribles auxquelles nos gouvernements peuvent penser à l'avenir, malgré ce qu'en disent les utilisateurs reddit. Malgré tout, le siège étant localisé en Angleterre, il faut surveiller les changements dans le code, qui pourraient être imposés par le gouvernement.[^simplexchatcontrol][^simplexwired][^simplexwiredoriginal] Le seul nuage à l'horizon est le fait que SimpleX ait eu plusieurs requêtes du gouvernement et ne nous ai pas montré leurs réponses finales excepté celles qui disaient qu'ils aideraient le gouvernement british. A voir ce que cela donne en réelle situation catastrophique comme pour Mullvad VPN ou session.

[^simplexhomepage]:[SimpleX chat homepage](https://simplex.chat/)
[^simplecommunities]:[SimpleX Communities](https://simplex.chat/directory/)
[^simplexfinancial]:[SimpleX Monetary incentive](https://simplex.chat/crowdfunding/)
[^simplexfunctionnalities]:[SimpleX Live messages and other functionnalities](https://simplex.chat/docs/guide/send-messages.html)
[^simplexsecretgroups]:[SimpleX Secret groups](https://simplex.chat/docs/guide/secret-groups.html)
[^simplexincognito]: [SimpleX Incognito mode and chat profiles](https://simplex.chat/docs/guide/chat-profiles.html)
[simplexaddresses]: [SimpleX's solution, safe addresses](https://simplex.chat/docs/guide/making-connections.html)
[^simplexprivacy]: [SimpleX Privacy policy](https://simplex.chat/privacy/)
[^simplexflux]: [SimpleX: Flux servers arriving on SimpleX](https://simplex.chat/blog/20241125-servers-operated-by-flux-true-privacy-and-decentralization-for-all-users.html)
[^simplexnetwork]: [SimpleX network](https://simplex.chat/blog/20240604-simplex-chat-v5.8-private-message-routing-chat-themes.html)
[^simplextransparency]: [SimpleX Transparency reports](https://simplex.chat/transparency/)
[^simplexwired]: [SimpleX attacked by Wired](https://simplex.chat/blog/20241016-wired-attack-on-privacy.html)
[^simplexgithub]: [SimpleX github](https://github.com/simplex-chat/simplexmq/blob/stable/protocol/simplex-messaging.md)

[^simplexreview]: [External SimpleX review](https://itsfoss.com/news/simplex-chat/)
[^simplexreddit]: [SimpleX chat discussed on reddit](https://www.reddit.com/r/privacy/comments/z4990l/thoughts_on_simplex_chat/)
[^simplexwiredoriginal]: [Wired on simpleX (for the laughs)](https://www.wired.com/story/neo-nazis-flee-telegram-encrypted-app-simplex/)
[^simplexchatcontrol]: [SimpleX and chat control on reddit](https://www.reddit.com/r/SimpleXChat/comments/1uue5e3/chat_control/)
[^simplexcommunityservers]: [SimpleX Community servers list](https://discuss.privacyguides.net/t/simplex-community-servers-list/21443/6)

[^simplexaudit]: [Independant audit of SimpleX](https://files.safe.de.fi/safe/files/audit/pdf/SimpleXChat.pdf)

</div>

<div class="note-embed-foot"><a href="/privacy/messaging/simplex/">Open the full note →</a>
</div>

</div>

<div class="note-embed">

<div class="note-embed-head"><a class="note-embed-title" href="/privacy/messaging/session/">Session</a><span class="note-embed-meta">Updated 2026-09-08</span>
</div>

<div class="note-embed-body">


### Session
#### TL;DR
Cette application est une messagerie qui passe par le réseau tor. La cryptographie est excellente et prouvée. L'application elle-même est facile et agréable à utiliser. Le réseau onion est une idée novatrice qui permet de sécuriser les messages mais le prix pour lancer un tel noeud transforme l'applciation en messagerie centralisée.

#### Analyse
La politique de Session est claire et honnête, le but est de proposer un service de messagerie sécurisé et anonyme. [^sessionmainpage] [^sessionlitepaper] [^sessionfinances] En plus d'insister sur l'importance de l'anonymat et les problèmes que représentent l'utilisation d'infos personnelles comme un numéro de téléphone ou un email, ils insistent sur l'absence d'info qui permettent d'identifier un utilisateur et la collecte minimale de métadonnées, ce qui présage de bonnes choses. [^sessionaccount][^sessionmessenger] Ils ont aussi la license AGPLv3 (j'aime cette license).[^sessiongithub]

L'envoi de messages est basé sur l'utilisation d'un réseau de nœuds entretenus par des volontaires.[^sessionnetwork] Ce network est développé comme un onion router, ce qui lui permet de garantir en sortes la sécurité des utilisateurs et leurs données. Un des problèmes majeurs de ce système est qu'un noeud peut décider de stocker les messages jusqu'à ce qu'il arrive à les déchiffrer, même si c'est très improbable. Autrement, l'encryption a l'air très solide, étant basé sur l'idée déjà théorisée des *onion routing*, et permet notamment de supprimer le problème des métadonnées.[^sessiononiontechnical][^sessionnetwork][^sessionmessage] Cette application est d'ailleurs, grâce à ce protocole, une des meilleures en terme de métadonnées actuellement, rien ne peut être obtenu sur les échanges.

Pour rassurer les utilisateurs, l'expérience semble montrer que l'on peut faire confiance à Session: entre l'idée des prix des noeuds pour protéger d'une Sybil attack comme celles qui peuvent viser Tor actuellement et le fait que Session ait décidé de déménager les bureaux pour ne plus avoir à subir la pression de la police, c'est franchement une bonne nouvelle.[^sessionmoving]

La motivation pour faire tourner des nœuds est plus qu'étrange: ils proposent de dédommager les utilisateurs avec des tokens SESH.[^sessionnetwork][^sessionstaking] Ils distribuent des parts de leur cryptomonnaie en fonction des contributions et des *staking*. C'est un système à double tranchant. L'avantage principal, au-delà de la motivation à faire tourner des nœuds, est de protéger contre les sybil attacks. Le problème majeur en revanche est probablement la valeur de ces tokens, qui ne fait que chuter depuis quelques temps, retirant ainsi probablement la motivation à maintenir un nœud. [^sessionseshvalue] Pour donner une idée à ceux qui auraient un doute sur le fait que le prix des noeuds puissent repousser certains utilisateurs, un noeud coûte, au moment de l'écriture de ce poste, environ 350€. Au lancement du service, faire tourner un noeud coûtait alors 3500€. Certes on peut partager le prix et ne payer que un quart, mais cela fait quand même quasiment 100€.[^sessionseshvalue][^sessionnetwork] Un utilisateur reddit avait affirmé que les noeuds étaient répartis parmis quelques utilisateurs mais je ne retrouve pas la source, d'autant plus que les sources de Session assurent qu'il existe maintenant plus de 1500 noeuds dans 50 pays différents.[^sessionnetwork]

Au-delà du réseau, l'équipe de développement elle-même a l'air d'avoir des problèmes financiers: après ce qui semblait être la fin de la messagerie pour des raisons financières et une levée de fonds désespérée, les 3 développeurs qui restent sur le projet semblent sur le bord de mettre la clé sous la porte. C'est à se demander si le service et le réseau tiendront encore une année.[^sessionfinances]

Pour conclure, le protocole de session a l'air franchement bien, sa sécurité est assurée par plusieurs sources, par le papier de recherche sur lequel ils se basent, l'expérience de Signal (même s'ils ont décide de jeter certaines parties) et le test indépendant. La sécurité en elle-même et le côté privé sont plus qu'assurés. Malheureusement il manque un peu de retour extérieurs, d'analyses ou de recherches third-party. Il serait également utile d'avoir certaines expériences légales comme pour Signal ou Mullvad. Le seul problème qui noircit l'horizon est la survivabilité du réseau dans un avenir proche comme lointain.

p.s. La preuve qu'il faut vérifier tous les articles que l'on lit avec l'article de cyberinsider:
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
[^sessionmoving]:[Session moving headquarters](https://www.webpronews.com/session-leaves-australia-for-switzerland-after-police-pressure/)

[^sessionaudit]:[Quarkslab's independant audit of Session's app](https://blog.quarkslab.com/resources/2021-05-04_audit-of-session-secure-messaging-application/20-08-Oxen-REP-v1.4.pdf)
[^sessionwhitepaper]:[Session's whitepaper](https://arxiv.org/pdf/2002.04609)

</div>

<div class="note-embed-foot"><a href="/privacy/messaging/session/">Open the full note →</a>
</div>

</div>

<div class="note-embed">

<div class="note-embed-head"><a class="note-embed-title" href="/privacy/messaging/rvnt/">RVNT</a><span class="note-embed-meta">Updated 2026-09-08</span>
</div>

<div class="note-embed-body">


### RVNT
#### TL;DR
RVNT a pour but de créer une messagerie privée, sécurisée, p2p. Ils insistent fort sur la vie privée et la sécurité et promettent d'utiliser certains protocoles très, très intéressants, qui en feraient peut-être la messagerie la plus sécurisée. L'application elle-même n'ayant pas encore de release open-source auditée ou d'avis extérieur, on ne peut vérifier leurs promesses.

#### Analyse
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

</div>

<div class="note-embed-foot"><a href="/privacy/messaging/rvnt/">Open the full note →</a>
</div>

</div>

<div class="note-embed">

<div class="note-embed-head"><a class="note-embed-title" href="/privacy/messaging/matrix/">Matrix</a><span class="note-embed-meta">Updated 2026-09-08</span>
</div>

<div class="note-embed-body">


### Matrix
#### TL;DR
Le but est d'avoir une messagerie fédérée pour échanger des messages dans des communautés. La cryptographie en elle-même est correcte mais pas exceptionnelle, l'ego des développeurs les empêche apparemment d'avancer et corriger leurs erreurs et certaines options sont à revoir pour avoir quelque chose de privé ou agréable à utiliser.

#### Analyse
Matrix se présente comme un service orienté vers les communautés, qui permet de joindre des communautés de toutes origines (skype, discord, signal, etc) en une seule application via des réseaux *fédérés*.

Le protocole et l'idée, en eux-même, n'ont pas l'air trop mal du tout. Ils ont l'air d'attacher une certaine importance à l'idée de vie privée et notamment de la développer avec cette idée de messagerie fédérée. En plus de ça leur application est centrée autour de leurs *bridges* qui permettent de connecter une room matrix à beaucoup d'autres types d'applications. Un autre point intéressant est l'absence d'information importante lors de l'inscription, matrix n'a besoin ni d'email ni de numéro de téléphone, rien du tout.

Le problème est que c'est un service trop dispersé, à vouloir tout faire il ne fait pas grand chose de bien. De plus, ils se démarquent un peu des derniers en corrigeant certains bugs mais n'ont pas pour autant réinventé la roue. Du côté de la protection, elle est suffisante dans beaucoup de cas mais a quand même des lacunes.

Déjà, les messages sont envoyés de bout en bout par TLS, c'est la seule sécurité qui existe par défaut. Certes cela permet de cacher certaines parties du message mais pas tout. Un tiers qui écoute sur le réseau obtient ainsi des métadonnées. En plus de ça, l'encryption E2EE est disponible, mais optionnelle, ce qui est sensiblement embêtant, ça fait notamment que, par défaut, les serveurs impliqués peuvent tout à fait lire les messages, ce qui est notamment embêtant quand matrix.org est hôte pour plus de 30% des utilisateurs. 

Le plus gros problème de cette application est les métadonnées. Entre celles collectées pour l'amélioration des services, celles collectées pour transmettre les messages ou celles collectées lors de l'inscription d'un utilisateur, tout est log. Alors certains pourraient vous dire que si l'on a rien à se reprocher, on a rien à craindre, auquel cas j'aimerais vous rappeler que oui c'est vrai en un sens mais aussi que "big brother is watching you", eux aussi n'avaient rien à cacher... Cela va jusqu'à leur obtenir le surnom d'"éponge à métadonnées" par un utilisateur reddit, surnom largement mérité en mon opinion. Pour couronner le tout un bon 30% des connexions se font sur les serveurs principaux de matrix ou sur leur application principale qui, si je comprends bien, force les utilisateurs à s'inscrire sur le réseau principal, recentralisant donc le service.

En plus de ça la mentalité des développeurs est problématique. Ils sont lents, n'arrivent pas vraiment à faire décoller leur application, qui a pourtant maintenant 6 ans, choisissent de développer le côté pratique plutôt que la sécurité et, plutôt que d'accepter leurs problèmes de leur application, ont l'air de tout tenter pour blâmer les autres et les enfoncer, tout en ayant une idée glorifiée de leur travail. Il faudrait leur donner encore du temps pour leur permettre de développer un meilleur protocole, pour leur donner le temps de s'atteler à une meilleure sécurité mais a-t-on vraiment besoin de tant d'années pour se jeter des lauriers pas mérités?

</div>

<div class="note-embed-foot"><a href="/privacy/messaging/matrix/">Open the full note →</a>
</div>

</div>

<div class="note-embed">

<div class="note-embed-head"><a class="note-embed-title" href="/privacy/messaging/rocket-chat/">Rocket.chat</a><span class="note-embed-meta">Updated 2026-09-08</span>
</div>

<div class="note-embed-body">


### Rocket.chat
#### TL;DR
Rocket.chat est une application orientée vers la commercialisation et la surveillance de votre communauté, ils font eux-même la pub de leur service comme un hébergement sur cloud d'un service de messagerie à la demande ou le déploiement d'une messagerie "sécurisée" en local. Ils ne sont pas du tout orientés vers la vie privée.

#### Analyse
Rocket.chat se présente comme un service de messagerie fédéré.[^rocketgetstarted] Plus que proche de matrix, ils se basent carrément sur le protocole de matrix pour faire tourner leur service.[^rocketmatrix] Ils bénéficient donc des systèmes de sécurité de Matrix plus ceux qu'ils rajoutent eux-même. Leur plus-value principale est de proposer différents déploiements: local, cloud ou air-gapped, un déploiement sur une version, selon leurs dires, isolée du reste du web.[^rocketplans] Local est bien évidemment un déploiement sur un serveur local tandis que cloud est une option hébergée sur leurs serveurs.

Le problème de s'être basé sur matrix est qu'ils continuent les erreurs précédentes de matrix, ils auraient pu décider de renforcer la sécurité mais à la place ont décidé de renforcer le logging et faire machine arrière sur certaines choses comme le E2EE ou les informations sur les utilisateurs.[^rocketauthentication] Un administrateur a maintenant les pleins pouvoirs: il peut forcer les utilisateurs à se connecter avec LDAP, oAuth, 2FA, etc.[^rocketauthentication] En plus de ça il a également les pleins pouvoirs sur le E2EE, il doit activer l'E2EE sur un workspace avant de pouvoir le mettre en place sur un chat, même privé, ce qui lui permet de décider que personne ne peut lui cacher des messages.[^rockete2ee] J'ai mentionné les informations sur les utilisateurs, il se trouve que les développeurs ont eu l'idée géniale de remettre en place des informations comme les marqueurs de lecture ou de connexion des utilisateurs. En bref leur but n'est clairement pas de limiter les informations mais plutôt de les multiplier et les centraliser vers un seul utilisateur. Pire que ça, ils assument clairement le côté surveillance et proposent des outils pour obtenir des données sur les utilisateurs et utilisations.[^rocketmetrics] Encore une preuve de la mentalité de l'application, le document qui permet de comparer les options est bloqué derrière un login...[^rocketdocumenthidden]

Les versions commerciales sont largement développées, à l'inverse des versions gratuites.[^rocketplans] La version gratuite a un nombre limité d'utilisateur, d'applications tierces pour l'utilisation de rocket, etc etc. Tout ce qui mérite d'être utilisé, même la version air-gapped, est payant, et bloqué derrière un abonnement pour entreprise. Même la license MIT qu'ils ont obtenue ne concerne qu'une partie de leur code sur github, la license commerciale, elle, concerne en revanche bien tout leur code sans exception.[^rocketgithub] (Il faut souligner d'ailleurs que leur point majeur de vente est la solution air-gapped mais que personne ne décrit vraiment ce qu'on y trouve, ça reste un mystère... hermétique !)

Dans ce qui est des avis utilisateurs, malgré la possibilité d'utiliser des applications tierces, les avis ressortent majoritairement négatifs. Les utilisateurs trouvent l'application peu pratique et la campagne aggressive pour la commercialisation de leurs plans est apparemment mal passée.[^rocketreview][^rocketreddit] Ironiquement le seul site sur lequel on trouve une grande majorité des avis positifs semble pouvoir être acheté puisque les avis ressemblent fort à de faux avis. Bien sûr je n'ai aucune preuve mais quelque chose (mon petit doigt) me dit qu'il y a de la corruption dans l'air.[^rocketfakereview]

Pour ce qui est de la sécurité en elle-même, ce qu'ils ont réutilisé, c'est à dire le protocole de matrix, semble robuste, il faut dire qu'il avait déjà fait ses preuves par le passé, tout le reste semble fragile comme du papier mâché. NoSQLi, auth bypass et autres CVEs, tout y est. Du moment qu'ils ne l'ont pas piqué, c'est vulnérable. C'est d'autant plus dommage qu'ils ont l'air de destiner leurs services à des organisations telles que l'armée des états-unis (déjà clients), l'air force et autres organisations gouvernementales ayant des missions secrètes à mettre à bien.

En bref on fait face à une entreprise qui est assoiffée d'argent et met l'accent sur vendre. Quand ses développeurs ne sont pas trop concentrés sur les chiffres, il semble qu'ils passent leur temps à dévier une application dédiée à la vie privée (en partie) et en faire un outil de surveillance isolé du monde extérieur, une petite corée du nord dans votre salon...

[^rocketgetstarted]:[Rocket presentation page](https://docs.rocket.chat/docs/rocketchat)
[^rocketmatrix]:[Rocket.chat base: matrix](https://www.rocket.chat/blog/delivering-matrix-federation-as-a-built-in-standard)
[^Rocketplans]:[Rocket plans](https://docs.rocket.chat/docs/our-plans)
[^rocketauthentication]:[Rocket.chat authentication methods](https://docs.rocket.chat/docs/authentication)
[^rockete2ee]:[Rocket.chat approach to E2EE](https://docs.rocket.chat/docs/configure-e2e-encryption)
[^rocketdocumenthidden]:[Rocket documentation on plans using document360](https://portal.us.document360.io/v1/docs/choose-your-deployment-model)
[^rocketgithub]:[Rocket.chat on github](https://github.com/RocketChat/Rocket.Chat?tab=License-1-ov-file)

[^rocketfakereview]:[Rocket fake reviews](https://www.capterra.com/p/161575/Rocket-Chat/reviews/)
[^rocketreview]:[Rocket review on technical blog](https://www.techradar.com/reviews/rocketchat)
[^rocketreddit]:[Rocket pushing premium options, reddit](https://www.reddit.com/r/selfhosted/comments/ynzakd/why_is_rocketchat_recommended/)

[^rocketnosqli]:[CVE affecting rocket: NoSQLi](https://www.sentinelone.com/vulnerability-database/cve-2026-30833/)
[^rocket2fabypass]:[CVE affecting rocket 2FA](https://vulners.com/cve/CVE-2026-30831)
[^rocketcvelist]:[List of CVEs affecting Rocket.chat (and not matrix, for the bigger part)](https://app.opencve.io/cve/?vendor=rocketchat)

</div>

<div class="note-embed-foot"><a href="/privacy/messaging/rocket-chat/">Open the full note →</a>
</div>

</div>

{% endraw %}
