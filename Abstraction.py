from abc import ABC,abstractmethod
class InstagramFrontEnd:
    def story(self):
        pass
    def post(self):
        pass
    def reels(self):
        pass
    def profile(self):
        pass
    def request(self):
        pass
class InstagramBackEnd(InstagramFrontEnd):
    @abstractmethod
    def story(self):
        print('Story display')
    def post(self):
        print('post display')
    def reels(self):
        print('reels display')
    def profile(self):
        print('profile display')
    def request(self):
        print('request display')
try:
    user1=InstagramBackEnd()
    user1.profile()
except Exception:
    print('Backend is not accessiable')