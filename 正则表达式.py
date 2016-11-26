import re
'''
[0-9a-zA-Z]:表示0-9，a-z,A-Z的所有数字和字母都在匹配的范围内（只匹配一个）
[0-3]:只匹配0-3的一个字符
[0-3]+ :匹配0-3的多个字符
\s  空白字符（空格）
\d 数字0-9
\D 非数字
\w [0-9a-zA-Z]单词字符
\W 非单词字符
r'..' 主要是避免转义字符的出现在正则表达式中，不能识别
\, ,
\;  ;

* 匹配前一个字符0次或者无限次 如：abc* ==abccccc==abc==abcc!=abcd
+ 匹配前一个字符1次或者无限次     abc+=abc=abccc=abcccc!=abc
？匹配前一个字符0次或者无限次   ab?=ab==abc
(?=...): 之后的内容匹配成功才能正确的返回,例如："def(?=abc)" and "xyzdefabc"(这里的表示def后面必须是abc才能匹配成功
(?<=...): 之前的内容匹配成功才能正确的返回，例如："(?<=abc)def" and "abcdefxyz"(这里的表示def之前必须是abc才能匹配成功
(?!...):之后的内容必须不匹配才能正确的返回  例如：abc(?!def) and "abcdef"(None)   abc(?!def) and "abchkjk"(返回正确的形式）
(?<!...):之前的内容必须不匹配才能正确的返回， 例如： (?<!abc)def and "abcdefuin"(None)  ,(?!abc)def and "cdedefghj"(返回正确的形式）
(?:..){n}:用于匹配多组一样的数据（必须紧贴在一起的） 例如： (?:abc){2} and "abcabcdef"(true)  (?:abc){2} and "abcdefabc"(None)
re 主要用于表示正则表达式，主要的函数：
match():主要用于从开头第一个字母匹配，如果匹配成功则返回正确的形式，如果不成功则返回的是None
search():主要的功能是从要匹配的字符串的任意位置开始匹配，如果匹配成功则返回正确的形式，反之返回None
compile():主要用于将正则表达式编译成一个对象，用于调用re的内置函数，（这个是大量要用到同一个正则表达式的时候才会使用）
split():按照指定的分隔符将字符串分成几份
match().group(n):主要用输出利用正则表达式分组
findall():用正则表达式在整个字符串中查找，搜索出所有满足正则表达式的字符串，然后一列表的形式打印出来
finditer():返回的是一个迭代器
suban()
'''
'''
print("chen\-\jdkck")

#print(re.match(r"\d{3}\w\d$","123u8"))
#print(re.search(r"^\d{3} ","oo1234"))
#print(re.match(r'\d{2,6  }\ \d{3,8}',"123-7890"))
#print(re.search(r"[0-9a-z\_]",'23Q'))   #这里只能匹配一个字符
#print(re.search(r"[0-9a-z\_]+",'23Q'))   #这里匹配的是一个字符串
#print(re.match(r"[0-9A-Z][0-9a-zA-z\_]*","q3467iot")) # [a-zA-Z\_][0-9a-zA-Z\_]*可
# 以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，
#print(re.match(r"\d{3}\D\d{3}","234 567"))
m=re.match(r"abc*","abccddd")
print(m)
print(m.string)
print(m.groups())
print(m.group())
'''
'''
#m=re.search(r'def(?=xyz)',"abcdefxyz")
#print(m)
#print(m.group(0))
#print(re.search(r'(?<=abc)def',"ddabcdef"))   #这里表示紧贴着def前面的是abc才能匹配成功
#print(re.search(r'(?!=abc)def',"ddabddef"))   #这里表示紧贴着def前面的不是abc才能匹配成功
#print(re.search(r'abc(?#456)789',"abc456789"))
#print(re.search(r'abc(?!cde)',"abcdef"))
#print(re.search(r"(?:abc){3}","abcabcabcabc"))
pattern=re.compile("hello")   #将字符串编译成一个pattern对象，用于调用re的函数进行匹配
print(pattern.search(r"hello wirf"))

p=re.compile(r'hello')   #编译成一个pattern对象
print(p.match("hello world"))  #调用这个函数
print(re.split(r'\-',"a-b-c"))   #按照-将字符串分割成三份
print(re.split(r'[\-]+',"a-b--c"))  #按照-或则多个-将字符串分割成三份


m=re.match(r'(^\d{3})-(\w{3})','123-abc')  #这里将正则表达式分成两组，用（）将要分组的信息在正则表达式中显示出来
print(m)
print(m.group(1))
print(m.group(2))                  #group(0)默认的打印出的是整个匹配到的整个字符串，没有匹配到的就不打印出来
print(re.match(r'\d\s\d',"1 2"))   #group(1)打印出来的是第一个分组的信息
print(re.match(r'(\d{3})-(\w{4})',"345-erty").group(0))

print(re.findall(r'\d{3}',"1234we456,789rt"))
m=re.finditer(r'\d{3}',"1234we456,789rt")
for i in m:
    print(i.group())
'''
print(re.match(r'[d-z]+',"fghjj"))