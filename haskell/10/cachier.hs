import System.IO
import Text.Regex.Posix

putStrF s = do
    putStr s
    hFlush stdout

ask q = do
    putStrF (q ++ " ")
    getLine

natNumPattern = "^[0-9]+$"

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

promptNatNum q = do
    s <- promptPattern q natNumPattern
    return (read s :: Integer)

promptItem n = do
    let nStr = show n
    price <- promptNatNum $ "Price of item "  ++ nStr ++ ":"
    quantity <- promptNatNum $ "Quantity of item " ++ nStr ++ ":"
    return (price, quantity)

promptItemsRec max n res = do
    if n > max
    then
        return res
    else
        do
            new <- promptItem n
            promptItemsRec max (n + 1) (res ++ [new])

promptItems n = promptItemsRec n 1 []

calcSubTotal r = foldl (+) 0 (map (\x -> (fst x) * (snd x)) r)

taxRatio = 5.5 :: Double
calcTax x = (fromInteger x :: Double) * (0.01 * taxRatio)
calcTotal x = (fromInteger x :: Double) + (calcTax x)

main = do
    results <- promptItems 3
    let subtotal = calcSubTotal results
    let tax = calcTax subtotal
    let total = calcTotal subtotal
    putStrLn $ "Subtotal: $" ++ (show subtotal) ++ ".00"
    putStrLn $ "Tax: $" ++ (show tax)
    putStrLn $ "Total: $" ++ (show total)
