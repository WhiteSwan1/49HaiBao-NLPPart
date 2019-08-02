import code
import codecs
text = codecs.open('D:\PyCharm Community Edition 2016.3.2\DeeCamp\\NLPpart\data\CarReport\CarReport_122.txt', 'r', 'gb18030').read()



keyword = code.keywords(text,10)
print(keyword)
pos = code.pos(keyword)
print(pos)
