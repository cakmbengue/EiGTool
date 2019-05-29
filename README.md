EiG-Tool
========
Recherche d'adresses emails sur Internet

Information
===========
```
Email information Gathering (EiG)

@author: Cheikh A. Khadre MBENGUE

@location: Dakar (Senegal)

@EiG-tool: open source, gratuit.
```

Description
===========
EiG-tool permet de trouver les emails d'un nom de domaine grâce aux moteurs de recherche. Son but est de vérifier la visibilité de vos adresse emails professionnels sur Internet qui peuvent être ciblées par un cyberattaquant.

Avertissement
=============
L'utilisation d'EiG-tool pour attaquer des cibles sans consentement mutuel préalable est illégale. Le développeur n'est pas responsable de tout dommage causé par EiG-tool.

Prérequis
=========

* Python <= 2.7

Installation
============

```
git clone https://github.com/cakmbengue/eig-tool.git EiG
cd EiG
pip install -r prerequis.txt
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

![example_1](https://github.com/cakmbengue/eig-tool/blob/master/screen/screen1.png)

![example_2](https://github.com/cakmbengue/eig-tool/blob/master/screen/screen2.png)

Exemples
========

```
python eig.py --domain domaine.sn --source google --verbose 3
```
ou

```
python eig.py --domain domaine.sn --source all --verbose 3
```
![example_3](https://github.com/cakmbengue/EiG-tool/blob/master/screen/screen3.png)
