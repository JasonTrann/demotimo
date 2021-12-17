import xlrd
from openpyxl import load_workbook


class ExcelUtil:

    def load_xlsx_sheet_to_dict(self, workbook_url, sheet_name):
        workbook_dict = {}

        if workbook_url is None:
            print('Error: file name is null or empty')
            return workbook_dict

        wb = load_workbook(workbook_url)

        print(wb.sheetnames)

        sheet = wb.get_sheet_by_name(sheet_name)
        columns = []
        r_count = 0
        rows = []

        for row in sheet.iter_rows():
            if r_count == 0:
                r_count += 1
                n_column = 0
                for cell in row:
                    if cell.value is None:
                        break
                    n_column += 1
                    columns.append(cell.value)
                continue

            r_count += 1
            cell_list = []
            n_column = 0
            for cell in row:
                if cell.value is None:
                    break
                n_column += 1
                cell_list.append(cell.value)
            if n_column > 0:
                rows.append(cell_list)

            if n_column == 0:
                break

        workbook_dict = self.make_json_from_data(columns, rows)

        return workbook_dict

    def make_json_from_data(self, column_names, row_data):
        """
        take column names and row info and merge into a single json object.
        :param row_data:
        :param column_names:
        :return:
        """
        row_list = []
        for item in row_data:
            json_obj = {}
            for i in range(0, column_names.__len__()):
                json_obj[column_names[i]] = item[i]
            row_list.append(json_obj)
        return row_list

    def xls_to_dict(self, workbook_url):
        """
        Convert the read xls file into JSON.
        :param workbook_url: Fully Qualified URL of the xls file to be read.
        :return: json representation of the workbook.
        """
        workbook_dict = {}

        if workbook_url is None:
            print('Error: file name is null or empty')
            return workbook_dict

        book = xlrd.open_workbook(workbook_url)
        sheets = book.sheets()

        for sheet in sheets:
            if sheet.name == 'PortHoles & Discrete Appurtenan':
                continue
            workbook_dict[sheet.name] = {}
            columns = sheet.row_values(0)
            rows = []
            for row_index in range(1, sheet.nrows):
                row = sheet.row_values(row_index)
                rows.append(row)
            sheet_data = self.make_json_from_data(columns, rows)
            workbook_dict[sheet.name] = sheet_data

        return workbook_dict

    def load_xls_sheet_to_dict(self, workbook_url, sheet_name):
        sheet_dict = {}

        workbook_dict = self.xls_to_dict(workbook_url)
        if workbook_dict is None:
            return sheet_dict

        return workbook_dict[sheet_name]

    def xls_to_list(self, workbook_url):
        """
        Convert the read xls file into JSON.
        :param workbook_url: Fully Qualified URL of the xls file to be read.
        :return: json representation of the workbook.
        """
        workbook_dict = {}

        if workbook_url is None:
            print('Error: file name is null or empty')
            return workbook_dict

        book = xlrd.open_workbook(workbook_url)
        sheets = book.sheets()

        for sheet in sheets:
            if sheet.name == 'PortHoles & Discrete Appurtenan':
                continue
            workbook_dict[sheet.name] = {}
            columns = sheet.row_values(0)
            rows = []
            for row_index in range(1, sheet.nrows):
                row = sheet.row_values(row_index)
                rows.append(row)
            # sheet_data = self.make_json_from_data(columns, rows)
            workbook_dict[sheet.name] = rows

        return workbook_dict

    def load_xls_sheet_to_list(self, workbook_url, sheet_name):
        sheet_dict = {}

        workbook_dict = self.xls_to_list(workbook_url)
        if workbook_dict is None:
            return sheet_dict

        return workbook_dict[sheet_name]
