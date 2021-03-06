# VideoMaker

A web app that concatenate videos with titles


## Road map

#### Upload
- Client
    - Index view
    - Id generation
    - Upload view
- Server
    - ~~File name, size, format assertion~~
    - ~~Adding to db~~
    - Return file list
        
#### Edit
- Client
    - Table view
    - Video previews
    - Drag and drop order
- Client & Server
    - Auto save
    - Delete video
    - Append video

#### Process & Result
- Server
    - Save Data
    - Push to rabbit mq
    - Load from rabbit mq
    - Process
    - Push result
- Client
    - Result view pushed
    
## Db connection

```shell script
mysql -h machine -u utilisateur -p video_maker -h localhost:3307 -u admin -p password
mysql -u admin -p password -h localhost:3306
```

## Running Docker
```shell script
docker-compose up -d
docker-compose restart server
docker-compose stop
```

## Documentations
- [Flask file upload](https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask)
- [React Dockerisation](https://xiaolishen.medium.com/develop-in-docker-a-node-backend-and-a-react-front-end-talking-to-each-other-5c522156f634)


## Improvements
- Logging utils (logger)
- Shared directory for logs (each service in a sub directory)
- Security: users, password, env variables
- Auto delete cron jobs



## Designs
- Used:
  - https://bulmatemplates.github.io/bulma-templates/templates/forum.html#
  - https://github.com/BulmaTemplates/bulma-templates/blob/master/templates/forum.html
- Potentially: 
  - https://jamstackthemes.dev/theme/jekyll-bulma-theme/