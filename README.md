City and temperature and humidity registration project

This project contains temperature and humidity information of a city written
 in Batflask and displayed to the user as json. This program reads the 
data from the json file and stores it in the database.
And in two types of container and orchestration infrastructure.

##Run app with python 


#2 
run with python appplication

`python app.py`

curl http://127.0.0.1:5000/tehran


#3  docker

for run docker and build new image

`docker build -t my-app:0.1.0 .`

`docker run -d --name my-container -p 5000:5000 my-app:0.1.0`

`docker tag my-app:0.1.0 my.registry/my-app:0.1.0`

`docker push my.registry/my-app:0.1.0`


# test with docker 

`docker ps`

curl http://ip-node:5000/tehran


============================================
# k8s

 **helm**

`helm create helm`

change files value.yaml and /template/deployment.yaml   and template/pv.yaml and pvc.yaml 
cp /template/deployment.yaml and template/pv.yaml pvc.yaml  .

`rm -rf template`

`ls -la`

value.yaml deployment.yaml pv.yaml pvc.yaml Chart.yaml

`helm package . `

`helm install helm ./helm-package.tgz:0.1.0 -f value.yaml`

`kubectl get pods -n default`

=======================================

**manifest**

in path /afra-ch/manifest/full-dep.yaml

`kubectl apply -f full-dep.yaml`

