import System.IO
import Text.Regex.Posix
import Data.Text.Encoding
import Data.ByteString.Char8 as C
import Data.String as S
import Data.Map as Map
import Data.Maybe
import Crypto.BCrypt

putStrF s = do
    Prelude.putStr s
    hFlush stdout

ask q = do
    putStrF (q ++ " ")
    str <- Prelude.getLine
    return str

message isPassed = 
    if isPassed
    then "Welcome!"
    else "That password is incorrect."

database = fromList [("foo", hash "bar"), ("bar", hash "baz")]

policy = HashingPolicy 12 $ pack "$2y$"
hash = hashPasswordUsingPolicy policy . C.pack

main = do
    id <- ask "What is the ID:"
    password <- ask "What is the password:"
    hashed <- hash password
    case Map.lookup id database of 
        Just trueHashIo -> do
            trueHashMaybe <- trueHashIo
            let trueHash = fromJust trueHashMaybe
            let isMatched = validatePassword trueHash (pack password)
            Prelude.putStrLn $ message isMatched
        Nothing -> Prelude.putStrLn $ message False 
