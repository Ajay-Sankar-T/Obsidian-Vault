---
aliases:
- ML Formula Theory
- Machine Learning Math
tags:
- machine-learning
- mathematics
- statistics
- formulas
- obsidian
title: Machine Learning Formula Sheet --- Theory and Intuition
---

# Machine Learning Formula Sheet --- Theory and Intuition

> [\!abstract\] How to use this note Each item explains what the formula
> measures, why it matters, and how to interpret it. The formulas are
> written in LaTeX so Obsidian can render them. Unless stated otherwise,
> vectors are column vectors and sums run over the indicated
> observations.

## 1. Descriptive statistics

### 1. Mean (average)

$$
\mu = \frac{1}{n}\sum_{i=1}^{n}x_i
$$

**Idea:** The arithmetic mean is the balance point of a dataset. Add all
values and divide by the number of observations.

**Use:** Summarising a feature, filling missing values (when
appropriate), and calculating variance or standardisation.

**Caution:** The mean is sensitive to outliers. For a sample, the symbol
$\bar{x}$ is often used; $\mu$ usually denotes a population mean.

### 2. Variance

$$
\sigma^2 = \frac{1}{n}\sum_{i=1}^{n}(x_i-\mu)^2
$$

**Idea:** Variance measures average squared distance from the mean.
Squaring prevents positive and negative deviations from cancelling and
penalises large deviations more heavily.

**Interpretation:** Larger variance means greater spread. Units are
squared.

**Caution:** This is the population variance. For an unbiased
sample-variance estimate, use
$s^2=\frac{1}{n-1}\sum_i(x_i-\bar{x})^2$.

### 3. Standard deviation

$$
\sigma = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_i-\mu)^2}
$$

**Idea:** Standard deviation is the square root of variance, so it
measures spread in the same units as the original feature.

**Use:** Understanding typical spread, z-scores, and spotting unusually
distant values. A standard deviation of zero means every value is
identical.

### 4. Covariance

$$
\operatorname{cov}(X,Y)=\frac{1}{n}\sum_{i=1}^{n}(x_i-\mu_X)(y_i-\mu_Y)
$$

**Idea:** Covariance indicates whether two variables tend to move
together.

-   Positive: values above the mean of $X$ tend to pair with values
    above the mean of $Y$.
-   Negative: one tends to be above its mean when the other is below.
-   Near zero: little *linear* co-movement; nonlinear relationships can
    still exist.

**Caution:** Its magnitude depends on the variables' units and scales.
Sample covariance commonly uses $n-1$.

### 5. Correlation coefficient

$$
\rho_{XY}=\frac{\operatorname{cov}(X,Y)}{\sigma_X\sigma_Y}
$$

**Idea:** Pearson correlation standardises covariance, producing a
unitless measure of linear association between $-1$ and $+1$.

-   $+1$: perfect positive linear relationship.
-   $-1$: perfect negative linear relationship.
-   $0$: no linear correlation.

**Caution:** Correlation does not establish causation and can miss
nonlinear relationships. If either variable has zero variance,
correlation is undefined.

## 2. Distances and feature scaling

### 6. Euclidean distance

$$
d(\mathbf{x},\mathbf{y})=\sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}
$$

**Idea:** Straight-line distance between two points in Euclidean space.

**Use:** Clustering, nearest-neighbour methods, and geometric
comparisons. Large-scale features can dominate, so scaling may be
necessary.

### 7. Manhattan distance

$$
d(\mathbf{x},\mathbf{y})=\sum_{i=1}^{n}|x_i-y_i|
$$

**Idea:** Sum of absolute coordinate differences; also called city-block
or $L_1$ distance.

**Use:** Grid-like movement, robust-ish distance-based comparisons, and
sparse/high-dimensional settings. It is less dominated by a single large
coordinate difference than squared Euclidean distance.

### 8. Minkowski distance

