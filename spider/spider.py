
from urllib import request
import ssl
import re

class Spider():
  url = 'http://www.huya.com/g/lol'
  root_pattern = '<span class="avatar fl">([\s\S]*?)</span>'
  name_pattern = '<i class="nick" title="[\s\S]*?">([\s\S]*?)</i>'
  def __fetch_content(self):
    context = ssl._create_unverified_context()
    r = request.urlopen(Spider.url, context=context)
    htmls = r.read().decode('utf-8')
    a = 1
    return htmls

  def __analysis(self, htmls):
    root_html = re.findall(Spider.root_pattern, htmls)
    anchors = []
    for html in root_html:
      name = re.findall(Spider.name_pattern, html)
      anchor = {'name': name}
      anchors.append(anchor)
    print(anchors)
    a = 1

  def go(self):
    htmls = self.__fetch_content()
    self.__analysis(htmls)

spider = Spider()
spider.go()
