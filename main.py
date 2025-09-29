print("hello world")

# Variables store data
variable_1 = 64 #integer
my_name = "KevinW" #str
wallet = 7.77 #float
raining_status  = bool(1) #bool
if raining_status == True:
    print(1)
# CONCATENATE string literal + string variable
greeting = "Howdy, " + my_name
print(greeting)
# You can use single quotes instead
greeting = 'Python is cool, it\'s better than Java'
# You can use triple double quotes for long strings
long_greeting = """
                we were both young
                when i first saw you
                i close my eyes
                """
# f-strings are FORMATTED strings (like templates)
f_string = f"My name is andy and my lucky number is 1"
print(f_string)

# FUNCTIONS are reusable recipes/processes
# Use the keyword def to DEFINE a new function
def helloworld():
    # function BODY indented under the colon
    print("hello world I am a function") 

# UN-indent to signal the END of that block
# CALL a void function (no output)
helloworld()

# Define a function with ARGUMENTS (input) + RETURN (output)
def multiply(x, y):
    result = x * y
    return result

# CALL a non-void function (handle the OUTPUT)
five_times_three = multiply(5,3)
print(five_times_three)
# you can also call the function directly in another
print(multiply(20,6)) # funcs evaluated from INSIDE to OUTSIDE
# *** LISTS ***
# ordered, mutable sequences
empty_list = list() # constructor
another_empty_list = [] 

class_roster = ["Bryce", "Finny", "Jackson", "Kevin", "Maia", "Natalie", "Paige"]
print(class_roster)
print(len(class_roster))

# Indexes start at 0
first_item = class_roster[0]
print(first_item)

# Update an item in a list, access by index
class_roster[2] = "Jack"
print(class_roster)

# Sorting lists
lottery_nums = [13, 7, 89, 99, 44, 23, 4]
print(sorted(lottery_nums))
print(sorted(lottery_nums, reverse=True))
print(lottery_nums) # sorted() does not modify OG list
# Sort IN PLACE -> modifies OG list
lottery_nums.sort()
print(lottery_nums)
class_roster.sort(reverse=True)
print(class_roster)

# List operations
class_roster.append("Alex")
class_roster.insert(0, "Zoie")
class_roster.remove("Zoie")
class_roster.pop() # remove last item 

# Check if item exists in a list
print(13 in lottery_nums) 

# Tuples

student = {'Kevin', 29, 'Game design', 4.0}
print(student)
# student[3]=5.0 Cant reassign item

# sets
# unsorted stores immutable items
# no duplicates
songs = {'stranger','2005','mutt'}
colors = {'red', 'blue', 'yellow','yellow'}
print(set(colors))
songs.add('mutt')
print(songs)

# dictionaries
# mutable them sleves but the keys need to be immutable types
# {key:value}, pairs, keys must be unique
# unordered, no index
grade_requirements = {9:['Bio','Maths','English','P.E.'],
                      10:['Chem','Maths','English','P.E.'],
                      11:['Physics','Maths','English','P.E.'],
                      12:['Maths', 'English','P.E.'],
                      }