$$
d_p(\mathbf{x},\mathbf{y})=\left(\sum_{i=1}^{n}|x_i-y_i|^p\right)^{1/p},\quad p\geq 1
$$

**Idea:** A family of distances. $p=1$ gives Manhattan distance; $p=2$
gives Euclidean distance.

**Use:** Adjusting how strongly large coordinate differences affect
distance. The choice of $p$ changes the geometry of "nearby."

### 9. Z-score standardisation

$$
z=\frac{x-\mu}{\sigma}
$$

**Idea:** Expresses a value in standard-deviation units relative to the
mean.

**Interpretation:** $z=2$ means two standard deviations above the mean.
Standardisation commonly gives a feature mean near zero and standard
deviation near one.

**Caution:** Calculate mean and standard deviation on the training set
only, then reuse them on validation/test data to avoid data leakage. If
$\sigma=0$, the feature is constant and needs special handling.

### 10. Min--max normalisation

$$
x'=\frac{x-x_{\min}}{x_{\max}-x_{\min}}
$$

**Idea:** Linearly maps the observed minimum to 0 and maximum to 1.

**Use:** Keeping features in a fixed range, particularly when algorithms
are sensitive to feature scale.

**Caution:** Outliers strongly affect the range. A constant feature
makes the denominator zero. Fit min/max on training data only; future
values may fall outside $[0,1]$.

## 3. Neural-network activation functions

### 11. Sigmoid

$$
\sigma(x)=\frac{1}{1+e^{-x}}
$$

**Idea:** Squashes any real input into $(0,1)$.

**Use:** Commonly converts a binary-classification logit into a
probability estimate.

**Limitations:** Saturates for very positive or negative inputs,
producing small gradients (vanishing-gradient problem). It is not
usually the default hidden-layer activation.

### 12. Hyperbolic tangent (tanh)

$$
\tanh(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}
$$

**Idea:** Squashes inputs into $(-1,1)$ and is zero-centred.

**Use:** Historically common in hidden layers and recurrent networks.

**Limitations:** It also saturates for large $|x|$, causing small
gradients.

### 13. ReLU

$$
f(x)=\max(0,x)
$$

**Idea:** Outputs zero for negative inputs and the input itself for
positive inputs.

**Use:** A common hidden-layer activation because it is simple and does
not saturate on the positive side.

**Limitation:** A unit can become "dead" if it remains in the negative
region and receives zero gradient.

### 14. Leaky ReLU

$$
f(x)=\begin{cases}x,&x>0 \\alpha x,&x\leq 0\end{cases}
$$

**Idea:** Like ReLU, but allows a small negative slope $\alpha$ for
negative inputs.

**Why:** Provides a nonzero gradient on the negative side and may reduce
dead ReLU units. The value of $\alpha$ is a design choice.

### 15. Softmax

$$
\operatorname{softmax}(z_i)=\frac{e^{z_i}}{\sum_{j=1}^{K}e^{z_j}}
$$

**Idea:** Converts $K$ logits into nonnegative values that sum to one.

**Use:** Multiclass classification, often paired with cross-entropy
loss.

**Caution:** The outputs are a probability distribution over classes,
but are not automatically well-calibrated probabilities. In practice,
implementations subtract the largest logit before exponentiation for
numerical stability.

## 4. Linear regression and loss functions

### 16. Linear model

$$
\hat{y}=\mathbf{w}^{T}\mathbf{x}+b
$$

**Idea:** Predicts a target as a weighted sum of input features plus an
intercept (bias) $b$.

**Interpretation:** Each weight describes the model's change in
prediction for a one-unit change in that feature, holding other features
fixed.

**Use:** Regression and as a simple building block for neural networks.
A linear model can still use transformed or engineered input features.

### 17. Mean squared error (MSE)

$$
J=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

**Idea:** Average squared prediction error.

**Strength:** Strongly penalises large errors and is differentiable,
making it convenient for optimisation.

**Limitation:** Sensitive to outliers. MSE has squared target units.

