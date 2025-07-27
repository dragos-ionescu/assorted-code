main :: IO ()

myReverse :: [a] -> [a]
myReverse [] = []
myReverse (x:xs) = myReverse xs ++ [x]

main = do 
    let res = myReverse "A man, a plan, a canal, panama!"
    print res
    let res = myReverse [1, 2, 3, 4]
    print res
