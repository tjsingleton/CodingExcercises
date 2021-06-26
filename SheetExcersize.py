# Try running pylint (https://www.pylint.org/) and learning from it's suggestions. It'll help you write python in a generally accepted style. 
import re


class Sheet:
    def __init__(self):
        self.sheet = {}

    def setCellValue(self, cell, input):
        self.sheet[cell] = input

    # If you were to write a description of what this method does, would you need to use "AND"? 
    # If so, your method is doing too much and it'd be easier to understand if you broke it up. 
    # Visually I can tell by the nesting and the size it's doing more than one thing. 
    def getCellValue(self, cell):
        cellInput = self.sheet[cell]
        cellValue = None
        cellValuesArray = []      

        if cellInput.startswith("="):
            matchCells = re.findall(
                r"(?P<cell>[A-z]+\d+)|(?P<operator>\+)|(?P<number>\d+)",
                cellInput)
            # print("Match= ", matchCells)
            for matchCell, matchOperator, matchNumber in matchCells:
                # print(matchCell, matchOperator, matchNumber)
                if matchCell:
                    cellValue = self.sheet[matchCell]
                    cellValuesArray.append(self.getCellValue(matchCell))
                if matchOperator:
                    cellValuesArray.append(matchOperator)
                if matchNumber:
                    cellValue = matchNumber
                    cellValuesArray.append(matchNumber)
                # This part is setting up cellValuesArray. Line 36 picks it back up, but reading flow is interruputed by the else statement.
                # The else case doesn't use cellValuesArray. Line 36 can only be true if line 18 is true.
        else:
            cellValue = cellInput
        # print(cellValuesArray)
        if "+" in cellValuesArray:
            sumTotal = 0
            for item in cellValuesArray:
                # Should this be an error? 
                if re.match(r"\d+", item):
                    sumTotal += int(item)
            cellValue = str(sumTotal)

        return cellValue


# Tests
# There is a lot of duplication in these tests that get in the way of reading them. 
# I kept finding that I'd change the expected value on the right side of the "==", but not the expected value "Expected X got:" part. 
# How could we print the expectation string only when the test fails? 
sheettest = Sheet()
sheettest.setCellValue("A1", "5")
assert sheettest.getCellValue("A1") == "5", "Get cell simple value.\
     Expected 5 got: {}".format(sheettest.getCellValue("A1"))

sheettest1 = Sheet()
sheettest1.setCellValue("A1", "5")
sheettest1.setCellValue("A2", "= A1")
assert sheettest1.getCellValue("A2") == "5", "Cell reference give value.\
     Expected 5 got: {}".format(sheettest1.getCellValue("A2"))

sheettest2 = Sheet()
sheettest2.setCellValue("A3", "=5")
assert sheettest2.getCellValue("A3") == "5", "Cell function handles integer.\
     Expected 5 got: {}".format(sheettest2.getCellValue("A3"))

sheettest3 = Sheet()
sheettest3.setCellValue("A3", "=5+5")
assert sheettest3.getCellValue("A3") == "10", "Cell function handles adding integers.\
     Expected 10 got: {}".format(sheettest3.getCellValue("A3"))

sheettest4 = Sheet()
sheettest4.setCellValue("A1", "5")
sheettest4.setCellValue("A2", "=A1+6")
assert sheettest4.getCellValue("A2") == "11", "Cell function handles adding\
    integers to cell refrence.\
    Expected 11 got: {}".format(sheettest4.getCellValue("A2"))

sheettest5 = Sheet()
sheettest5.setCellValue("A1", "7")
sheettest5.setCellValue("A2", "6")
sheettest5.setCellValue("A3", "= A1 + A2")
assert sheettest5.getCellValue("A3") == "13", "Cell function handles adding\
     cell reference to cell refrence. Expected 13 got: {}".format(
         sheettest5.getCellValue("A2"))

sheettest6 = Sheet()
sheettest6.setCellValue("A1", "5")
sheettest6.setCellValue("A2", "= A1")
sheettest6.setCellValue("A3", "= 5 + A2")
assert sheettest6.getCellValue("A3") == "10", "Cell function handles adding\
     nested cell references. Expected 10 got: {}".format(
         sheettest6.getCellValue("A3"))

sheettest7 = Sheet()
sheettest7.setCellValue("A1", "= 15 + 15")
assert sheettest7.getCellValue("A1") == "30", "Cell function handles adding\
     multidigit integers. Expected 30 got: {}".format(
         sheettest7.getCellValue("A1"))

# Modifying the same code will cause you to live with your decisions and see what makes it easy to change. 
# * What would it look like if you wanted to support subtraction? division, and multiplication? Would you handle precendence? Could you handle parens? 
# * What about other range functions like = SUM(A1:A3)
# * If I were to write a UI, when I setCellValue then I need to understand which other cells I need to getCellValue to update. 
#   Can you add to the interface a method which tells me which cells reference a cell address? Then I can getCellValue for each of these. 
# * How would you persist a spreadsheet to disk and load it back into memory? 
# * How would you display it, say a output a html file with a <table>? 
