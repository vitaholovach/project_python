class DataAdapter:
    def __init__(self, file_path):
        self.__file_path = file_path

    def from_txt_to_html(self):
        with open(self.__file_path, 'r') as file:
            lines = file.readlines()
        headers = lines[0].replace('\n', '').split(',')

        data = [item.replace('\n', '').split(',') for item in lines[1:]]
        result = ""
        for user_data in data:
            for index, value in zip(headers, user_data):
                result += f"<{index}>{value}</{index}>\n"
        return result


if __name__ == '__main__':
    html_data = DataAdapter("data.txt")
    html_file = html_data.from_txt_to_html()
    print(html_file)
