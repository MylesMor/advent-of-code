import timeit

class Directory():
    def __init__(self, name):
        self.name = name
        self.parent_directory = None
        self.directories = {}
        self.files = {}
    
    def size(self):
        return sum(self.files.values()) + sum([directory.size() for directory in self.directories.values()])

    def __list(self, dir_list):
        dir_list.append({self.name: self.size()})
        for directory in self.directories.values():
            directory.__list(dir_list)
        return dir_list

    def list_dirs(self):
        return self.__list([])

    def add_directory(self, name):
        new_directory = Directory(name)
        new_directory.parent_directory = self
        self.directories[name] = new_directory
        return new_directory

    def add_files(self, files):
        for name, size in files.items():
            self.files[name] = size

    def cd(self, name):
        if isinstance(name, str):
            parts = name.split("/")
        else:
            parts = name
        if len(parts) == 0 or parts[0] == "":
            return self
        elif parts[0] == "..":
            return self.parent_directory.cd(parts[1:])
        else:
            return self.directories[parts[0]].cd(parts[1:])

    def get_root_directory(self):
        if self.parent_directory != None:
            return self.parent_directory.get_root_directory()
        return self



def build_filesystem(filename):
    lines = []
    root_dir = Directory("/")
    current_dir = Directory("/") 
    with open(filename, "r") as file:
        lines = [line.strip() for line in file]
        for x in range(0, len(lines)):
            line = lines[x]
            if line.startswith("$"):
                if "cd" in line:
                    cd_to = line.split("$ cd ")[1]
                    current_dir = current_dir.cd(cd_to)
                elif 'ls' in line:
                    for ls_line in lines[x+1:]:
                        if not ls_line.startswith("$"):
                            if "dir" in ls_line:
                                current_dir.add_directory(ls_line.split('dir ')[1])
                            else:
                                parts = ls_line.split(" ")
                                current_dir.add_files({parts[1]: int(parts[0])})
                        else:
                            break
    return current_dir.get_root_directory()


def get_directories(root):
    total_size = 0
    for item in root.list_dirs():
        size = list(item.values())[0]
        if size <= 100000:
            total_size += size
    return total_size

def free_up_space(root):
    unused_space = 70000000 - root.size()
    required_space = 30000000 - unused_space
    deletion_candidates = []
    for item in root.list_dirs():
        size = list(item.values())[0]
        if size >= required_space:
            deletion_candidates.append(size)
    return min(deletion_candidates)



if __name__ == "__main__":

    test_root = build_filesystem("test_input.txt")
    assert get_directories(test_root) == 95437
    assert free_up_space(test_root) == 24933642

    start_time = timeit.default_timer()
    root = build_filesystem("input.txt")
    print(f'Challenge 1 Answer: {get_directories(root)}')
    print(f'Challenge 2 Answer: {free_up_space(root)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
