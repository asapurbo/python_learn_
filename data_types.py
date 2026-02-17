'''
১. ডেটা টাইপস কী এবং কেন দরকার?
২. পাইথনের বিল্ট-ইন ডেটা টাইপস
৩. type() ফাংশন দিয়ে ডেটা টাইপ জানা
৪. বিভিন্ন ডেটা টাইপের বিস্তারিত
   - Text Type (str)
   - Numeric Types (int, float, complex)
   - Sequence Types (list, tuple, range)
   - Mapping Type (dict)
   - Set Types (set, frozenset)
   - Boolean Type (bool)
   - Binary Types (bytes, bytearray, memoryview)
   - None Type (NoneType)
৫. ডেটা টাইপ নির্ধারণ করা
৬. টাইপ কনভার্শন (Type Conversion/Casting)
৭. বাস্তব জীবনের প্রয়োগ
৮. অনুশীলন প্রশ্ন

'''

# x = [
#     {
#     "Name": "rohim",
#     "Roll": 10098,
#     "dfas": 'akldfjalksdjf'
# },

# {
#     "Name": "rohim",
#     "Roll": 10098,
#     "dfas": 'akldfjalksdjf'
# },

# {
#     "Name": "rohim",
#     "Roll": 10098,
#     "dfas": 'akldfjalksdjf'
# }
# ]

# y = ['rohim', 'korim', 'kamal']


'''
১. ডেটা টাইপস কী এবং কেন দরকার?

ডেটা টাইপ হলো তথ্যের ধরন। যেমন তোমার স্কুলে বিভিন্ন ধরনের জিনিস আছে:
- বই (Text/লেখা)
- রোল নম্বর (সংখ্যা)
- উপস্থিতির তালিকা (তালিকা)
- ছাত্র-ছাত্রীদের নাম ও বয়স (অভিধান)

ঠিক একইভাবে, কম্পিউটার প্রোগ্রামিংয়ে বিভিন্ন ধরনের ডেটা আছে। পাইথন স্বয়ংক্রিয়ভাবে বুঝে নেয় কোন ধরনের ডেটা তুমি ব্যবহার করছো।

কেন ডেটা টাইপ গুরুত্বপূর্ণ?
- বিভিন্ন টাইপের ডেটা দিয়ে বিভিন্ন কাজ করা যায়
- সংখ্যা যোগ করা যায়, কিন্তু নাম যোগ করা যায় না
- সঠিক ডেটা টাইপ ব্যবহার করলে প্রোগ্রাম দ্রুত এবং সঠিক কাজ করে

'''




'''
২. পাইথনের বিল্ট-ইন ডেটা টাইপস

পাইথনে মূলত ৮ ধরনের ডেটা টাইপ আছে:

১. Text Type (লেখা):
   - str (String - শব্দ বা বাক্য)

name = "My name is Apurbo!"

# ' ', " "

২. Numeric Types (সংখ্যা):
   - int (Integer - পূর্ণসংখ্যা)
   - float (দশমিক সংখ্যা)
   - complex (জটিল সংখ্যা)

integer => 1, 2, 3, 4, 5, 6 ... 199999
float => 1.30, 4.74, 6.89, 7.43
complex =>
x = 3+5j
y = 5j
z = -5j

৩. Sequence Types (ক্রম):
   - list (তালিকা - পরিবর্তনযোগ্য)
   - tuple (টাপল - অপরিবর্তনীয়)
   - range (রেঞ্জ - সংখ্যার ধারা)

       [0]      [1]       [2]
x = ['rohim', 'korim', 'kamal', 'rohim']
x[0] = 'kahdflakjsldfk'

y = ('rohim', 'korim')
y[0] = 'kahdflakjsldfk'

range(1, 100)

৪. Mapping Type (অভিধান):
   - dict (Dictionary - চাবি-মান জোড়া)

x = {
    "Name": "rohim",
    "Roll": 10098,
    "dfas": 'akldfjalksdjf'
}

৫. Set Types (সেট):
   - set (সেট - অনন্য আইটেম)
   - frozenset (অপরিবর্তনীয় সেট)

x = {'rohim', 'korim', 'rohim'}

৬. Boolean Type (সত্য/মিথ্যা):
   - bool (Boolean - True বা False)

x = True
y = False

৭. Binary Types (বাইনারি):
   - bytes, bytearray, memoryview

৮. None Type:
   - NoneType (কিছু নেই)

x = None

'''



'''

৩. type() ফাংশন দিয়ে ডেটা টাইপ জানা

type() ফাংশন ব্যবহার করে যেকোনো ভেরিয়েবলের ডেটা টাইপ জানা যায়।

উদাহরণ ১: সহজ টাইপ চেক
----------------------------
x = 5
print(type(x))

আউটপুট:
<class 'int'>

ব্যাখ্যা: x একটি integer (পূর্ণসংখ্যা)


উদাহরণ ২: বিভিন্ন টাইপ চেক
----------------------------

name = "রহিম"

'''

# name = str('Apurbo Howlader')


# Falsy Values

# False
# None
# 0 (integer), 0.0 (float), 0j (complex)
# '' or ""
# []
# ()
# {}
# set()
# range(0)

# number_type = bool(())

# print(number_type)


string_value = '32'

number_value = int(string_value)

x = number_value + 2

print(x)







