# StreamingProcessing
Streaming processing using Spark and Kafka

This is an example of streaming processing using Apache Spark consuming data from Apache Kafka. The figure shows the data-flow.

<img src="images/Architect.png">


On the left is a Producer, who produces messages to Kafka. In the middle is Kafka and on the right is the Spark programm.

The Producer is a Kafka producer. I use the confluent-kafka python API.

The Kafka version I use is 2.12-2.3.0.

The Spark version I use is 2.4.4-bin-hadoop2.7 and for the streaming processing I use the spark streaming API.



# Example

Below is a example of the data-flow. From the beginning, where the Producer sends messages to the Kafka, to the moment in which the Spark app consumes the messages and process them. The messages that the Producer produce, each contain a name of a phone.

Figure 1.2 shows tha Kafka saved succesfully the messages that the Producer send. The messages that the Producer send were .

<img src="images/Screenshot from 2020-01-07 18-36-00.png'>
