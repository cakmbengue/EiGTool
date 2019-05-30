EiG Tool
========
Outil de recherche d'adresses emails sur Internet.

Information
===========
```
Email information Gathering (EiG)

@author: Cheikh A. Khadre MBENGUE

@location: Dakar (Senegal)

@EiGTool: open source, gratuit.
```

Description
===========
EiG Tool permet de trouver les emails d'un nom de domaine grâce aux moteurs de recherche. Son but est de vérifier la visibilité de vos adresse emails professionnels sur Internet qui peuvent être ciblées par un cyberattaquant.

Avertissement
=============
L'utilisation d'EiG Tool pour attaquer des cibles sans consentement mutuel préalable est illégale. Le développeur n'est pas responsable de tout dommage causé par EiG-tool.

Prérequis
=========

* Python <= 2.7

Installation
============

```
git clone https://github.com/cakmbengue/EiGTool.git EiG
cd EiG
python eig.py
```

Usage
=====

```
python eig.py --domain [DOMAIN] --source [SOURCE] --verbose [LEVEL]

```
ou 

```
python eig.py --info [EMAIL] --verbose [LEVEL]
```

![example_1](https://github.com/cakmbengue/EiGTool/blob/master/screen/screen1.png)

![example_2](https://github.com/cakmbengue/EiGTool/blob/master/screen/screen2.png)

Exemples
========

```
python eig.py --domain site.sn --source google --breach -v 2 --report ../site.sn.txt
```
ou

```
python eig.py --domain site.sn --source all --breach -v 3 --report ../site.sn.txt
```
![example_3](https://github.com/cakmbengue/EiGTool/blob/master/screen/screen3.png)
