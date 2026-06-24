from PIL import Image, ImageDraw,ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader 
import csv

FONT_FILE =r"C:\certificate genrator\font\RobotoCondensed-Italic-VariableFont_wght.ttf"
FONT_COLOR = "#09023F"

template = Image.open(r"template.jpeg")
WIDTH , HEIGHT = template.size

def make_certificates(name, course, date):
        
        image_source = Image.open(r'template.jpeg')
        draw = ImageDraw.Draw(image_source)

        try:

                font_name = ImageFont.truetype(FONT_FILE ,55)
                font_course = ImageFont.truetype(FONT_FILE ,40)
                font_date = ImageFont.truetype(FONT_FILE ,26)
        except IOError:
                font_name = font_course = font_date = ImageFont.load_default()

        name_bbox = draw.textbbox((0,0) , name , font=font_name)
        name_width = name_bbox[2] - name_bbox[0]

        course_bbox = draw.textbbox((0,0), course , font=font_course)
        course_width = course_bbox[2] - course_bbox[0]

        date_bbox = draw.textbbox((0,0) , date , font=font_date)
        date_width = date_bbox[2] - date_bbox[0] 

        
        x_name = (WIDTH - name_width ) / 2
        y_name = HEIGHT * 0.36
        draw.text((x_name,y_name), name ,fill=FONT_COLOR, font=font_name)


        x_course = (WIDTH - course_width) / 2
        y_course = HEIGHT * 0.49
        draw.text((x_course,y_course), course, fill=FONT_COLOR, font=font_course)

        x_date = WIDTH * 0.58 
        y_date = HEIGHT * 0.653
        draw.text((x_date,y_date), date, fill=FONT_COLOR, font=font_date)

        image_path ="./out/" +name+ ".png"
        image_source.save(image_path)

        output_filename = "./pdf/" +name+ ".pdf"
       
        pdf_canvas = canvas.Canvas(output_filename,pagesize=letter)

        pdf_canvas.drawImage(ImageReader(image_source), 0, 0, width=612, height=792)
        
        pdf_canvas.save()

        print(f"certificate successfully genrated: {name}")

if __name__  == "__main__":
         with open("name.csv","r" , encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                        if len(row) >= 3:
                                name_val= row[0].strip()
                                course_val = row[1].strip()
                                date_val = row[2].strip()

                                make_certificates(name_val,course_val,date_val)




    
    