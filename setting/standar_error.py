class StandarError(Exception):

    def __init__(self, message):
        self.message = message

    def error(self):
        """_summary_
        """
        raise Exception(self.message)



class SqliteInError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, message="Error com sqlite3"):
        # self.salary = salary
        self.message = message
        super().__init__(self.message)


#salary = int(input("Enter salary amount: "))
#if not 5000 < salary < 15000:
#    raise SalaryNotInRangeError(salary)

# class DataError(DatabaseError):

class MyException(BaseException):  # Noncompliant
    pass

# class MyException(GeneratorExit):  # Noncompliant
#     pass

# class MyException(KeyboardInterrupt):  # Noncompliant
#     pass

# class MyException(SystemExit):  # Noncompliant
#     pass