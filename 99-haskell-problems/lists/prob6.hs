main :: IO ()

-- myReverse :: [a] -> [a]
myReverse [] = []
myReverse (x:xs) = myReverse xs ++ [x]

-- isPalindrome :: [a] -> Bool
isPalindrome xs = xs == myReverse xs

main = do
    let res = isPalindrome [1, 2, 3]
    print res
    let res = isPalindrome "madamimadam"
    print res
    let res = isPalindrome [1,2,4,8,16,8,4,2,1]
    print res
