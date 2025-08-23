---
layout: paper
categories: papers
permalink: papers/conceptevo
id: conceptevo
title: "Concept Evolution in Deep Learning Training: A Unified Interpretation Framework and Discoveries"
authors: 
  - Haekyu Park
  - Seongmin Lee
  - Benjamin Hoover
  - Austin Wright
  - Omar Shaikh
  - Rahul Duggal
  - Nilaksh Das
  - Judy Hoffman
  - Duen Horng (Polo) Chau
venue-num:
 - 0
venue: 
  - Full Paper, ACM International Conference on Information and Knowledge Management
venue-shorthand: 
  - CIKM
year: 
  - 2023
url: /papers/conceptevo
pdf: https://arxiv.org/abs/2203.16475
code: https://github.com/poloclub/ConceptEvo
type: conference
figure: /images/papers/23-conceptevo-cikm.png
selected: false
doi: "10.1145/3583780.3614819"
feature-title: ConceptEvo
feature-description: Unified interpretation framework for deep neural networks that reveals the inception and evolution of learned concepts during training
featured: false
bibtex: |-

  @article{park2022conceptevo,
    title={ConceptEvo: Interpreting Concept Evolution in Deep Learning Training},
    author={Park, Haekyu and Lee, Seongmin and Hoover, Benjamin and Wright, Austin and Shaikh, Omar and Duggal, Rahul and Das, Nilaksh and Hoffman, Judy and Chau, Duen Horng},
    journal={arXiv preprint arXiv:2203.16475},
    year={2022}
  }
---

We present ConceptEvo, a unified interpretation framework for deep neural networks (DNNs) that reveals the inception and evolution of learned concepts during training. Our work addresses a critical gap in DNN interpretation research, as existing methods primarily focus on post-training interpretation. ConceptEvo introduces two novel technical contributions: (1) an algorithm that generates a unified semantic space, enabling side-by-side comparison of different models during training, and (2) an algorithm that discovers and quantifies important concept evolutions for class predictions. Through a large-scale human evaluation and quantitative experiments, we demonstrate that ConceptEvo successfully identifies concept evolutions across different models, which are not only comprehensible to humans but also crucial for class predictions. ConceptEvo is applicable to both modern DNN architectures, such as ConvNeXt, and classic DNNs, such as VGGs and InceptionV3.