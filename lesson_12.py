class File_:
    def __init__(self, file_name):
        self.filename = file_name

    def get_rows(self):
        if self.filename:
            with open(self.filename, "r") as file:
                return file.read().split("\n")

    def get_domains(self):
        self.domains = list(map(lambda row: row[1:], self.get_rows()))

    def get_surnames(self):
        return list(map(lambda row: row.split("\t")[1], self.get_rows()))

    def get_dates(self):
        dates = []
        for row in self.get_rows():
            if "-" in row:
                dates.append({"date": row.split("-")[0].strip()})
        return dates


f1 = File_("domains.txt")

f1.get_domains()
print(f1.domains)

f1 = File_("names.txt")

print(f1.get_surnames())

f1 = File_("authors.txt")

print(f1.get_dates())