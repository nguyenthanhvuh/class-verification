[[_TOC_]]

# CSCE990 (Spring 2019): Software Verification - READING LIST


## Topic 1: Intro

1. ~~William G. Griswold, [How to Read an Engineering Research Paper](http://cseweb.ucsd.edu/~wgg/CSE210/howtoread.html)~~
1. ~~Mike Hicks, [Advice on Reviewing Papers](http://www.pl-enthusiast.net/2014/08/21/advice-reviewing-papers/)~~
1. ~~Hoare, [Axiomatic Basis for Computer Programming](https://www.cs.cmu.edu/~crary/819-f09/Hoare69.pdf). CACM 1969.~~

*Note*: You might want to start by with the [Hoare logic article](https://en.wikipedia.org/wiki/Hoare_logic) from Wikipedia.


## Topic 2: Model Checking

1. ~~JHala et al., [Software Model Checking](https://cse.unl.edu/~tnguyen/class/csce990/files/SoftwareModelChecking.pdf).  ACM Computing Surveys, 2009 *Chapter 1*~~
1. ~~JHala et al., [Software Model Checking](https://cse.unl.edu/~tnguyen/class/csce990/files/SoftwareModelChecking.pdf). ACM Computing Surveys, 2009 *Chapters 2,3*~~

1. ~~**OPTIONAL** Visser et al., [Model Checking Programs](https://ti.arc.nasa.gov/m/tech/rse/publications/papers/ASE00/jpf2-ase.pdf). ASE 2003~~

## Topic 3: Abstraction / Static Analysis

1. ~~JHala et al., [Software Model Checking](https://cse.unl.edu/~tnguyen/class/csce990/files/SoftwareModelChecking.pdf). ACM Computing Surveys, 2009 *Chapters 4*~~    
1. ~~JHala et al., [Software Model Checking](https://cse.unl.edu/~tnguyen/class/csce990/files/SoftwareModelChecking.pdf). ACM Computing Surveys, 2009 *Chapters 5*~~
1. ~~Ball et al., Automatic predicate abstraction of C programs. PLDI, 2001~~
1. ~~Mike Hick's post on [Soundness of Static Analysis](http://www.pl-enthusiast.net/2017/10/23/what-is-soundness-in-static-analysis/)~~


## Topic 4: Symbolic Execution/Test Case Generation

1. ~~Baldoni et al., [A Survey of Symbolic Execution Techniques](http://season-lab.github.io/papers/survey-symbolic-execution-preprint-CSUR18.pdf). CSUR, 2018.~~

*Tool*: Java Symbolic PathFinder (SE for Java), KLEE (SE for C)


## Topic 5: Dynamic analysis, Invariant Generation

1. ~~Ernst et al., [Daikon: Dynamically Discovering Likely Program Invariants](https://ece.uwaterloo.ca/~agurfink/ece653w17/assets/pdf/W12-Daikon.pdf). **Note**: Just read the slides.~~
1. ~~Nguyen et al., [SymInfer: Inferring Program Invariants using Symbolic States](https://cse.unl.edu/~tnguyen/Pub/symtraces_pres.pdf). ASE 2017. **Note**: Just read the slides.~~
1. ~~**OPTIONAL** Garg et al., Learning invariants using decision trees and implication counterexamples. POPL 2016.~~

*Tool*: Daikon, SymInfer

**Optional**: http://se.inf.ethz.ch/old/teaching/2009-S/0276/slides/schwab.pdf
   
## Topic 6: Program Synthesis and Repair
1. ~~Weimer et al., Automatically finding patches using genetic programming. ICSE 2009~~
1. ~~Nguyen et al., Connecting Program Synthesis and Reachability: Automatic Program Repair using Test-Input Generation. TACAS 2017.~~
1. ~~Gulwani et al., [Program Synthesis](https://www.microsoft.com/en-us/research/publication/program-synthesis/), CSUR, Chapters 1 and 2~~
1. ~~Gulwani et al., [Program Synthesis](https://www.microsoft.com/en-us/research/publication/program-synthesis/), CSUR, Chapters 3 and 4~~

*Optional*: [Facebook's automatic bug fixing](https://code.fb.com/developer-tools/getafix-how-facebook-tools-learn-to-fix-bugs-automatically/)

*Tool*: Sketch
  
  
## Topic 7: Logics/SAT Solving

- ~~[Propositional calculus](https://en.wikipedia.org/wiki/Propositional_calculus)~~
- ~~[Conflict Driven Clause Learning](https://en.wikipedia.org/wiki/Conflict-Driven_Clause_Learning)~~
- ~~[First-Order Logic](https://en.wikipedia.org/wiki/First-order_logic)~~
- ~~[SMT Solver](https://web.stanford.edu/class/cs357/lectures/lec9.pdf)~~

Optional: Shankar, [Speaking Logic](http://fm.csl.sri.com/SSFT18/speaklogicV8.pdf)
*Tool*: Z3

## Topic 8: Type Systems
1. ~~Luca Cardelli, [Type Systems](http://lucacardelli.name/papers/typesystems.pdf), CSUR 1996~~

## Topic 9: Automated Debugging

1. James A. Jones et al., [Visualization of test information to assist fault localization](https://www.cc.gatech.edu/~john.stasko/papers/icse02.pdf). ICSE 2002.
1. Bessey et al., A Few Billion Lines of Code Later: Using Static Analysis to Find Bugs in the Real World. CACM

Optional: 
1. Andreas Zeller, Yesterday, My Program Worked. Today, It Does Not. Why?. FSE 1999.
1. Le et al., [Compiler Validation via Equivalence Modulo Inputs](http://vuminhle.com/pdf/pldi14-emi.pdf) , PLDI 2014,


*Tool*: [delta debugging](http://www.st.cs.uni-saarland.de/dd/)



## Additional Resources:
- Basic stuff: control flow graph, live/reach defs: https://www.cs.odu.edu/~zeil/cs350/f18/Public/analysis/index.html
- Build System: https://www.cs.odu.edu/~zeil/cs350/f18/Public/make/index.html
- Call graphs etc: http://web.cs.iastate.edu/~weile/cs513x/4.ControlFlowAnalysis.pdf
- Dependency Graph/Slicing: http://web.cs.iastate.edu/~weile/cs513x/5.DependencySlicing.pdf
