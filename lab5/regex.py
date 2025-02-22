#1
import re

def text_match(text):
        patterns = 'ab*'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return('Not matched')
print(text_match("abbc"))
print(text_match("tsa"))
print(text_match("bc"))
print(text_match("tsd"))
# Output
# Found a match!
# Found a match!
# Not matched
# Not matched

#2
import re

def text_match(text):
        patterns = 'ab{2,3}?'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return ('Not matched!')
print(text_match("abb"))
print(text_match("aaabbb"))
#Output
# Found a match!
# Found a match!

#3
import re

def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return ('Not matched!')
print(text_match("harry_potter"))
print(text_match("kaha_Sergo"))
print(text_match("tom_jerry"))
#Output
# Found a match!
# Not matched!
# Found a match!

#4
import re

def text_match(text):
        patterns = '^[a-z]+_[A-Z][a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return ('Not matched!')
print(text_match("harry_potter"))
print(text_match("kaha_Sergo"))
print(text_match("tom_jerry"))
#Output
# Not matched!
# Found a match!
# Not matched!

#5
import re

def text_match(text):
        patterns = 'a.*?b$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return ('Not matched!')
print(text_match("shaurma"))
print(text_match("kebab"))
print(text_match("samsa"))
#Output
# Not matched!
# Found a match!
# Not matched!

#6
import re

def text_match(text):
        result = re.sub("[ ,.]", ":", text)
        return result

print(text_match("ab,ac"))
print(text_match("sa.sa"))
print(text_match("ka kf"))
# Output
# ab:ac
# sa:sa
# ka:kf

#7
import re

def text_match(text):
    result = re.sub(r'_([a-zA-Z])', lambda m: m.group(1).upper(), text)
    return result

print(text_match("harry_potter"))
print(text_match("kaha_Sergo"))
print(text_match("tom_jerry"))
# Output
# harryPotter
# kahaSergo
# tomJerry

#8
import re

def text_match(text):
    result = re.split(r'(?=[A-Z])', text)
    return result

print(text_match("harryPotter"))
print(text_match("kahaSergo"))
print(text_match("tomJerry"))
#Output
# ['harry', 'Potter']
# ['kaha', 'Sergo']
# ['tom', 'Jerry']

#9
import re

def text_match(text):
    result = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
    return result

print(text_match("HarryPotter"))
print(text_match("KahaSergo"))
print(text_match("TomJerry"))
# Output
# Harry Potter
# Kaha Sergo
# Tom Jerry

#10
import re

def camel_to_snake(text):
    result = re.sub(r'([A-Z])', r'_\1', text).lower().lstrip('_')
    return result

print(camel_to_snake("HarryPotter"))
print(camel_to_snake("KahaSergo"))
print(camel_to_snake("TomJerry"))
# Output
# harry_potter
# kaha_sergo
# tom_jerry
