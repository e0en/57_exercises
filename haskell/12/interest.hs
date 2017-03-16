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

calculateSimpleInterest p i y = p * (1.0 + 0.01 * i * (fromIntegral y))

main = do
    principal <- promptCurrency "Enter the principal:"
    interest <- promptDouble "Enter the rate of interest:"
    years <- promptInt "Enter the number of years:"
    let investment = calculateSimpleInterest principal interest years
    printf "After %d years at %g%%, the investment will be worth $%g" years interest investment
