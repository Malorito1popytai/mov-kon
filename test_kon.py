from simple_term_menu import TerminalMenu

main_menu_title = " Main Menu.\n Press Q or Esc to quit.\n"
main_menu_items = ["Edit Menu", "Second Item", "Third Item", "Quit"]
main_menu_cursor = "> "
main_menu_cursor_style = ("fg_red", "bold")
main_menu_style = ("bg_red", "fg_yellow")
main_menu = TerminalMenu(
    menu_entries=main_menu_items,
    title=main_menu_title,
    menu_cursor=main_menu_cursor,
    menu_cursor_style=main_menu_cursor_style,
    menu_highlight_style=main_menu_style,
    cycle_cursor=True,
    clear_screen=True
)
main_menu.show()