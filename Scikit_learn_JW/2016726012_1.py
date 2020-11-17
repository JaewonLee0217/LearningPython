from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier,export_graphviz
import pydot
Breast_cancer = load_breast_cancer()

#데이터들을 훈련, 테스트 데이터를 나눠주고
X_train, X_test, y_train, y_test = train_test_split(Breast_cancer.data,Breast_cancer.target,stratify=Breast_cancer.target,random_state=42)

#깊이 제한 걸어주기
depMTree = DecisionTreeClassifier(criterion='entropy',max_depth=4, random_state=0)

depMTree.fit(X_train,y_train)

#깊이 제한한 모델의 점수 출력
print()
print("case5_(criterion = entropy, max_depth: 4)")
print("Train Set Score1: {:.2f}".format(depMTree.score(X_train,y_train)))
print("Test Set Score1: {:.2f}".format(depMTree.score(X_test,y_test)))

export_graphviz(depMTree, out_file="depMtree.dot", class_names=["malignat", "benign"],
                feature_names=Breast_cancer.feature_names, impurity=False, filled=True)

(graph,) = pydot.graph_from_dot_file('depMtree.dot',encoding='utf8')

graph.write_png('depMtreeR.png')
