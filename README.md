# ML_Project_01
## This is my first machine learning project.

### Project requirements:

1. [Github account](https://github.com/)
2. [Heroku account](https://id.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [Git CLI](https://git-scm.com/downloads)
5. [Git Documentation](https://git-scm.com/docs/gittutorial)

3 Steps why we need Github Repo:
1. Multiple developer can use same repo in different location i.e Content updation [git pull and git push]
2. Version control system [Maintaning history]
3. Branching.[main branch, integration(replica) branch, release1, release2..]
    also resolve the code conflicts on same line of code.

Docker: [Portability of own code]
Containers -- Image concept -- Isolation

Continous Integration: Local --> Github
Continous Deployment: Github with Trigger --> Docker image --> Cloud service(Publish app)

Creating conda Environment:
conda create -p venv python==3.7 -y
conda activate venv/     --- in cmd tertminal
pip install -r requirements.txt

-----------------------------------------------------------------------------------------------
To Add files to git
```
git add .
```
OR
```
git add <file_name>
```
Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
```
git status
```
To check all version maintained by git
```
git log
```
To create version/commit all changes by git
```
git commit -m "message"
```
To send version/changes to github
```
git push origin main
```
To check remote url
```
git remote -v
```

To setup CI/CD Pipeline in Heroku:
```
    1. Email - narendas10@gmail.com
    2. API Key = 54f1a407-ff42-4555-b948-adb775705eb0
    3. App Name = simpleflaskapp-10
```
-----------------------------------------------------------------------------------------------

BUILD DOCKER IMAGE:
```
docker build -t <image_name>:<tagname> .
```
Note: Image name for docker must be lowercase

To list docker image
```
docker images
```
Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```
To check running container in docker
```
docker ps
```
To stop docker container
```
docker stop <container_id>
```
-----------------------------------------------------------------------------------------------