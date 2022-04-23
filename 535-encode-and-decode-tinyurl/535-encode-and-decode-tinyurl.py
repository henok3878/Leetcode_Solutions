class Codec:
    counter = 0
    base = "https://tiny.com/"
    def __init__(self):
        self.map = {}
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        curr = self.base + str(self.counter)   
        self.map[self.counter] = longUrl
        self.counter += 1
        return curr

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        a = int(shortUrl.split('/')[-1])
        return self.map[a]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))