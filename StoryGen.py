import random

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan', 'In my childhood', 'During the summer vacation']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat', 'a bear', 'a bird']
name = ['Ali', 'Miriam', 'Daniel', 'Hoouk', 'Starwalker', 'Elena', 'Jacob']
residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England', 'New York', 'Tokyo']
went = ['cinema', 'university', 'seminar', 'school', 'laundry', 'beach', 'zoo']
happened = ['made a lot of friends', 'ate a burger', 'found a secret key', 'solved a mystery', 'wrote a book', 'discovered a hidden treasure', 'learned a new language']

print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
