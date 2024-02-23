---
layout: page
title: Test Site
tagline: This is a test site.
description: 
---

The interplay between brain, behavior, and cognition from childhood to adulthood: The creation of simulated datasets from eight independent groups worldwide 

Each group simulated three sets of longitudinal data for brain measures such as volume and cortical thickness as well as cognitive and behavioral measures based on their understanding and models of development. These datasets have been released to the community where different modeling approaches (e.g., linear mixed effects model, cross-lagged panel model) can be used to estimate brain-behavior relationship. 
The following guidelines to create the datasets are as follows:
Number of subjects: 10000
Number of waves/time-points per subject: 7 (about every two years)
Age: 7-20 years. Starting with an age window between 7 and 8 years and continuing every two years to 20 years: Wave 1 – 7-8 years-of-age; Wave 2 – 9-10 years-of-age; Wave 3 – 11-12 years-of-age; Wave 4 – 13-14 years-of-age; Wave 5 – 15-16 years-of-age; Wave 6 – 17-18 years-of-age; Wave 7 – 19-20 years-of-age. 
Sex: 0: male (approximately 50%), 1: female (approximately 50%)
Cognitive measures: IQ (mean = 100, standard deviation = 15)
Behavioral measures: internalizing and externalizing symptoms and attention problems scale based on child behavior checklist (CBCL)
Autism diagnosis: 0: no, 1: yes. 
Brain volume measures: intracranial volume, total gray matter volume, total white matter volume, hippocampal volume, amygdala volume, and cortical thickness of frontal lobe. The units should be in mm3. Each group determines the starting point and trajectory of each brain measure. 
Parental Education: 0: less than 12th grade (5.3%), 1: High School or GED (35.4%), 2: Bachelor’s Degree (25.3%), 3: Master’s or higher degree (34%)
Attrition/Missing data: missing timepoints 20%. With release of the key the full data should also include the missing data. Thus the algorithm for generating missing data should be applied after simulated dataset is generated. Finally, release of the key should also include the assumption related to the missing data (i.e. missing at random, missing completely at random, missing not at random). 
Effect size, noise: each group decided what effect size and amount of noise they would like to include. 

- [How do I submit data?](pages/tutorial.md)
- [Create pull request to submit data](https://github.com/dmoracze/test.github.io/pulls)
- [Full Abstract](pages/full_abstract.md)

---

Underneath
