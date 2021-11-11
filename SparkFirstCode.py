from pyspark import SparkContext
  
sc = SparkContext.getOrCreate()

words = sc.textFile('hamlet.txt').flatMap(lambda lines: lines.split(" "))

counts = words.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y).collect()

with open('hamletout.txt', 'w') as f:
    for count in counts:
        f.write(str(count[0]) + ':\t' + str(count[1]) + '\n')