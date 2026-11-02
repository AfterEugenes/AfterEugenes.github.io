---
layout: privacy-doc
title: Session
description: ''
excerpt: ''
date: 2026-09-08T16:34
platform: privacy
permalink: /privacy/messaging/session/
category: Messaging
tags:
- Privacy
- Messaging
---

{% raw %}

# Session
## TL;DR
Cette application est une messagerie qui passe par le réseau tor. La cryptographie est excellente et prouvée. L'application elle-même est facile et agréable à utiliser. Le réseau onion est une idée novatrice qui permet de sécuriser les messages mais le prix pour lancer un tel noeud transforme l'applciation en messagerie centralisée.

## Analyse
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
{% endraw %}