### 18. Mean absolute error (MAE)

$$
J=\frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
$$

**Idea:** Average absolute prediction error.

**Strength:** Easier to interpret in the target's original units and
less sensitive to large outliers than MSE.

**Limitation:** The absolute value is not differentiable at zero, though
optimisation methods can use subgradients.

### 19. Gradient of linear-regression MSE

For a design matrix $X$ with one row per observation and parameter
vector $\mathbf{w}$,

$$
J(\mathbf{w})=\frac{1}{n}\|X\mathbf{w}-\mathbf{y}\|_2^2
$$

$$
\nabla_{\mathbf{w}}J=\frac{2}{n}X^T(X\mathbf{w}-\mathbf{y})
$$

**Idea:** The gradient points in the direction of steepest local
increase in the loss.

**Shape check:** If $X$ is $n\times d$, then $X^T(Xw-y)$ has $d$
entries, one per weight. If the model includes an intercept, it can be
represented by a column of ones in $X$.

### 20. Gradient-descent update

$$
\mathbf{w}_{t+1}=\mathbf{w}_t-\eta\nabla_{\mathbf{w}}J(\mathbf{w}_t)
$$

**Idea:** Update parameters in the direction opposite the gradient to
reduce the objective locally.

**Role of learning rate $\eta$:** Too small can make learning slow; too
large can overshoot or diverge. Gradients may be computed using all
examples, a mini-batch, or a single example.

## 5. Classification and probability

### 21. Logistic regression

$$
P(y=1\mid\mathbf{x})=\frac{1}{1+e^{-(\mathbf{w}^T\mathbf{x}+b)}}
$$

**Idea:** Logistic regression applies sigmoid to a linear score (logit)
to estimate the probability of the positive class.

**Decision:** With a 0.5 threshold, predict class 1 when the logit is
nonnegative. The threshold can be changed to reflect different costs of
false positives and false negatives.

**Note:** Despite its name, logistic regression is a classification
model.

### 22. Binary log loss

$$
J=-\frac{1}{n}\sum_{i=1}^{n}\left[y_i\log(p_i)+(1-y_i)\log(1-p_i)\right]
$$

**Idea:** Penalises probability estimates that assign low probability to
the true binary label.

**Interpretation:** Confident correct predictions incur low loss;
confident incorrect predictions incur very high loss.

**Caution:** Use numerically stable implementations and avoid evaluating
$\log(0)$ directly.

### 23. Multiclass cross-entropy loss

$$
J=-\frac{1}{n}\sum_{i=1}^{n}\sum_{k=1}^{K}y_{ik}\log(p_{ik})
$$

**Idea:** For one-hot labels, only the log-probability of the correct
class contributes to each example's loss.

**Use:** Commonly paired with a softmax output for mutually exclusive
classes. Some libraries expect raw logits and combine softmax with
cross-entropy internally; do not apply softmax twice.

### 24. Naive Bayes

$$
P(C_k\mid\mathbf{x})\propto P(C_k)\prod_{j=1}^{d}P(x_j\mid C_k)
$$

**Idea:** Uses Bayes' rule with the conditional-independence assumption
that features are independent given the class.

**Terms:** $P(C_k)$ is the prior; $P(x_j\mid C_k)$ is a feature
likelihood; the posterior is the updated class probability.

**Why "naive":** The independence assumption is often imperfect, but the
model can still work well, especially for text classification. Products
are commonly computed as sums of log-probabilities.

### 25. Bayes' theorem

$$
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}
$$

**Idea:** Updates belief in event $A$ after observing evidence $B$.

-   $P(A)$: prior.
-   $P(B\mid A)$: likelihood.
-   $P(A\mid B)$: posterior.
-   $P(B)$: evidence/normalising probability.

**Requirement:** $P(B)>0$.

### 26. Prior probability

$$
P(C_k)
$$

**Idea:** Probability of class $C_k$ before considering the current
example's features.

