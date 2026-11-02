---
layout: privacy-hub
title: Cryptocurrencies
description: ''
excerpt: ''
date: 2026-09-08T16:34
platform: privacy
permalink: /privacy/cryptocurrencies/
category: Cryptocurrencies
tags:
- Privacy
- Cryptocurrencies
---

{% raw %}

### Monero
- [x] Monero
	- [x] Logging *per documentation*
	- [x] Privacy *per documentation*
	- [x] Deanonymization, traceability
- [ ] Further readings
	- [?] Feather Wallet
	- [>] Haveno
	- [>] Retoswap

[Factually review](https://factually.co/fact-checks/technology/monero-privacy-coins-darknet-traceability-countermeasures-bba4a1)
[Crypto currency explanations](https://www.kraken.com/learn/how-do-cryptocurrency-transactions-work)
[Monero's ringct, stealth address and ring signature](https://www.getmonero.org/resources/moneropedia/ringCT.html)
[Research on monero's anonymous features](https://eprint.iacr.org/2015/1098.pdf (RingCT)https://www.getmonero.org/resources/moneropedia/stealthaddress.html)
[Details on ring signatures](https://www.getmonero.org/resources/moneropedia/ringsignatures.html)
[Traceability heuristics of Monero, breaking ring signatures](https://arxiv.org/pdf/2408.05332)
[Deanonymization of monero nodes over tor](https://arxiv.org/pdf/2607.07062)
[Review of assumptions in deanonymization attacks papers](attackshttps://petsymposium.org/popets/2022/popets-2022-0091.pdf)
[In-depth explanation](https://eprint.iacr.org/2017/338.pdf)
[Janus attack on subaddresses](https://web.getmonero.org/2019/10/18/subaddress-janus.html)
[Monero technical explanations](https://docs.getmonero.org/development/)
[Monero book](https://monero-book.cuprate.org/)
[Monero audit](https://www.getmonero.org/resources/research-lab/audits/clsag.pdf)

Monero est une blockchain à part entière qui se base sur CryptoNote. Monero a pour but de régler les soucis d'anonymat principaux de Bitcoin. Pour cela Monero propose trois solutions:
- Stealth addresses: Pour chaque transaction, une adresse est générée aléatoirement et envoyée à l'expéditeur, il est pratiquement impossible de les remonter jusqu'à l'expéditeur.
- Ring signatures: Chaque transaction est signée en utilisant les clés d'autres utilisateurs (réels ou non) qui possèdent le montant nécessaire pour finaliser la transaction, ces utilisateurs sont appelés decoys.
- Ring CT: Plusieurs transactions sont liées entre elles pour former celle qui sera inscrite dans la blockchain, cachant ainsi le montant envoyé par chaque expéditeur et à chaque destinataire.
En plus de toutes ces fonctionnalités, la plus importante est la politique de *Privacy by default*. Contrairement aux autres cryptomonnaies, Monero met en place ces fonctionnalités par défaut, pas moyen donc d'isoler les personnes utilisant les fonctionnalités d'anonymat, tout le monde est dans le même panier.

La plupart des attaques, par construction, visent à identifier le réel expéditeur. Certaines visent tout de même à identifier le destinataire mais sont plus rares, il en existe bien une connue (Janus attack) et documentée, mais elle n'est pas toute puissante. Pour les autres attaques, ils procèdent souvent avec une cible en tête: le *true spender* ou les *decoys*. Comme le *ring* est composé d'un nombre limité de *decoys*, les identifier permet de réduire les possibilités et augmenter la chance d'identifier le *true spender*.

Dans ces attaques-ci, il en existe un nombre significatif. Depuis ses débuts en 2014, la cryptomonnaie a connu beaucoup de vulnérabilités. Toutes ont cependant été adressées avec le temps. Aujourd'hui aucune faille majeure ne permet d'identifier les utilisateurs avec autant de certitude que lors des *zero-mixins attacks* ou du *off-by-one bug*. La seule faille majeure qui reste permet d'identifier l'IP réelle d'un node utilisant tor, à condition d'avoir des moyens conséquents (demande la possibilité de se faire choisir comme guard node).

Dans les attaques passées, la plupart se basaient sur des erreurs de sélection des *decoys*. Sinon, comme toute partie de la vie privée, des bonnes pratiques sont requises pour ne pas donner son identité avant même qu'ils n'essayent de l'avoir (VPN, pgp, ...).

En sommes, la cryptomonnaie reste très sécurisée pour le moment, promet de s'améliorer encore à l'avenir, à voir ce qu'elle donnera.

### Feather wallet
- [?] Feather wallet
	- [?] Logging *per documentation*
	- [?] Privacy *per documentation*
	- [?] Deanonymization, traceability
- [ ] Further readings

Le Logging est vraiment trop peu clair. Le seul logging que l'on trouve est issu de la documentation de whonix:
- cannot spend your XMR (you hold the keys);
- does not know your IP address (we are connecting to it over Tor);
- does not know your XMR address; and
- does not know your balance or private view key.
Mais rien nous dit ce que ça stocke vraiment ou ce qui est log. Dans le principe le *wallet* est censé garder comme infos l'*adresse*, les *sub-addresses*, les *clés*, et autres détails. De plus si le *wallet* est *non-custodial*, il n'a pas besoin de se connecter à un serveur, stocke les informations essentielles localement et seul l'utilisateur y a accès.

Comme Feather Wallet est *non-custodial*, nous sommes normalement les seuls à avoir accès à tout ça. Pour ce qui est des informations personnelles, il n'a normalement pas besoin d'accéder à des infos, ne fait que gérer le *wallet*. Au plus il pourrait accéder à l'IP mais il se trouve qu'il est aussi possible de configurer l'application pour accéder au wallet via Tor.

Pour ce qui est des attaques il ne semble pas y avoir eu de quelconque attaque importante visant Feather wallet, prouvant peut-être qu'il n'y a vraiment aucune possibilité de récupérer des infos.

Tout ce qui reste est donc basé sur la confiance qu'on accorde à Feather wallet. Le souci est qu'il n'y a jamais eu d'audit indépendant apparemment, aucun article sur ce qu'il y a pu y avoir comme information tirée d'une évaluation.
L'avantage est que le code est open source et que l'on a aucune nouvelle sur une quelconque attaque déjà faite ou une partie du code douteuse trouvée, ce qui nous permet tout de même de pencher vers l'idée que ce *wallet* est sécurisé et ne pose aucun risque.

Le plus gros risque après la blockchain n'est pas le wallet mais bien le *node* auquel un utilisateur se connecte. **Feather** maintient une liste de *nodes* fiables (considérés comme tel tout du moins) auxquels il est possible de se connecter. Bien que cette liste vienne d'un organisme de confiance, elle n'est pas totalement imperméable aux risques. L'idéal dans ce cas est de se connecter à un *node* en local en utilisant <a class="obsidian-link" href="#monerod">Monerod</a>. Sinon les *nodes* auront accès à des infos telles que
- *Refresh height and access paterns*: Les infos qui sont normalement utilisées pour synchroniser deux clients/*nodes* peuvent être utilisées pour traquer l'instant de création du *wallet*.
- *Output requests*: Le client demande une liste de *ring members* qui serviront de *decoys*. Combiné avec l'IP, il est possible de l'utiliser pour retracer la transaction.
- *Transaction submission*: Le *remote node* étant le premier que l'on contact, **Dandelion++** ne s'appliquera que pour les *nodes* suivants, ne protégeant pas l'utilisateur ici.

### Haveno
- [>] Haveno
	- [>] Logging *per documentation*
	- [>] Privacy *per documentation*
	- [>] Deanonymization, traceability
	- [ ] Avoiding scams *per documentation*
- [ ] Further readings
	- [x] What are Haveno networks *per documentation*

[Retoswap suffered an attack through haveno's protocol, trading is stopped](https://xmrlist.com/blog/is-retoswap-safe-haveno-p2p-status)
[Details on the protocol flaw](https://torwire.com/news/cybersecurity/hackers-steal-27-million-haveno-protocol-flaw/)
[Haveno actions on the failure](https://www.coingabbar.com/en/crypto-currency-news/retoswap-suspends-trading-haveno-protocol-exploit-again)
[Haveno documentation on trades (non custodial, peer to peer, safety)](https://docs.haveno.exchange/overview/trade-protocol/#overview-of-a-trade)
[Monero DEXs & Haveno: risks, security, privacy (research)](https://www.researchgate.net/publication/391461654_Moneros_Decentralized_P2P_Exchanges_Functionality_Adoption_and_Privacy_Risks/fulltext/6819800ebd3f1930dd6ca5eb/Moneros-Decentralized-P2P-Exchanges-Functionality-Adoption-and-Privacy-Risks.pdf?origin=publication_detail)

Bien que la documentation semble une fois de plus limitée, on peut tirer quelques informations importantes des données disponibles en ligne. Déjà l'application en elle-même est open-source, avec la license **AGPL-3.0**, c'est une bonne nouvelle.

Pour ce qui est des failles, c'est un peu difficile. Certaines failles sont apparues récemment (*haveno* n'ayant que 2 ans, c'est la moitié de sa durée de vie), bien qu'ayant pris place sur les *DEXs*, elles viennent tout de même de *Haveno*. Heureusement *Haveno* a tout de suite gelé toutes les transactions et *woodser* a par la suite fait une communication pour annoncer un patch et conseiller les utilisateurs. La faille est arrivée de nouveau par la suite, les mêmes actions ont été prises. Dans les deux cas la faille visait les grosses transactions qui ne concernaient pas de fiat suite à une erreur dans le protocole.

Parmis les failles on en trouve aussi des plus anciennes, notamment une faille dans la première année de service de *haveno* qui visait les grosses transactions ainsi qu'une autre, vers le début du fonctionnement de l'application, qui permettait d'identifier les transactions qui échangeaient du bitcoin pour du *XMR*.

Un autre point inquiétant est les autorités. Les échanges dans *haveno* sont assuré par des *2-out-of-3 multisig*, ce qui signifie qu'il y a 3 personnes qui interviennent: l'acheteur (*taker*), le vendeur (*maker*) ainsi que l'arbitre (*arbitrator*), qui vérifie qu'un échange se déroule comme il faut. Chacun a une clé privée qui intervient dans l'échange. Les fonds peuvent être débloqués par 2 clés quelconques parmi les 3 données. Le problème est que rien ne prouve que l'arbitre est digne de confiance. Bien qu'il ne puisse pas récupérer les fonds pour lui, il a accès à plus de métadonnées que la blockchain, il contrôle qui récupère l'argent, il a du pouvoir et c'est une faille potentielle.

En sommes *haveno* ne semble pas malhonnête, il ne semble pas non plus qu'ils aient de mauvaises intentions. Les failles majeures sont issues d'erreurs de programmation, de protocoles, pas d'une volonté des développeurs. Cela prouve en revanche que *haveno* est en effet faillible, c'est bien ce qui est le plus inquiétant ici. Certes, qui peut se vanter d'avoir créé quelque chose qui fonctionne dès sa sortie, il n'empêche que *haveno* manque un peu de maturité.

### RetoSwap
- [>] RetoSwap
	- [?] Logging *per documentation*
	- [?] Privacy *per documentation*
	- [>] Deanonymization
	- [ ] Avoiding scams *per documentation*
- [ ] Further readings

[Independant review of retoswap](https://haveno.nokycme.com/)
[Retoswap attack, may 26](https://xmrlist.com/blog/is-retoswap-safe-haveno-p2p-status)

[Retoswap est un honeypot? (non) (un des pires articles jamais fait)](https://openmonero.com/knowledge/haveno-retoswap-smells-like-a-honeypot)


RetoSwap bénéficie aussi d'une license AGPLv3.0 qui permet déjà d'inférer une certaine transparence de la part des développeurs.

Encore une fois nul ne peut se sentir noyé sous les preuves. Tout ce que l'on arrive à trouver sont des articles concernant l'attaque récente visant *retoswap* MAIS s'appuyant sur un protocole faillible de *haveno*, un papier de recherche qui explique que *haveno* (non pas *retoswap*) est faillible SI la monnaie d'échange utilisée est le bitcoin et de faux articles traitant retoswap de *honeypot*, rien qui tienne vraiment suite à une examination approfondie.

Encore une fois le meilleur moyen ici est de faire confiance aux créateurs, ce qui n'est jamais une bonne chose dans le contexte de la vie privée...


### Cryptocurrencies

#### Currencies
- [ ] Bitcoin
	- [ ] Deanonymization attacks/traceability
- [ ] Ethereum
	- [ ] Deanonymization attacks/traceability
- [ ] Zcash
- [ ] Dash
- [ ] MimbleWimble
- [ ] Confidential Transactions

[Failures of bitcoin](https://dl.acm.org/doi/pdf/10.1145/2660267.2660379)
[Latest attack on Ethereum](https://www.usenix.org/system/files/usenixsecurity25-heimbach.pdf)


#### Monero nodes
- [ ] Monerod

##### Monerod
- [ ] Monerod
	- [ ] connecting to the network using tor
	- [ ] infos kept
	- [ ] what is seen by isp?
	- [ ] connecting over tor to local monerod
- [ ] Further readings

[Running monerod over tor](https://docs.getmonero.org/interacting/monerod-reference/#server)
[How to run monerod](https://www.monero.how/how-to-run-monero-node)

#### Monero wallets
- [ ] Monero GUI
- [ ] Cake wallet

##### Monero GUI
- [ ] Monero GUI
	- [ ] Logging
	- [ ] Deanonymization
- [ ] Further readings

#### Cake wallet
- [ ] Cake wallet
	- [ ] Logging
	- [ ] Deanonymization, traceability
- [ ] Further readings

### Monero funds

#### Monero gift cards
- [ ] Monero gift cards
{% endraw %}
