_La version française est ci-dessous._

# Reeborg's World distribution

[Reeborg's World](http://reeborg.ca/reeborg.html) is a free "Karel the robot" type of
environment used to teach programming, using either Python or Javascript.
Some users may find that it might be difficult to use due to limited Internet bandwidth,
or because of some firewall restriction, etc.
This repository contains the file `reeborg.zip` meant for local deployment which
should help solve such problems. The main repository is https://github.com/aroberge/reeborg.

Note that this distribution does not include the documentation, which is maintained in a completely different repository.

## How to use it on a standard web server

To use it on a running web server, simply extract the content of reeborg.zip
at the desired location.

If the web server does not allow external files to be used, then
use `reeborg_offline.html` instead of `reeborg.html` as your main html file.
For example, http://reeborg.ca/reeborg_offline.html instead of
http://reeborg.ca/reeborg.html

### Note for web administrators

If you run a server that is set up to interpret Python scripts, you may need
to disable this functionality. On the commercial server where the public site is running,
my `.htaccess` file contains the following:

`
RemoveHandler .py
`

## How to use it on a single-user computer

You can not simply open `reeborg.html` as a file on your computer; you must
have a local web server running.  My favourite way to do this is to use Python
(version 3.x, installed on my computer) from a terminal window,
navigate to the root directory of the reeborg distribution, for example `C:\Users\Andre\GitHub\reeborg>`,
and run

`python -m http.server`

The following message is displayed in the terminal:
`Serving HTTP on 0.0.0.0 port 8000 ...`

I then use `http://localhost:8000/reeborg.html` as the URL in my browser (Chrome).

## Final note

The content of this repository is not created automatically. If you find that it contains
a version older than that found on http://reeborg.ca/ and you wish to use the newer version,
please contact me.

# Votre copie du Monde de Reeborg

[Le Monde de Reeborg](http://reeborg.ca/reeborg.html) est un site d'accès gratuit conçu
pour l'enseignement de la programmation (en utilisant soit Python ou Javascript) suivant
le paradigme du "robot Karel".
Certains utilisateurs pourraient avoir des difficultés à utiliser ce site, soit en
raison de limitation au niveau de la bande passante, ou à la présence de pare-feu bloquant
des sites externes, etc.
Ce répertoire contient le fichier `reeborg.zip` qui inclut tout ce qui est requis pour
avoir une version du Monde de Reeborg sur votre propre site, excluant la documentation.


## Utilisation sur un serveur web standard 

Pour utiliser le contenu sur un serveur web actif, vous n'avez qu'à extraire
le contenu du fichier à l'endroit désiré.

Si le serveur web ne permet pas l'accès aux fichiers externes, alors
utilisez `reeborg_offline.html` au lieu de `reeborg.html` comme nom de fichier principal.
Par exemple, http://reeborg.ca/reeborg_offline.html au lieu de
http://reeborg.ca/reeborg.html.

### Note pour les administrateurs web

Si votre serveur a été configuré pour interpréter les scripts Python, vous allez
devoir changer la configuration pour empêcher ceci. Par exemple, sur le
serveur commercial où le site reeborg.ca se trouve, mon fichier 
`.htaccess` inclut ceci:

`</FilesMatch>
RemoveHandler .py
`

## Utilisation sur un ordinateur personnel

Vous ne pouvez pas simplement ouvrir le ficher `reeborg.html` dans votre
navigateur: vous devez avoir un serveur web local activé. 
Ma façon préférée pour faire ceci est d'utiliser Python (version 3.x, installée sur
mon ordinateur) dans une invite de commande, naviguer jusqu'au répertoire contenant
les fichiers pour le monde de Reeborg, comme par exemple:
`C:\Utilisateurs\Andre\GitHub\reeborg>`,
et d'exécuter

`python -m http.server`

Le message suivant apparaît alors dans l'invite de commande:
`Serving HTTP on 0.0.0.0 port 8000 ...`

Ensuite, j'utilise `http://localhost:8000/reeborg.html` commme adresse (URL) dans mon navigateur (Chrome).

## Finalement ...

Le contenu de ce répertoire n'est pas créé automatiquement. Si vous trouvez qu'il contient
une ancienne version du site et que vous voudriez avoir une copie de la version la
plus récente qu'on trouve sur le site http://reeborg.ca/, SVP n'hésitez pas à me contacter.

