import System.IO
import Data.Map (Map, (!))
import qualified Data.Map as Map

prompt :: String -> IO String
prompt q = do
    putStr (q ++ " ")
    hFlush stdout
    getLine

message :: String -> String -> String
message quoteStr name = name ++ " says, \"" ++ quoteStr ++ "\""


database = Map.fromList [("Obi-Wan Kenobi", "These aren't the droids you're looking for")]

main :: IO ()
main = do
    let x = map (\n -> message (database ! n) n) (Map.keys database)
    mapM_ putStrLn x
