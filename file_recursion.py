import os


def print_files(start_folder):

    # print('\n** Called print_files with', start_folder)

    # get the absolute path of this folder
    root_folder = os.path.abspath(start_folder)

    # loop through each item in the directory
    try:
        for item in os.listdir(root_folder):

            # compute the absolute path of each item
            abs_path = os.path.join(root_folder, item)

            # ask the os, is this item a file or a directory?
            if os.path.isfile(abs_path):
                pass
                # it is a file - therefore, base case!  stop the recursion
                # print("{:s} - {:d} bytes".format(abs_path, os.stat(abs_path).st_size))
            else:
                # it is a directory - therefore, continue with recursion
                # and go down one more level into the directory
                print_files(abs_path)
    except BaseException as e:
            print("Exception for this folder", root_folder,"Exception was", e.__class__.__name__, e) # e is the exception object (error message)
            return

def main():
    # set this path to something that doesn't have too many files!
    start_folder_name = "/Users/saradjebbari"
    print_files(start_folder_name)

main()