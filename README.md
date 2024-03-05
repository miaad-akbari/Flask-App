City and temperature and humidity registration project

This project contains temperature and humidity information of a city written
 in Batflask and displayed to the user as json. This program reads the 
data from the json file and stores it in the database.
And in two types of container and orchestration infrastructure.

## Run App With Python 
1. git clone  git@github.com:miaad-akbari/Flask-App.git

2. pip install -r requirements.txt

3. python3 app.py

4. curl http://localhost:5000/tehran


## Run App With Docker

1. git clone  git@github.com:miaad-akbari/Flask-App.git

2. docker build -t my-app:0.1.0 .

3. docker tag my-app:0.1.0 registry/my-app:0.1.0

4. docker push registry/my-app:0.1.0

5. docker run -d --namee app-flask -p 5000:5000  registry/my-app:0.1.0

6. docker ps

7. docker logs -f app-flask

8. curl http://localhost:5000/tehran

## Run App K8S (helm)

1. git clone  git@github.com:miaad-akbari/Flask-App.git

2. helm create helm

3. change file value.yaml and deployment.yaml and service.yaml

4. cp template/deployment.yaml ../  && cp template/service.yaml

5. helm package .

6. helm install helm ./helm-package.tgz:0.1.0 -f value.yaml

7. kubectl get all


## Run App With K8S (manifest)

1. git clone  git@github.com:miaad-akbari/Flask-App.git

2. cd manifest/

3. kubectl create ns app

4. kubectl apply -f full-dep.yaml -n app

5. kubectl get pv,pvc -n app

6. kubectl get po -n app

