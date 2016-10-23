import System.IO
import qualified Data.List as L
import Data.Maybe as M
import Text.Printf as P

prompt q = do
    putStr (q ++ " ")
    hFlush stdout
    getLine

isVowel c = M.isJust $ L.find (== c) vowels
    where vowels = "aeiou"

addA w = if isVowel $ L.last w
    then "an " ++ w
    else "a " ++ w

enterPrompt q = prompt ("Enter " ++ (addA q) ++ ":")

msg n v a av = P.printf "Do you %s your %s %s %s? That's hilarious!" v n a av

main = do
    noun <- enterPrompt "noun"
    verb <- enterPrompt "verb"
    adjective <- enterPrompt "adjective"
    adverb <- enterPrompt "adverb"
    putStrLn $ msg noun verb adjective adverb
