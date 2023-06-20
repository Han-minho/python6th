import http.client
from urllib.request import urlopen, urlretrieve
from html.parser import HTMLParser
from pathlib import Path

class ImageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []
        # 이미지 URL 집합

    def handle_stattag(self,tag,attrs):
        if tag != 'img':
            return
        if not hasattr(self,'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)

def parse_image(data):

    parser = ImageParser()   # parser 인스턴스를 만듭니다.
    parser.feed(data)
    return parser.result

def download_Image(url,data):
    download_dir = Path('DOWNLOAD')
    download_dir.mkdir(exist_ok=True)

    parser = ImageParser()
    parser.feed(data)
    data_set = set(x for x in parser.result)
    for x in sorted(data_set):
        from urllib.parse import urljoin
        image_url = urljoin(url,x)
        basename = Path(image_url).name
        target_file = download_dir / basename
        print(target_file)

        print("Downloading........",image_url)
        urlretrieve(image_url,target_file)


def main():
    # url = "https://www.google.co.kr"
    # with urlopen(url) as f:
        # charset = f.headers.getparam('charset')
        # data = f.read().decode(charset)
    host = "www.google.co.kr"
    conn = http.client.HTTPConnection(host)
    conn.request('GET','')
    resp = conn.getresponse()

    charset = resp.msg.get_param('charset')
    data = resp.read().decode(charset)
    conn.close()
    print('\n>>>>>>> Downloading........',host)
    from urllib.parse import urlunparse
    url = urlunparse(('http',host,'','','',''))

    dataset = parse_image(data)
    print("Fetched images from",host)
    print(",".join(sorted(dataset)))
    download_Image(url,data)

if __name__ == "__main__":
    main()