**Example:** If 10% of training emails are spam, the empirical spam
prior is about 0.10.

**Role:** Affects predictions when classes are imbalanced or feature
evidence is weak.

### 27. Likelihood

$$
P(\mathbf{x}\mid C_k)
$$

**Idea:** How probable the observed features are under class $C_k$.

**Distinction:** $P(\mathbf{x}\mid C_k)$ is not the same as
$P(C_k\mid\mathbf{x})$. The former is the likelihood of the evidence
under a class; the latter is the posterior probability of the class
given evidence.

### 28. Posterior probability

$$
P(C_k\mid\mathbf{x})
$$

**Idea:** Probability of class $C_k$ after combining prior information
with observed features.

**Use:** Classification can choose the class with the largest posterior,
though application-specific decision costs may justify a different rule.

## 6. Regularisation and support vector machines

### 29. L2 regularisation (Ridge)

$$
J=\operatorname{MSE}+\lambda\|\mathbf{w}\|_2^2
$$

**Idea:** Adds a penalty proportional to the squared size of the
weights.

**Effect:** Encourages smaller weights, often improving generalisation
and reducing sensitivity to correlated features. Weights usually shrink
toward zero but rarely become exactly zero.

**Parameter:** Larger $\lambda$ means stronger regularisation.
Bias/intercept terms are often excluded from the penalty.

### 30. L1 regularisation (Lasso)

$$
J=\operatorname{MSE}+\lambda\|\mathbf{w}\|_1
$$

where $\|\mathbf{w}\|_1=\sum_j|w_j|$.

**Idea:** Penalises the absolute values of weights.

**Effect:** Can drive some weights exactly to zero, creating a sparse
model and performing a form of feature selection.

**Caution:** With highly correlated features, which feature remains can
be unstable.

### 31. Elastic Net

$$
J=\operatorname{MSE}+\lambda_1\|\mathbf{w}\|_1+\lambda_2\|\mathbf{w}\|_2^2
$$

**Idea:** Combines L1 sparsity with L2 shrinkage.

**Why:** Can select features while behaving more stably than pure Lasso
when predictors are correlated. Implementations may parameterise the
overall strength and the L1/L2 mixture differently.

### 32. SVM margin

For a linear separator with weight vector $\mathbf{w}$,

$$
M=\frac{2}{\|\mathbf{w}\|_2}
$$

**Idea:** Under the canonical SVM scaling, the distance between the two
margin boundaries $w^Tx+b=+1$ and $w^Tx+b=-1$ is $2/\|w\|$.

**Goal:** Support Vector Machines seek a separating boundary with a
large margin, which can improve generalisation.

**Caution:** This expression assumes the canonical margin scaling;
multiplying $w$ and $b$ by a constant changes their numerical values but
not the decision boundary.

### 33. SVM decision function

$$
f(\mathbf{x})=\operatorname{sign}(\mathbf{w}^T\mathbf{x}+b)
$$

**Idea:** The sign of the score assigns one of two classes. The boundary
is $w^Tx+b=0$.

**Note:** The raw score's magnitude relates to distance from the
boundary after scaling by $\|w\|$; it is not automatically a
calibrated probability.

### 34. Hinge loss

$$
L=\max\left(0,\,1-y(\mathbf{w}^T\mathbf{x}+b)\right),\quad y\in\{-1,+1\}
$$

**Idea:** Gives zero loss when an example is correctly classified with a
margin of at least one. Otherwise, it penalises insufficient margin or
misclassification.

**Use:** Standard loss for a linear SVM, typically combined with a
weight regularisation term.

### 35. Kernel trick

$$
K(\mathbf{x},\mathbf{z})=\phi(\mathbf{x})^T\phi(\mathbf{z})
$$

**Idea:** A kernel computes an inner product in a transformed feature
space without explicitly constructing $\phi(\mathbf{x})$.

