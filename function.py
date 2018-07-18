#delete
text.capitalize() # ตัวแรกใหญ่หลังเล็ก
text.strip() #deleteลบช่องว่าง
text.lstrip() #delete L
text.rtrip() #
text.strip('p') #ลด p ทั้งหมดในtext

#check
text.isalpha() #str check
text.isdigit() #ตัวเลข check
text.isnumberic() #
text.find() #หาตำแหน่ง only str
text.count()#หาว่ามีกี่ตัว only for list
text.islanum() #checkว่าเป็นตัวstrกับเลขหรือเปล่า
text.isupper() #ตัวพิมใหญ่เช็ค
text.islower() #พิมเล็กเช็ค
    #positoin
text.center() #position of text
text.replace() #replace some position what ever u want

    #list
text.append("sometext") #การเพิ่มค่าเข้าไปในlist
text[เลขคำที่จะแทน] = "ชื่อที่จะเขียนแทน"
text.remove("สิ่งที่จะลบในlist") # delete something in list
text.pop(postion)  #delete
text.insert(1, "ant") #เพิ่มค่าแบบกำหนดตำแหน่ง
text.index() # find position in list
text.sort() # จัดค่าให้เป็นระเบียบในlist if it's num = น้อยไปมาก
sorted() # same sort but bult in function
text.sort(revers=True) # เรียงจากมากไปน้อย
text.sort(revers=False, key=len) #เรียงจากมากไปน้อย
text.split() #ทำค่าธรรมดาให้เป๋นlist เช่น str only
1, 2, 3 กลายเป็น[1,2 ,3 ]
text = "-".join(text) #ใส่เครื่องหมายเพื่อเชื่อมข้อความ
A-B-C-D
sum() # เอาค่าในlistมา+กัน










