#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 04/22/2018
# Descr. : Inserting events on Index elasticsearch 

# Import Elasticsearch package 
from elasticsearch import Elasticsearch 
# Connect to the elastic cluster
es=Elasticsearch([{'host':'localhost','port':9200}])

# Create event structure to insert.
e1 = {    "logId":"id112",                  \
      "eventTime":"2018-04-10T11:25:20",    \
          "url":"http://google.com/rum6", \
     "us_country":"USA",                    \
         "userId":"u2",                     \
        "browser":"IE",                     \
          "ua_os":"WINDOWS",                \
   "responseCode":400,                      \
           "ttfb":2.0 }
# Insert events on elasticsearch.
res = es.index(index='hw11_p2_index',doc_type='log',id="id112",body=e1)
# Print the result
print (res)

# Create event structure to insert.
e1 = {    "logId":"id113",                  \
      "eventTime":"2018-04-10T12:25:20",    \
          "url":"http://google.com/rum2", \
     "us_country":"BRAZIL",                    \
         "userId":"u3",                     \
        "browser":"FIREFOX",                     \
          "ua_os":"CENTOS7",                \
   "responseCode":400,                      \
           "ttfb":4.0 }
# Insert events on elasticsearch.
res = es.index(index='hw11_p2_index',doc_type='log',id="id113",body=e1)
# Print the result
print (res)

# Create event structure to insert.
e1 = {    "logId":"id114",                  \
      "eventTime":"2018-04-10T15:25:21",    \
          "url":"http://google.com/rum4", \
     "us_country":"USA",                    \
         "userId":"u2",                     \
        "browser":"IE",                     \
          "ua_os":"WINDOWS",                \
   "responseCode":200,                      \
           "ttfb":2.4 }
# Insert events on elasticsearch.
res = es.index(index='hw11_p2_index',doc_type='log',id="id114",body=e1)
# Print the result
print (res)


# Create event structure to insert.
e1 = {    "logId":"id115",                  \
      "eventTime":"2018-04-10T16:25:20",    \
          "url":"http://google.com/rum3", \
     "us_country":"BRAZIL",                    \
         "userId":"u4",                     \
        "browser":"FIREFOX",                     \
          "ua_os":"CENTOS7",                \
   "responseCode":501,                      \
           "ttfb":4.8 }
# Insert events on elasticsearch.
res = es.index(index='hw11_p2_index',doc_type='log',id="id115",body=e1)
# Print the result
print (res)

# Create event structure to insert.
e1 = {    "logId":"id116",                  \
      "eventTime":"2018-04-10T18:25:21",    \
          "url":"http://google.com/rum1", \
     "us_country":"USA",                    \
         "userId":"u5",                     \
        "browser":"IE",                     \
          "ua_os":"WINDOWS",                \
   "responseCode":503,                      \
           "ttfb":2.0 }
# Insert events on elasticsearch.
res = es.index(index='hw11_p2_index',doc_type='log',id="id116",body=e1)
# Print the result
print (res)

    
