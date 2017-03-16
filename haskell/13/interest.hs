import System.IO
import Text.Regex.Posix
import Text.Printf

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

promptDouble q = do
    s <- promptPattern q "^[0-9]+($|\\.[0-9]+$)"
    return (read s :: Double)

promptInt q = do
    s <- promptPattern q "^[0-9]+$"
    return (read s :: Integer)

calculateComplexInterest p i y n = 
    let percent = i * 0.01 in
    let base = (1.0 + percent / (fromIntegral n)) in 
    let exponent = fromIntegral $ n * y in
    fromIntegral (ceiling $ p * (base ** exponent) * 100.0) / 100.0 :: Double

main = do
    principal <- promptCurrency "Enter the principal:"
    interest <- promptDouble "Enter the rate of interest:"
    years <- promptInt "Enter the number of years:"
    perYear <- promptInt "What is the number of times the interest\nis compounded per year:"
    let investment = calculateComplexInterest principal interest years perYear
    printf "After %d years at %g%%, the investment will be worth $%g" years interest investment
