'''
days = week()
next(days) # 'Monday'
next(days) # 'Tuesday'
next(days) # 'Wednesday'
next(days) # 'Thursday'
next(days) # 'Friday'
next(days) # 'Saturday'
next(days) # 'Sunday'
next(days) # StopIteration
'''

#days = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#print(days.pop(0))

def week():
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    i = 0
    while i <= 6:
        yield days_of_week[i]
        i += 1

days = week()

next(days) # 'Monday'
next(days) # 'Tuesday'
next(days) # 'Wednesday'
next(days) # 'Thursday'
next(days) # 'Friday'
next(days) # 'Saturday'
next(days) # 'Sunday'
next(days) # StopIteration

'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''

def yes_or_no():
    answer = ["yes", "no"]
    i = 0
    while True:
        if i % 2 == 0:
            yield answer[0]
        else:
            yield answer[1]
        i += 1
        
        
gen = yes_or_no()

next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'

def current_beat():
    i = 1
    while True:
        if i == 5:
            i = 1
        yield i
        i +=1
        
gen = current_beat()

print(next(gen) )
print(next(gen) )
print(next(gen) )
print(next(gen) )
print(next(gen) )
print(next(gen) )


def make_song(cnt = 99, beverage = "soda"):
    while cnt >= 0:
        if cnt == 0:
            yield "No more " + beverage + "!"
        elif cnt == 1:
            yield "Only 1 bottle of " + beverage + " left!"
        else:
            yield str(cnt) + " bottles of " + beverage + " on the wall."
        cnt -= 1
            
kombucha_song = make_song(5, "kombucha")

next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration


def get_multiples(num = 1, cnt = 10):
    next_num = num
    while cnt >= 1:
        yield next_num
        next_num += num
        cnt -= 1

evens = get_multiples(2, 3)
next(evens) # 2
next(evens) # 4
next(evens) # 6
next(evens) # StopIteration    


default_multiples = get_multiples()
list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    

def get_unlimited_multiples(num = 1):
    next_num = num
    while True:
        yield next_num
        next_num += num

sevens = get_unlimited_multiples(7)
[next(sevens) for i in range(15)] 
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

ones = get_unlimited_multiples()
[next(ones) for i in range(20)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]    
    
    
    
    