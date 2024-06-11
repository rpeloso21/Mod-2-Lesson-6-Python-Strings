

python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
keywords = ["good", "excellent", "bad", "poor", "average"]
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def string_varient_creator(lst):
    new_lst = []
    for item in lst:
        new_lst.append(item + " ")
        new_lst.append(item + ".")
        new_lst.append(item.capitalize())
    
    return new_lst        


# Task 1

def highlighter(reviews, keywords):
    for review in reviews:
        for word in keywords:
            if word in review:
                new_review = review.replace(word, word.upper())
                print(new_review)

            
# Task 2

def sentiment_tally(reviews, goods, bads):
    good_words = 0
    bad_words = 0
    for review in reviews:
        split_review = review.split()
        for word in split_review:
            for item in goods:
                if item.upper() == word.upper():
                    good_words += 1
            for item in bads:
                if item.upper() == word.upper():
                    bad_words += 1


    return print(f"We found {good_words} positive words and {bad_words} negative words in these reviews.")

# Task 3

def review_summery(reviews):
    for review in reviews:
        review_at = 30
        for char in review[30:]:
            if char.isspace():
                print (review[:review_at] + "...")
                break
            else:
                review_at += 1
            



all_keywords = string_varient_creator(keywords)
all_positive_words = string_varient_creator(positive_words)
all_negative_words = string_varient_creator(negative_words)

highlighter(python_reviews, all_keywords)
sentiment_tally(python_reviews, all_positive_words, all_negative_words)
review_summery(python_reviews)