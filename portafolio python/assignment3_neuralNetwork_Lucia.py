"""Lucia Martinez
C0863954
2023F-T3 AML 3104 - Neural Networks and Deep Learning 01 (DSMM Group 1 & Group 2)
Assignment3



1)
A decision tree is defined as a non-parametric supervised learning method that is commonly used for classification and regression. With a hierarchical structure made of nodes, it’s known for its flowchart structure that resembles a tree-like diagram. It is divided into the "root node", the tree branches ( "internal nodes" that contain decision rules), and "leaf nodes" (that represent the class labels or regression values). Classification rules are represented by the pathways from root to leaf.
To select a feature, at each internal node, the decision aims to choose the feature that best separates the data based on some criteria, often using metrics like Gini impurity, information gain, or entropy. These metrics measure the impurity or disorder of the data, and the algorithm aims to minimize it.

Based on the selected feature, the algorithm creates branches or child nodes, each representing a different value or range of values for that feature. This process continues recursively until a stopping condition is met.

When the splitting process reaches a leaf node, it assigns a class label to that node. In a classification problem, the majority class of the training samples in that leaf node is assigned as the predicted class label. In regression problems, the leaf node contains the mean or median value of the target variable for the samples in that node.

To make a prediction, new data follows the decision tree from the root node down to a leaf node by following the decision rules based on the features. The leaf node's assigned class label is the predicted outcome for the input data.

2)
The decision tree algorithm involves mathematical calculations to determine how to split the data at each internal node of the tree. The primary mathematical concepts used in decision trees are impurity measures and splitting criteria.
Decision trees use impurity measures to quantify the disorder or randomness of a dataset. The most common impurity measures used in decision trees are Gini impurity, entropy, and information gain.

Gini Impurity (Gini Index):
The Gini impurity for a node  with respect to a  classification problem is calculated as:
Gini(t) = 1 - (Σ p_i^2)
where p_i is the proportion of samples belonging to class i.

We can say that Gini impurity index is the probability of diverse data. If there is no diversity or impurity in data or there is only one type of instance, that means Gini Impurity Index for that data is Zero, because it is a pure data.
Entropy:
The entropy for a node 't' is defined as:
H(S)= -Σ (p_i * log2(p_i))
Entropy measures the level of impurity or disorder in a node.
Splitting Criteria:
Decision trees determine how to split the data by selecting the feature and threshold that minimize the impurity after the split. Common splitting criteria include the Gini gain (or Gini decrease) and information gain (for entropy).

Gini Gain:
The Gini gain measures the reduction in Gini impurity after a split. It is calculated as follows:
Gini Gain = Gini(t) - (Weighted Sum of Gini Impurities in Child Nodes)
Decision trees aim to maximize the Gini gain when selecting the best feature to split the data.

Information Gain:
The amount of "information" a characteristic provides us with about the class is measured by information gain (IG). It indicates the relative importance of a particular feature vector characteristic. A decision tree's nodes' attribute ordering is determined by information gain (IG).
It quantifies the reduction in entropy after a split and is calculated as:
Information Gain = Entropy(t) - (Weighted Sum of Entropy in Child Nodes)
Decision trees aim to maximize information gain when selecting the best feature to split the data.

Pruning:
After constructing the decision tree, you may apply pruning to reduce its complexity and prevent overfitting. Pruning involves removing some branches or nodes based on statistical tests or other criteria. The primary mathematical aspect here is to determine when to prune, typically based on cross-validation performance.

https://vpoliwal.hashnode.dev/deep-dive-into-the-basics-of-gini-impurity-in-decision-trees-with-math-intuition-46c721d4aaec

3)
In binary classification, the goal is to categorize data into one of two classes: a positive class (usually denoted as "1") and a negative class (usually denoted as "0"). Decision tree classifiers make decisions at each node to classify data into one of these two classes. To accomplish this, data points are divided into two child nodes based on whether the feature's value is above or below a threshold. The two child nodes represent the two classes in binary classification: the positive class (1) and the negative class (0).
For each child node, the impurity measure is calculated based on the distribution of class labels in that node. The algorithm aims to reduce impurity in each child node.
The process of selecting the best feature, threshold, and creating child nodes is repeated recursively for each child node that is not perfectly pure (i.e., not all data points in the node belong to the same class).

4) Decision tree classification takes the shape of as tree-like structure with partitions in the feature space. It starts 


The root node of the decision tree is the starting point in the feature space. As the algorithm recursively splits the data, it creates more and more partitions in the feature space, effectively segmenting it into different regions. The final regions are the leaf nodes of the decision tree. Each leaf node represents a region with a specific class label or distribution of class labels. These leaf nodes are the regions in the feature space where the decision tree makes predictions.

5)
A Confusion matrix is an N x N matrix used for evaluating the performance of a classification model, where N is the total number of target classes. The matrix compares the actual target values with those predicted by the machine learning model.

 

True Positive (TP) — model correctly predicts the positive class (prediction and actual both are positive)
True Negative (TN) — model correctly predicts the negative class (prediction and actual both are negative). 
False Positive (FP) — model gives the wrong prediction of the negative class (predicted-positive, actual-negative). 
False Negative (FN) — model wrongly predicts the positive class (predicted-negative, actual-positive). 
 

6)
A machine learning model is trained to predict tumor in patients. The test dataset consists of 100 people.
 
Confusion Matrix for tumor detection
True Positive (TP) -- 10 people who have tumors are predicted positively by the model.
True Negative (TN) — 60 people who don’t have tumors are predicted negatively by the model.
False Positive (FP) —22 people are predicted as positive of having a tumor, although they don’t have a tumor. FP is also called a TYPE I error.
False Negative (FN) —8 people who have tumors are predicted as negative. FN is also called a TYPE II error.
Precision
Precision is the ratio of true positives to the total number of positive predictions.  
Precision in this case is  10/(10+22)=0.3
Recall
Out of the total positive, what percentage are predicted positive.
 
Recall in this case is  10/(10+8) = 0.5
F1 score
The ideal model would have the highest possible Precision and Recall. F1 score shows a balance between Precision and Recall. t is a good choice when class imbalance is present, as it considers both false positives and false negatives
. F1=2*([0.3*0.5])/([0.3+0.5])
F1 in this case is  10/(10+8) = 0.37

7)
Choosing an appropriate evaluation metric for a classification problem allows people to make decisions regarding its suitability for a particular application. For balanced datasets, Metrics like accuracy, precision, recall are good ways to evaluate classification models.

Different classification problems have different objectives. For instance, in medical diagnosis, you may be more concerned with minimizing false negatives (misdiagnosing a serious disease as not present) even if it means accepting some false positives. In fraud detection, false positives (flagging legitimate transactions as fraud) may be costly. Your choice of metric should reflect these specific goals.

8) 
Sorting incoming emails into two categories—"spam" or "not spam" (ham)—is the duty of email spam detection. This is a traditional case of binary categorization.
The Value of Accuracy
For the purpose of creating confidence and guaranteeing a good user experience in email spam detection, accuracy is essential. Email filters are used by users to prevent unsolicited spam from entering their inboxes. Users risk missing crucial communications if the email filter is very lax and accepts an excessive number of false positives, or valid emails mistakenly flagged as spam. This may cause users to lose faith in the email service. However, incorrectly classifying spam as non-spam lowers user pleasure and experience.

Therefore, although recall and precision are always trade-offs, in this particular situation, precision +takes precedence to ensure that important emails are not mistakenly classified as spam, ultimately enhancing user satisfaction and trust in the email filtering system.

9)
Example: Anomaly Detection in Credit Card Transactions
The challenge in the field of financial fraud detection is to distinguish between fraudulent and authentic credit card transactions. The transactions in this scenario can be categorized as either "fraudulent" or "non-fraudulent" (legal).
In this case, safeguarding clients against fraudulent or unauthorized transactions is the main objective. A cardholder may suffer financial damages if there is a fail to detect a fraudulent transaction, often known as a false negative. High recall makes sure that the greatest number of fraudulent transactions are found and prevented.
High recall guarantees that resources and efforts are focused on looking into and addressing possibly fraudulent transactions, even if it may lead to some false positives (good transactions incorrectly reported as fraudulent).
"""