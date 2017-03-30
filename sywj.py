import re
import requests
from bs4 import BeautifulSoup
import os
class SYWJ():
    def __init__(self):
        self.url = "http://photo.xitek.com/"
        user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
        self.headers = {"User-Agent":user_agent}
        self.last_page = self.get_last_page()
        
    def get_last_page(self):
        page_html = self.getcontentauto(self.url)
        soup = BeautifulSoup(page_html,'lxml')
        page = soup.find_all('a',class_ = 'blast')
#         print(page[0]['href'].split('/'))
        last_page = page[0]['href'].split('/')[-1]
        return (int(last_page))
           
    def getcontentauto(self,url):
        html = requests.get(url,headers = self.headers)
        content = html.text
        return content
    
    def download(self,url):
        p = re.compile(r'href="(/photoid/\d+)"')
        html_2 = self.getcontentauto(url)
        content_2 = re.findall(p,html_2)
        for i in content_2:
                    
            photoid=self.getcontentauto(self.url+i)
            bs=BeautifulSoup(photoid,"lxml")
            final_link=bs.find('img',class_="mimg")['src']
            #print final_link
            #pic_stream=self.__getContentAuto(final_link)
            title=bs.title.string.strip()
            filename = re.sub('[\/:*?"<>|]', '-', title)
            print('正在下载',filename)   
            filename=filename+'.jpg'
            img = requests.get(final_link).content
            with open(filename,'ab') as f:
                f.write(img)
                f.close
        
    def getPhoto(self):
        start=0
    #use style/0
        photo_url="http://photo.xitek.com/style/0/p/"
        for i in range(start,self.last_page+1):
            url=photo_url+str(i)
            print (url)
            #time.sleep(1)
            self.download(url)
        
def main():
    sub_folder = os.path.join(os.getcwd(), "content")
    if not os.path.exists(sub_folder):
        os.mkdir(sub_folder)
    os.chdir(sub_folder)
    a = SYWJ()
    a.getPhoto()
    
    

if __name__=="__main__":
    main()
        
        
        

        
        
        
