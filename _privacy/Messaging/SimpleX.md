---
title: SimpleX
description:
tags:
-
date: 2026-09-08T16:34
category:
  - privacy
---

## SimpleX
### TL;DR
SimpleX est une application fédérée en premier lieu. Au-delà du but initial de proposer un réseau de messagerie sécurisé et digne de confiance, ils ont développé, entre autres, les messages directs, le SimpleX network et les addresses anonymes, en faisant une des solutions à la fois les plus sûres et les plus polyvalentes. L'entreprise a en plus l'air d'avoir assuré et bonne base d'utilisateur et continue à se développer, sans promesse de s'éteindre bientôt.

### Footnotes
#### Documentation
[SimpleX chat homepage](https://simplex.chat/)
[Communities](https://simplex.chat/directory/)
[Monetary incentive](https://simplex.chat/crowdfunding/)
[Live messages and other functionnalities](https://simplex.chat/docs/guide/send-messages.html)
[Secret groups](https://simplex.chat/docs/guide/secret-groups.html)
[Incognito mode and chat profiles](https://simplex.chat/docs/guide/chat-profiles.html)
[SimpleX's solution, safe addresses](https://simplex.chat/docs/guide/making-connections.html)
[Flux servers arriving on SimpleX](https://simplex.chat/blog/20241125-servers-operated-by-flux-true-privacy-and-decentralization-for-all-users.html)
[SimpleX network](https://simplex.chat/blog/20240604-simplex-chat-v5.8-private-message-routing-chat-themes.html)
[Privacy policy](https://simplex.chat/privacy/)
[SimpleX github](https://github.com/simplex-chat/simplexmq/blob/stable/protocol/simplex-messaging.md)
[Transparency reports](https://simplex.chat/transparency/)
[Wired's attack on SimpleX](https://simplex.chat/blog/20241016-wired-attack-on-privacy.html)

#### Outside sources, critics
[External SimpleX review](https://itsfoss.com/news/simplex-chat/)
[reddit on SimpleX chat](https://www.reddit.com/r/privacy/comments/z4990l/thoughts_on_simplex_chat/)
[Wired on simpleX (for the laughs)](https://www.wired.com/story/neo-nazis-flee-telegram-encrypted-app-simplex/)
[SimpleX and chat control on reddit](https://www.reddit.com/r/SimpleXChat/comments/1uue5e3/chat_control/)
[Community servers list](https://discuss.privacyguides.net/t/simplex-community-servers-list/21443/6)

#### Scientific research
[Independant audit of SimpleX](https://files.safe.de.fi/safe/files/audit/pdf/SimpleXChat.pdf)

### Analyse
Pour commencer, comme d'habitude, le but de l'application. Ce service de messagerie fédéré est destiné aux utilisateurs professionnels (journalistes, whitleblowers, activistes, victimes de dictatures, anglais, ... Notre lot classique de personnes en milieu sensible.) mais aussi aux utilisateurs particuliers avec un simple but d'améliorer leur vie privée. Eh oui, n'importe qui peut facilement utiliser SimpleX. leur but est d'amener un service de messagerie qui s'adapte à chaque utilisateur. Même si je suis d'habitude assez opposé à utiliser un couteau-suisse, celui-ci est tellement bien pensé qu'il est difficile de l'éviter.[^simplexhomepage]

Déjà pour la partie importante, est-ce sécurisé? Oui. On retrouve le classique E2EE, double ratchet, et même de la post-quantum encryption. Et puis bien sûr le classique audit indépendant a permis de trouver quelques failles mais rien de majeur.[^simplexaudit]

Pour le reste je vais essayer de vous énumérer les fonctionnalités les plus importantes. Commençons par l'identification. Déjà vous ne donnez aucune information à la création d'un compte, vous entrez simplement un nom, un mot de passe et voilà. Le mieux là-dedans c'est que rien n'est stocké en ligne, le mot de passe vous sert à déchiffrer la base de données en local et rien d'autre. Alors il faut faire attention parce que cela signifie, comme pour briar, que vous ne pouvez avoir deux appareils sur le même compte et que si vous perdez votre compte, vous dites adieu à vos conversations.

C'est d'autant plus important que la façon d'ajouter un contact est, je dois le dire, un coup de génie. Chaque utilisateur peut avoir une addresse moyenne durée sur demande mais l'addresse de base, partagée à vos contact, change en fonction du contact.[^simplexaddresses] Cela signifie notamment que personne ne peut relier deux conversations avec deux personnes différentes à un seul utilisateur. Cela signifie aussi que c'est votre base de données locale qui gère ces connexions.

Une autre fonctionnalité importante, j'irais jusqu'à dire la plus séduisante, est le SimpleX network. SimpleX, après quelques changements, a décidé de développer son propre réseau s'apparentant à un onion routeur.[^simplexnetwork] Les différences sont qu'ils n'utilisent que deux noeuds pour router les connexions et que, plutôt que d'utiliser des noeuds aléatoires, ils ont décidé de n'utiliser que des noeuds choisis. L'expéditeur choisit le noeud de relais, premier noeud dans la suite, la destination choisit le noeud de destination, le second dans ce réseau. De cette façon aucun noeud ne peut avoir toutes les informations sur le réseau, il est impossible pour un organisme comme la NSA d'avoir un dixième des noeuds déployés sur le réseau. Alors ça a bien sûr ses inconvénients, notamment sur la difficulté pour une personne lambda d'avoir un serveur de confiance, mais ça a quand même le mérite de particulièrement bien fonctionner pour cacher les connexions, surtout que le protocole encrypte la destination (oui, la destination, non pas l'expéditeur) et la cache au noeud de relais, ce qui l'empêche de connaître tout le chemin et ne lui permet de connaître que l'expéditeur et le prochain noeud.[^simplexnetwork] Cette simple fonctionnalité de cacher la destination, combinée avec les serveurs et développeurs de confiance, font que je pense sincèrement que SimpleX peut tout à fait rivaliser avec Signal en terme de messagerie centralisée de confiance, alors qu'elle le fait largement en tant que messagerie fédérée.

La messagerie étant fédérée (j'aurais dû en parler dès le début mais vous voyez tout ce qu'il y a à dire) vous pouvez bien sûr faire tourner votre propre serveur localement sans grande difficulté. Si vous n'avez pas spécialement envie de le faire vous-même, certaines communautés et personnes proposent d'utiliser leurs serveurs et vous proposent des listes de tels serveurs, ce qui permet de multiplier les serveurs utilisés et est d'autant plus important de par la construction de SimpleX network.[^simplexcommunityservers]

Bien sûr cela peut poser problème pour les conversations où les deux utilisateurs se connectent aux serveurs d'une même entité, d'autant plus quand simplex est la connexion par défaut, mais encore une fois ils y ont pensé. Déjà ils ont ajouté la possibilité de se connecter aux serveurs de flux, un autre provider qui propose de se connecter par défaut à ses serveurs. Si l'option est activée, l'application se connecte d'ailleurs à l'un pour envoyer et l'autre pour recevoir, assurant qu'aucun n'aura d'infos sur le chemin complet.[^simplexflux] En plus SimpleX a (partiellement) prouvé être digne de confiance entre l'importance qu'ils accordent aux métadonnées et la façon dont ils ont répondu aux exigences de la loi et puis surtout la license AGPLv3.[^simplexprivacy][^simplextransparency][^simplexgithub]

En plus de tout ça on retrouve quelques fonctionnalités de sécurité telles que la connexion par tor, la messagerie incognito et les groupes secrets.[^simplexincognito][^simplexsecretgroups] Ces fonctionnalités combinées au développement de SimpleX font qu'aucune info ne peut vraiment transiter: SimpleX n'a jamais demandé votre identité, les quelques métadonnées qu'ils peuvent connecter sont en fait juste quel profil de conversation est associé à quel ip (puisqu'ils ne peuvent pas lier vos différentes addresses de vos différentes conversations ***a priori*** ils ne peuvent donc dire à qui vous parlez ou quand) lorsque ***et uniquement lorsque*** vous et votre interlocuteur utilisez tous deux leurs serveurs, auquel cas vous pouvez simplement décider d'utiliser Tor avant la connexion au noeud pour cacher votre IP, la seule info qu'ils avaient sur vous disparaît dans le vent.

Pour ce qui est de l'utilisation et des retours utilisateurs, ils sont étonnamment positifs. SimpleX a développé un paquet de fonctionnalités plutôt intéressantes. Certaines comme les communautés sont faites pour l'aisance d'utilisation alors que d'autre comme les live messages sont faites pour les utilisateurs sensibles, ce qui prouve d'autant plus l'importance qu'ils accordent à la sécurité de leur application et la possibilité de l'utiliser en contexte difficile.[^simplexfunctionnalities] En plus de ça les quelques reviews qui existent ont l'air de faire les louanges de SimpleX et de sa facilité d'utilisation, ce qui est d'autant plus rare que certaines de ces louanges viennent de reddit.[^simplexreview][^simplexreddit]

La messagerie elle-même est très bien développée. Entre la base d'utilisateurs massive et leurs idées pour développer l'application, c'est largement prometteur. Ils ont en effet prévu de financer la continuation du développement de l'application et la maintenance des serveurs en proposant aux serveurs des fonctionnalités payantes (nom de domaine personnalisé, serveurs, etc). Tout cela donne plus d'espoir sur le développement de SimpleX que sur celui de Session ou Briar. C'est d'autant plus intéressant que ces fonctionnalités sont utiles pour les communautés et qu'ils ne poussent pas leur modèle économique sur les utilisateurs comme rocket.chat. Ils annoncent même financer l'application entière en se basant entièrement sur les financements apportés par les serveurs.[^simplexfinancial] Certaines sources s'amusent à critiquer ouvertement SimpleX et les associer à des communautés néo-nazies dans le but de promouvoir le chat control, ce qui prouve d'autant plus l'importance qu'a pu gagner SimpleX à travers les années. En plus de ça, de par sa construction, SimpleX, ou plutôt les serveurs privés permettant de se connecter à SimpleX, sont immunisés normalement à chatcontrol et aux autres lois horribles auxquelles nos gouvernements peuvent penser à l'avenir, malgré ce qu'en disent les utilisateurs reddit.[^simplexchatcontrol][^simplexwired][^simplexwiredoriginal] Le seul nuage à l'horizon est le fait que SimpleX ait eu plusieurs requêtes du gouvernement et ne nous ai pas montré leurs réponses finales excepté celles qui disaient qu'ils aideraient le gouvernement british. A voir ce que cela donne en réelle situation catastrophique comme pour Mullvad VPN ou session.

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
