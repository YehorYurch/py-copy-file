def copy_file(command) -> None:
    split_command = command.split()
    if len(split_command) != 3 or split_command[1] == split_command[2] or "cp" not in split_command:
        return
    try:
        with open(split_command[1], "r") as f1, open(split_command[2], "w") as f2:
            info_to_copy = f1.read()
            f2.write(info_to_copy)
    except FileNotFoundError:
        print(f"File {split_command[1]} not found.")