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

# Introduction

Les services de messagerie sont importants ils permettent de communiquer. La différence principale réside dans la différence entre centralisé, fédéré et p2p, la comprendre donne des indications sur le fonctionnement de chacune et l'importance accordée à la vie privée. [^decentralizedcomparison]

[^decentralizedcomparison]: [P2P, federated et centralized comparaison - RVNT](https://rvntos.io/blog/p2p-vs-federated-vs-centralized-messaging/)

# Contenu

Dans cette partie vous verrez tous les services de messagerie que je trouve intéressants, sûrs, pratiques, enfin bref ce que je juge suffisamment sûr d'utiliser. Les critères de sélection pouvant être très personnels, je vous invite fortement à prendre cette décision par vous-même, c'est pourquoi chaque page contient aussi des liens permettant de se faire une meilleure idée sur le sujet.

<div class="note-embed">

<div class="note-embed-head"><a class="note-embed-title" href="/privacy/messaging/signal/">Signal</a><span class="note-embed-meta">Updated 2026-09-08</span>
</div>

<div class="note-embed-body">


### Signal
#### TL;DR
Très probablement la meilleure messagerie que vous pourrez installer pour une utilisation quotidienne et simple. La sécurité est sans appel. La messagerie est centralisée donc Signal pourrait décider d'enregistrer certaines métadonnées sur les communications mais le groupe a été est prouvé digne de confiance ***a posteriori*** et ***a priori***, un bel avantage.

#### Analyse
Signal est une messagerie instantanée, centralisée, proposée comme un service de communication digne de confiance, tant pour la sécurité que pour la vie privée.<sup class="fn-ref" id="fnref-messaging-signal-signalattack"><a href="#fn-messaging-signal-signalattack">1</a></sup><sup class="fn-ref" id="fnref-messaging-signal-signalprinciples"><a href="#fn-messaging-signal-signalprinciples">2</a></sup><sup class="fn-ref" id="fnref-messaging-signal-signalphoneprivacy"><a href="#fn-messaging-signal-signalphoneprivacy">3</a></sup> Ils accordent clairement une forte importance à la transparence en effectuant des audits third-party<sup class="fn-ref" id="fnref-messaging-signal-signalaudits"><a href="#fn-messaging-signal-signalaudits">4</a></sup> et les instructions de la justice.<sup class="fn-ref" id="fnref-messaging-signal-signallegal"><a href="#fn-messaging-signal-signallegal">5</a></sup><sup class="fn-ref" id="fnref-messaging-signal-signallsubpoena"><a href="#fn-messaging-signal-signallsubpoena">6</a></sup> Pour appuyer ça, ils ont aussi une license AGPLv3.0 sur l'application ET le serveur. <sup class="fn-ref" id="fnref-messaging-signal-signallicense"><a href="#fn-messaging-signal-signallicense">7</a></sup><sup class="fn-ref" id="fnref-messaging-signal-signalserverlicense"><a href="#fn-messaging-signal-signalserverlicense">8</a></sup> Si vous en doutez encore, vous pouvez opter pour l'option fédérée et faire tourner votre propre serveur.<sup class="fn-ref" id="fnref-messaging-signal-signallocalserver"><a href="#fn-messaging-signal-signallocalserver">9</a></sup>

La théorie: Signal est une application largement tournée vers la vie privée. Tout ce qui est important (contacts, données personnelles, clés, messages, ...) est stocké sur l'appareil de l'utilisateur, nulle part ailleurs.<sup class="fn-ref" id="fnref-messaging-signal-signalprivateprofiles"><a href="#fn-messaging-signal-signalprivateprofiles">10</a></sup> Les seules informations stockées sur les serveurs sont le numéro de l'utilisateur, la date de création de son compte et la dernière date de connexion, tout le reste n'est que sur votre appareil, nulle part ailleurs. Certains articles mettent justement l'accent sur l'importance qu'ils accordent aux profils privés. En plus de ça Signal a développé le "**sealed sender**", qui permet normalement de cacher qui envoie un message (sauf pour le premier message.<sup class="fn-ref" id="fnref-messaging-signal-signalsealedsender"><a href="#fn-messaging-signal-signalsealedsender">11</a></sup>

La pratique: En pratique oui, Signal ne log rien du tout, certains cas d'intervention de la justice le prouvent d'ailleurs, ce qui renforce ce que signal dit de son système.<sup class="fn-ref"><a href="#fn-messaging-signal-signallegal">5</a></sup> En revanche cela ne signifie pas que tout est imperméable à l'identification. Pour ce qui est de l'encryption,  <sup class="fn-ref" id="fnref-messaging-signal-signalencryption"><a href="#fn-messaging-signal-signalencryption">12</a></sup>

En théorie il est possible de traquer un utilisateur: le traffic n'étant pas infini, le nombre de messages reçus par une personne en particulier puis par une autre, potentiellement liée à cette première personne ou non, peuvent être corrélés.<sup class="fn-ref" id="fnref-messaging-signal-signalsurveillance"><a href="#fn-messaging-signal-signalsurveillance">13</a></sup> Il est rare que Alice reçoive 4 messages dans la journée, que Bob en reçoive 5 et que cela n'ait aucun lien. Tout cela se renforce encore lorsque l'on peut analyser les paquets qui partent vers signal ou encore les *timestamp* sur les paquets, car **Signal** n'utilise pas le **mixnet**. Mais encore une fois Signal a prouvé qu'il était digne de confiance par le passé, a démontré à de multiples reprises qu'ils ne céderaient pas aux injonctions des forces de l'ordre et qu'ils tenaient particulièrement à ne garder aucune info.

En somme la conclusion est simple: tout comme un VPN, vous choisissez de faire confiance à une entité particulière et de garder un semblant de facilité d'utilisation plutôt que d'utiliser quelque chose d'intraçable. C'est, il me semble, un bon équilibre pour la vie de tous les jours.




<div class="note-embed-footnotes">

1. <span id="fn-messaging-signal-signalattack"></span>[Attaque sur Signal - official website](https://support.signal.org/hc/en-us/articles/4850133017242-Twilio-Incident-What-Signal-Users-Need-to-Know) <a class="fn-back" href="#fnref-messaging-signal-signalattack">↩</a>
2. <span id="fn-messaging-signal-signalprinciples"></span>[Signal's principles (official website)](https://signal.org/blog/looking-back-as-the-world-moves-forward/) <a class="fn-back" href="#fnref-messaging-signal-signalprinciples">↩</a>
3. <span id="fn-messaging-signal-signalphoneprivacy"></span>[Signal phone numbers privacy - official documentation](https://support.signal.org/hc/en-us/articles/6712070553754-Phone-Number-Privacy-and-Usernames) <a class="fn-back" href="#fnref-messaging-signal-signalphoneprivacy">↩</a>
4. <span id="fn-messaging-signal-signalaudits"></span>[Signal List of third-party security audits - official website](https://community.signalusers.org/t/overview-of-third-party-security-audits/13243) <a class="fn-back" href="#fnref-messaging-signal-signalaudits">↩</a>
5. <span id="fn-messaging-signal-signallegal"></span>[Legal orders on Signal - official website](https://signal.org/bigbrother/) <a class="fn-back" href="#fnref-messaging-signal-signallegal">↩</a>
6. <span id="fn-messaging-signal-signallsubpoena"></span>[Subpoenas aiming Signal - official website](https://signal.org/bigbrother/central-california-grand-jury/) <a class="fn-back" href="#fnref-messaging-signal-signallsubpoena">↩</a>
7. <span id="fn-messaging-signal-signallicense"></span>[Signal Android - github](https://github.com/signalapp/Signal-Android) <a class="fn-back" href="#fnref-messaging-signal-signallicense">↩</a>
8. <span id="fn-messaging-signal-signalserverlicense"></span>[Signal server on github](https://github.com/signalapp/Signal-Server) <a class="fn-back" href="#fnref-messaging-signal-signalserverlicense">↩</a>
9. <span id="fn-messaging-signal-signallocalserver"></span>[Running a local server](https://www.reddit.com/r/signal/comments/7poh3f/is_it_possible_to_create_a_private_signal_server/) <a class="fn-back" href="#fnref-messaging-signal-signallocalserver">↩</a>
10. <span id="fn-messaging-signal-signalprivateprofiles"></span>[Signal's private profiles - official website](https://signal.org/blog/signal-profiles-beta/) <a class="fn-back" href="#fnref-messaging-signal-signalprivateprofiles">↩</a>
11. <span id="fn-messaging-signal-signalsealedsender"></span>[Signal's sealed sender - official website](https://signal.org/blog/sealed-sender/) <a class="fn-back" href="#fnref-messaging-signal-signalsealedsender">↩</a>
12. <span id="fn-messaging-signal-signalencryption"></span>[Why is Signal so secure? - article](https://aboutsignal.com/signal-security-privacy-guide/) <a class="fn-back" href="#fnref-messaging-signal-signalencryption">↩</a>
13. <span id="fn-messaging-signal-signalsurveillance"></span>[On signal's ability to know who is talking to who - article](https://sanesecurityguy.com/articles/signal-knows-who-youre-talking-to/) <a class="fn-back" href="#fnref-messaging-signal-signalsurveillance">↩</a>

</div>

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
Leur mission est claire: apporter des systèmes de messagerie à ceux pour qui ça peut être difficile de communiquer comme les utilisateurs dans des pays sous dictature, les journalistes, whistleblowers, etc. Il est donc clair dès le départ que l'emphase sera mise sur la sécurité et la vie privée et non sur la maniabilité.<sup class="fn-ref" id="fnref-messaging-briar-briarhomepage"><a href="#fn-messaging-briar-briarhomepage">1</a></sup><sup class="fn-ref" id="fnref-messaging-briar-briarusermanual"><a href="#fn-messaging-briar-briarusermanual">2</a></sup> C'est d'ailleurs très bien illustré par le modèle d'attaquant choisi, stipulé tout en bas de la page d'accueil.<sup class="fn-ref"><a href="#fn-messaging-briar-briarhomepage">1</a></sup>

La sécurité elle-même est assurée par leur protocole p2p: Bramble Transport Protocol.[^briarbramble] Le protocole en lui-même est robuste, il a été audité, prouvé, il n'y a aucun doute sur sa capacité à résister.<sup class="fn-ref" id="fnref-messaging-briar-briarrelease"><a href="#fn-messaging-briar-briarrelease">3</a></sup><sup class="fn-ref" id="fnref-messaging-briar-briarcryptography"><a href="#fn-messaging-briar-briarcryptography">4</a></sup><sup class="fn-ref" id="fnref-messaging-briar-briaraudit"><a href="#fn-messaging-briar-briaraudit">5</a></sup> En plus de toute cette encryption, Briar utilise Tor pour router ses messages quand ils sont envoyés en ligne, ce qui renforce la sécurité mais aussi le côté privé de l'application.<sup class="fn-ref"><a href="#fn-messaging-briar-briarhomepage">1</a></sup><sup class="fn-ref"><a href="#fn-messaging-briar-briarcryptography">4</a></sup>

La vie privée est clairement un des points importants pour briar, ils ont à coeur de développer quelque chose qui pourrait entièrement cacher les utilisateurs qui l'utilisent. Pour cela, dès que les messages sont envoyés par le réseau ils passent par Tor, dès qu'ils sont envoyés en local, ils ne sont reçus ou transmis que par les appareils concernés, clairement une mesure d'exception pour la vie privée.

Evidemment toutes ces mesures de sécurité ont un impact sur la facilité d'utilisation. Le plus important à mon avis est que Briar est loin d'être intuitif et certaines opérations ne sont pas du tout évidentes.<sup class="fn-ref" id="fnref-messaging-briar-briarreview"><a href="#fn-messaging-briar-briarreview">6</a></sup><sup class="fn-ref" id="fnref-messaging-briar-briarreddit"><a href="#fn-messaging-briar-briarreddit">7</a></sup> En plus de ça les quelques fonctionnalités sur lesquelles les services se basent pour faciliter la vie aux utilisateurs sont retirées: contacts, ajout rapide, envoi hors ligne, etc etc. D'autant plus que Briar est inaccessible sur un produit Apple, une très bonne nouvelle à mon avis (disons le, n'importe quelle personne prétendant vouloir protéger ses données n'achètera pas un apple...). Malgré tout Briar a ajouté quelques fonctionnalités pour combler ce manque: une liste de contact qui correspond aux critères de Briar, une application mailbox pour pouvoir recevoir des messages hors ligne ou presque, etc.[^briermailbox]

Il faut aussi mentionner les groupes et communautés qui sont d'autant plus intéressantes en utilisant briar offline: du moment que deux personnes d'une communauté sont à portée l'une de l'autre, les messages sont transmis. Ca permet notamment qu'une personne qui voyage, se déplace, puisse transmettre les messages aux différentes parties de la communauté, vraiment sexy!

Enfin l'équipe de développement est plus qu'intéressante. Entre l'accent mis sur la vie privée, le but même de l'application et l'apparente absence de concession dans leur développement, même lorsqu'il s'agit de batterie, ils donnent plus que des raisons de leur faire confiance. En plus de ça le projet est open source et protégé par une license AGPLv3, un point positif à mon goût.<sup class="fn-ref" id="fnref-messaging-briar-briarmaintenance"><a href="#fn-messaging-briar-briarmaintenance">8</a></sup><sup class="fn-ref" id="fnref-messaging-briar-briargithub"><a href="#fn-messaging-briar-briargithub">9</a></sup>




<div class="note-embed-footnotes">

1. <span id="fn-messaging-briar-briarhomepage"></span>[Briar Homepage](https://briarproject.org/how-it-works/) <a class="fn-back" href="#fnref-messaging-briar-briarhomepage">↩</a>
2. <span id="fn-messaging-briar-briarusermanual"></span>[Briar User manual](https://briarproject.org/manual/) <a class="fn-back" href="#fnref-messaging-briar-briarusermanual">↩</a>
3. <span id="fn-messaging-briar-briarrelease"></span>[Briar Post about briar's release and audit](https://briarproject.org/news/2017-beta-released-security-audit/) <a class="fn-back" href="#fnref-messaging-briar-briarrelease">↩</a>
4. <span id="fn-messaging-briar-briarcryptography"></span>[Cryptography in the wild: Briar - Yuanming Song](https://ethz.ch/content/dam/ethz/special-interest/infk/inst-infsec/appliedcrypto/education/theses/report_YuanmingSong.pdf) <a class="fn-back" href="#fnref-messaging-briar-briarcryptography">↩</a>
5. <span id="fn-messaging-briar-briaraudit"></span>[Briar Cure 53 security audit](https://briarproject.org/raw/BRP-01-report.pdf) <a class="fn-back" href="#fnref-messaging-briar-briaraudit">↩</a>
6. <span id="fn-messaging-briar-briarreview"></span>[Briar Review by tech-oblivious people](https://www.pcmag.com/reviews/briar) <a class="fn-back" href="#fnref-messaging-briar-briarreview">↩</a>
7. <span id="fn-messaging-briar-briarreddit"></span>[Briar User comparison with Signal](https://www.reddit.com/r/privacytoolsIO/comments/kpq3ri/comment/gisj73a/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) <a class="fn-back" href="#fnref-messaging-briar-briarreddit">↩</a>
8. <span id="fn-messaging-briar-briarmaintenance"></span>[Briar Development state & maintenance mode](https://briarproject.org/news/2026-maintenance-mode/) <a class="fn-back" href="#fnref-messaging-briar-briarmaintenance">↩</a>
9. <span id="fn-messaging-briar-briargithub"></span>[Briar on github](https://github.com/briar/briar?tab=License-1-ov-file) <a class="fn-back" href="#fnref-messaging-briar-briargithub">↩</a>

</div>

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
Pour commencer, comme d'habitude, le but de l'application. Ce service de messagerie fédéré est destiné aux utilisateurs professionnels (journalistes, whitleblowers, activistes, victimes de dictatures, anglais, ... Notre lot classique de personnes en milieu sensible.) mais aussi aux utilisateurs particuliers avec un simple but d'améliorer leur vie privée. Eh oui, n'importe qui peut facilement utiliser SimpleX. leur but est d'amener un service de messagerie qui s'adapte à chaque utilisateur. Même si je suis d'habitude assez opposé à utiliser un couteau-suisse, celui-ci est tellement bien pensé qu'il est difficile de l'éviter.<sup class="fn-ref" id="fnref-messaging-simplex-simplexhomepage"><a href="#fn-messaging-simplex-simplexhomepage">1</a></sup>

Déjà pour la partie importante, est-ce sécurisé? Oui. On retrouve le classique E2EE, double ratchet, et même de la post-quantum encryption. Et puis bien sûr le classique audit indépendant a permis de trouver quelques failles mais rien de majeur.<sup class="fn-ref" id="fnref-messaging-simplex-simplexaudit"><a href="#fn-messaging-simplex-simplexaudit">2</a></sup>

Pour le reste je vais essayer de vous énumérer les fonctionnalités les plus importantes. Commençons par l'identification. Déjà vous ne donnez aucune information à la création d'un compte, vous entrez simplement un nom, un mot de passe et voilà. Le mieux là-dedans c'est que rien n'est stocké en ligne, le mot de passe vous sert à déchiffrer la base de données en local et rien d'autre. Alors il faut faire attention parce que cela signifie, comme pour briar, que vous ne pouvez avoir deux appareils sur le même compte et que si vous perdez votre compte, vous dites adieu à vos conversations.

C'est d'autant plus important que la façon d'ajouter un contact est, je dois le dire, un coup de génie. Chaque utilisateur peut avoir une addresse moyenne durée sur demande mais l'addresse de base, partagée à vos contact, change en fonction du contact.[^simplexaddresses] Cela signifie notamment que personne ne peut relier deux conversations avec deux personnes différentes à un seul utilisateur. Cela signifie aussi que c'est votre base de données locale qui gère ces connexions.

Une autre fonctionnalité importante, j'irais jusqu'à dire la plus séduisante, est le SimpleX network. SimpleX, après quelques changements, a décidé de développer son propre réseau s'apparentant à un onion routeur.<sup class="fn-ref" id="fnref-messaging-simplex-simplexnetwork"><a href="#fn-messaging-simplex-simplexnetwork">3</a></sup> Les différences sont qu'ils n'utilisent que deux noeuds pour router les connexions et que, plutôt que d'utiliser des noeuds aléatoires, ils ont décidé de n'utiliser que des noeuds choisis. L'expéditeur choisit le noeud de relais, premier noeud dans la suite, la destination choisit le noeud de destination, le second dans ce réseau. De cette façon aucun noeud ne peut avoir toutes les informations sur le réseau, il est impossible pour un organisme comme la NSA d'avoir un dixième des noeuds déployés sur le réseau. Alors ça a bien sûr ses inconvénients, notamment sur la difficulté pour une personne lambda d'avoir un serveur de confiance, mais ça a quand même le mérite de particulièrement bien fonctionner pour cacher les connexions, surtout que le protocole encrypte la destination (oui, la destination, non pas l'expéditeur) et la cache au noeud de relais, ce qui l'empêche de connaître tout le chemin et ne lui permet de connaître que l'expéditeur et le prochain noeud.<sup class="fn-ref"><a href="#fn-messaging-simplex-simplexnetwork">3</a></sup> Cette simple fonctionnalité de cacher la destination, combinée avec les serveurs et développeurs de confiance, font que je pense sincèrement que SimpleX peut tout à fait rivaliser avec Signal en terme de messagerie centralisée de confiance, alors qu'elle le fait largement en tant que messagerie fédérée.

La messagerie étant fédérée (j'aurais dû en parler dès le début mais vous voyez tout ce qu'il y a à dire) vous pouvez bien sûr faire tourner votre propre serveur localement sans grande difficulté. Si vous n'avez pas spécialement envie de le faire vous-même, certaines communautés et personnes proposent d'utiliser leurs serveurs et vous proposent des listes de tels serveurs, ce qui permet de multiplier les serveurs utilisés et est d'autant plus important de par la construction de SimpleX network.<sup class="fn-ref" id="fnref-messaging-simplex-simplexcommunityservers"><a href="#fn-messaging-simplex-simplexcommunityservers">4</a></sup>

Bien sûr cela peut poser problème pour les conversations où les deux utilisateurs se connectent aux serveurs d'une même entité, d'autant plus quand simplex est la connexion par défaut, mais encore une fois ils y ont pensé. Déjà ils ont ajouté la possibilité de se connecter aux serveurs de flux, un autre provider qui propose de se connecter par défaut à ses serveurs. Si l'option est activée, l'application se connecte d'ailleurs à l'un pour envoyer et l'autre pour recevoir, assurant qu'aucun n'aura d'infos sur le chemin complet.<sup class="fn-ref" id="fnref-messaging-simplex-simplexflux"><a href="#fn-messaging-simplex-simplexflux">5</a></sup> En plus SimpleX a (partiellement) prouvé être digne de confiance entre l'importance qu'ils accordent aux métadonnées et la façon dont ils ont répondu aux exigences de la loi et puis surtout la license AGPLv3.<sup class="fn-ref" id="fnref-messaging-simplex-simplexprivacy"><a href="#fn-messaging-simplex-simplexprivacy">6</a></sup><sup class="fn-ref" id="fnref-messaging-simplex-simplextransparency"><a href="#fn-messaging-simplex-simplextransparency">7</a></sup><sup class="fn-ref" id="fnref-messaging-simplex-simplexgithub"><a href="#fn-messaging-simplex-simplexgithub">8</a></sup>

En plus de tout ça on retrouve quelques fonctionnalités de sécurité telles que la connexion par tor, la messagerie incognito et les groupes secrets.<sup class="fn-ref" id="fnref-messaging-simplex-simplexincognito"><a href="#fn-messaging-simplex-simplexincognito">9</a></sup><sup class="fn-ref" id="fnref-messaging-simplex-simplexsecretgroups"><a href="#fn-messaging-simplex-simplexsecretgroups">10</a></sup> Ces fonctionnalités combinées au développement de SimpleX font qu'aucune info ne peut vraiment transiter: SimpleX n'a jamais demandé votre identité, les quelques métadonnées qu'ils peuvent connecter sont en fait juste quel profil de conversation est associé à quel ip (puisqu'ils ne peuvent pas lier vos différentes addresses de vos différentes conversations ***a priori*** ils ne peuvent donc dire à qui vous parlez ou quand) lorsque ***et uniquement lorsque*** vous et votre interlocuteur utilisez tous deux leurs serveurs, auquel cas vous pouvez simplement décider d'utiliser Tor avant la connexion au noeud pour cacher votre IP, la seule info qu'ils avaient sur vous disparaît dans le vent.

Pour ce qui est de l'utilisation et des retours utilisateurs, ils sont étonnamment positifs. SimpleX a développé un paquet de fonctionnalités plutôt intéressantes. Certaines comme les communautés sont faites pour l'aisance d'utilisation alors que d'autre comme les live messages sont faites pour les utilisateurs sensibles, ce qui prouve d'autant plus l'importance qu'ils accordent à la sécurité de leur application et la possibilité de l'utiliser en contexte difficile.<sup class="fn-ref" id="fnref-messaging-simplex-simplexfunctionnalities"><a href="#fn-messaging-simplex-simplexfunctionnalities">11</a></sup> En plus de ça les quelques reviews qui existent ont l'air de faire les louanges de SimpleX et de sa facilité d'utilisation, ce qui est d'autant plus rare que certaines de ces louanges viennent de reddit.<sup class="fn-ref" id="fnref-messaging-simplex-simplexreview"><a href="#fn-messaging-simplex-simplexreview">12</a></sup><sup class="fn-ref" id="fnref-messaging-simplex-simplexreddit"><a href="#fn-messaging-simplex-simplexreddit">13</a></sup>

La messagerie elle-même est très bien développée. Entre la base d'utilisateurs massive et leurs idées pour développer l'application, c'est largement prometteur. Ils ont en effet prévu de financer la continuation du développement de l'application et la maintenance des serveurs en proposant aux serveurs des fonctionnalités payantes (nom de domaine personnalisé, serveurs, etc). Tout cela donne plus d'espoir sur le développement de SimpleX que sur celui de Session ou Briar. C'est d'autant plus intéressant que ces fonctionnalités sont utiles pour les communautés et qu'ils ne poussent pas leur modèle économique sur les utilisateurs comme rocket.chat. Ils annoncent même financer l'application entière en se basant entièrement sur les financements apportés par les serveurs.<sup class="fn-ref" id="fnref-messaging-simplex-simplexfinancial"><a href="#fn-messaging-simplex-simplexfinancial">14</a></sup>

SimpleX est même utilisé en ce moment même par la communauté principale de monero, vous permettant d'accéder à des ressources importantes ou de l'aide des développeurs.

En note additionnelle mais pas nécessairement utile, certaines sources s'amusent à critiquer ouvertement SimpleX et les associer à des communautés néo-nazies dans le but de promouvoir le chat control, ce qui prouve partiellement l'importance qu'a pu gagner SimpleX à travers les années.

En plus de ça, de par sa construction, SimpleX, ou plutôt les serveurs privés permettant de se connecter à SimpleX, sont immunisés normalement à chatcontrol et aux autres lois horribles auxquelles nos gouvernements peuvent penser à l'avenir, malgré ce qu'en disent les utilisateurs reddit. Malgré tout, le siège étant localisé en Angleterre, il faut surveiller les changements dans le code, qui pourraient être imposés par le gouvernement.<sup class="fn-ref" id="fnref-messaging-simplex-simplexchatcontrol"><a href="#fn-messaging-simplex-simplexchatcontrol">15</a></sup><sup class="fn-ref" id="fnref-messaging-simplex-simplexwired"><a href="#fn-messaging-simplex-simplexwired">16</a></sup><sup class="fn-ref" id="fnref-messaging-simplex-simplexwiredoriginal"><a href="#fn-messaging-simplex-simplexwiredoriginal">17</a></sup> Le seul nuage à l'horizon est le fait que SimpleX ait eu plusieurs requêtes du gouvernement et ne nous ai pas montré leurs réponses finales excepté celles qui disaient qu'ils aideraient le gouvernement british. A voir ce que cela donne en réelle situation catastrophique comme pour Mullvad VPN ou session.

[simplexaddresses]: [SimpleX's solution, safe addresses](https://simplex.chat/docs/guide/making-connections.html)



<div class="note-embed-footnotes">

1. <span id="fn-messaging-simplex-simplexhomepage"></span>[SimpleX chat homepage](https://simplex.chat/) <a class="fn-back" href="#fnref-messaging-simplex-simplexhomepage">↩</a>
2. <span id="fn-messaging-simplex-simplexaudit"></span>[Independant audit of SimpleX](https://files.safe.de.fi/safe/files/audit/pdf/SimpleXChat.pdf) <a class="fn-back" href="#fnref-messaging-simplex-simplexaudit">↩</a>
3. <span id="fn-messaging-simplex-simplexnetwork"></span>[SimpleX network](https://simplex.chat/blog/20240604-simplex-chat-v5.8-private-message-routing-chat-themes.html) <a class="fn-back" href="#fnref-messaging-simplex-simplexnetwork">↩</a>
4. <span id="fn-messaging-simplex-simplexcommunityservers"></span>[SimpleX Community servers list](https://discuss.privacyguides.net/t/simplex-community-servers-list/21443/6) <a class="fn-back" href="#fnref-messaging-simplex-simplexcommunityservers">↩</a>
5. <span id="fn-messaging-simplex-simplexflux"></span>[SimpleX: Flux servers arriving on SimpleX](https://simplex.chat/blog/20241125-servers-operated-by-flux-true-privacy-and-decentralization-for-all-users.html) <a class="fn-back" href="#fnref-messaging-simplex-simplexflux">↩</a>
6. <span id="fn-messaging-simplex-simplexprivacy"></span>[SimpleX Privacy policy](https://simplex.chat/privacy/) <a class="fn-back" href="#fnref-messaging-simplex-simplexprivacy">↩</a>
7. <span id="fn-messaging-simplex-simplextransparency"></span>[SimpleX Transparency reports](https://simplex.chat/transparency/) <a class="fn-back" href="#fnref-messaging-simplex-simplextransparency">↩</a>
8. <span id="fn-messaging-simplex-simplexgithub"></span>[SimpleX github](https://github.com/simplex-chat/simplexmq/blob/stable/protocol/simplex-messaging.md) <a class="fn-back" href="#fnref-messaging-simplex-simplexgithub">↩</a>
9. <span id="fn-messaging-simplex-simplexincognito"></span>[SimpleX Incognito mode and chat profiles](https://simplex.chat/docs/guide/chat-profiles.html) <a class="fn-back" href="#fnref-messaging-simplex-simplexincognito">↩</a>
10. <span id="fn-messaging-simplex-simplexsecretgroups"></span>[SimpleX Secret groups](https://simplex.chat/docs/guide/secret-groups.html) <a class="fn-back" href="#fnref-messaging-simplex-simplexsecretgroups">↩</a>
11. <span id="fn-messaging-simplex-simplexfunctionnalities"></span>[SimpleX Live messages and other functionnalities](https://simplex.chat/docs/guide/send-messages.html) <a class="fn-back" href="#fnref-messaging-simplex-simplexfunctionnalities">↩</a>
12. <span id="fn-messaging-simplex-simplexreview"></span>[External SimpleX review](https://itsfoss.com/news/simplex-chat/) <a class="fn-back" href="#fnref-messaging-simplex-simplexreview">↩</a>
13. <span id="fn-messaging-simplex-simplexreddit"></span>[SimpleX chat discussed on reddit](https://www.reddit.com/r/privacy/comments/z4990l/thoughts_on_simplex_chat/) <a class="fn-back" href="#fnref-messaging-simplex-simplexreddit">↩</a>
14. <span id="fn-messaging-simplex-simplexfinancial"></span>[SimpleX Monetary incentive](https://simplex.chat/crowdfunding/) <a class="fn-back" href="#fnref-messaging-simplex-simplexfinancial">↩</a>
15. <span id="fn-messaging-simplex-simplexchatcontrol"></span>[SimpleX and chat control on reddit](https://www.reddit.com/r/SimpleXChat/comments/1uue5e3/chat_control/) <a class="fn-back" href="#fnref-messaging-simplex-simplexchatcontrol">↩</a>
16. <span id="fn-messaging-simplex-simplexwired"></span>[SimpleX attacked by Wired](https://simplex.chat/blog/20241016-wired-attack-on-privacy.html) <a class="fn-back" href="#fnref-messaging-simplex-simplexwired">↩</a>
17. <span id="fn-messaging-simplex-simplexwiredoriginal"></span>[Wired on simpleX (for the laughs)](https://www.wired.com/story/neo-nazis-flee-telegram-encrypted-app-simplex/) <a class="fn-back" href="#fnref-messaging-simplex-simplexwiredoriginal">↩</a>

</div>

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
La politique de Session est claire et honnête, le but est de proposer un service de messagerie sécurisé et anonyme. <sup class="fn-ref" id="fnref-messaging-session-sessionmainpage"><a href="#fn-messaging-session-sessionmainpage">1</a></sup> <sup class="fn-ref" id="fnref-messaging-session-sessionlitepaper"><a href="#fn-messaging-session-sessionlitepaper">2</a></sup> <sup class="fn-ref" id="fnref-messaging-session-sessionfinances"><a href="#fn-messaging-session-sessionfinances">3</a></sup> En plus d'insister sur l'importance de l'anonymat et les problèmes que représentent l'utilisation d'infos personnelles comme un numéro de téléphone ou un email, ils insistent sur l'absence d'info qui permettent d'identifier un utilisateur et la collecte minimale de métadonnées, ce qui présage de bonnes choses. <sup class="fn-ref" id="fnref-messaging-session-sessionaccount"><a href="#fn-messaging-session-sessionaccount">4</a></sup><sup class="fn-ref" id="fnref-messaging-session-sessionmessenger"><a href="#fn-messaging-session-sessionmessenger">5</a></sup> Ils ont aussi la license AGPLv3 (j'aime cette license).<sup class="fn-ref" id="fnref-messaging-session-sessiongithub"><a href="#fn-messaging-session-sessiongithub">6</a></sup>

L'envoi de messages est basé sur l'utilisation d'un réseau de nœuds entretenus par des volontaires.<sup class="fn-ref" id="fnref-messaging-session-sessionnetwork"><a href="#fn-messaging-session-sessionnetwork">7</a></sup> Ce network est développé comme un onion router, ce qui lui permet de garantir en sortes la sécurité des utilisateurs et leurs données. Un des problèmes majeurs de ce système est qu'un noeud peut décider de stocker les messages jusqu'à ce qu'il arrive à les déchiffrer, même si c'est très improbable. Autrement, l'encryption a l'air très solide, étant basé sur l'idée déjà théorisée des *onion routing*, et permet notamment de supprimer le problème des métadonnées.<sup class="fn-ref" id="fnref-messaging-session-sessiononiontechnical"><a href="#fn-messaging-session-sessiononiontechnical">8</a></sup><sup class="fn-ref"><a href="#fn-messaging-session-sessionnetwork">7</a></sup><sup class="fn-ref" id="fnref-messaging-session-sessionmessage"><a href="#fn-messaging-session-sessionmessage">9</a></sup> Cette application est d'ailleurs, grâce à ce protocole, une des meilleures en terme de métadonnées actuellement, rien ne peut être obtenu sur les échanges.

Pour rassurer les utilisateurs, l'expérience semble montrer que l'on peut faire confiance à Session: entre l'idée des prix des noeuds pour protéger d'une Sybil attack comme celles qui peuvent viser Tor actuellement et le fait que Session ait décidé de déménager les bureaux pour ne plus avoir à subir la pression de la police, c'est franchement une bonne nouvelle.<sup class="fn-ref" id="fnref-messaging-session-sessionmoving"><a href="#fn-messaging-session-sessionmoving">10</a></sup>

La motivation pour faire tourner des nœuds est plus qu'étrange: ils proposent de dédommager les utilisateurs avec des tokens SESH.<sup class="fn-ref"><a href="#fn-messaging-session-sessionnetwork">7</a></sup><sup class="fn-ref" id="fnref-messaging-session-sessionstaking"><a href="#fn-messaging-session-sessionstaking">11</a></sup> Ils distribuent des parts de leur cryptomonnaie en fonction des contributions et des *staking*. C'est un système à double tranchant. L'avantage principal, au-delà de la motivation à faire tourner des nœuds, est de protéger contre les sybil attacks. Le problème majeur en revanche est probablement la valeur de ces tokens, qui ne fait que chuter depuis quelques temps, retirant ainsi probablement la motivation à maintenir un nœud. <sup class="fn-ref" id="fnref-messaging-session-sessionseshvalue"><a href="#fn-messaging-session-sessionseshvalue">12</a></sup> Pour donner une idée à ceux qui auraient un doute sur le fait que le prix des noeuds puissent repousser certains utilisateurs, un noeud coûte, au moment de l'écriture de ce poste, environ 350€. Au lancement du service, faire tourner un noeud coûtait alors 3500€. Certes on peut partager le prix et ne payer que un quart, mais cela fait quand même quasiment 100€.<sup class="fn-ref"><a href="#fn-messaging-session-sessionseshvalue">12</a></sup><sup class="fn-ref"><a href="#fn-messaging-session-sessionnetwork">7</a></sup> Un utilisateur reddit avait affirmé que les noeuds étaient répartis parmis quelques utilisateurs mais je ne retrouve pas la source, d'autant plus que les sources de Session assurent qu'il existe maintenant plus de 1500 noeuds dans 50 pays différents.<sup class="fn-ref"><a href="#fn-messaging-session-sessionnetwork">7</a></sup>

Au-delà du réseau, l'équipe de développement elle-même a l'air d'avoir des problèmes financiers: après ce qui semblait être la fin de la messagerie pour des raisons financières et une levée de fonds désespérée, les 3 développeurs qui restent sur le projet semblent sur le bord de mettre la clé sous la porte. C'est à se demander si le service et le réseau tiendront encore une année.<sup class="fn-ref"><a href="#fn-messaging-session-sessionfinances">3</a></sup>

Pour conclure, le protocole de session a l'air franchement bien, sa sécurité est assurée par plusieurs sources, par le papier de recherche sur lequel ils se basent, l'expérience de Signal (même s'ils ont décide de jeter certaines parties) et le test indépendant. La sécurité en elle-même et le côté privé sont plus qu'assurés. Malheureusement il manque un peu de retour extérieurs, d'analyses ou de recherches third-party. Il serait également utile d'avoir certaines expériences légales comme pour Signal ou Mullvad. Le seul problème qui noircit l'horizon est la survivabilité du réseau dans un avenir proche comme lointain.

p.s. La preuve qu'il faut vérifier tous les articles que l'on lit avec l'article de cyberinsider:
- "But Signal isn’t as strong on privacy as it is on security. It collects some metadata and doesn’t have a corporate sponsor like Facebook sucking up and monetizing that metadata." est aussi bien formulé que si l'on devait faire la promotion de la diarhée, les deux phrases sont contraires mais en fait pas du tout liées, rien ne prouve que Signal a des problèmes de collecte de métadata, absolument rien, on peut au contraire dire *a posteriori* qu'ils sont honnêtes. Pour ce qui est de la vie privée, la seule menace est le serveur centralisant les messages, ne prouvant pour le moment pas que la solution de vie privée qu'ils apportent est pire qu'une autre.
- "- Perfect Forward Secrecy removed" n'est plus d'actualité. Ils avaient apparemment décidé de se passer du PFS à la sortie mais l'ont repris lors de la v2 du protocole.<sup class="fn-ref" id="fnref-messaging-session-sessionredditremovedsecrecy"><a href="#fn-messaging-session-sessionredditremovedsecrecy">13</a></sup>
- "We consider the metadata issue to be the Achilles heel of many [secure messaging services](https://cyberinsider.com/secure-encrypted-messaging-apps/) and [secure email services](https://cyberinsider.com/email/secure/). Even the most popular secure email services, such as [ProtonMail](https://cyberinsider.com/email/reviews/protonmail/), do not have a good solution to the metadata problem." est en grande partie faux. Non seulement David Chaum a théorisé les emails anonymes il y a déjà plus de 40 ans<sup class="fn-ref" id="fnref-messaging-session-davidchaummasterthesis"><a href="#fn-messaging-session-davidchaummasterthesis">14</a></sup>, RVNT promet les messages complètement anonymisés, Signal a implémenté *sealed sender*, Proton a seulement décidé de traquer les utilisateurs sans les prévenir, c'est différent.[^signalsealedsender]





<div class="note-embed-footnotes">

1. <span id="fn-messaging-session-sessionmainpage"></span>[Session main page](https://getsession.org/) <a class="fn-back" href="#fnref-messaging-session-sessionmainpage">↩</a>
2. <span id="fn-messaging-session-sessionlitepaper"></span>[Session litepaper](https://getsession.org/assets/papers/Litepaper_Session_private_messenger.pdf) <a class="fn-back" href="#fnref-messaging-session-sessionlitepaper">↩</a>
3. <span id="fn-messaging-session-sessionfinances"></span>[Session financial problems](https://getsession.org/blog/the-future-of-session) <a class="fn-back" href="#fnref-messaging-session-sessionfinances">↩</a>
4. <span id="fn-messaging-session-sessionaccount"></span>[Session requirement for account creation](https://docs.getsession.org/session-network/session-protocol/account-ids-and-self-managed-keys) <a class="fn-back" href="#fnref-messaging-session-sessionaccount">↩</a>
5. <span id="fn-messaging-session-sessionmessenger"></span>[Session's messenger's main page, technical details and privacy](https://docs.getsession.org/) <a class="fn-back" href="#fnref-messaging-session-sessionmessenger">↩</a>
6. <span id="fn-messaging-session-sessiongithub"></span>[Session android's github page and AGPLv3 license](https://github.com/session-foundation/session-android) <a class="fn-back" href="#fnref-messaging-session-sessiongithub">↩</a>
7. <span id="fn-messaging-session-sessionnetwork"></span>[Session's network](https://docs.getsession.org/session-network) <a class="fn-back" href="#fnref-messaging-session-sessionnetwork">↩</a>
8. <span id="fn-messaging-session-sessiononiontechnical"></span>[Session's onion protocol code (v4)](https://deepwiki.com/session-foundation/session-desktop/2.3-network-layer-and-onion-routing) <a class="fn-back" href="#fnref-messaging-session-sessiononiontechnical">↩</a>
9. <span id="fn-messaging-session-sessionmessage"></span>[Session's message routing in the onion network](https://docs.getsession.org/session-network/session-protocol/onion-requests-and-message-routing) <a class="fn-back" href="#fnref-messaging-session-sessionmessage">↩</a>
10. <span id="fn-messaging-session-sessionmoving"></span>[Session moving headquarters](https://www.webpronews.com/session-leaves-australia-for-switzerland-after-police-pressure/) <a class="fn-back" href="#fnref-messaging-session-sessionmoving">↩</a>
11. <span id="fn-messaging-session-sessionstaking"></span>[session's staking incentive](https://docs.getsession.org/session-network/staking/staking-reward-pool) <a class="fn-back" href="#fnref-messaging-session-sessionstaking">↩</a>
12. <span id="fn-messaging-session-sessionseshvalue"></span>[Value of session's SESH tokens](https://www.coingecko.com/en/coins/session-token?chart=type%3Dprice%26mode%3Dline%26timeframe%3Dmax) <a class="fn-back" href="#fnref-messaging-session-sessionseshvalue">↩</a>
13. <span id="fn-messaging-session-sessionredditremovedsecrecy"></span>[reddit post, Session's removal of PFS](https://www.reddit.com/r/privacy/comments/13vanfj/session_messenger/) <a class="fn-back" href="#fnref-messaging-session-sessionredditremovedsecrecy">↩</a>
14. <span id="fn-messaging-session-davidchaummasterthesis"></span>[David Chaum's master thesis](https://cdn.nakamotoinstitute.org/docs/untraceable-electronic-mail.pdf) <a class="fn-back" href="#fnref-messaging-session-davidchaummasterthesis">↩</a>

</div>

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
RVNT se pose comme un service de messagerie p2p dont le but n'est pas de remplacer signal mais putôt une alternative qui ne vous demanderait jamais de faire confiance à quiconque, à l'image de Tor. C'est une alternative d'autant plus utile dans des pays en guerre ou dans lesquels il est dangereux d'être reconnu.<sup class="fn-ref" id="fnref-messaging-rvnt-rvntofflinemesh"><a href="#fn-messaging-rvnt-rvntofflinemesh">1</a></sup>

Le service paraît phénoménal. Tout d'abord le plus évident, l'encryption. A travers l'utilisation de **double ratchet**, **tor**, **mixnet**, **sealed enveloppes**, **signing**, il semble impossible de lire quoi que ce soit, c'est à se demander comment ça peut même trouver son destinataire.<sup class="fn-ref" id="fnref-messaging-rvnt-rvntratchet"><a href="#fn-messaging-rvnt-rvntratchet">2</a></sup><sup class="fn-ref" id="fnref-messaging-rvnt-rvntprotection"><a href="#fn-messaging-rvnt-rvntprotection">3</a></sup> Le double hatchet protège en plus des attaquants, si un attaquant prend le contrôle d'une clé et arrive à lire un message, il ne pourra pas lire le suivant, ce qui rend toute attaque vraiment difficile si elle ne cible pas l'utilisateur directement. Grâce au **mixnet**, aux tailles de paquets et aux paquets aléatoires, même si quelqu'un analyse le réseau, il lui sera impossible de savoir ce qu'il se passe vraiment. <sup class="fn-ref" id="fnref-messaging-rvnt-rvntmixnet"><a href="#fn-messaging-rvnt-rvntmixnet">4</a></sup> Il en est de même pour la vie privée: rien ne transparaît. De l'expéditeur au contenu du message en comprenant toutes les métadonnées, il semble que les seules infos qui persistent sont les *timestamp* de connexion ainsi que les clés publiques associées aux noms d'utilisateurs. Un point bonus là-dedans est que, selon **RVNT** directement, même si un parti tiers parvenait à prendre le contrôle d'un relais, il ne pourrait absolument rien lire (ce qui est logique puisque tout est basé sur Tor).<sup class="fn-ref"><a href="#fn-messaging-rvnt-rvntprotection">3</a></sup><sup class="fn-ref" id="fnref-messaging-rvnt-rvnttor"><a href="#fn-messaging-rvnt-rvnttor">5</a></sup>

Le réseau en lui-même a l'avantage d'être p2p, il est donc insensible aux lois gouvernementales, locales, etc. Il ne peut subir d'obligation légale, ne peut donner de secrets puisqu'il ne possède rien.<sup class="fn-ref" id="fnref-messaging-rvnt-rvntsealedsender"><a href="#fn-messaging-rvnt-rvntsealedsender">6</a></sup> Comparé à un serveur fédéré ou centralisé, il est presque invincible. Ca a quand même l'inconvénient de ne pas permettre d'envoyer des messages lorsque l'un des deux est hors ligne, ce qui est corrigé par un système assez pratique: un *buffering* des messages. A voir ce que cela donne à l'avenir.<sup class="fn-ref" id="fnref-messaging-rvnt-rvntcomparison"><a href="#fn-messaging-rvnt-rvntcomparison">7</a></sup>

Entre le site web qui a l'air exhaustif sur tout ce qu'ils font et ne font pas, qui s'empresse de se comparer (honnêtement, qui plus est) aux autres services et le *warrant canary*, ils ont l'air de tenir la transparence à coeur, ce qui est d'autant plus louable.[^rvtncanary]<sup class="fn-ref" id="fnref-messaging-rvnt-rvntsignal"><a href="#fn-messaging-rvnt-rvntsignal">8</a></sup> Ils sont parfois peut-être un peu TROP exhaustifs, en plus d'un simple service de messagerie, ils ont l'air de vouloir proposer un service de payement utilisant la même méthode de contact ainsi que des méthodes pour envoyer des fichiers de toute taille! (source à vérifier, j'avais trouvé 50Go mais je ne trouve plus la phrase dans laquelle ils affirmaient ça)<sup class="fn-ref" id="fnref-messaging-rvnt-rvntfiletransfer"><a href="#fn-messaging-rvnt-rvntfiletransfer">9</a></sup><sup class="fn-ref" id="fnref-messaging-rvnt-rvntpayment"><a href="#fn-messaging-rvnt-rvntpayment">10</a></sup>

En regardant les promesses seules ce service a l'air phénoménal, à voir si le développement suit.



<div class="note-embed-footnotes">

1. <span id="fn-messaging-rvnt-rvntofflinemesh"></span>[RVNT Offline mesh](https://rvntos.io/docs/offline-mesh/) <a class="fn-back" href="#fnref-messaging-rvnt-rvntofflinemesh">↩</a>
2. <span id="fn-messaging-rvnt-rvntratchet"></span>[RVNT Double ratchet encryption](https://rvntos.io/docs/double-ratchet/) <a class="fn-back" href="#fnref-messaging-rvnt-rvntratchet">↩</a>
3. <span id="fn-messaging-rvnt-rvntprotection"></span>[RVNT Network protection & zero logging policy](https://rvntos.io/docs/server/ (official documentation)) <a class="fn-back" href="#fnref-messaging-rvnt-rvntprotection">↩</a>
4. <span id="fn-messaging-rvnt-rvntmixnet"></span>[RVNT mixnet](https://rvntos.io/docs/mixnet/) <a class="fn-back" href="#fnref-messaging-rvnt-rvntmixnet">↩</a>
5. <span id="fn-messaging-rvnt-rvnttor"></span>[RVNT Tor integration](https://rvntos.io/docs/tor-integration/) <a class="fn-back" href="#fnref-messaging-rvnt-rvnttor">↩</a>
6. <span id="fn-messaging-rvnt-rvntsealedsender"></span>[RVNT Sealed sender](https://rvntos.io/glossary/sealed-sender/) <a class="fn-back" href="#fnref-messaging-rvnt-rvntsealedsender">↩</a>
7. <span id="fn-messaging-rvnt-rvntcomparison"></span>[RVNT comparison between federated, P2P and centralised](https://rvntos.io/blog/p2p-vs-federated-vs-centralized-messaging/) <a class="fn-back" href="#fnref-messaging-rvnt-rvntcomparison">↩</a>
8. <span id="fn-messaging-rvnt-rvntsignal"></span>[RVNT vs Signal](https://rvntos.io/compare/rvnt-vs-signal/) <a class="fn-back" href="#fnref-messaging-rvnt-rvntsignal">↩</a>
9. <span id="fn-messaging-rvnt-rvntfiletransfer"></span>[RVNT file transfer](https://rvntos.io/docs/file-transfer/) <a class="fn-back" href="#fnref-messaging-rvnt-rvntfiletransfer">↩</a>
10. <span id="fn-messaging-rvnt-rvntpayment"></span>[RVNT payment system](https://rvntos.io/docs/payments/) <a class="fn-back" href="#fnref-messaging-rvnt-rvntpayment">↩</a>

</div>

</div>

<div class="note-embed-foot"><a href="/privacy/messaging/rvnt/">Open the full note →</a>
</div>

</div>

{% endraw %}
