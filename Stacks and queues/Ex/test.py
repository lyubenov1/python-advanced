def split_names_into_rows(name_list, modulus=3):
    for index, name in enumerate(name_list, start=1):
        print(f"{name:-^15} ", end="")
        if index % modulus == 0:
            print()
    print()


names = ["Picard", "Riker", "Troi", "Crusher", "Worf", "Data", "La Forge"]
split_names_into_rows(names)
