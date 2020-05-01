from unittest import TestLoader, TestSuite, TextTestRunner
from unitTest_login import MS_Test1
from unitTest_logout import MS_Test2
from unitTest_review import MS_Test4
from unitTest_contact import MS_Test6
from unitTest_addtocart import MS_Test5
from unitTest_contshop import MS_Test3
from unitTest_adminlogin import MS_Test7

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(MS_Test1),
        loader.loadTestsFromTestCase(MS_Test2),
        loader.loadTestsFromTestCase(MS_Test3),
        loader.loadTestsFromTestCase(MS_Test4),
        loader.loadTestsFromTestCase(MS_Test5),
        loader.loadTestsFromTestCase(MS_Test6),
        loader.loadTestsFromTestCase(MS_Test7),

    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)