**Why:** Enables linear algorithms in feature space to learn nonlinear
boundaries in the original input space.

**Requirement:** Standard kernel SVM theory relies on a valid
positive-semidefinite kernel.

### 36. Polynomial kernel

$$
K(\mathbf{x},\mathbf{z})=(\mathbf{x}^T\mathbf{z}+c)^d
$$

**Idea:** Represents interactions up to a polynomial degree controlled
by $d$; $c$ controls the contribution of lower-degree terms.

**Use:** Modelling nonlinear relationships with feature interactions
without manually expanding all polynomial features.

**Note:** Some libraries use a scale factor as well as $c$ and $d$.

### 37. RBF (Gaussian) kernel

$$
K(\mathbf{x},\mathbf{z})=e^{-\gamma\|\mathbf{x}-\mathbf{z}\|_2^2}
$$

**Idea:** Similarity decreases exponentially with squared distance.

**Role of $\gamma$:** Large $\gamma$ makes similarity highly local and
can create complex boundaries; small $\gamma$ makes similarity vary
more smoothly.

**Caution:** Feature scaling is important. Some references write
$\gamma=1/(2\sigma^2)$.

## 7. Similarity and classification metrics

### 38. Cosine similarity

$$
\operatorname{sim}(\mathbf{x},\mathbf{y})=\frac{\mathbf{x}^T\mathbf{y}}{\|\mathbf{x}\|_2\|\mathbf{y}\|_2}
$$

**Idea:** Measures the cosine of the angle between two nonzero vectors.

**Interpretation:** Near 1 means similar direction; 0 means
perpendicular; near -1 means opposite direction.

**Use:** Text embeddings, document similarity, and high-dimensional
sparse vectors. It ignores vector magnitude; undefined if either vector
is zero.

### 39. Precision

$$
\operatorname{Precision}=\frac{TP}{TP+FP}
$$

**Idea:** Of all examples predicted positive, what fraction really are
positive?

**Prioritise precision when:** False positives are costly, such as
flagging legitimate transactions as fraud.

**Edge case:** Undefined when $TP+FP=0$; libraries may define a
convention.

### 40. Recall (sensitivity)

$$
\operatorname{Recall}=\frac{TP}{TP+FN}
$$

**Idea:** Of all actual positive examples, what fraction did the model
find?

**Prioritise recall when:** Missing a positive case is costly, such as
failing to flag a dangerous defect.

**Trade-off:** Raising the decision threshold often increases precision
and decreases recall, though not universally at every threshold.

### 41. F1-score

$$
F_1=2\frac{PR}{P+R}
$$

where $P$ is precision and $R$ is recall.

**Idea:** Harmonic mean of precision and recall. It is high only when
both are reasonably high.

**Use:** Imbalanced classification when both false positives and false
negatives matter.

**Limitation:** F1 ignores true negatives and depends on the chosen
decision threshold.

### 42. Accuracy

$$
\operatorname{Accuracy}=\frac{TP+TN}{TP+TN+FP+FN}
$$

**Idea:** Fraction of all predictions that are correct.

**Limitation:** Can be misleading for imbalanced datasets. If 99% of
examples are negative, always predicting negative gives 99% accuracy but
zero recall for the positive class.

## 8. Bias, variance, and generalisation

### 43. Bias

A common prediction-bias definition is

$$
\operatorname{Bias}(\hat{f}(x))=\mathbb{E}[\hat{f}(x)]-f(x)
$$

**Idea:** Bias measures the systematic difference between the model's
average prediction over possible training sets and the true target
function.

**High bias:** Often associated with an overly simple model that
underfits. The image's shorthand "$E[\hat{y}]-y$" conveys this idea,
but $f(x)$ makes the target function explicit.

### 44. Variance of an estimator

$$
\operatorname{Var}(\hat{f}(x))=\mathbb{E}\left[(\hat{f}(x)-\mathbb{E}[\hat{f}(x)])^2\right]
$$

