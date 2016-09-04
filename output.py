__author__ = 'yzh'
class htmloutput(object):
    def __init__(self):
        self.date=[]

    def collect(self,date):
        if date is None:
            return
        self.date.append(date)

    def output(self):
        fout=open("output.html",'w')
        fout.write("<!DOCTYPE html>")
        fout.write("<html>")
        fout.write("<meta charset=\"UTF-8\">")
        fout.write("<body>")
        fout.write("<table>")
        for date in self.date:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%date['url'])
            fout.write("<td>%s</td>"%date ['tittle'])
            fout.write("<td>%s</td>"%date['summy'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")