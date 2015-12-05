# HPAF-tv-show-viewer

## put data on HDFS

`hdfs dfs -mkdir /user/cloudera/input`
`hdfs dfs -copyFromLocal join2_gen* /user/cloudera/input`

## run hadoop

`hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input /user/cloudera/input -output /user/cloudera/output -mapper /home/cloudera/join2_mapper.py -reducer /home/cloudera/join2_reducer.py`

## get result from HDFS

`hdfs dfs -getmerge /user/cloudera/output ./out`

