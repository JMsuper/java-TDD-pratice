class TestResult:
    def __init__(self):
        self.runCount = 0
        self.failedCount = 0

    def testStarted(self):
        self.runCount = self.runCount + 1

    def testFailed(self):
        self.failedCount = self.failedCount + 1

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.failedCount)

class TestCase:
    def __init__(self,name):
        self.name = name

    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def run(self,result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except Exception as e:
            print(self.name,e)
            result.testFailed()
        self.tearDown()
        return result


class WasRun(TestCase):
    def __init__(self,name):
        TestCase.__init__(self,name)

    def setUp(self):
        self.log = "setUp "
    
    def testMethod(self):
        self.log = self.log + "testMethod "

    def tearDown(self):
        self.log = self.log + "tearDown "

    def testBrokenMethod(self):
        raise Exception

class TestSuite():
    def __init__(self):
        self.tests = []
    
    def add(self, test):
        self.tests.append(test)
    
    def run(self, result):
        for test in self.tests:
            test.run(result)

class TestCaseTest(TestCase):
    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())

    def testFailedResult(self):
        test= WasRun("testBrokenMethod")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())


# 부트스트랩 테스터(테스트 프레임워크를 테스트하는 테스터)
if __name__ == "__main__":
   suite = TestSuite()
   suite.add(TestCaseTest("testTemplateMethod"))
   suite.add(TestCaseTest("testResult"))
   suite.add(TestCaseTest("testFailedResultFormatting"))
   suite.add(TestCaseTest("testFailedResult"))
   suite.add(TestCaseTest("testSuite"))
   result = TestResult()
   suite.run(result)
   print(result.summary())