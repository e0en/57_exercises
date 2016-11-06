import System.IO
import Data.List

prompt q = do
    putStr (q ++ " ")
    hFlush stdout
    getLine

intPrompt q = do
    nStr <- prompt q
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