**Idea:** Measures how much predictions vary when the model is trained
on different datasets.

**High variance:** Often associated with a model that is too sensitive
to its training data and may overfit.

### 45. Bias--variance trade-off

For squared-error prediction under the usual assumptions,

$$
\mathbb{E}[(\hat{f}(x)-y)^2]
=\operatorname{Bias}(\hat{f}(x))^2
+\operatorname{Var}(\hat{f}(x))
+\sigma_\epsilon^2
$$

**Idea:** Expected prediction error can be decomposed into squared bias,
variance, and irreducible noise.

**Trade-off:** Increasing model complexity often reduces bias but
increases variance. The objective is good performance on unseen data,
not simply minimising training error.

**Note:** This decomposition is an idealised result under assumptions
such as additive zero-mean noise; it is not a universal identity for
every loss and setting.

## 9. Optimisation algorithms

### 46. Learning-rate decay

One schedule is

$$
\eta_t=\frac{\eta_0}{1+kt}
$$

**Idea:** Gradually reduces the learning rate from initial value
$\eta_0$; $k$ controls how quickly it decays.

**Why:** Larger steps can help early progress, while smaller steps later
can improve stability around a minimum.

**Note:** This is one possible schedule, not the only one.

### 47. Exponential decay

$$
\eta_t=\eta_0e^{-\lambda t}
$$

**Idea:** Learning rate decreases by a multiplicative factor over time.

**Parameter:** Larger $\lambda$ causes faster decay. A practical
schedule should not reduce the learning rate so quickly that learning
stalls prematurely.

### 48. Momentum update

A common momentum convention is

$$
\mathbf{v}_t=\beta\mathbf{v}_{t-1}+(1-\beta)\nabla J(\mathbf{w}_t)
$$

$$
\mathbf{w}_{t+1}=\mathbf{w}_t-\eta\mathbf{v}_t
$$

**Idea:** Momentum smooths gradients over time, accumulating consistent
directions and reducing oscillation in narrow valleys.

**Notation caution:** Some textbooks omit the $(1-\beta)$ factor or
define the velocity differently. These conventions are equivalent only
with appropriate parameter rescaling.

### 49. Adam optimiser

A common Adam formulation is

$$
\mathbf{m}_t=\beta_1\mathbf{m}_{t-1}+(1-\beta_1)\mathbf{g}_t
$$

$$
\mathbf{v}_t=\beta_2\mathbf{v}_{t-1}+(1-\beta_2)(\mathbf{g}_t\odot\mathbf{g}_t)
$$

Bias corrections:

$$
\hat{\mathbf{m}}_t=\frac{\mathbf{m}_t}{1-\beta_1^t},
\qquad
\hat{\mathbf{v}}_t=\frac{\mathbf{v}_t}{1-\beta_2^t}
$$

Update:

$$
\mathbf{w}_{t+1}=\mathbf{w}_t-
\eta\frac{\hat{\mathbf{m}}_t}{\sqrt{\hat{\mathbf{v}}_t}+\epsilon}
$$

**Idea:** Adam combines momentum-like first-moment estimates with
adaptive per-parameter scaling from second moments.

**Terms:** $\mathbf{g}_t$ is the current gradient; $\odot$ is
elementwise multiplication; $\epsilon$ prevents division by zero.

**Why bias correction:** The moment estimates start at zero and are
biased toward zero early in training. Typical defaults are
$\beta_1=0.9$ and $\beta_2=0.999$, though tuning may help.

### 50. Matrix multiplication

For matrices $A$ of size $m\times n$ and $B$ of size $n\times p$,

$$
C=AB,\qquad C_{ij}=\sum_{k=1}^{n}A_{ik}B_{kj}
$$

**Idea:** Each output entry is the dot product of row $i$ of $A$ and
column $j$ of $B$.

**Shape rule:** The inner dimensions must match:
$(m\times n)(n\times p)=(m\times p)$.

