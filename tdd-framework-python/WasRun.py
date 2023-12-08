class WasRun:
    def __init__(self,name):
        self.wasRun = None

    def run(self):
        self.testMethod()
    
    def testMethod(self):
        self.wasRun = 1

# 부트스트랩 테스터(테스트 프레임워크를 테스트하는 테스터)
if __name__ == "__main__":
    test = WasRun("testMethod")
    print(test.wasRun)
    test.run()
    print(test.wasRun)