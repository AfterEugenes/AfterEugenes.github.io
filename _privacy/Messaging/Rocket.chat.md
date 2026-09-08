---
title: Rocket.chat
description:
tags:
-
date: 2026-09-08T16:34
category:
  - privacy
---

## Rocket.chat
### TL;DR
Rocket.chat est une application orientée vers la commercialisation et la surveillance de votre communauté, ils font eux-même la pub de leur service comme un hébergement sur cloud d'un service de messagerie à la demande ou le déploiement d'une messagerie "sécurisée" en local. Ils ne sont pas du tout orientés vers la vie privée.

### Footnotes
#### Documentation
[Rocket.chat base: matrix](https://www.rocket.chat/blog/delivering-matrix-federation-as-a-built-in-standard)
[Rocket.chat approach to E2EE](https://docs.rocket.chat/docs/configure-e2e-encryption)
[Rocket.chat authentication methods](https://docs.rocket.chat/docs/authentication)
[Rocket documentation on plans using document360](https://portal.us.document360.io/v1/docs/choose-your-deployment-model)
[Rocket presentation page](https://docs.rocket.chat/docs/rocketchat)
[Rocket plans](https://docs.rocket.chat/docs/our-plans)
[Rocket air gapped configuration](https://docs.rocket.chat/docs/air-gapped-workspace-configuration)
[Rocket surveillance solution](https://docs.rocket.chat/docs/access-workspace-logs)
[Rocket.chat on github](https://github.com/RocketChat/Rocket.Chat?tab=License-1-ov-file)
#### Outside sources, critics
[Rocket review on technical blog](https://www.techradar.com/reviews/rocketchat)
[Rocket fake reviews](https://www.capterra.com/p/161575/Rocket-Chat/reviews/)
[Rocket pushing premium options](https://www.reddit.com/r/selfhosted/comments/ynzakd/why_is_rocketchat_recommended/)
#### Scientific research
[CVE affecting rocket 2FA](https://vulners.com/cve/CVE-2026-30831)
[CVE affecting rocket: NoSQLi](https://www.sentinelone.com/vulnerability-database/cve-2026-30833/)
[List of CVEs affecting Rocket.chat (and not matrix, for the bigger part)](https://app.opencve.io/cve/?vendor=rocketchat)

### Analyse
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
