from urllib.request import urlopen
from html.parser import HTMLParser

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

    """
        주어진 HTML 데이터를 파싱하고 모든 이미지 URL을 추출합니다.

        Args :
            data : 파싱할 HTML 데이터
        Returns:
            이미지 URL 집합.
    """

    parser = ImageParser()   # parser 인스턴스를 만듭니다.
    parser.feed(data)
    return parser.result

def main():

    url = "https://www.google.co.kr"
    with urlopen(url) as f:
        charset = f.headers.getparam('charset')
        data = f.read().decode(charset)
        dataset = parse_image(data)
        print("Fetched images from",url)
        print(",".join(sorted(dataset)))

    if __name__ == "__main__":
        main()