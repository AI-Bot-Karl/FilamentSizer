self.l2 = tk.Label(self.master, text="Detector scripts:")
self.l2.grid(row=2, column=0)


# treeview

# treeview_columns = ['Use', 'Name']
# self.decoder_list = []
# for x in range(10):
#     self.decoder_list.append([True, 'decoder'+str(x)])


# container = ttk.Frame(self.master)
# container.grid(row=3, column=0)
#
# self.tree1 = ttk.Treeview(columns= treeview_columns, show="headings" )
# vsb = ttk.Scrollbar(orient="vertical",
#                     command=self.tree1.yview)
# hsb = ttk.Scrollbar(orient="horizontal",
#                     command=self.tree1.xview)
# self.tree1.configure(yscrollcommand=vsb.set,
#                     xscrollcommand=hsb.set)
# self.tree1.grid(column=0, row=0, sticky='nsew', in_=container)
# vsb.grid(column=1, row=0, sticky='ns', in_=container)
# hsb.grid(column=0, row=1, sticky='ew', in_=container)
# container.grid_columnconfigure(0, weight=1)
# container.grid_rowconfigure(0, weight=1)


# container2 = ttk.Frame(self.master)
# container2.grid(row=4, column=0)
#
# self.tree2 = ttkwidgets.CheckboxTreeview(columns= treeview_columns, show="headings" )
# vsb2 = ttk.Scrollbar(orient="vertical",
#                     command=self.tree2.yview)
# hsb2 = ttk.Scrollbar(orient="horizontal",
#                     command=self.tree2.xview)
# self.tree2.configure(yscrollcommand=vsb2.set,
#                      xscrollcommand=hsb2.set)
# self.tree2.grid(column=0, row=0, sticky='nsew', in_=container2)
# vsb2.grid(column=1, row=0, sticky='ns', in_=container2)
# hsb2.grid(column=0, row=1, sticky='ew', in_=container2)
# container2.grid_columnconfigure(0, weight=1)
# container2.grid_rowconfigure(0, weight=1)


# for col in treeview_columns:
#     self.tree1.heading(col, text=col.title(),
#     command=lambda c=col: sortby(self.tree1, c, 0))
#     # adjust the column's width to the header string
#     self.tree1.column(col,
#         width=tkFont.Font().measure(col.title()))
#
# for item in self.decoder_list:
#     self.tree1.insert('', 'end', values=item)
#     # adjust column's width if necessary to fit each value
#     for ix, val in enumerate(item):
#         col_w = tkFont.Font().measure(val)
#         if self.tree1.column(treeview_columns[ix],width=None)<col_w:
#             self.tree1.column(treeview_columns[ix], width=col_w)




# for col in treeview_columns:
#     self.tree2.heading(col, text=col.title(),
#     command=lambda c=col: sortby(self.tree2, c, 0))
#     # adjust the column's width to the header string
#     self.tree2.column(col,
#         width=tkFont.Font().measure(col.title()))
#
# for item in self.decoder_list:
#     self.tree2.insert('', 'end', values=item)
#     # adjust column's width if necessary to fit each value
#     for ix, val in enumerate(item):
#         col_w = tkFont.Font().measure(val)
#         if self.tree2.column(treeview_columns[ix],width=None)<col_w:
#             self.tree2.column(treeview_columns[ix], width=col_w)
#
# def sortby(tree, col, descending):
#     """sort tree contents when a column header is clicked on"""
#     # grab values to sort
#     data = [(tree.set(child, col), child) \
#             for child in tree.get_children('')]
#     # if the data to be sorted is numeric change to float
#     # data =  change_numeric(data)
#     # now sort the data in place
#     data.sort(reverse=descending)
#     for ix, item in enumerate(data):
#         tree.move(item[1], '', ix)
#     # switch the heading so it will sort in the opposite direction
#     tree.heading(col, command=lambda col=col: sortby(tree, col, \
#                                                      int(not descending)))

