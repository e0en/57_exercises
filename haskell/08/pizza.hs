import System.IO

putStrF s = do
    putStr s
    hFlush stdout

ask q f = do
    putStrF (q ++ " ")
    f

getInteger = do
    hSetEcho stdin False
    hSetBuffering stdin NoBuffering
    n <- getIntegerRec ""
    hSetEcho stdin True
    return n

getIntegerRec s = do
    c <- getChar
    if c == '\n' || (c >= '0' && c <= '9')
    then do
        putChar c
        hFlush stdout
        if c == '\n' then return s else getIntegerRec (s ++ [c])
    else getIntegerRec s

promptInt q = do
    nStr <- ask q getInteger
    return (read nStr :: Integer)


data Piece = Piece Integer

piece 1 = "piece"
piece n = "pieces"

main = do
    nPeople <- promptInt "How many people?"
    nPizza <- promptInt "How many pizzas do you have?"
    nPiece <- promptInt "How many pieces are in a pizza?"
    let totalPiece = nPiece * nPizza
    let piecePerPerson = totalPiece `div` nPeople
    let leftOver = totalPiece - (nPeople * piecePerPerson)
    putStrLn $ "Each person gets " ++ (show piecePerPerson) ++ 
        " " ++ (piece piecePerPerson) ++ " of pizza."
    putStrLn $ "There are " ++ (show leftOver) ++ 
        " leftover " ++ (piece leftOver) ++ "."
