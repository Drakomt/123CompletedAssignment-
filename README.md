"# 123CompletedAssignment-" 

Docker Commands:
docker-compose up -d     ==> Start the project (-d for decoupled mode)
docker-compose down      ==> Stop the project (removes the containers)
docker-compose ps        ==> Print active containers

Consumer Test:
docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic events

Producer Test:
docker exec -it kafka kafka-console-producer --bootstrap-server localhost:9092 --topic events

Mongodb sh (Terminal/Shell):
docker exec -it mongodb mongosh     ==>  add "-u admin -p admin" for username and password

Redis View:
docker exec -it redis redis-cli      ==>    redis Terminal/Shell Start
KEYS *       ==> show all keys
GET <your-key>       ==> show the value of the key