def main():
    def formatted_numbers():
        beautiful_table_lines = ["|{:^10}|{:^10}|{:^10}|".format('decimal', 'hex', 'binary')]
        for num in range(16):
            beautiful_table_lines.append(
                "|{:<10d}|{:^10x}|{:>10b}|".format(num, num, num))
        return beautiful_table_lines


    for el in formatted_numbers():
        print(el)        

if __name__ == '__main__':
    main()
