**errata**

- 12/9/24: autograder updated for redirection issues. You can either pull, or replace all instances of ```&>``` with ```>```

---

# Extra Credit Autograder

- This is the autograder for the Extra Credit Assignment. Instead of providing a tar file to scp to the ilabs, I provided you with a github repository to make things easier. 

cd to whatever directory you want to store the autograder in, and run the following command:

```
git clone https://github.com/AFE123x/GSC5-8CS211-Extra-Credit-Autograder.git
```

- This will make a folder called ```GSC5-8CS211-Extra-Credit-Autograder```. to get the autograder working, you just need to **copy** your pa6 folder into the ```GSC5-8CS211-Extra-Credit-Autograder``` folder. Your folder should look like the following:

```
.
├── PAEC.pdf
├── README.md
├── autograder.py
├── pa6
│   ├── eighth
│   │   ├── Makefile
│   │   ├── eighth.c
│   │   └── eighth.h
│   ├── fifth
│   │   ├── Makefile
│   │   ├── fifth.c
│   │   └── fifth.h
│   ├── first
│   │   ├── Makefile
│   │   ├── first.c
│   │   └── first.h
│   ├── fourth
│   │   ├── Makefile
│   │   ├── fourth.c
│   │   └── fourth.h
│   ├── second
│   │   ├── Makefile
│   │   ├── second.c
│   │   └── second.h
│   ├── seventh
│   │   ├── Makefile
│   │   ├── seventh.c
│   │   └── seventh.h
│   ├── sixth
│   │   ├── Makefile
│   │   ├── sixth.c
│   │   └── sixth.h
│   └── third
│       ├── Makefile
│       ├── third.c
│       └── third.h
└── testcases
    ├── eighth
    │   ├── expected_output
    │   │   ├── expected1.txt
    │   │   ├── expected2.txt
    │   │   ├── expected3.txt
    │   │   ├── expected4.txt
    │   │   └── expected5.txt
    │   ├── input
    │   │   ├── input1.txt
    │   │   ├── input2.txt
    │   │   ├── input3.txt
    │   │   ├── input4.txt
    │   │   └── input5.txt
    │   └── output
    │       ├── info
    │       ├── output1.txt
    │       ├── output2.txt
    │       ├── output3.txt
    │       ├── output4.txt
    │       └── output5.txt
    ├── fifth
    │   ├── expected_output
    │   │   ├── expected1.txt
    │   │   ├── expected2.txt
    │   │   ├── expected3.txt
    │   │   ├── expected4.txt
    │   │   └── expected5.txt
    │   ├── input
    │   │   ├── input1.txt
    │   │   ├── input2.txt
    │   │   ├── input3.txt
    │   │   ├── input4.txt
    │   │   └── input5.txt
    │   └── output
    │       ├── info
    │       ├── output1.txt
    │       ├── output2.txt
    │       ├── output3.txt
    │       ├── output4.txt
    │       └── output5.txt
    ├── first
    │   ├── expected_output
    │   │   ├── expected1.txt
    │   │   ├── expected2.txt
    │   │   ├── expected3.txt
    │   │   ├── expected4.txt
    │   │   └── expected5.txt
    │   ├── input
    │   │   ├── input1.txt
    │   │   ├── input2.txt
    │   │   ├── input3.txt
    │   │   ├── input4.txt
    │   │   └── input5.txt
    │   └── output
    │       ├── output1.txt
    │       ├── output2.txt
    │       ├── output3.txt
    │       ├── output4.txt
    │       └── output5.txt
    ├── fourth
    │   ├── expected_output
    │   │   ├── expected1.txt
    │   │   ├── expected2.txt
    │   │   ├── expected3.txt
    │   │   ├── expected4.txt
    │   │   ├── expected5.txt
    │   │   └── expected6.txt
    │   ├── input
    │   │   ├── input1.txt
    │   │   ├── input2.txt
    │   │   ├── input3.txt
    │   │   ├── input4.txt
    │   │   ├── input5.txt
    │   │   └── input6.txt
    │   └── output
    │       ├── info
    │       ├── output1.txt
    │       ├── output2.txt
    │       ├── output3.txt
    │       ├── output4.txt
    │       ├── output5.txt
    │       └── output6.txt
    ├── second
    │   ├── expected_output
    │   │   ├── expected1.txt
    │   │   ├── expected2.txt
    │   │   ├── expected3.txt
    │   │   ├── expected4.txt
    │   │   └── expected5.txt
    │   └── input
    │       ├── input1.txt
    │       ├── input2.txt
    │       ├── input3.txt
    │       ├── input4.txt
    │       └── input5.txt
    ├── seventh
    │   ├── expected_output
    │   │   ├── expected1.txt
    │   │   ├── expected2.txt
    │   │   ├── expected3.txt
    │   │   ├── expected4.txt
    │   │   └── expected5.txt
    │   ├── input
    │   │   ├── input1.txt
    │   │   ├── input2.txt
    │   │   ├── input3.txt
    │   │   ├── input4.txt
    │   │   └── input5.txt
    │   └── output
    │       ├── info
    │       ├── output1.txt
    │       ├── output2.txt
    │       ├── output3.txt
    │       ├── output4.txt
    │       └── output5.txt
    ├── sixth
    │   ├── expected_output
    │   │   ├── expected1.txt
    │   │   ├── expected2.txt
    │   │   ├── expected3.txt
    │   │   ├── expected4.txt
    │   │   └── expected5.txt
    │   ├── input
    │   │   ├── input1.txt
    │   │   ├── input2.txt
    │   │   ├── input3.txt
    │   │   ├── input4.txt
    │   │   └── input5.txt
    │   └── output
    │       ├── info
    │       ├── output1.txt
    │       ├── output2.txt
    │       ├── output3.txt
    │       ├── output4.txt
    │       └── output5.txt
    └── third
        ├── expected_output
        │   ├── expected1.txt
        │   ├── expected2.txt
        │   ├── expected3.txt
        │   ├── expected4.txt
        │   └── expected5.txt
        └── input
            ├── input1.txt
            ├── input2.txt
            ├── input3.txt
            ├── input4.txt
            └── input5.txt
```

- To run the autograder, you simply run:

```
python3 autograder.py
```

- This will run your code and check for correctness based on **given** test cases.
- Your Makefile should have a clean, and a "make <part-num>" function.
    - For example, the Makefile for the first part should have clean, and ```first``` function.
- If the autograder marks a testcase as wrong, you can look at your program in the output folder, and compare it to the expected text file in the expected_output folder.
```
make clean
make first
```

- For the first part.
