import System.IO
import Text.Regex.Posix
import Text.Printf
import Data.Text

putStrF s = do
    putStr s
    hFlush stdout

ask q = do
    putStrF (q ++ " ")
    getLine

promptPattern :: String -> String -> IO String
promptPattern q p = do
    nStr <- ask q
    if nStr =~ p :: Bool
    then
        return nStr
    else
        do
            putStrLn "Wrong input"
            promptPattern q p

promptCurrency q = do
    s <- promptPattern q "^[0-9]+($|\\.[0-9]{1,2}$)"
    return (read s :: Double)

ratio = 5.5
calculateTax amount = fromInteger (ceiling $ amount * ratio) / 100.0

message amount state =
    let tax = calculateTax amount in
    let total = amount + tax in
    let totalStr = "The total is $" ++ (show total) in
    if state == "wi" || state == "wisconsin"
        then "The subtotal is $" ++ (show amount) ++ 
            "\nThe tax is $" ++ (show tax) ++ 
            "\n" ++ totalStr
        else totalStr


main = do
    amount <- promptCurrency "What is the order amount?"
    state <- ask "What is the state?"
    let stateNormalized = unpack (toLower $ pack state)
    putStrLn $ message amount stateNormalized
