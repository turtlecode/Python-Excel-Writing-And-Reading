from openpyxl import Workbook

data = {
  "Ronaldo": {
    "Goals":815,
    "Games":1120
  },
  "Bican": {
    "Goals":805,
    "Games":530
  },
  "Romario": {
    "Goals":772,
    "Games":961
  },
  "Messi": {
    "Goals":769,
    "Games":973
  },
}

wb = Workbook()
ws = wb.active
ws.title = "Top Scorers"

headings = ['Name'] + list(data['Ronaldo'].keys())
ws.append(headings)

for person in data:
  scorers = list(data[person].values())
  ws.append([person] + scorers)

wb.save("excel.xlsx")