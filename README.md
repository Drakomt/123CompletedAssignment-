"# 123CompletedAssignment-" 

Consumer:
docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic test_topic

Producer:
docker exec -it kafka kafka-console-producer --bootstrap-server localhost:9092 --topic test_topic