import subprocess
#subprocess.call(["python"])

proxy = ""
package = []

while True:
    print("Choose what to do? \n 1.Add package to install \n 2.Install packages \n 3.Set different proxy \n 4.Exit ")
    x = input()
    if x == 1:
        while True:
            print("Choose what to do? \n 1.Add new package \n 2.View list of queued packages \n 3.Delete certain package \n 4.Exit Loop")
            y = input()
            if y == 1:
                print("Input package name \n")
                newPackage = raw_input()
                package.append(newPackage)
            elif y == 2:
                counter = 1

                for pack in package:
                    print(str(counter) + " :" + pack)
                    counter += 1
            elif y == 3:
                print("Which package you want to dele1te ? \n")
                counter = 1

                for pack in package:
                    print(str(counter)+" :"+pack)
                    counter += 1
                delete = input();
                val = package.pop(delete-1)
                print("Package named: " + val + " was deleted.\n")

            elif y == 4:
                break

    elif x == 2:
        for pack in package:
            subprocess.call("pip install --proxy "+proxy+" "+pack)
    elif x == 3:
        proxy = raw_input()
        print("Your new Proxy: "+proxy)
    elif x == 4:
        break
