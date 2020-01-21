class Solution:
    def removeSubfolders(self, folder):

        roots = ['0']
        for fd in sorted(folder):
            #examine if starts with the same character
            if not fd.startswith(roots[-1] + '/'):
                roots.append(fd)
        return roots[1:]
