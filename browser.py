from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Browser:
    def __init__ (self, link, id, pw):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.id = id
        self.pw = pw
        self.link = link
        self.browser = webdriver.Chrome(options = self.options)
        Browser.goInstagram(self)

    def goInstagram(self):
        self.browser.get(self.link)
        time.sleep(2)
        Browser.login(self)
        Browser.getUnfollowers(self)

    def getUnfollowers(self):
        Browser.scrollDown(self)
        followers = self.browser.find_elements(By.CSS_SELECTOR, ".x9f619.xjbqb8w.x1rg5ohu.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1")
        followers_list = []

        for follower in followers:
            followers_list.append(follower.text)

        time.sleep(1)

        self.browser.get(self.link + "/" + self.id + "/following/")

        time.sleep(5)

        Browser.scrollDown(self)
        following = self.browser.find_elements(By.CSS_SELECTOR, ".x9f619.xjbqb8w.x1rg5ohu.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1")
        following_list = []
        for follow in following:
            following_list.append(follow.text)

        print(*list(set(following_list) - set(followers_list)), sep = "\n")

        fileName = "result.txt"
        file = open(fileName, "w")

        for line in list(set(following_list) - set(followers_list)):
            file.write(line + "\n")
        
        file.close()

    def scrollDown(self):
        js = """
        sayfa = document.querySelector("._aano");
        sayfa.scrollTo(0, sayfa.scrollHeight);
        var sayfaSonu = sayfa.scrollHeight;
        return sayfaSonu;
        """
        
        endOfLine = self.browser.execute_script(js)

        while True:
            end = endOfLine
            time.sleep(1)
            endOfLine = self.browser.execute_script(js)
            if end == endOfLine:
                break

    def login(self):

        username = self.browser.find_element(By.NAME, "username")
        password = self.browser.find_element(By.NAME, "password")
        
        username.send_keys(self.id)
        password.send_keys(self.pw)
        password.send_keys(Keys.ENTER)
        
        time.sleep(5)
        self.browser.get(self.link + "/" + self.id + "/followers/")
        time.sleep(5)