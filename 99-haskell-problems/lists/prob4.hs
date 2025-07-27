main :: IO ()

myLength :: [a] -> Int
myLength [] = 0
myLength (x:xs) = 1 + myLength xs

main = do
    let res = myLength [123, 456, 789]
    print res
    let res = myLength "Hello, world!"    
    print res
