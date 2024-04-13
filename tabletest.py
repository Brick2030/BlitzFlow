from prettytable import PrettyTable

myTab = PrettyTable(['Student Name', 'Class', 'Section'])
myTab.add_row(['Mike','10th','A'])
myTab.align = "r"
print(myTab)