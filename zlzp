import re
import requests
import pyodbc




class zlzp():
    def __init__(self):
        self.url_yuan = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%e5%85%a8%e5%9b%bd&kw=%e6%95%b0%e6%8d%ae%e5%88%86%e6%9e%90%e5%b8%88&sm=0&isfilter=0&fl=489&isadv=0&sg=810aba78de204b83b4bf602eeb6c52a4&p='
        self.result_title = []
        self.result_zhiwei = []
        self.result_gongzi = []
        self.result_didian = []
        self.result_faburiqi = []  
    
    
    def getHTML(self,url):
        response = requests.get(url).text
        return response
    
    def get_url(self,url):
        pattern_1 = re.compile('onclick="submitLog.*?">(.*?)</a>')
        pattern_2 = re.compile('<td class="gsmc">.*?href=.*?>(.*?)</a>')
        pattern_3 = re.compile('<td class="zwyx">(.*?)</td>')
        pattern_4 = re.compile('<td class="gzdd">(.*?)</td>')
        pattern_5 = re.compile('class="gxsj">.*?<span>(.*?)</span')
        html =self.getHTML(url)
        title = re.findall(pattern_1,html)
        zhiwei = re.findall(pattern_2,html)
        gongzi = re.findall(pattern_3,html)
        didian = re.findall(pattern_4,html)
        faburiqi = re.findall(pattern_5,html)
        self.result_title.extend(title)
        self.result_zhiwei.extend(zhiwei)
        self.result_gongzi.extend(gongzi)
        self.result_didian.extend(didian)
        self.result_faburiqi.extend(faburiqi)
#         l = [title,zhiwei,gongzi,didian,faburiqi]
#         print(l)
        
        
            
    def get_page(self):
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=python;UID=sa;PWD=duanhaolan')
        cursor =conn.cursor()
    
        for i in range(1,90):
            html =self.url_yuan + str(i)
            self.get_url(html)
#         print(self.result_title)
#         print(','.join(self.result_title))
#         cursor.execute("INSERT INTO dbo.HOUSE(title,zhiwei,gongzi,didian,faburiqi) VALUES(?,?,?,?,?)",self.result_title,'b','c','d','e')
        for i in range(len(self.result_title)):
            cursor.execute("INSERT INTO dbo.HOUSE(title,zhiwei,gongzi,didian,faburiqi) VALUES(?,?,?,?,?)",str(self.result_title[i]),str(self.result_zhiwei[i]),str(self.result_gongzi[i]),str(self.result_didian[i]),str(self.result_faburiqi[i]))
            cursor.commit()
        cursor.close()  
        conn.close()
#         a123.insert(self.result_title,self.result_zhiwei,self.result_gongzi,self.result_didian,self.result_faburiqi)
            
            
            
            
def main():
    about=zlzp()
    about.get_page()
    
    
    
if __name__ == '__main__':
    main()
        
