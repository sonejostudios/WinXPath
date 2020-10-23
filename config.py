

# general prefix dictionary
prefix_dict = {"C:":"",
               "D:":"/media/sda6",
               "O:":"smb://isgnashacluster.local/organisation",
               "H:":"smb://isgnashacluster.local/home"}



# custom prefix list (is needed for paths without win drives)
prefix_list = ["/media/sda6",
               "smb://isgnashacluster.local/organisation",
               "smb://isgnashacluster.local/home"]



# set "Use Prefix Dictionary" checkbox on startup
prefix_dict_checkbox_state = True

# set "Replace Spaces with %20" checkbox on startup
replace_spaces_checkbox_state = True

# setup preferred file browser
file_browser = "caja" #nautilus


