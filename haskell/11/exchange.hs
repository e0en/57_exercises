import System.IO
import Text.Regex.Posix
import Text.Printf

putStrF s = do
    putStr s
    hFlush stdout

ask q = do
    putStrF (q ++ " ")
    getLine

currencyNumPattern = "^[0-9]+($|\\.[0-9]{1,2}$)"

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

promptCurrency :: String -> IO Double
promptCurrency q = do
    s <- promptPattern q currencyNumPattern
    return (read s :: Double)


main = do
    euros <- promptCurrency "How many Euros are you exchanging?"
    rate <- promptCurrency "What is the exchange rate?"
    let dollars = (fromIntegral $ ceiling (euros * rate)) / 100 :: Double
    printf "%g Euros at an exchange rate of %g is\n%g Dollars" euros rate dollars
