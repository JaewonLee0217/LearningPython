from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images

#구글 이미지 crawling를 하기 위해 다음과 같은 라이브러리(google_images_douwnload)를 활용하였으나,
#google search에서도 최근 업데이트가잇어 라이브러리가 막혔다..
#구글에서 다양한 서비스를 제공하지만, crawling과 같은 데이터 수집의 경우, 사용자가 원하는 데이터와 정보를
#편하게 수집하는 목저으로 이용해서, 오류가 나는 것에 대해 구글에서 책임은 없다. 개발자들은 알아서 우회해서 데이터를 받는 방법을 알아내던가,
#누군가가 그 방법을 만들어 주길 기다려야 한다.