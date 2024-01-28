"# 123CompletedAssignment-" 

Consumer Test:
docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic test_topic    //confluentinc image
docker exec -it <consumer-container-id> kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-topic --from-beginning   //bitnami image


Producer Test:
docker exec -it kafka kafka-console-producer --bootstrap-server localhost:9092 --topic test_topic   //confluentinc image
docker exec -it <consumer-container-id> kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test-topic --from-beginning   //bitnami image


Mongodb sh (Terminal/Shell):
docker exec -it mongodb mongosh -u admin -p admin