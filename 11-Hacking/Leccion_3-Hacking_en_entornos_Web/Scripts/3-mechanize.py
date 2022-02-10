import mechanize

br = mechanize.Browser()
br.open("https://www.google.com/")
for form in br.forms():
	form.find_control("hl").readonly = False
	br.select_form(nr=0)
	br.form["hl"] = "Edited"
	print(form)
br.submit()
