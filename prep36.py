def get_ok_items(carryon,personal,restricted):
    ''''''

    chk_lst = []
    restrict_lst = []

    for item in carryon:
        chk_lst.append(item)

    for other_item in personal:
        chk_lst.append(other_item)

    for bad_item in restricted:
        restrict_lst.append(bad_item)

    for i in range(len(chk_lst)):
        for thing in chk_lst:
            if thing in restrict_lst:
                chk_lst.remove(thing)


    return chk_lst


'''def main():
    ''''''
    restricted = {'tnt','gun','knife','razor'}
    carryon = {'tnt', 'gun', 'clothes'}
    personal = {'tnt', 'gun', 'knife','razor'}
    result = get_ok_items(carryon, personal, restricted)


main()'''