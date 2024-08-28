import sys

def get_last_tag(tags: list) -> str:
    """
    Returns the last tag found in all tags
    :param tags: list
    :return: string
    """
    for tag in tags:
        tag = tag.strip()
        if len(tag) == 0:
            continue
        trimmed = ".".join(tag.split(".")[:3])
        if tag == trimmed:
            return tag
    return ""

if __name__ == "__main__":
    data = []
    if len(sys.argv) == 2:
        data = sys.argv[1].split("\n")
    elif len(sys.argv) > 2:
        data = sys.argv[2:]
    output = get_last_tag(data)
    print(output)