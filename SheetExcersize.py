import re

class Sheet:
    def __init__(self):
        self.sheet = {}

    def setCellValue (self,cell, input):
        self.sheet[cell] = input

    def getCellValue (self, cell):
        cellInput = self.sheet[cell]
        cellValue = None
        cellValuesArray = []
        if cellInput.startswith("="):
            matchCells = re.findall(r"(?P<cell>[A-z]+\d+)|(?P<operator>\+)|(?P<number>\d+)", cellInput)
            #print("Match= ", matchCells)
            for matchCell, matchOperator, matchNumber in matchCells:
                #print(matchCell, matchOperator, matchNumber)
                if matchCell:
                    cellValue = self.sheet[matchCell]
                    cellValuesArray += self.sheet[matchCell]
                if matchOperator:
                    cellValuesArray += matchOperator
                if matchNumber:
                    cellValue = matchNumber
                    cellValuesArray += matchNumber
        else:
            cellValue = cellInput

        if "+" in cellValuesArray:
            sumTotal = 0
            for item in cellValuesArray:
                if re.match(r"\d",item):
                    sumTotal += int(item)
            cellValue = str(sumTotal)

        return cellValue
    


# Tests

sheettest = Sheet()
sheettest.setCellValue("A1", "5")
print("Expected 5 got:", sheettest.getCellValue("A1"))
assert sheettest.getCellValue("A1") == "5", "Get cell simple value"

sheettest1 = Sheet()
sheettest1.setCellValue("A1", "5")
sheettest1.setCellValue("A2", "= A1")
print("Expected 5 got:", sheettest1.getCellValue("A2"))
assert sheettest1.getCellValue("A2") == "5", "Cell reference give value"

sheettest2 = Sheet()
sheettest2.setCellValue("A3", "=5")
print("Expected 5 got:", sheettest2.getCellValue("A3"))
assert sheettest2.getCellValue("A3") == "5", "Cell function handles integer"

sheettest3 = Sheet()
sheettest3.setCellValue("A3", "=5+5")
print("Expected 10 got:", sheettest3.getCellValue("A3"))
assert sheettest3.getCellValue("A3") == "10", "Cell function handles adding integers"

sheettest4 = Sheet()
sheettest4.setCellValue("A1", "5")
sheettest4.setCellValue("A2", "=A1+6")
print("Expected 10 got:", sheettest4.getCellValue("A2"))
assert sheettest4.getCellValue("A2") == "11", "Cell function handles adding integers to cell refrence"

sheettest5 = Sheet()
sheettest5.setCellValue("A1", "7")
sheettest5.setCellValue("A2", "6")
sheettest5.setCellValue("A3", "= A1 + A2")
print("Expected 13 got:", sheettest5.getCellValue("A3"))
assert sheettest5.getCellValue("A3") == "13", "Cell function handles adding cell reference to cell refrence"

sheettest6 = Sheet()
sheettest6.setCellValue("A1", "5")
sheettest6.setCellValue("A2", "= A1")
sheettest6.setCellValue("A3", "= 5 + A2")
print("Expected 10 got:", sheettest6.getCellValue("A3"))
assert sheettest6.getCellValue("A3") == "10", "Cell function handles adding nested cell references"
