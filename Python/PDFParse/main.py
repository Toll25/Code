from prettytable import PrettyTable
from pypdf import PdfReader

if __name__ == '__main__':
    readers = []
    readers.append(PdfReader('Veltlinerman/1.Veltlinerman-2005.pdf'))
    readers.append(PdfReader('Veltlinerman/2.Veltlinerman-2006.pdf'))
    readers.append(PdfReader('Veltlinerman/3.Veltlinerman-2007.pdf'))
    readers.append(PdfReader('Veltlinerman/4.Veltlinerman-2008.pdf'))
    readers.append(PdfReader('Veltlinerman/5.Veltlinerman-2009.pdf'))
    readers.append(PdfReader('Veltlinerman/6.Veltlinerman-2010.pdf'))
    readers.append(PdfReader('Veltlinerman/7.Veltlinerman-2011.pdf'))
    readers.append(PdfReader('Veltlinerman/8.Veltlinerman-2012.pdf'))
    readers.append(PdfReader('Veltlinerman/9.Veltlinerman_2013.pdf'))
    readers.append(PdfReader('Veltlinerman/10.Veltlinerman_2014.pdf'))
    readers.append(PdfReader('Veltlinerman/11.Veltlinerman_2015.pdf'))
    readers.append(PdfReader('Veltlinerman/12.Veltlinerman_2016.pdf'))
    readers.append(PdfReader('Veltlinerman/13.Veltlinerman_2017.pdf'))
    readers.append(PdfReader('Veltlinerman/14.Veltlinerman_2018.pdf'))
    readers.append(PdfReader('Veltlinerman/15.Veltlinerman_2019.pdf'))
    readers.append(PdfReader('Veltlinerman/16.Veltlinerman_2020.pdf'))
    readers.append(PdfReader('Veltlinerman/17.Veltlinerman_2021.pdf'))
    readers.append(PdfReader('Veltlinerman/18.Veltinerman-2022.pdf'))

    for index, reader in enumerate(readers):
        file = open(str(index+1)+".txt", "w+")
        for page in reader.pages:
            text = page.extract_text()
            for line in text.split('\n'):
                file.write(line)
                file.write("\n")
# page = reader.pages[0]
# text = page.extract_text()
#
# table = PrettyTable()
# lines = []
# for line in text.split('\n'):
#     lines.append(line.split()[:10])
#
# table.add_rows(lines)
# print(text)
# print(table)
