from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier,export_graphviz
import pydot
Iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(Iris.data,Iris.target,stratify=Iris.target,random_state=11)

#깊이 제한 걸어주기
IrisdepMTree = DecisionTreeClassifier(criterion='entropy',max_depth=4,random_state=0)
#
IrisdepMTree.fit(X_train,y_train)

#깊이 제한한 모델의 점수 출력
print()
print("Iris_case6_(criterion='entropy',max_depth=4)")
print("Train Set Score1: {:.2f}".format(IrisdepMTree.score(X_train,y_train)))
print("Test Set Score1: {:.2f}".format(IrisdepMTree.score(X_test,y_test)))

export_graphviz(IrisdepMTree, out_file="depMtree.dot", class_names=Iris.target_names,
                feature_names=Iris.feature_names, impurity=False, filled=True)

(graph,) = pydot.graph_from_dot_file('depMtree.dot',encoding='utf8')

graph.write_png('IrisdepMtree.png')