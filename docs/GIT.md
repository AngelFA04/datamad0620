# Repaso git

* Crear un repositorio git: `git init`
* Ver estado de un repositorio: `git status`
* Añadir ficheros al repo: `git add <fichero>`
* Comitear los cambios: `git commit -am "<mensaje>"`
* Ver los repositiorios remotos vinculados: `git remote -v`
* Añadir un remoto: `git remote add <remote_name> <git_url>`
* Clonar un repositorio: `git clone <repo_url>`

## Push

* Pushear codigo a remoto en la rama master: `git push origin master`
* Pushear una rama a remoto `git push <remote_name> <branch_name>`

## Ramas

* Crear nueva rama: `git checkout -b <nombre_rama>`
* Cambiar de rama: `git checkout <nombre_rama>`
* Ver en que rama estoy: `git status`
* Merge (trae contenido desde la rama `<branch_name>` a la rama actual): `git merge <branch_name>`

## Otros

* Ver todos los commits: `git log` (para salir, pulsar `q`) o en github "Insights -> Network"


## REGLA DE ORO

* Nothing to commit, working tree clean al hacer `git status`
* git push
* Cuando me levanto de la silla, hago un `commit` & `push`

