import logging


def load_fasta():
    with open("data_input/input.txt", "r", encoding="utf8") as file_obj:
        file_lines = file_obj.read().splitlines()

    if not file_lines:
        raise ValueError("File is empty")

    records = {}
    header_found = False

    for i in range(len(file_lines)):

        if file_lines[i] == "":
            continue

        elif file_lines[i].startswith(">"):

            header = file_lines[i][1:]
            parts = header.split(maxsplit=1)

            record_id = parts[0]

            if len(parts) > 1:
                description = parts[1]
            else:
                description = ""

            if record_id in records:
                logging.warning("Duplicate ID: " + record_id)
            else:
                header_found = True
                sequence = ""

                for j in range(i + 1, len(file_lines)):

                    if file_lines[j].startswith(">"):
                        break

                    if file_lines[j] == "":
                        continue

                    sequence += file_lines[j].upper()

                if sequence == "":
                    raise ValueError("Header has no sequence")

                records[record_id] = {
                    "description": description,
                    "sequence": sequence,
                }

        elif not header_found:
            raise ValueError("Sequence before header")

    return records

result = load_fasta()
print(result)
