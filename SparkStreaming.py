from pyspark.streaming import StreamingContext
from pyspark import SparkContext, SparkConf
from pyspark.streaming.kafka import KafkaUtils

kafka_params = {'bootstrap.servers': 'localhost:9092',
                'group.id': 'StreamingGroup',
                'auto.offset.reset': 'largest'
                }  #Kakfa consumer parametres

if __name__ == '__main__':

    sc = SparkContext(appName='StreamingAp')
    ssc = StreamingContext(sc, 4) # 4 second window
    lines = KafkaUtils.createDirectStream(ssc, ['Test'], kafka_params) #Initial Dstream
    Phones = lines.map(lambda Order: (Order[1],1)).reduceByKey(lambda x,y : x + y).pprint() #MapReduce and print the results
    ssc.start()             # Start the computation
    ssc.awaitTermination()  # Wait for the computation to terminate
