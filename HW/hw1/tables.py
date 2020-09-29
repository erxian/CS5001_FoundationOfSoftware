'''
Zengping Xu
CS 5001, Fall 2020

This program gets input from the designer about the ingredients of table and 
calculate the number of table the robot can make.

Examples:
7 tops, 28 legs, 63 screws => 7 tables assembled. Leftover parts: 0 table tops, 0 legs, 7 screws. 
16 tops, 49 legs, 86 screws => 10 tables assembled. Leftover parts: 6 table tops, 9 legs, 6 screws. 
5 tops, 32 legs, 19 screws => 2 tables assembled. Leftover parts: 3 table tops, 24 legs, 3 screws. 
'''


def main():
    tops = int(input("Number of tops: "))
    legs = int(input("Number of legs: "))
    screws = int(input("Number of screws: "))

    assemble_table_by_tops = tops // 1
    assemble_table_by_legs = legs // 4
    assemble_table_by_screws = screws // 8

    table_amount = min(assemble_table_by_tops, assemble_table_by_legs, assemble_table_by_screws)

    top_remains = tops - table_amount * 1
    leg_remains = legs - table_amount * 4
    screw_remain = screws - table_amount * 8

    top_remains_with_unit = str(top_remains) + " tops,"
    leg_remains_with_unit = str(leg_remains) + " legs,"
    screw_remain_with_unit = str(screw_remain) + " screws."
    
    print(str(table_amount) + " tables assembled.", "Leftover parts:", top_remains_with_unit, leg_remains_with_unit, screw_remain_with_unit)


if __name__ == "__main__":
    main()
