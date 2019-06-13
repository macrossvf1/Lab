from tkinter import *


def printDescription(*args):
    tool_details_TextBox.delete('1.0', END)
    tool_details_TextBox.insert(INSERT, 'Description:\n' + tool_description.get(choose_Tool.get()) + '\n\n')
    tool_details_TextBox.insert(INSERT, 'Location:\n' + tool_location.get(choose_Tool.get()) + '\n\n')
    tool_details_TextBox.insert(INSERT, 'Weight:\n' + tool_weight.get(choose_Tool.get()) + '\n\n')
    #tool_details_TextBox.insert(INSERT, 'Purchase Methods: ' + tool_purchase_methods(choose_Tool.get()))
    tool_details_TextBox.update()



list_of_tools = ['hammer',
                'wrench',
                'screwdriver']
tool_description = {
    'hammer': 'A tool with a heavy metal head mounted at right angles at the end of a handle, used for jobs such as breaking things and driving in nails.',
    'wrench': 'A wrench or spanner is a tool used to provide grip and mechanical advantage in applying torque to turn objects—usually rotary fasteners, such as nuts and bolts—or keep them from turning.',
    'screwdriver': 'A tool with a flattened, cross-shaped, or star-shaped tip that fits into the head of a screw to turn it.'
}

tool_location = {
    'hammer': 'shelf',
    'wrench': 'desk',
    'screwdriver': 'drawer'
}

tool_weight = {
    'hammer': '1',
    'wrench': '1',
    'screwdriver': '0.5'
}

tool_purchase_methods = {
    'hammer': ['Anonymous', 'Declared'],
    'wrench': ['Declared'],
    'screwdriver': ['Anonymous']
}

main_frame = Tk()
main_frame.title("Tool Box")

choose_Tool = StringVar()
choose_Tool.set("hammer")
choose_Tool.trace("w", printDescription)

dropDown = OptionMenu(main_frame, choose_Tool, *list_of_tools)
dropDown.pack()

tool_details_TextBox = Text()
tool_details_TextBox.pack()

main_frame.mainloop()
