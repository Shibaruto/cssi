Person = {
"name": {
"first": "Jermaine",
"middle": "N",
"last": "Reid"
}
}

print Person["name"]["first"]
print "{2},{0},{1}".format(Person["name"]["first"], Person["name"]["middle"], Person["name"]["last"])
