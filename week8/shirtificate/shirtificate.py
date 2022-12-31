from fpdf import FPDF


class PDF(FPDF):
    def compose_shirt(self):
        self.set_auto_page_break(False)
        self.add_page()
        self.image("shirtificate.png", x=10, y=65, w=190, h=190)
        self.set_font("helvetica", "B", 50)
        self.cell(190, 50, "CS50 Shirtificate", new_x="LMARGIN", new_y="TOP", align="C")

    def set_name(self, name):
        self.set_font("helvetica", "B", 25)
        self.set_text_color(255, 255, 255)
        self.cell(190, 240, f"{name} took CS50", align="C")

    def save(self, text_name):
        self.output(text_name)


def main():
    pdf = PDF()
    pdf.compose_shirt()
    name = input("Name: ")
    pdf.set_name(name)
    pdf.save("shirtificate.pdf")


if __name__ == "__main__":
    main()
