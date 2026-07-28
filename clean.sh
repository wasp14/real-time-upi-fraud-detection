# Reset feature consumer
docker exec kafka /opt/kafka/bin/kafka-consumer-groups.sh \
--bootstrap-server localhost:9092 \
--group feature-service-dev \
--topic transactions \
--reset-offsets \
--to-latest \
--execute

# Reset storage consumer
docker exec kafka /opt/kafka/bin/kafka-consumer-groups.sh \
--bootstrap-server localhost:9092 \
--group storage-service \
--topic enriched_transaction_v2 \
--reset-offsets \
--to-latest \
--execute