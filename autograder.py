import os
import subprocess

def partfour():
    compilation = subprocess.run("make clean",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if compilation.returncode != 0:
       print("make clean failed")
       print(compilation.stderr.decode())
       return
    print("make clean - success")
    compilation = subprocess.run("make fourth",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if compilation.returncode != 0:
       print("make fourth")
       print(compilation.stderr.decode())
       return
    print("make fourth - success")
    # testing program
    testcases = subprocess.run("./fourth ../../testcases/fourth/input/input1.txt &> ../../testcases/fourth/output/output1.txt", shell=True)
    testcases = subprocess.run("./fourth ../../testcases/fourth/input/input2.txt &> ../../testcases/fourth/output/output2.txt", shell=True)
    testcases = subprocess.run("./fourth ../../testcases/fourth/input/input3.txt &> ../../testcases/fourth/output/output3.txt", shell=True)
    testcases = subprocess.run("./fourth ../../testcases/fourth/input/input4.txt &> ../../testcases/fourth/output/output4.txt", shell=True)
    testcases = subprocess.run("./fourth ../../testcases/fourth/input/input5.txt &> ../../testcases/fourth/output/output5.txt", shell=True)
    testcases = subprocess.run("./fourth ../../testcases/fourth/input/input6.txt &> ../../testcases/fourth/output/output6.txt", shell=True)

    compare = subprocess.run("diff ../../testcases/fourth/expected_output/expected1.txt ../../testcases/fourth/output/output1.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 1 - failed ✗")
    else:
        print("Testcase 1 - passed ✓")
    compare = subprocess.run("diff ../../testcases/fourth/expected_output/expected2.txt ../../testcases/fourth/output/output2.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 2 - failed ✗")
    else:
        print("Testcase 2 - passed ✓")
    compare = subprocess.run("diff ../../testcases/fourth/expected_output/expected3.txt ../../testcases/fourth/output/output3.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 3 - failed ✗")
    else:
        print("Testcase 3 - passed ✓")
    compare = subprocess.run("diff ../../testcases/fourth/expected_output/expected4.txt ../../testcases/fourth/output/output4.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 4 - failed ✗")
    else:
        print("Testcase 4 - passed ✓")

    compare = subprocess.run("diff ../../testcases/fourth/expected_output/expected5.txt ../../testcases/fourth/output/output5.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 5 - failed ✗")
    else:
        print("Testcase 5 - passed ✓")
    compare = subprocess.run("diff ../../testcases/fourth/expected_output/expected6.txt ../../testcases/fourth/output/output6.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 6 - failed ✗ ")
    else:
        print("Testcase 6 - passed ✓")

def partfive():
    print("Part five")
    compilation = subprocess.run("make clean",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if compilation.returncode != 0:
       print("make clean failed")
       print(compilation.stderr.decode())
       return
    print("make clean - success")
    compilation = subprocess.run("make fifth",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if compilation.returncode != 0:
       print("make five")
       print(compilation.stderr.decode())
       return
    print("make five - success")
    # Tests
    testcases = subprocess.run("./fifth ../../testcases/fifth/input/input1.txt &> ../../testcases/fifth/output/output1.txt", shell=True)
    testcases = subprocess.run("./fifth ../../testcases/fifth/input/input2.txt &> ../../testcases/fifth/output/output2.txt", shell=True)
    testcases = subprocess.run("./fifth ../../testcases/fifth/input/input3.txt &> ../../testcases/fifth/output/output3.txt", shell=True)
    testcases = subprocess.run("./fifth ../../testcases/fifth/input/input4.txt &> ../../testcases/fifth/output/output4.txt", shell=True)
    testcases = subprocess.run("./fifth ../../testcases/fifth/input/input5.txt &> ../../testcases/fifth/output/output5.txt", shell=True)
    compare = subprocess.run("diff ../../testcases/fifth/expected_output/expected1.txt ../../testcases/fifth/output/output1.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 1 - failed ✗ ")
    else:
        print("Testcase 1 - passed ✓")
    compare = subprocess.run("diff ../../testcases/fifth/expected_output/expected2.txt ../../testcases/fifth/output/output2.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 2 - failed ✗ ")
    else:
        print("Testcase 2 - passed ✓")
    compare = subprocess.run("diff ../../testcases/fifth/expected_output/expected3.txt ../../testcases/fifth/output/output3.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 3 - failed ✗ ")
    else:
        print("Testcase 3 - passed ✓")
    compare = subprocess.run("diff ../../testcases/fifth/expected_output/expected4.txt ../../testcases/fifth/output/output4.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 4 - failed ✗ ")
    else:
        print("Testcase 4 - passed ✓")
    compare = subprocess.run("diff ../../testcases/fifth/expected_output/expected5.txt ../../testcases/fifth/output/output5.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 5 - failed ✗ ")
    else:
        print("Testcase 5 - passed ✓")

def partsix():
    print("Part six")
    compilation = subprocess.run("make clean",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if compilation.returncode != 0:
       print("make clean failed")
       print(compilation.stderr.decode())
       return
    print("make clean - success")
    compilation = subprocess.run("make sixth",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if compilation.returncode != 0:
       print("make six")
       print(compilation.stderr.decode())
       return
    print("make six - success")
    # Tests
    testcases = subprocess.run("./sixth ../../testcases/sixth/input/input1.txt &> ../../testcases/sixth/output/output1.txt", shell=True)
    testcases = subprocess.run("./sixth ../../testcases/sixth/input/input2.txt &> ../../testcases/sixth/output/output2.txt", shell=True)
    testcases = subprocess.run("./sixth ../../testcases/sixth/input/input3.txt &> ../../testcases/sixth/output/output3.txt", shell=True)
    testcases = subprocess.run("./sixth ../../testcases/sixth/input/input4.txt &> ../../testcases/sixth/output/output4.txt", shell=True)
    testcases = subprocess.run("./sixth ../../testcases/sixth/input/input5.txt &> ../../testcases/sixth/output/output5.txt", shell=True)
    compare = subprocess.run("diff ../../testcases/sixth/expected_output/expected1.txt ../../testcases/sixth/output/output1.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 1 - failed ✗ ")
    else:
        print("Testcase 1 - passed ✓")
    compare = subprocess.run("diff ../../testcases/sixth/expected_output/expected2.txt ../../testcases/sixth/output/output2.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 2 - failed ✗ ")
    else:
        print("Testcase 2 - passed ✓")
    compare = subprocess.run("diff ../../testcases/sixth/expected_output/expected3.txt ../../testcases/sixth/output/output3.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 3 - failed ✗ ")
    else:
        print("Testcase 3 - passed ✓")
    compare = subprocess.run("diff ../../testcases/sixth/expected_output/expected4.txt ../../testcases/sixth/output/output4.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 4 - failed ✗ ")
    else:
        print("Testcase 4 - passed ✓")
    compare = subprocess.run("diff ../../testcases/sixth/expected_output/expected5.txt ../../testcases/sixth/output/output5.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 5 - failed ✗ ")
    else:
        print("Testcase 5 - passed ✓")
def partseven():
    print("Part seven")
    compilation = subprocess.run("make clean",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if compilation.returncode != 0:
       print("make clean failed")
       print(compilation.stderr.decode())
       return
    print("make clean - success")
    compilation = subprocess.run("make seventh",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if compilation.returncode != 0:
       print("make seven")
       print(compilation.stderr.decode())
       return
    print("make seven - success")
    # Tests
    testcases = subprocess.run("./seventh ../../testcases/seventh/input/input1.txt &> ../../testcases/seventh/output/output1.txt", shell=True)
    testcases = subprocess.run("./seventh ../../testcases/seventh/input/input2.txt &> ../../testcases/seventh/output/output2.txt", shell=True)
    testcases = subprocess.run("./seventh ../../testcases/seventh/input/input3.txt &> ../../testcases/seventh/output/output3.txt", shell=True)
    testcases = subprocess.run("./seventh ../../testcases/seventh/input/input4.txt &> ../../testcases/seventh/output/output4.txt", shell=True)
    testcases = subprocess.run("./seventh ../../testcases/seventh/input/input5.txt &> ../../testcases/seventh/output/output5.txt", shell=True)
    compare = subprocess.run("diff ../../testcases/seventh/expected_output/expected1.txt ../../testcases/seventh/output/output1.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 1 - failed ✗ ")
    else:
        print("Testcase 1 - passed ✓")
    compare = subprocess.run("diff ../../testcases/seventh/expected_output/expected2.txt ../../testcases/seventh/output/output2.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 2 - failed ✗ ")
    else:
        print("Testcase 2 - passed ✓")
    compare = subprocess.run("diff ../../testcases/seventh/expected_output/expected3.txt ../../testcases/seventh/output/output3.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 3 - failed ✗ ")
    else:
        print("Testcase 3 - passed ✓")
    compare = subprocess.run("diff ../../testcases/seventh/expected_output/expected4.txt ../../testcases/seventh/output/output4.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 4 - failed ✗ ")
    else:
        print("Testcase 4 - passed ✓")
    compare = subprocess.run("diff ../../testcases/seventh/expected_output/expected5.txt ../../testcases/seventh/output/output5.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 5 - failed ✗ ")
    else:
        print("Testcase 5 - passed ✓")
def parteight():
    print("Part eight")
    compilation = subprocess.run("make clean",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if compilation.returncode != 0:
       print("make clean failed")
       print(compilation.stderr.decode())
       return
    print("make clean - success")
    compilation = subprocess.run("make eighth",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if compilation.returncode != 0:
       print("make seven")
       print(compilation.stderr.decode())
       return
    print("make seven - success")
    # Tests
    testcases = subprocess.run("./eighth ../../testcases/eighth/input/input1.txt &> ../../testcases/eighth/output/output1.txt", shell=True)
    testcases = subprocess.run("./eighth ../../testcases/eighth/input/input2.txt &> ../../testcases/eighth/output/output2.txt", shell=True)
    testcases = subprocess.run("./eighth ../../testcases/eighth/input/input3.txt &> ../../testcases/eighth/output/output3.txt", shell=True)
    testcases = subprocess.run("./eighth ../../testcases/eighth/input/input4.txt &> ../../testcases/eighth/output/output4.txt", shell=True)
    testcases = subprocess.run("./eighth ../../testcases/eighth/input/input5.txt &> ../../testcases/eighth/output/output5.txt", shell=True)
    compare = subprocess.run("diff ../../testcases/eighth/expected_output/expected1.txt ../../testcases/eighth/output/output1.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 1 - failed ✗ ")
    else:
        print("Testcase 1 - passed ✓")
    compare = subprocess.run("diff ../../testcases/eighth/expected_output/expected2.txt ../../testcases/eighth/output/output2.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 2 - failed ✗ ")
    else:
        print("Testcase 2 - passed ✓")
    compare = subprocess.run("diff ../../testcases/eighth/expected_output/expected3.txt ../../testcases/eighth/output/output3.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 3 - failed ✗ ")
    else:
        print("Testcase 3 - passed ✓")
    compare = subprocess.run("diff ../../testcases/eighth/expected_output/expected4.txt ../../testcases/eighth/output/output4.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 4 - failed ✗ ")
    else:
        print("Testcase 4 - passed ✓")
    compare = subprocess.run("diff ../../testcases/eighth/expected_output/expected5.txt ../../testcases/eighth/output/output5.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 5 - failed ✗ ")
    else:
        print("Testcase 5 - passed ✓")

def partone():
    print("Part one")
    compilation = subprocess.run("make clean",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if compilation.returncode != 0:
       print("make clean failed")
       print(compilation.stderr.decode())
       return
    print("make clean - success")
    compilation = subprocess.run("make first",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if compilation.returncode != 0:
       print("make first")
       print(compilation.stderr.decode())
       return
    print("make first - success")
    # Tests
    testcases = subprocess.run("./first ../../testcases/first/input/input1.txt &> ../../testcases/first/output/output1.txt", shell=True)
    testcases = subprocess.run("./first ../../testcases/first/input/input2.txt &> ../../testcases/first/output/output2.txt", shell=True)
    testcases = subprocess.run("./first ../../testcases/first/input/input3.txt &> ../../testcases/first/output/output3.txt", shell=True)
    testcases = subprocess.run("./first ../../testcases/first/input/input4.txt &> ../../testcases/first/output/output4.txt", shell=True)
    testcases = subprocess.run("./first ../../testcases/first/input/input5.txt &> ../../testcases/first/output/output5.txt", shell=True)
    compare = subprocess.run("diff ../../testcases/first/expected_output/expected1.txt ../../testcases/first/output/output1.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 1 - failed ✗ ")
    else:
        print("Testcase 1 - passed ✓")
    compare = subprocess.run("diff ../../testcases/first/expected_output/expected2.txt ../../testcases/first/output/output2.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 2 - failed ✗ ")
    else:
        print("Testcase 2 - passed ✓")
    compare = subprocess.run("diff ../../testcases/first/expected_output/expected3.txt ../../testcases/first/output/output3.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 3 - failed ✗ ")
    else:
        print("Testcase 3 - passed ✓")
    compare = subprocess.run("diff ../../testcases/first/expected_output/expected4.txt ../../testcases/first/output/output4.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 4 - failed ✗ ")
    else:
        print("Testcase 4 - passed ✓")
    compare = subprocess.run("diff ../../testcases/first/expected_output/expected5.txt ../../testcases/first/output/output5.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 5 - failed ✗ ")
    else:
        print("Testcase 5 - passed ✓")

def parttwo():
    print("Part two")
    compilation = subprocess.run("make clean",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if compilation.returncode != 0:
       print("make clean failed")
       print(compilation.stderr.decode())
       return
    print("make clean - success")
    compilation = subprocess.run("make first",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if compilation.returncode != 0:
       print("make second")
       print(compilation.stderr.decode())
       return
    print("make second - success")
    # Tests
    testcases = subprocess.run("./second ../../testcases/second/input/input1.txt &> ../../testcases/second/output/output1.txt", shell=True)
    testcases = subprocess.run("./second ../../testcases/second/input/input2.txt &> ../../testcases/second/output/output2.txt", shell=True)
    testcases = subprocess.run("./second ../../testcases/second/input/input3.txt &> ../../testcases/second/output/output3.txt", shell=True)
    testcases = subprocess.run("./second ../../testcases/second/input/input4.txt &> ../../testcases/second/output/output4.txt", shell=True)
    testcases = subprocess.run("./second ../../testcases/second/input/input5.txt &> ../../testcases/second/output/output5.txt", shell=True)
    compare = subprocess.run("diff ../../testcases/second/expected_output/expected1.txt ../../testcases/second/output/output1.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 1 - failed ✗ ")
    else:
        print("Testcase 1 - passed ✓")
    compare = subprocess.run("diff ../../testcases/second/expected_output/expected2.txt ../../testcases/second/output/output2.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 2 - failed ✗ ")
    else:
        print("Testcase 2 - passed ✓")
    compare = subprocess.run("diff ../../testcases/second/expected_output/expected3.txt ../../testcases/second/output/output3.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 3 - failed ✗ ")
    else:
        print("Testcase 3 - passed ✓")
    compare = subprocess.run("diff ../../testcases/second/expected_output/expected4.txt ../../testcases/second/output/output4.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 4 - failed ✗ ")
    else:
        print("Testcase 4 - passed ✓")
    compare = subprocess.run("diff ../../testcases/second/expected_output/expected5.txt ../../testcases/second/output/output5.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 5 - failed ✗ ")
    else:
        print("Testcase 5 - passed ✓")
def partthree():
    print("Part three")
    compilation = subprocess.run("make clean",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if compilation.returncode != 0:
       print("make clean failed")
       print(compilation.stderr.decode())
       return
    print("make clean - success")
    compilation = subprocess.run("make third",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if compilation.returncode != 0:
       print("make third")
       print(compilation.stderr.decode())
       return
    print("make third - success")
    # Tests
    testcases = subprocess.run("./third ../../testcases/third/input/input1.txt &> ../../testcases/third/output/output1.txt", shell=True)
    testcases = subprocess.run("./third ../../testcases/third/input/input2.txt &> ../../testcases/third/output/output2.txt", shell=True)
    testcases = subprocess.run("./third ../../testcases/third/input/input3.txt &> ../../testcases/third/output/output3.txt", shell=True)
    testcases = subprocess.run("./third ../../testcases/third/input/input4.txt &> ../../testcases/third/output/output4.txt", shell=True)
    testcases = subprocess.run("./third ../../testcases/third/input/input5.txt &> ../../testcases/third/output/output5.txt", shell=True)
    compare = subprocess.run("diff ../../testcases/third/expected_output/expected1.txt ../../testcases/third/output/output1.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 1 - failed ✗ ")
    else:
        print("Testcase 1 - passed ✓")
    compare = subprocess.run("diff ../../testcases/third/expected_output/expected2.txt ../../testcases/third/output/output2.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 2 - failed ✗ ")
    else:
        print("Testcase 2 - passed ✓")
    compare = subprocess.run("diff ../../testcases/third/expected_output/expected3.txt ../../testcases/third/output/output3.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 3 - failed ✗ ")
    else:
        print("Testcase 3 - passed ✓")
    compare = subprocess.run("diff ../../testcases/third/expected_output/expected4.txt ../../testcases/third/output/output4.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 4 - failed ✗ ")
    else:
        print("Testcase 4 - passed ✓")
    compare = subprocess.run("diff ../../testcases/third/expected_output/expected5.txt ../../testcases/third/output/output5.txt",shell=True, stdout=subprocess.PIPE)
    if compare.returncode != 0:
        print("Testcase 5 - failed ✗ ")
    else:
        print("Testcase 5 - passed ✓")
def main():
    # compile and test part 4
    os.chdir("./pa6/first/")
    partone()
    os.chdir("../../")
    os.chdir("./pa6/second/")
    partone()
    os.chdir("../../")
    os.chdir("./pa6/fourth/")
    partfour()
    os.chdir("../../")
    os.chdir("./pa6/fifth/")
    partfive()
    os.chdir("../../")
    os.chdir("./pa6/sixth/")
    partsix()
    os.chdir("../../")
    os.chdir("./pa6/seventh/")
    partseven()
    os.chdir("../../")
    os.chdir("./pa6/eighth/")
    parteight()
    os.chdir("../../")

if __name__ == "__main__":
  main()