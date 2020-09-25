import csv

print("\nWriting test data delimited file...\n")

file_name = "EDW_SCIMS_2020-09-25.csv"
write_path = "/incoming/s_fsaedw_01/inbound/"
full_path = f"{write_path}/{file_name}"

with open(full_path, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=",")
    header = ["c1", "c2", "c3", "c4", "c5", "c6"]
    writer.writerow(header)
    for i in range(10):
        row = ["foo", "bar", "fizz", "buzz", "some value", "some other value"]
        writer.writerow(row)

print("Test data writing complete!\n")
