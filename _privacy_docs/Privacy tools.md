---
layout: privacy-hub
title: Privacy tools
description: ''
excerpt: ''
date: 2026-09-08T16:33
platform: privacy
permalink: /privacy/privacy-tools/
category: Privacy tools
tags:
- Privacy
- Privacy tools
---

{% raw %}

# Préambule

Avec le développement d'internet et sa conception actuelle, les achats et ventes de services ne sont plus suffisant pour faire tourner ces machines à sous, ces monstres à données. Géants du web, *data brokers*, agences gouvernementales, pour chacun d'entre eux vos données sont devenues le centre des opérations. Que ce soit pour vous faire acheter un produit, influencer les décisions de vote ou encore vous traquer, rien n'est sacré.

Bien que je pourrais rentrer dans les détails et continuer, cela me semble inutile quand Mullvad VPN a écrit un si bon article sur tout ce que ces entreprises sont prêtes à faire pour récupérer vos infos et pourquoi votre vie privée est importante.
[Total surveillance - Mullvad VPN](https://mullvad.net/pdfs/Total_surveillance.pdf)

La vie privée est, plus qu'une histoire qu'un informaticien raconte à ses enfants afin qu'ils se tiennent sages en attendant noël, un droit. Pour certaines personnes comme les activistes, les *whistle blowers* et les personnes recherchées (Ne vendez pas de drogue, s'ilv ous plaît, c'est dangereux la drogue), la vie privée est encore plus, elle représente une sécurité, une assurance 

Puisque je suis le seul et tout puissant auteur je me permet de vous lier quelques sites ou projets qui sont très intéressants et ont à coeur de protéger vos droits.

[Free your android - Free software foundation Europe](https://fsfe.org/activities/android/android.en.html)
[Quadrature du net](quadrature du net)

# Validated services

Dans cette catégorie vous trouverez tous les services qui ont, aujourd'hui, passé tous mes critères de sélection et que j'utilise au quotidien. Ceci constitue une recommendation pratique sur les services à utiliser mais explorer les différentes catégories une à une vous permettra de trouver d'autres recommendations ou, mieux encore, de peser vous-même le pour et le contre.

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

{% endraw %}
