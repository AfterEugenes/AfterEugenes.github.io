---
title: Briar
description:
tags:
-
date: 2026-09-08T16:33
category:
  - privacy
  - writeups
---

## Briar
### TL;DR
Briar est destinée aux personnes dans des situations délicates qui ont besoin de pouvoir communiquer malgré tout (journalistes, utilisateurs en pays sous dictatures, etc) Il fait très bien le travail dans ce cas mais à un certain coût. La cryptographie en elle-même est robuste et les métadonnées sont bien protégées puisque les communications en ligne passent par Tor.

### Footnotes
#### Documentation
[Homepage](https://briarproject.org/how-it-works/)
[User manual](https://briarproject.org/manual/)
[Post about briar's release and audit](https://briarproject.org/news/2017-beta-released-security-audit/)
[Bramble transport protocol v4](https://code.briarproject.org/briar/briar-spec/-/blob/master/protocols/BTP.md)
[Briar wiki](https://code.briarproject.org/briar/briar/-/wikis/connect-with-nearby-contact)
[Mailbox app](https://briarproject.org/download-briar-mailbox/)
[Development state & maintenance mode](https://briarproject.org/news/2026-maintenance-mode/)
[Briar on github](https://github.com/briar/briar?tab=License-1-ov-file)

#### Outside sources, critics
[Review by tech-oblivious people](https://www.pcmag.com/reviews/briar)
[User comparison with Signal](https://www.reddit.com/r/privacytoolsIO/comments/kpq3ri/comment/gisj73a/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
[Cure 53 security audit](https://briarproject.org/raw/BRP-01-report.pdf)
[RVNT on briar](https://rvntos.io/answers/is-briar-end-to-end-encrypted/)

#### Scientific research
[Cryptography in the wild: Briar - Yuanming Song](https://ethz.ch/content/dam/ethz/special-interest/infk/inst-infsec/appliedcrypto/education/theses/report_YuanmingSong.pdf)

### Analyse
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
