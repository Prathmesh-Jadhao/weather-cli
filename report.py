from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from typing import List,Dict

def create_pdf(weather_data: List[Dict], filename: str = "weather_report.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    table_data = [["City", "Temp (°C)", "Humidity (%)", "Description"]]
    
    for data in weather_data:
        table_data.append([
            data["city"],
            data["temp"],
            data["humidity"],
            data["description"].title()
        ])
    
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.darkblue),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTSIZE', (0,0), (-1,0), 14),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.lightgrey, colors.white])
    ]))
    
    doc.build([table])