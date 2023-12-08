class TestCase:
    def __init__(self,name):
        self.name = name

    def setUp(self):
        pass
    
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self,name):
        self.wasSetUp = None
        TestCase.__init__(self,name)

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1
    
    def testMethod(self):
        self.wasRun = 1


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)

    def testSetUp(self):
        self.test.run()
        assert(self.test.wasSetUp)


# 부트스트랩 테스터(테스트 프레임워크를 테스트하는 테스터)
if __name__ == "__main__":
    TestCaseTest("testSetUp").run()