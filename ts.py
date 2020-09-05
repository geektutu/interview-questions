import sys

def main(filename):
    if not filename.endswith(".bak"):
        raise "need a backup file"
    print(filename)
    s = ""
    with open(filename) as f:
        end = False
        for line in f:
            if line.startswith("## "):
                if end:
                    s += "\n</div>\n</details>\n\n"
                    end = False
                s += line
                print(line.replace("##", "-"), end="")
                s += "\n<details>\n<summary>答案</summary>\n<div>\n"
                end = True
            else:
                s += line
        s += "\n</div>\n</details>\n\n"
    

    with open(filename.strip(".bak"), "w") as f:
        f.write(s)


main(sys.argv[1])