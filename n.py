from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Example Table")
table.add_column("Column 1", style="bold")
table.add_column("Column 2")
table.add_row("Value 1", "Value 2")
table.add_row("Value 3", "Value 4")

console.print(table)