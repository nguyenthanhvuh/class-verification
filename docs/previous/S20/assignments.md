# Reading

## Instructions

On average, we will discuss **three papers** a week (~50 minutes to each paper). 
You are responsible for reading at least **two papers** in advance for any given discussion.

At the beginning of each paper discussion I will choose up to **three students** at random. 
Each student will give a **five-minute** presentation about the paper. 

!!! info "This presentation must include:"
    - the problem (what is it? why is it interesting?)
    - existing approaches (what are they? what are their limitations?)
    - the proposed technical approach (also talk about the strengths of approach and how the approach addresses the weaknesses of existing works)
    - limitations of the proposed approach and lists ways in which it might be improved.

You can also include other information, such as your opinion about the
work, or its relation to other work you may know. The goals of this
approach are to encourage all participants to read the material
thoroughly in advance, to provide jumping-off points for detailed
discussions, and to allow me to evaluate participation.

In addition, these chosen students will help engage discussions about the paper.

## Reading List

### Background: Program Analysis

- Software Testing using **Fuzzing**
    - {--[Fuzzing: Hack, Art, and Science](files/godefroid2020fuzzing.pdf)--}
    - {--[Evaluating Fuzz Testing](files/klees2018evaluating.pdf)--}
- **Model Checking**
    - {--[Model Checking: Algorithmic Verification and Debugging](files/clarke2009model.pdf)--}
<!-- - **Software Verification**
    - [Hoare Logic](files/hoare-logic.pdf) (**Optional**: [Wikipedia](https://en.wikipedia.org/wiki/Hoare_logic))
    - Abstract Intepretation
      - [Wikipedia](https://en.wikipedia.org/wiki/Abstract_interpretation)
      - [Abstract Interpretation: Past, Present, and Future](https://cs.nyu.edu/~pcousot/publications.www/CousotCousot-CSL-LICS-2014.pdf)
       -->
<!-- - **Symbolic Execution**
    - [Wikipedia: Symbolic Execution](https://en.wikipedia.org/wiki/Symbolic_execution)
    - [Wikipedia: Concolic Testing](https://en.wikipedia.org/wiki/Concolic_testing)
    - [Symbolic Execution and Program Testing](https://dl.acm.org/doi/10.1145/360248.360252t)
    - [Symbolic Execution For Software Testing: Three Decades Later](https://cacm.acm.org/magazines/2013/2/160161-symbolic-execution-for-software-testing/fulltext) -->

- Miscs:
  <!-- - Trends in Software Verification -->
    - {--[A Gentle Introduction to Program Analysis](https://www.cs.utexas.edu/~isil/dillig-plmw14.pdf)--}
  
<!-- - **Invariant Generation**
    - SymInfer: inferring program invariants using symbolic states
    - Learning nonlinear loop invariants with gated continuous logic networks
- **Miscs**
    - Scaling Static Analyses at Facebook -->

   
### Domain 1: IoT systems

1. {--[Scalable analysis of interaction threats in IoT systems](files/alhanahnah20scalable.pdf). ISSTA 2020--}
1. {--Understanding and Automatically Detecting Conflicting Interactions between Smart Home IoT Applications. FSE 2020--}
1. {--Trace2TAP: Synthesizing Trigger-Action Programs From Traces of Behavior--} 
1. {--Charting the Attack Surface of Trigger-Action IoT Platforms.--}
1. Decentralized Action Integrity for Trigger-Action IoT Platforms.


### Domain 2: Deep Neural Networks
- [Youtube Video: Verification of ML Programs](https://www.youtube.com/watch?v=Reo5REo71GU), Guy Katz
    - [pdf](files/verification_of_ml_programs_katz.pdf)
- [Towards Verified Artificial Intelligence](files/seshia2016towards.pdf), Seshia et al.  
- [Algorithms for Verifying Deep Neural Networks](files/liu2019algorithms.pdf), Lieu et al.  SECTIONS 1-3 
- [Algorithms for Verifying Deep Neural Networks](files/liu2019algorithms.pdf), Lieu et al.  SECTIONS 4-5
- [Algorithms for Verifying Deep Neural Networks](files/liu2019algorithms.pdf), Lieu et al.  SECTIONS 4-5
- [Reluplex: An Efficient SMT Solver for Verifying Deep Neural Networks](https://link.springer.com/chapter/10.1007/978-3-319-63387-9_5)
- [The Marabou Framework for Verification and Analysis of Deep Neural Networks](https://link.springer.com/chapter/10.1007/978-3-030-25540-4_26) **NEXT CLASS**
- [AI2: Safety and Robustness Certification of Neural Networks with Abstract Interpretation](https://ieeexplore.ieee.org/document/8418593)
- [Reluval: Formal security analysis of neural networks using symbolic intervals](https://dl.acm.org/doi/10.5555/3277203.3277323)
- [NNV: The Neural Network Verification Tool for Deep Neural Networks and Learning-Enabled Cyber-Physical Systems](https://link.springer.com/chapter/10.1007/978-3-030-53288-8_1)
- General Lectures
    - [AI^2: AI Safety and Robustness with Abstract Interpretation](http://safeai.ethz.ch/files/FLOC18-AI2.pdf)
    - Lots of good talks/slides: https://mlcertifiedsystems.deel.ai/#Intro
    

### Domain 3: Networking
1. Applying Formal Methods to Networking: Theory, Techniques, and Applications
1. A Formally Verified NAT 
1. Model-Agnostic and Efficient Exploration of Numerical State Space of Real-World TCP Congestion Control Implementations. NSDI 2019
1. Automated Verification of Customizable Middlebox Properties with Gravel

