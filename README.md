This the implementation of our new data-driven context-sensitive pointer analysis.

We integrated our data-driven context-sensitivity technique on [Doop](https://bitbucket.org/yanniss/doop) ([OOPSLA'18 artifact version](https://silverbullettt.bitbucket.io/papers/oopsla2018.pdf)), which provide various context sensitivity heuristics for Java pointer analysis.


## Requirements

- A 64-bit Ubuntu system
- A Java 8 distribution
- A Python 2.x interpreter

Please set your `JAVA_HOME` environment variable to point to your Java installation directory.

### Installing Datalog Engine

To run DOOP framework, you need to install a LogicBlox engine that interprets the Datalog rules in DOOP. You can use PA-Datalog engine which is available for academic use. See [this page](http://snf-705535.vm.okeanos.grnet.gr/agreement.html) (`.deb` package installation is recommended).


### Running DOOP

First, move your current directory to 'doop/'. Then, type:

$ ./run -jre1.6 <analysis> <program>

where <analysis> can be one of the analysis in 'doop/logic/' folder such as 3-object-sensitive+2-heap+Data, 2-object-sensitive+heap, context-insensitive. You can check all the supported analyses and other options with `./run -h`.

For <program>, type .jar file to be analyzed.

For example, to analyze `foo.jar` with context-insensitive pointer analysis, just type:

`$ ./run -jre1.6 context-insensitive foo.jar`


### Running DOOP with our data-driven context-sensitive pointer analysis:

To run our data-driven context-sensitive pointer analysis replace <analysis> with 3-object-sensitive+2-heap+Data.

For example, to analyze `foo.jar` with our pointer analysis, type:

'$ ./run -jre1.6 3-object-sensitive+2-heap+Data foo.jar' 



### Donghoon이 만든 스크립트 돌리는법

당신의 directory를 Data-Driven-Pointer-Analysis/Facts 로 옴길것

run.py python파일을 실행시킬것 (python run.py)

학습된 heuristic이 heuristic.logic 에 생성됨


