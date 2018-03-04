from prettytable import PrettyTable

table = PrettyTable(["animal", "ferocity", "check"])
table.add_row(["wolverine", 100, 3])
table.add_row(["grizzly", 87, 5])
table.add_row(["Rabbit of Caerbannog", 110, 8])
table.add_row(["cat", -1, 0])
table.add_row(["platypus", 23, 119])
table.add_row(["dolphin", 63, 75])
table.add_row(["albatross", 44, 100])
table.sort_key("ferocity")
table.reversesort = True

print table