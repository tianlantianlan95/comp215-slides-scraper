# comp215-slides-scraper
The program downloads the slides on comp215 website to the current directory or a designated directory

1. Prerequisite:
  1. Install Python (2.0 above)
  2. With Python installed, simply type "easy_install beautifulsoup4"(excluding the quotes) on terminal to install beautifulsoup4. <br />(Note: beautifulsoup4 is a Python library which allow you to pull data out of HTML and XML files).

2. To run the program on Mac: 
  1. Open terminal
  2. Either type "python [path]/comp215dl.py" or navigate to the source folder and type "python comp215dl.py"

3. Example(The source file is put in /Users/Tim/Documents/comp215-slides-backup):

$ python /Users/Tim/Documents/comp215-slides-backup/comp215dl.py
************************************************
input the dir path you want to put the slides in.
If you have navigated to the destination dir,
simply input ".." (excluding the quotes):
/Users/Tim/Documents/comp215-slides-backup/
************************************************
Rename the slides?
If you choose to rename,
the slides will be named "slide1," "slide2" and so forth.
Type Q to quit the program
Y/N/Q: N
************************************************
/Users/Tim/Documents/comp215-slides-backup/week01-intro-2cipd5f.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week01-java-1jl1778.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week01-functional-1jtsvhp.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week02-lambda-generic1-21hzbsv.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week02-lambda-generic2-2kr1o76.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week02-recursion-1fjm15o.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week03-lazy-1tt4jgb.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week03-matching-2grxx6u.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week04-trees-1y85mw3.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week04-treaps-21qb4kl.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week04-heaps-15r1ob5.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week05-regex-1ofb749.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week05-enumtesting-2hjw23t.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week05-grammar-21hosgc.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week06-parsing-urzxy9.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week06-beautiful-238z6hm.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week06-db-1k82y6g.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week07-hashing-2gs9730.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week07-db-255mmfs.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week07-internals-vvzt84.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week08-monads-2l7nsqt.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week09-covariance-p5qwc4.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week09-design-2a3hvss.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week09-realworld-2kb49a7.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week10-events-1udjwsm.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week10-mocks-refactoring-s49zwo.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week10-realworld-debug-sv0ix9.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week11-failures-21kjkr7.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week11-java-history-1tgnml5.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week11-design-u2e4h5.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week12-web101-1y4txuo.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week12-javascript-x0haze.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week12-genetic-algorithms-2ehw0iq.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week13-genetic-algorithms2-1f76pvh.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week13-web-dom-24j1k4j.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week13-performance-26uhx2l.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week14-security-2huy1oz.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week15-android-1p0r5w3.pdf completed
/Users/Tim/Documents/comp215-slides-backup/week15-after-comp215-xuqfa3.pdf completed
************************************************
Done!
