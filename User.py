class User:
    def parsefile(self, path):
        file = open(path, 'r')
        d = file.read()
        users = d.split(';')
        users_new = []
        for i in users:
            b = i.split(',')
            f = {}
            for j in b:
                c = j.split(':')
                if c[0] == 'pin' or c[0] == 'summa':
                    f[c[0]] = int(c[1])
                else:
                    f[c[0]] = c[1]
            users_new.append(f)
        file.close()
        return users_new