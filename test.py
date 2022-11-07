from sklearn.base import BaseEstimator, TransformerMixin


class data_setter(BaseEstimator,TransformerMixin):
    def fit(self,X,y=None):
            return self
    def transform(self,X):
        import pandas as pd
        from sklearn.preprocessing import MinMaxScaler  
        from sklearn.model_selection import train_test_split
        SEED = 12345

        for col in X.columns:
            if(X[col].nunique() == 1):
                X.drop(col,inplace=True, axis=1)

        X['Attrition'] = X['Attrition'].map({'Yes':1, 'No':0})
        X['OverTime'] = X['OverTime'].map({'Yes':1, 'No':0})
        X['MaritalStatus'] = X['MaritalStatus'].map({'Single':0, 'Married':1,'Divorced':0.5})
        X.drop("EmployeeNumber",inplace = True, axis = 1)
        X.drop('JobLevel', inplace = True,axis = 1)

        X = pd.get_dummies(X)
        scale = MinMaxScaler()
        X = pd.DataFrame(scale.fit_transform(X.values), columns=X.columns, index=X.index)

        
        X_train, X_test, y_train, y_test = train_test_split(X.drop('Attrition', axis=1), X["Attrition"], 
                                                            test_size=0.15, random_state=SEED)
        X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, 
                                                        test_size=0.176, random_state=SEED)
        return X_train,y_train,X_test,y_test,X_validation,y_validation