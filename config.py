

# general prefix dictionary
prefix_dict = {"C:":"",
               "D:":"/media/sda6",
               "O:":"smb://isgnashacluster.local/organisation",
               "P:":"smb://isgnashacluster.local/projekte",
               "T:":"smb://isgnashacluster.local/temp",
               "X:":"smb://isgnashacluster.local/externe",
               "H:":"smb://isgnashacluster.local/home"}



# custom prefix list (is needed for paths without win drives)
prefix_list = ["/media/sda6",
               "smb://isgnashacluster.local/organisation",
               "smb://isgnashacluster.local/projekte",
               "smb://isgnashacluster.local/temp",
               "smb://isgnashacluster.local/externe",
               "smb://isgnashacluster.local/home"]



# set "Use Prefix Dictionary" checkbox on startup
prefix_dict_checkbox_state = True

# set "Replace Spaces with %20" checkbox on startup
replace_spaces_checkbox_state = True

# setup preferred file browser
file_browser = "caja" #nautilus


