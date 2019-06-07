import fasttext
import product_utils
import calendar
import time
import sys
import json
import datetime

start = time.time()
date_created = date_created = datetime.date.today()
query_limit_offset = 5000

# Get number of reviews to be tokenize
connection = product_utils.db_connect()
read_cursor = connection.cursor(dictionary=True)

classifier = fasttext.supervised('temp.ft.txt', 'fastText-0.1.0/reviews_model', label_prefix='__label__')


myresult = read_cursor.execute("select count(*) as cnt  FROM product_reviews \
WHERE is_processed = 0 ")
records = read_cursor.fetchone()

if (connection.is_connected()):
    read_cursor.close()
    connection.close()
    print("connection is closed")

print(records['cnt'])

reviews_count = records['cnt']

while (reviews_count > 0):
    connection = product_utils.db_connect()
    read_cursor = connection.cursor(dictionary=True)

    read_cursor.execute("SELECT * FROM product_reviews WHERE is_processed = 0 and review_text is not null LIMIT " + str(query_limit_offset))
    myresult = read_cursor.fetchall()

    review_id_list = []
    insert_data_list = []
    list_25=[]
    id_list25=[]
    record=len(myresult)//25
    remainder=len(myresult)%25
    count=1
    for row in myresult:
        #Exp started
        review_text=None
        review_text = row['review_text']

        if len(review_text.strip()) > 0:
            labels_full_review = classifier.predict_proba([review_text])
            
            review_id=row["id"]
            final_score = labels_full_review[0][0][0]
            confidence_level = labels_full_review[0][0][1]
            data_row = (review_id, date_created, final_score, confidence_level)
            insert_data_list.append(data_row)
            review_id_list.append(review_id)
            

    product_utils.reviews_sentiment_insert_fasttext(insert_data_list)
    insert_data_list.clear()
    review_ids = ", ".join(str(x) for x in review_id_list)
    print(review_ids)
    sql = "UPDATE product_reviews SET is_processed = 1 WHERE id in (%s)" % review_ids
    print(sql)
    write_cursor = connection.cursor(dictionary=True)
    write_cursor.execute(sql)
    connection.commit()
    review_id_list.clear()
    print(write_cursor.rowcount, "record(s) affected")
        
        
    reviews_count = reviews_count - query_limit_offset
    

print('It took', time.time() - start, 'seconds.')


