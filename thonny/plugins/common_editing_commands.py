# -*- coding: utf-8 -*-

def load_plugin(workbench):
    def create_edit_command_handler(virtual_event_sequence):
        def handler():
            widget = workbench.focus_get()
            if widget:
                return widget.event_generate(virtual_event_sequence)
        
        return handler
    
    workbench.add_separator("edit")
    
    workbench.add_command("undo", "edit", "Undo",
        create_edit_command_handler("<<Undo>>"),
        tester=None, # TODO:
        default_sequence="<Control-z>",
        skip_sequence_binding=True)
    
    workbench.add_command("redo", "edit", "Redo",
        create_edit_command_handler("<<Redo>>"),
        tester=None, # TODO:
        default_sequence="<Control-y>",
        skip_sequence_binding=True)
    
    workbench.add_separator("edit")
    
    workbench.add_command("Cut", "edit", "Cut",
        create_edit_command_handler("<<Cut>>"),
        tester=None, # TODO:
        default_sequence="<Control-x>",
        skip_sequence_binding=True)
    
    workbench.add_command("Copy", "edit", "Copy",
        create_edit_command_handler("<<Copy>>"),
        tester=None, # TODO:
        default_sequence="<Control-c>",
        skip_sequence_binding=True)
    
    workbench.add_command("Paste", "edit", "Paste",
        create_edit_command_handler("<<Paste>>"),
        tester=None, # TODO:
        default_sequence="<Control-v>",
        skip_sequence_binding=True)
    
    workbench.add_command("SelectAll", "edit", "Select all",
        create_edit_command_handler("<<SelectAll>>"),
        tester=None, # TODO:
        default_sequence="<Control-a>",
        skip_sequence_binding=True)
    
