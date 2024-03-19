
from tkinter import*
from tkinter import messagebox

app = Tk()
app.title("Symptom Survey")
app.geometry("600x800")
app.configure(bg="light blue")

q1rb = StringVar(value="0")

q1 = Label(app, text="Do you have a constantly runny/stuffy nose?",
           bg="light blue")
q1.pack()

q1r1 = Radiobutton(app, text="Yes", variable=q1rb,
                   value="Yes", bg="light blue")
q1r1.pack()
q1r2 = Radiobutton(app, text="No", variable=q1rb, value="no", bg="light blue")
q1r2.pack()

q2rb = StringVar(value="0")

q2 = Label(app, text="Do you have a dry/hoarse or constant cough?",
           bg="light blue")
q2.pack()
q2r1 = Radiobutton(app, text="Yes", variable=q2rb,
                   value="Yes", bg="light blue")
q2r1.pack()
q2r2 = Radiobutton(app, text="No", variable=q2rb, value="no", bg="light blue")
q2r2.pack()

q3rb = StringVar(value="0")

q3 = Label(app, text="Are you experiencing any post-nasal drip (where mucus drips down into your throat)?", bg="light blue")
q3.pack()
q3r1 = Radiobutton(app, text="Yes", variable=q3rb,
                   value="Yes", bg="light blue")
q3r1.pack()
q3r2 = Radiobutton(app, text="No", variable=q3rb, value="no", bg="light blue")
q3r2.pack()

q4rb = StringVar(value="0")

q4 = Label(app, text="Is your throat strep/sore?", bg="light blue")
q4.pack()
q4r1 = Radiobutton(app, text="Yes", variable=q4rb,
                   value="Yes", bg="light blue")
q4r1.pack()
q4r2 = Radiobutton(app, text="No", variable=q4rb, value="no", bg="light blue")
q4r2.pack()

q5rb = StringVar(value="0")

q5 = Label(
    app, text="Do you feel weak/exerted without doing anything?", bg="light blue")
q5.pack()
q5r1 = Radiobutton(app, text="Yes", variable=q5rb,
                   value="Yes", bg="light blue")
q5r1.pack()
q5r2 = Radiobutton(app, text="No", variable=q5rb, value="no", bg="light blue")
q5r2.pack()


def symptoms():
    symptom = 0
    if q1rb.get() == "Yes":
        symptom = symptom+5
        print(symptom)

    if q2rb.get() == "Yes":
        symptom = symptom+5
        print(symptom)

    if q3rb.get() == "Yes":
        symptom = symptom+5
        print(symptom)

    if q4rb.get() == "Yes":
        symptom = symptom+5
        print(symptom)

    if q5rb.get() == "Yes":
        symptom = symptom+5
        print(symptom)

    if symptom <= 10:
        messagebox.showinfo(
            "Report", "Use OTC medications or take a dose of Parcetamol if you feel any mild symptoms or weakness")

    elif symptom > 10 and symptom <= 20:
        messagebox.showinfo(
            "Report", "Use prescription drugs but contanct your physician before doing so. A visit to the doctor may not be nessecarry.")

    else:
        messagebox.showinfo("Report", "You may need to visit your doctor.")
submit = Button(app, text="Submit", bg="grey", command=symptoms)
submit.pack()

app.mainloop()
