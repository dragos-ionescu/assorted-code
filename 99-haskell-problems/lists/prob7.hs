main :: IO()

data NestedList a = Elem a | List [NestedList a]

flatten (Elem a) = [a]
flatten (List []) = []
flatten (List (x:xs)) = flatten x ++ flatten (List xs)

main = do
    let nestedList0 = Elem 5
    let nestedList1 = List [Elem 1, List [Elem 2, List [Elem 3, Elem 4], Elem 5]]
    let nestedList2 = List [List [List [List [List [Elem 1, Elem 999, List []]]]]]
    let nestedList3 = List []

    print (flatten nestedList0) -- [5]
    print (flatten nestedList1) -- [1,2,3,4,5]
    print (flatten nestedList2) -- [1,999]
    print (flatten nestedList3) -- []
