from pulp import LpProblem, LpVariable, LpMaximize, value
from colorama import Fore, Style, init
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
import os

init(autoreset=True)

model = LpProblem("Maximization_of_beverage_production", LpMaximize)
lemonade = LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

model += 2 * lemonade + 1 * fruit_juice >= 100, "WaterLimit"
model += lemonade <= 50, "SugarLimit"
model += lemonade <= 30, "LemonJuiceLimit"
model += 2 * fruit_juice <= 40, "FruitPureeLimit"
model += lemonade + fruit_juice, "TotalProducts"

model.solve()

max_products = int(value(lemonade) + value(fruit_juice))
lemonade_qty = int(value(lemonade))
fruit_juice_qty = int(value(fruit_juice))

print(Fore.GREEN + Style.BRIGHT + f"Максимальна кількість продуктів: {max_products}")
print(Fore.CYAN + f"Лимонад: {lemonade_qty}")
print(Fore.MAGENTA + f"Фруктовий сік: {fruit_juice_qty}")

plt.figure(figsize=(6, 4))
plt.bar(["Лимонад", "Фруктовий сік"], [lemonade_qty, fruit_juice_qty], color=['orange', 'purple'])
plt.title("Кількість вироблених напоїв")
plt.ylabel("Одиниці")
chart_file = "production_chart.png"
plt.savefig(chart_file)
plt.close()

pdf_file = "production_results.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)
c.setFont("Helvetica-Bold", 16)
c.drawString(100, 750, "Production Optimization Results")
c.setFont("Helvetica", 12)
c.drawString(100, 700, f"Maximum number of products: {max_products}")
c.drawString(100, 680, f"Lemonade: {lemonade_qty}")
c.drawString(100, 660, f"Fruit Juice: {fruit_juice_qty}")
c.drawImage(chart_file, 100, 400, width=300, height=200)
c.save()

try:
    if os.name == 'nt':
        os.startfile(pdf_file)
    elif os.name == 'posix':
        os.system(f"open {pdf_file}")
except Exception as e:
    print(Fore.RED + f"He вдалося автоматично відкрити PDF: {e}")

print(Fore.YELLOW + f"Результати збережено y {pdf_file} та графік y {chart_file}")