**ML use:** Dense layers, linear regression, attention calculations, and
batches of vector operations. Matrix multiplication is generally not
commutative: $AB\ne BA$.

## 10. Quick comparison tables

### Common scaling choices

  -------------------------------------------------------------------------------
  Method            Transformation    Useful when       Main caution
  ----------------- ----------------- ----------------- -------------------------
  Z-score           Subtract mean,    Features need     Sensitive to outliers;
                    divide by         comparable spread save training statistics
                    standard                            
                    deviation                           

  Min--max          Map training      A bounded feature Outliers distort range;
                    range to 0--1     range is useful   future values may leave
                                                        range

  No scaling        Keep original     Units are         Distance/gradient-based
                    units             meaningful and    models may be dominated
                                      algorithm         by large-scale features
                                      tolerates scale   
  -------------------------------------------------------------------------------

### Classification metrics

  -----------------------------------------------------------------------
  Metric                  Answers                 Most directly penalises
  ----------------------- ----------------------- -----------------------
  Precision               "When I predict         False positives
                          positive, how often am  
                          I right?"               

  Recall                  "How many actual        False negatives
                          positives do I catch?"  

  F1                      "How balanced are       Poor precision or poor
                          precision and recall?"  recall

  Accuracy                "What fraction of all   All misclassifications
                          predictions are         equally
                          correct?"               
  -----------------------------------------------------------------------

### Common losses and regularisers

  -----------------------------------------------------------------------
  Method                  Main behaviour          Typical use
  ----------------------- ----------------------- -----------------------
  MSE                     Squares errors;         Regression
                          emphasises large misses 

  MAE                     Absolute errors; more   Regression
                          robust to outliers than 
                          MSE                     

  Binary cross-entropy    Scores predicted        Binary classification
                          probability for a       
                          binary label            

  Multiclass              Scores probability      Multiclass
  cross-entropy           assigned to the correct classification
                          class                   

  L1 penalty              Encourages exact-zero   Sparse models / feature
                          weights                 selection

  L2 penalty              Shrinks weights         Stabilisation /
                          smoothly                reducing overfitting

  Elastic Net             Combines L1 and L2      Sparsity with
                                                  correlated features
  -----------------------------------------------------------------------

## 11. Important notation

-   $n$: number of observations.
-   $d$: number of features.
-   $K$: number of classes.
-   $x_i$: observation/value; $\mathbf{x}$: feature vector.
-   $y$: true target/label; $\hat{y}$: prediction.
-   $\mathbf{w}$: model weights; $b$: intercept/bias.
-   $\eta$: learning rate.
-   $\lambda$: regularisation strength (exact meaning varies by
    implementation).
-   $TP$: true positive; $TN$: true negative; $FP$: false positive;
    $FN$: false negative.
-   $\nabla J$: gradient of objective/loss $J$.
-   $\mathbb{E}[\cdot]$: expectation; $\operatorname{Var}(\cdot)$:
    variance.

## 12. Suggested learning order

1.  **Statistics:** mean, variance, standard deviation, covariance,
    correlation.
2.  **Geometry and preprocessing:** distances, z-score, min--max
    scaling.
3.  **Prediction and optimisation:** linear model, MSE/MAE, gradients,
    gradient descent.
4.  **Classification:** sigmoid/logistic regression, cross-entropy,
    Bayes' theorem, Naive Bayes.
5.  **Generalisation:** L1/L2/Elastic Net, bias--variance.
6.  **Advanced classifiers:** SVM, kernels, classification metrics.
7.  **Neural-network training:** activations, momentum, Adam,
    learning-rate schedules.
8.  **Linear algebra foundation:** vectors, norms, dot products, matrix
    multiplication.

> \[!tip\] Study method For each formula, learn (1) what each symbol
> means, (2) what happens when the input/parameter increases, (3) one
> tiny numerical example, and (4) when the formula is appropriate.
> Memorising symbols without the assumptions is much less useful.
