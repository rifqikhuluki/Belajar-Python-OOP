from dearpygui.dearpygui import *

create_context()

def say_hello():
    set_value("label", "Hello World!")

with window(label="Hello World App"):
    add_text("Tekan tombol", tag="label")
    add_button(label="Click Me", callback=say_hello)

create_viewport(title="Dear PyGui Hello World", width=300, height=150)
setup_dearpygui()
show_viewport()
start_dearpygui()
destroy_context()
