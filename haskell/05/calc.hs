import System.IO
import Data.List

ask q f = do
    putStr (q ++ " ")
    hFlush stdout
    f

prompt q = ask q getLine

getInt = do
    hSetEcho stdin False
    hSetBuffering stdin NoBuffering
    n <- getIntRec ""
    hSetEcho stdin True
    return n

getIntRec s = do
    c <- getChar
    if c == '\n' || (c >= '0' && c <= '9')
    then do
        putChar c
        hFlush stdout
        if c == '\n' then return s else getIntRec (s ++ [c])
    else getIntRec s

intPrompt q = do
    nStr <- ask q getInt
    return (read nStr :: Int)

printCalc op sig = \x y ->
    let r = op x y
        intStrs = zipWith (\s1 s2 -> [s1, s2]) (map show [x, y, r]) [sig, "=", ""]
    in intercalate " " $ foldr (++) [] intStrs

opPairs = [((+), "+"), ((-), "-"), ((*), "*"), (div, "/")]

showAll x y = intercalate "\n" $ map (\p -> (printCalc (fst p) (snd p)) x y) opPairs

main = do
    num1 <- intPrompt "What is the first number?"
    num2 <- intPrompt "What is the second number?"
    putStrLn $ showAll num1 num2
